#!/usr/bin/python3
# -*- coding:utf8 -*-
from termcolor import colored, cprint


def gh():
    banner = """
    __________________ ___________           ________   ___ ___  
    \_   _____/\      \\__    ___/          /  _____/  /   |   \ 
     |    __)  /   |   \ |    |     ______ /   \  ___ /    ~    \\
     |     \  /    |    \|    |    /_____/ \    \_\  \\    Y    /
     \___  /  \____|__  /|____|             \______  / \___|_  / 
         \/           \/                           \/        \/   v1.0


     * Fishing Net Tools-Google Hack (FNT-GH) coded by austfish
     * please use -h to see help
    """
    print(colored(banner, 'blue'))


def info():
    banner = """
    * Info Mode:
        - Login pages
        - phpinfo()
        - Signup pages
    """

    print(colored(banner, 'blue'))


def file():
    banner = """
   * File Mode:
        - Publicly exposed documents
        - Directory listing vulnerabilities
        - Configuration files exposed
        - Database files exposed
        - Log files exposed
        - Backup and old files
    """

    print(colored(banner, 'blue'))


def error():
    banner = """
   * File Mode:
        - SQL errors
        - PHP errors / warnings
    """

    print(colored(banner, 'blue'))


def github():
    banner = """
   * File Mode:
        - Search Github.com and Gitlab.com
    """

    print(colored(banner, 'blue'))


def pastebin():
    banner = """
   * File Mode:
        - Search Pastebin.com / pasting sites
    """

    print(colored(banner, 'blue'))


def stackoverflow():
    banner = """
   * File Mode:
        - Search Stackoverflow.com
    """

    print(colored(banner, 'blue'))