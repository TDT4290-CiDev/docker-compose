import os

organization_url = 'git@github.com:TDT4290-CiDev/'


def pull_all_repos():
    with open('repositories.txt') as f:
        repos = f.read().split('\n')

    os.chdir('..')
    for repo in repos:
        if os.path.isdir(repo):
            os.chdir(repo)
            os.system('git pull')
            os.chdir('..')
        else:
            os.system('git clone {}{}.git'.format(organization_url, repo))


if __name__ == '__main__':
    pull_all_repos()
