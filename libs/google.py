import os

import requests
import proxybroker
from googlesearch import search
from banner import banner
import sys
import sys
from termcolor import colored, cprint
import warnings
import random
from http import cookiejar


class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False


def fxn():
    warnings.warn("deprecated", DeprecationWarning)


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


def GoogleSearch(query):
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/68.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) '
        'Gecko/20100101 Firefox/68.0',
        'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/68.0']
    TLD = ["com", "com.tw", "co.in", "be", "de", "co.uk", "co.ma", "dz", "ru", "ca"]
    beta = random.choice(TLD)
    s = requests.Session()
    s.cookies.set_policy(BlockAll())
    print(colored(f'[+] Google {query}  ', 'green'))
    for gamma in search(query, tld=beta, num=10, stop=95, pause=2, user_agent=random.choice(user_agents)):
        print(colored('[+] Found > ', 'yellow') + gamma)
