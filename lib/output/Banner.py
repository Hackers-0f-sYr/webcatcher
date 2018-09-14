from pyfiglet import Figlet

class Banner(object):
    def __init__(self):
       self.banner = Figlet(font='graffiti').renderText('Web Catcher')
    
    def __str__(self):
        return self.banner