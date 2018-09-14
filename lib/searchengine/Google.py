from googlesearch import search
from urllib.parse import urlparse

class Google(object):
   def __init__(self, url, pages = 4):
       self.domain = '{uri.netloc}'.format(uri=urlparse(url))
       self.pages = pages
       self.search()
    
   def search(self):
        self.result = []
        for url in search('site:{}'.format(self.domain), stop = (self.pages*10)):
            self.result.append(url)
