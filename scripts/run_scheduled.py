#!/usr/bin/env python3
"""Run a locked, clean-worktree collection and push only generated reports."""
from datetime import datetime, timezone
import fcntl
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def git(*args, check=True):
    return subprocess.run(['git', '-C', str(ROOT), *args], check=check, text=True, capture_output=True)


def main():
    os.environ.setdefault('GIT_SSH_COMMAND', 'ssh -o BatchMode=yes -o ConnectTimeout=15')
    os.environ['GIT_TERMINAL_PROMPT'] = '0'
    git_dir = Path(git('rev-parse', '--absolute-git-dir').stdout.strip())
    with (git_dir/'mcp-radar-schedule.lock').open('w') as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print('Another scheduled MCP Radar run is active; skipped.', flush=True)
            return 0
        print('Started '+datetime.now(timezone.utc).isoformat(timespec='seconds'), flush=True)
        if git('status','--porcelain').stdout.strip():
            raise RuntimeError('Worktree has uncommitted changes; scheduled run left them untouched.')
        branch=git('branch','--show-current').stdout.strip()
        if branch!='main':
            raise RuntimeError('Scheduled collection requires main; current branch left untouched.')
        git('pull','--ff-only','origin','main')
        result=subprocess.run([sys.executable,str(ROOT/'scripts/radar.py'),'collect','--days','14'])
        if result.returncode not in (0,2):
            return result.returncode
        git('add','--','data/','reports/')
        different=git('diff','--cached','--quiet',check=False)
        if different.returncode==1:
            git('commit','-m','data: update MCP activity and coverage report')
        elif different.returncode!=0:
            raise RuntimeError('Could not inspect generated changes.')
        git('push','origin','main')
        print('Finished '+datetime.now(timezone.utc).isoformat(timespec='seconds')+f'; collector exit {result.returncode}', flush=True)
        return result.returncode


if __name__=='__main__':
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        # Git may include user-provided remote data; do not print environment or credentials.
        print('Scheduled Git operation failed; inspect the local branch and remote connection.',file=sys.stderr)
        raise SystemExit(1)
    except Exception as exc:
        print(str(exc),file=sys.stderr)
        raise SystemExit(1)
