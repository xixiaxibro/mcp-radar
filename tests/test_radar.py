import copy
from datetime import datetime, timedelta, timezone
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import argparse

SPEC = importlib.util.spec_from_file_location('radar', Path(__file__).resolve().parents[1] / 'scripts/radar.py')
radar = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(radar)
NOW = datetime(2026, 11, 5, 12, tzinfo=timezone.utc)
CONFIG = json.loads((radar.ROOT / 'config/watchlist.json').read_text())
SOURCE = {'repo': 'example/server', 'topic': 'sdk', 'tier': 1, 'issues': True, 'commits': False, 'keywords': []}


def pr(number=1, **kwargs):
    return {'number': number, 'title': 'Fix MCP transport cancellation', 'body': 'Close client resources',
            'html_url': f'https://github.com/example/server/pull/{number}', 'state': 'closed',
            'created_at': '2026-11-01T00:00:00Z', 'updated_at': '2026-11-04T00:00:00Z',
            'merged_at': None, 'head': {'sha': 'abc'}, 'labels': [], **kwargs}


class FakeAPI:
    def __init__(self, fail=None, private=False):
        self.fail = fail
        self.private = private
        self.seen = []

    def get(self, path):
        return {'full_name': SOURCE['repo'], 'private': self.private, 'archived': False, 'default_branch': 'main'}

    def pages(self, path, *args):
        self.seen.append(path)
        endpoint = path.split('/')[-1]
        if endpoint == self.fail:
            raise RuntimeError('HTTP 403 from api.github.com')
        if endpoint == 'pulls':
            return [pr(), pr(2, merged_at='2026-11-04T00:00:00Z'), pr(3, updated_at='2025-01-01T00:00:00Z')], False
        if endpoint == 'issues':
            return [dict(pr(), pull_request={'url':'x'}), {**pr(4), 'html_url':'https://github.com/example/server/issues/4'}], False
        return [], False


class CollectionTests(unittest.TestCase):
    def test_closed_is_not_merged_and_old_and_issue_pr_duplicates_are_excluded(self):
        items, errors, warnings, coverage = radar.collect_repo(FakeAPI(), SOURCE, NOW-timedelta(days=14))
        self.assertFalse(errors)
        self.assertEqual([x['status'] for x in items if x['kind']=='pull_request'], ['closed', 'merged'])
        self.assertEqual(len(items), 3)
        self.assertEqual(coverage['status'], 'ok')
        self.assertEqual(items[0]['head_sha'], 'abc')

    def test_endpoint_failure_preserves_other_results(self):
        items, errors, _, coverage = radar.collect_repo(FakeAPI(fail='releases'), SOURCE, NOW-timedelta(days=14))
        self.assertEqual(len(items), 3)
        self.assertEqual(errors[0]['endpoint'], 'releases')
        self.assertEqual(coverage['status'], 'partial')

    def test_private_repo_is_rejected_before_reading_activity(self):
        api = FakeAPI(private=True)
        items, errors, _, coverage = radar.collect_repo(api, SOURCE, NOW-timedelta(days=14))
        self.assertFalse(items)
        self.assertTrue(errors)
        self.assertEqual(api.seen, [])
        self.assertEqual(coverage['status'], 'failed')

    def test_keyword_filter(self):
        source = {**SOURCE, 'keywords':['OAuth audience']}
        items, _, _, _ = radar.collect_repo(FakeAPI(), source, NOW-timedelta(days=14))
        self.assertEqual(items, [])

    def test_release_collection_can_be_disabled_for_unrelated_monorepos(self):
        api = FakeAPI()
        radar.collect_repo(api, {**SOURCE, 'releases': False}, NOW-timedelta(days=14))
        self.assertFalse(any(path.endswith('/releases') for path in api.seen))

    def test_unpublished_releases_and_private_advisories_are_excluded(self):
        class API(FakeAPI):
            def pages(self, path, *args):
                if path.endswith('/releases'):
                    return [{**pr(), 'draft':True, 'tag_name':'private-release'}], False
                if path.endswith('/security-advisories'):
                    return [{**pr(), 'state':'draft'}], False
                return [], False
        items, _, _, _ = radar.collect_repo(API(), SOURCE, NOW-timedelta(days=14))
        self.assertEqual(items, [])


class PaginationTests(unittest.TestCase):
    def test_cap_is_reported_without_assuming_complete_coverage(self):
        api = radar.PublicAPI(max_pages=2, per_page=2)
        with patch.object(api, 'get', return_value=[pr(1), pr(2)]):
            rows, capped = api.pages('x', {}, NOW-timedelta(days=14))
        self.assertTrue(capped)
        self.assertEqual(len(rows), 4)

    def test_ordered_list_can_stop_outside_window(self):
        api = radar.PublicAPI(max_pages=3, per_page=2)
        with patch.object(api, 'get', return_value=[pr(1),pr(2, updated_at='2025-01-01T00:00:00Z')]) as get:
            _, capped = api.pages('x', {}, NOW-timedelta(days=14))
        self.assertFalse(capped)
        self.assertEqual(get.call_count, 1)

    def test_unordered_list_does_not_stop_on_old_first_page(self):
        api = radar.PublicAPI(max_pages=3, per_page=2)
        with patch.object(api, 'get', side_effect=[[pr(1, updated_at='2025-01-01T00:00:00Z'),pr(2, updated_at='2025-01-01T00:00:00Z')], [pr(3)]]) as get:
            rows, capped = api.pages('x', {}, NOW-timedelta(days=14), ordered=False)
        self.assertFalse(capped)
        self.assertEqual(len(rows), 3)
        self.assertEqual(get.call_count, 2)


