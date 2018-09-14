from lib.output.Output import Output
from lib.args.Args import Args
from lib.searchengine.Google import Google
from lib.list.Dictionary import Dictionary
from lib.list.Generator import Generator
from lib.http.HttpDirectory import HttpDirectory
from lib.http.HttpFile import HttpFile
from lib.http.HttpRoute import HttpRoute
import concurrent.futures

class WebCatcher(object):
    def __init__(self):
        self.output = Output()
        self.args = Args().parse_args()
        self.start()

    def start(self):
        if self.args.searchengine:
            self.google = Google(self.args.url, self.args.pages)
            self.output.searchengine(self.google.result, type(self.google).__name__)
        try:
            self.args.extensions = self.args.extensions.split(',')
        except:
            pass        
        if self.args.wordlist:
            self.wordlist = Dictionary(self.args.wordlist, self.args.extensions)
        elif self.args.charset:
            self.wordlist = Generator(self.args.charset, self.args.minimum, self.args.maximum, self.args.extensions)
        
        if 'd' in self.args.type:
            self.httpDirectory = HttpDirectory(self.args.url)
            self.requester(self.httpDirectory, self.wordlist.directories)
        if self.args.extensions:
            self.httpFile = HttpFile(self.args.url)
            self.requester(self.httpFile, self.wordlist.files)
        if 'r' in self.args.type:
            self.args.method = 'options'
            self.httpRoute = HttpRoute(self.args.url)
            self.requester(self.httpRoute, self.wordlist.directories)
    
    def requester(self, function, wordlist):
        if self.args.method == 'get':
            if self.args.body:
                function = function.body
                if self.args.notstring:
                    with concurrent.futures.ProcessPoolExecutor() as executor:
                        for response in zip(self.wordlist.directories, executor.map(function, wordlist)):
                            self.output.notBody(response[1][0], response[1][1], response[1][2], self.args.notstring)
                else:
                    with concurrent.futures.ProcessPoolExecutor() as executor:
                        for response in zip(self.wordlist.directories, executor.map(function, wordlist)):
                            self.output.inBody(response[1][0], response[1][1], response[1][2], self.args.string)
            else:
                function = function.get
                with concurrent.futures.ProcessPoolExecutor() as executor:
                    for response in zip(self.wordlist.directories, executor.map(function, wordlist)):
                        self.output.status(response[1][0], response[1][1])
        else:
            function = function.options
            with concurrent.futures.ProcessPoolExecutor() as executor:
                for response in zip(self.wordlist.directories, executor.map(function, wordlist)):
                    self.output.header(response[1][0], response[1][1], response[1][2])
    
if __name__ == "__main__":
    main = WebCatcher()