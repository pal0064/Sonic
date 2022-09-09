import subprocess

packages = [
    'pathlib2',
    'pip',
    'setuptools',
    'wheel',
]

pip_only_packages = [
    'pre-commit',
]

dependencies = 'requirements.txt'

def write_dependencies():
    with open(dependencies, 'w') as f:
        lines = sorted(packages + pip_only_packages)

        lines += [
            ""
            "-e ."
        ]

        f.write("\n".join(lines))
        f.write("\n")

write_dependencies()
master_branch_name ='{{cookiecutter.git_remote_master_branch}}'
remote = '{{cookiecutter.git_remote}}'
subprocess.call(['git', 'add', '.'])
subprocess.call(['git', 'commit', '-m', 'feat(core): initialization using cookiecutter'])
subprocess.call(['pre-commit', 'install'])

