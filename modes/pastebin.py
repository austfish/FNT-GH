from libs.google import GoogleSearch
from banner import banner
from termcolor import colored


def pastebin(target):
    banner.pastebin()

    pastebin_modes = {
        'Pastebin': 'site:pastebin.com | site:paste2.org | site:pastehtml.com | site:slexy.org | site:snipplr.com | site:snipt.net | site:textsnip.com | site:bitpaste.app | site:justpaste.it | site:heypasteit.com | site:hastebin.com | site:dpaste.org | site:dpaste.com | site:codepad.org | site:jsitor.com | site:codepen.io | site:jsfiddle.net | site:dotnetfiddle.net | site:phpfiddle.org | site:ide.geeksforgeeks.org | site:repl.it | site:ideone.com | site:paste.debian.net | site:paste.org | site:paste.org.ru | site:codebeautify.org  | site:codeshare.io | site:trello.com '
        }
    for mode in pastebin_modes:
        print(colored(f'[+] Pastebin-{mode}', 'green'))
        query = f'{pastebin_modes[mode]}"{target}"'
        GoogleSearch(query)
    print(colored('[+] Done  ', 'green'))

