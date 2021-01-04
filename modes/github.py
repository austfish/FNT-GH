from libs.google import GoogleSearch
from banner import banner
from termcolor import colored


def github(target):
    banner.github()

    github_modes = {
        'Github': 'site:github.com | site:gitlab.com '
        }
    for mode in github_modes:
        print(colored(f'[+] github-{mode}', 'green'))
        query = f'{github_modes[mode]}"{target}"'
        GoogleSearch(query)
    print(colored('[+] Done  ', 'green'))

