import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SPEC=importlib.util.spec_from_file_location('scheduled',Path(__file__).resolve().parents[1]/'scripts/run_scheduled.py')
scheduled=importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(scheduled)


class ScheduledTests(unittest.TestCase):
    def test_dirty_worktree_exits_before_pull_or_collection(self):
        with tempfile.TemporaryDirectory() as directory:
            calls=[]
            def git(*args,**kwargs):
                calls.append(args)
                return subprocess.CompletedProcess([],0,stdout=directory if args[0]=='rev-parse' else ' M README.md\n')
            with patch.object(scheduled,'git',side_effect=git),patch.object(scheduled.subprocess,'run') as run:
                with self.assertRaisesRegex(RuntimeError,'uncommitted'):
                    scheduled.main()
                self.assertFalse(run.called)
                self.assertFalse(any(c[0]=='pull' for c in calls))

    def test_only_generated_directories_are_staged(self):
        with tempfile.TemporaryDirectory() as directory:
            calls=[]
            def git(*args,**kwargs):
                calls.append(args)
                text=directory if args[0]=='rev-parse' else ('main\n' if args[0]=='branch' else '')
                return subprocess.CompletedProcess([],1 if args[0]=='diff' else 0,stdout=text)
            with patch.object(scheduled,'git',side_effect=git),patch.object(scheduled.subprocess,'run',return_value=subprocess.CompletedProcess([],0)):
                self.assertEqual(scheduled.main(),0)
            self.assertIn(('add','--','data/','reports/'),calls)
            self.assertIn(('pull','--ff-only','origin','main'),calls)
            self.assertIn(('push','origin','main'),calls)

    def test_failed_collection_does_not_commit_or_push(self):
        with tempfile.TemporaryDirectory() as directory:
            calls=[]
            def git(*args,**kwargs):
                calls.append(args)
                return subprocess.CompletedProcess([],0,stdout=directory if args[0]=='rev-parse' else ('main\n' if args[0]=='branch' else ''))
            with patch.object(scheduled,'git',side_effect=git),patch.object(scheduled.subprocess,'run',return_value=subprocess.CompletedProcess([],1)):
                self.assertEqual(scheduled.main(),1)
            self.assertFalse(any(c[0] in ('add','commit','push') for c in calls))


if __name__=='__main__':unittest.main()
