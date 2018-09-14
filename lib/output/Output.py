from lib.output.Banner import Banner
import sys

class Output(object):
    def __init__(self):
        self.banner()
    
    def banner(self):
        print(Banner())

    def status(self, responseCode, url, condition = 404):
        if responseCode != condition:
            sys.stdout.write('[{0}] {1}\n'.format(responseCode, url))
    
    def header(self, responseCode, headers, url, condition = 'allow'):
        if condition in str(headers).lower():
            sys.stdout.write('[{0}] {1}\n'.format(responseCode, url))
    
    def notBody(self, responseCode, body, url, condition):
        if condition not in str(body):
            sys.stdout.write('[{0}] {1}\n'.format(responseCode, url))
    
    def inBody(self, responseCode, body, url, condition):
        if condition in str(body):
            sys.stdout.write('[{0}] {1}\n'.format(responseCode, url))
    
    def searchengine(self, result, engine):
        for url in result:
            sys.stdout.write('[{0}] {1}\n'.format(engine, url))
