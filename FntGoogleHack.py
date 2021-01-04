# @name:    Katana-DorkScanner
# @repo:    https://github.com/adnane-X-tebbaa/Katana
# @author:  Adnane tebbaa (AXT)
# Main-file V2.0
from banner import banner
import argparse
from termcolor import colored

banner.gh()

parser = argparse.ArgumentParser(prog='FntGoogleHack.py',
                                 description='Uses advanced search operators (Google Dorks) to find juicy information about target websites')
parser.version = '1.0'
parser.add_argument("domain", type=str, help="target domain")
parser.add_argument("-f", "--file", help="find juicy information about target files", action='store_true')
parser.add_argument("-i", "--info", help="find juicy information about target websites", action='store_true')
parser.add_argument("-e", "--error", help="find juicy information about target errors", action='store_true')
parser.add_argument("-g", "--github", help="ind juicy information about target Github.com", action='store_true')
parser.add_argument("-p", "--pastebin", help="ind juicy information about target Pastebin.com", action='store_true')
parser.add_argument("-s", "--stackoverflow", help="ind juicy information about target Stackoverflow.com",
                    action='store_true')

args = parser.parse_args()

if args.file:
    from modes import file
if args.info:
    from modes.info import info
    info(args.domain)

if args.error:
    from modes import error
if args.github:
    from modes import github
if args.pastebin:
    from modes import pastebin
if args.stackoverflow:
    from modes import stackoverflow

print(colored('[! >] delete .google-cookie file in FNT DIR  ', 'red'))