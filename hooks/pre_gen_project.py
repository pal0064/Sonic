import subprocess

master_branch_name ='{{cookiecutter.git_remote_master_branch}}'
remote = '{{cookiecutter.git_remote}}'
subprocess.call(['git', 'init'])
if remote != 'Git remote (if known)':
    subprocess.call(['git', 'remote', 'add', 'origin', remote])
    subprocess.call(['git', 'fetch', '--all'])
    subprocess.call(['git', 'checkout', 'origin/'+ master_branch_name])
    subprocess.call(['git', 'pull', 'origin/'+ master_branch_name])
subprocess.call(['git', 'checkout', '-b','feat/initialization-using-cookiecutter'])
