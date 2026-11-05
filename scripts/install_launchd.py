#!/usr/bin/env python3
"""Install/remove a per-user macOS launchd schedule. No tokens are written to plist."""
import argparse
import os
from pathlib import Path
import plistlib
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
LABEL='org.xixiaxibro.mcp-radar'


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['install','remove','status'])
    parser.add_argument('--hour',type=int,default=9)
    parser.add_argument('--minute',type=int,default=17)
    args=parser.parse_args()
    if sys.platform!='darwin':
        parser.error('This installer is for macOS; use the GitHub workflow or your own scheduler elsewhere.')
    if not 0<=args.hour<=23 or not 0<=args.minute<=59:
        parser.error('Invalid local clock time')
    domain=f'gui/{os.getuid()}'
    service=f'{domain}/{LABEL}'
    destination=Path.home()/'Library/LaunchAgents'/f'{LABEL}.plist'
    if args.command=='status':
        return subprocess.run(['launchctl','print',service]).returncode
    if args.command=='remove':
        subprocess.run(['launchctl','bootout',service],capture_output=True)
        destination.unlink(missing_ok=True)
        print('Removed '+str(destination))
        return 0
    if destination.exists():
        raise RuntimeError('Schedule already exists; inspect or remove it before reinstalling.')
    for required in ['gh','git','ssh']:
        if not shutil.which(required):
            raise RuntimeError(required+' must be installed and available on PATH')
    logs=Path.home()/'Library/Logs/mcp-radar';logs.mkdir(parents=True,exist_ok=True)
    paths=[]
    for path in [str(Path(sys.executable).parent),str(Path(shutil.which('gh')).parent),'/opt/homebrew/bin','/usr/local/bin','/usr/bin','/bin','/usr/sbin','/sbin']:
        if path not in paths:paths.append(path)
    job={
        'Label':LABEL,
        'ProgramArguments':[sys.executable,str(ROOT/'scripts/run_scheduled.py')],
        'WorkingDirectory':str(ROOT),
        'StartCalendarInterval':{'Hour':args.hour,'Minute':args.minute},
        'RunAtLoad':False,
        'EnvironmentVariables':{'PATH':':'.join(paths),'PYTHONUNBUFFERED':'1','GIT_TERMINAL_PROMPT':'0'},
        'StandardOutPath':str(logs/'stdout.log'),
        'StandardErrorPath':str(logs/'stderr.log'),
    }
    destination.parent.mkdir(parents=True,exist_ok=True)
    with destination.open('wb') as output:plistlib.dump(job,output)
    try:
        subprocess.run(['launchctl','bootstrap',domain,str(destination)],check=True)
    except Exception:
        destination.unlink(missing_ok=True)
        raise
    print(f'Installed {service}: daily {args.hour:02d}:{args.minute:02d} local time')
    print('Plist: '+str(destination))
    print('Logs: '+str(logs))
    print('Test once: launchctl kickstart '+service)
    print('Disable: '+sys.executable+' '+str(ROOT/'scripts/install_launchd.py')+' remove')
    return 0


if __name__=='__main__':
    try:raise SystemExit(main())
    except Exception as exc:
        print(str(exc),file=sys.stderr)
        raise SystemExit(1)
