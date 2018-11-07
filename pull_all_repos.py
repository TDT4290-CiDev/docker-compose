import os
import sys

organization_url = 'git@github.com:TDT4290-CiDev/'


def pull_all_repos(checkout_master=False):
    print("Updating docker-compose repo before pulling other repos...")
    if checkout_master:
        os.system('git checkout master')
    os.system('git pull')
    print('\n')

    with open('repositories.txt') as f:
        repos = f.read().split('\n')

    os.chdir('..')
    for repo in repos:
        print('Pulling', repo)
        if os.path.isdir(repo):
            os.chdir(repo)
            if checkout_master:
                os.system('git checkout master')
            os.system('git pull')
            os.chdir('..')
        else:
            os.system('git clone {}{}.git'.format(organization_url, repo))
        print('\n')


if __name__ == '__main__':
    checkout_master = False
    for arg in sys.argv[1:]:
        if arg in ['--master', '-m']:
            checkout_master = True
    pull_all_repos(checkout_master)
