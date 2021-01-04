from libs.google import GoogleSearch
from banner import banner
from termcolor import colored


def error(target):
    banner.error()

    error_modes = {
        'SQL': ' intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()"',
        'PHP': ' "PHP Parse error" | "PHP Warning" | "PHP Error"'
        }
    for mode in error_modes:
        print(colored(f'[+] Error-{mode}', 'green'))
        query = f'site:{target}{error_modes[mode]}'
        GoogleSearch(query)
    print(colored('[+] Done  ', 'green'))
