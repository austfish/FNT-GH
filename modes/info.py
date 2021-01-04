from libs.google import GoogleSearch
from banner import banner
from termcolor import colored


def info(target):
    banner.info()

    info_modes = {'login': ' inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:auth',
                  'signup': ' inurl:signup | inurl:register | intitle:Signup',
                  'phpinfo': ' ext:php intitle:phpinfo "published by the PHP Group"'}
    for mode in info_modes:
        print(colored(f'[+] Info-{mode}', 'green'))
        query = f'site:{target}{info_modes[mode]}'
        GoogleSearch(query)
    print(colored('[+] Done  ', 'green'))

