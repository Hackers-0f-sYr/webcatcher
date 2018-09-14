import argparse
from sys import argv

class Args(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        

    def parser_error(self, errmsg):
        print("Usage: python " + argv[0] + " use -h for help")
        print("Error: {}".format(errmsg))
        exit()

    def parse_args(self):
        self.parser._optionals.title = "OPTIONS"
        self.parser.add_argument('-u', '--url', help="URL target, example: -u http://example.com/")
        self.parser.add_argument('-w', '--wordlist', help='wordlist, example: -w wordlists/dirb-common.txt')
        self.parser.add_argument('-c', '--charset', help='charset for list generator example: -c az,AZ,09')
        self.parser.add_argument('-min', '--minimum', help='minimum length for list generator', type=int, default=1)
        self.parser.add_argument('-max', '--maximum', help='maximum length for list generator', type=int, default=4)
        self.parser.add_argument('-e', '--extensions', help='extensions, example: php,txt,zip', default = [])
        self.parser.add_argument('-t', '--type', help='search for f:files, d:directories, r:routes example: -t d,f,r', default='d')
        self.parser.add_argument('-m', '--method', help='search based on method example: -m get || -m options', default='get')
        self.parser.add_argument('-b', '--body', help='flag to check for a match of either --notstring or --string, example: -b true')
        self.parser.add_argument('--notstring', help='the string does not exist in the body, example: --notstring "Hello World"')
        self.parser.add_argument('--string', help='the string does is exist in the body, example: --string "Hello World"')
        self.parser.add_argument('-s', '--searchengine', help='search engine (only google now) example: -s google')
        self.parser.add_argument('-p', '--pages', help='expected pages for search engine example: -p 10', type=int, default=4)
        return self.parser.parse_args()