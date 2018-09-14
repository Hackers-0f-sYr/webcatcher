import pycurl
from io import BytesIO
from urllib.parse import quote_plus

class HttpFile(object):
    def __init__(self, url):
        if not url.endswith('/'):
            self.url = url + '/'
        else:
            self.url = url

    def get(self, path):
        target = self.url + quote_plus(path)
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, target)
        curl.setopt(pycurl.HEADER, False)
        curl.setopt(pycurl.NOBODY, True)
        curl.perform()
        return curl.getinfo(pycurl.RESPONSE_CODE), target
    
    def options(self, path):
        target = self.url + quote_plus(path)
        headers = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, target)
        curl.setopt(pycurl.HEADER, True)
        curl.setopt(pycurl.NOBODY, True)
        curl.setopt(pycurl.CUSTOMREQUEST, 'OPTIONS')
        curl.setopt(pycurl.WRITEDATA, headers)
        curl.perform()
        return curl.getinfo(pycurl.RESPONSE_CODE), headers.getvalue(), target

    def body(self, path):
        target = self.url + quote_plus(path)
        body = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, target)
        curl.setopt(pycurl.HEADER, False)
        curl.setopt(pycurl.WRITEDATA, body)
        curl.perform()
        return curl.getinfo(pycurl.RESPONSE_CODE), body.getvalue(), target