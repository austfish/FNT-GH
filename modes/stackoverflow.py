from libs.google import GoogleSearch
from banner import banner
from termcolor import colored


def stackoverflow(target):
    banner.stackoverflow()

    stackoverflow_modes = {
        'Stackoverflow': 'site:stackoverflow.com '
        }
    for mode in stackoverflow_modes:
        print(colored(f'[+] Stackoverflow-{mode}', 'green'))
        query = f'{stackoverflow_modes[mode]}"{target}"'
        GoogleSearch(query)
    print(colored('[+] Done  ', 'green'))