class FeedAndFingerprintTests(unittest.TestCase):
    def test_rss_window_and_keyword_filter(self):
        xml = b'''<rss><channel><item><title>MCP auth</title><link>https://example.org/mcp</link><pubDate>Wed, 04 Nov 2026 00:00:00 GMT</pubDate><description>OAuth</description></item><item><title>Unrelated</title><link>https://example.org/other</link><pubDate>Wed, 04 Nov 2026 00:00:00 GMT</pubDate></item></channel></rss>'''
        source={'id':'feed','topics':['protocol'],'tier':1,'keywords':['mcp']}
        rows, count=radar.parse_feed(xml,source,NOW-timedelta(days=7))
        self.assertEqual(count,2)
        self.assertEqual(len(rows),1)
        self.assertEqual(rows[0]['status'],'published')

    def test_atom_alternate_link_and_updated_date(self):
        xml=b'''<feed xmlns="http://www.w3.org/2005/Atom"><entry><title>MCP</title><updated>2026-11-04T00:00:00Z</updated><link rel="self" href="https://example.org/self"/><link href="https://example.org/article"/></entry></feed>'''
        rows,_=radar.parse_feed(xml,{'id':'feed','topics':['protocol'],'tier':1,'keywords':[]},NOW-timedelta(days=7))
        self.assertEqual(rows[0]['url'],'https://example.org/article')

    def test_comment_timestamp_does_not_trigger_change_but_head_and_merge_do(self):
        item=radar.make_item(SOURCE,pr(),'pull_request','Fix','https://example.org/pr','open',head_sha='abc')
        base=radar.event_key(item)
        self.assertEqual(base,radar.event_key({**item,'updated_at':'later','comments':999}))
        self.assertNotEqual(base,radar.event_key({**item,'head_sha':'def'}))
        self.assertNotEqual(base,radar.event_key({**item,'status':'merged'}))

    def test_security_and_migration_rank_above_routine_dependency_bump(self):
        high=radar.make_item(SOURCE,pr(),'pull_request','Fix OAuth audience validation breaking migration','https://example.org/a','merged')
        low=radar.make_item(SOURCE,pr(),'pull_request','chore(deps): bump formatting library','https://example.org/b','merged')
        self.assertGreater(radar.rank(high,CONFIG)[0],radar.rank(low,CONFIG)[0])

    def test_external_redirect_removes_authorization_header(self):
        from urllib.request import Request
        req=Request('https://api.github.com/path',headers={'Authorization':'Bearer fake'})
        redirect=radar.SafeRedirect().redirect_request(req,None,302,'Moved',{},'https://example.org/path')
        self.assertIsNone(redirect.get_header('Authorization'))
        with self.assertRaises(ValueError):
            radar.SafeRedirect().redirect_request(req,None,302,'Moved',{},'http://example.org/path')


class StateTests(unittest.TestCase):
    def test_same_day_idempotency_and_state_change_history(self):
        config=copy.deepcopy(CONFIG)
        config['repositories']=[SOURCE]
        config['feeds']=[]
        item=radar.make_item(SOURCE,pr(),'pull_request','Fix timeout','https://example.org/pr','open',head_sha='abc')
        with tempfile.TemporaryDirectory() as directory:
            output=Path(directory)
            config_file=output/'watch.json';config_file.write_text(json.dumps(config))
            args=argparse.Namespace(config=config_file,days=14,repo=None,output=output)
            info={'source':SOURCE['repo'],'status':'ok'}
            def collect(*_):return [copy.deepcopy(item)],[],[],info
            with patch.object(radar,'utcnow',return_value=NOW),patch.object(radar,'token',return_value=None),patch.object(radar,'collect_repo',side_effect=collect):
                self.assertEqual(radar.run_collect(args),0)
                self.assertEqual(radar.run_collect(args),0)
                run=json.loads((output/'data/latest.json').read_text())
                self.assertEqual(run['changes_this_run'],0)
                day=json.loads((output/'data/daily/2026-11-05.json').read_text())
                self.assertEqual(len(day['events']),1)
                item['status']='merged'
                radar.run_collect(args)
                day=json.loads((output/'data/daily/2026-11-05.json').read_text())
                self.assertEqual(len(day['events']),2)
                self.assertTrue((output/'reports/weekly.md').exists())

    def test_all_failed_keeps_previous_files(self):
        with tempfile.TemporaryDirectory() as directory:
            output=Path(directory)
            config=copy.deepcopy(CONFIG);config['repositories']=[SOURCE];config['feeds']=[]
            cfg=output/'watch.json';cfg.write_text(json.dumps(config))
            sentinel=output/'data/latest.json';sentinel.parent.mkdir();sentinel.write_text('{"previous":true}')
            args=argparse.Namespace(config=cfg,days=14,repo=None,output=output)
            with patch.object(radar,'token',return_value=None),patch.object(radar,'collect_repo',return_value=([],[{'source':'x','error':'failed'}],[],{'source':'x','status':'failed'})):
                with self.assertRaises(RuntimeError):radar.run_collect(args)
            self.assertEqual(sentinel.read_text(),'{"previous":true}')


if __name__=='__main__':unittest.main()
