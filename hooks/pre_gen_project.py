import subprocess

remote = '{{cookiecutter.git_remote}}'
branch_name = 'origin/{{cookiecutter.git_remote_master_branch}}'
subprocess.call(['git', 'init'])
if remote != 'Git remote (if known)':
    subprocess.call(['git', 'remote', 'add', 'origin', remote])
subprocess.call(['git', 'fetch', '--all'])
subprocess.call(['git', 'checkout', branch_name])
