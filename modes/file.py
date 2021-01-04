from libs.google import GoogleSearch, clear
from banner import banner
from termcolor import colored, cprint


def file(target):
    banner.file()

    file_modes = {'documents': ' ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv',
                  'Directory': ' intitle:index.of',
                  'Configuration': ' ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env',
                  'Database ': ' ext:sql | ext:dbf | ext:mdb',
                  'Log': ' ext:log',
                  'Backup ': ' ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup',
                  }
    for mode in file_modes:
        print(colored(f'[+] File-{mode}', 'green'))
        query = f'site:{target}{file_modes[mode]}'
        GoogleSearch(query)
    print(colored('[+] Done  ', 'green'))