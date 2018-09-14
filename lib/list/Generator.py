from itertools import product

class Generator():
    def __init__(self, charset, minlength, maxlength, extensions = []):
        self.iterables = ''
        self.minlength = minlength
        self.maxlength = maxlength
        self.charset = charset
        self.extensions = extensions
        self.generate()
      
    def lowercaseAlphabets(self):
        alphabets = ''
        for alphabet in range(97, 123):
            alphabets = alphabets + chr(alphabet)
        return alphabets

    def uppercaseAlphabets(self):
        alphabets = ''
        for alphabet in range(65, 91):
            alphabets = alphabets + chr(alphabet)
        return alphabets

    def digits(self):
        digits = ''
        for digit in range(0, 10):
            digits = digits + str(digit)
        return digits

    def possibilities(self):
        possibilities = 0
        for base in range(self.minlength, self.maxlength + 1):
            possibilities = pow(len(self.iterables), base) 
        return possibilities
    
    def generate(self):
        self.directories = []
        self.files = []
        if('az' in self.charset):
            self.iterables += self.lowercaseAlphabets()
        if('AZ' in self.charset):
            self.iterables += self.uppercaseAlphabets()
        if('09' in self.charset):
            self.iterables += self.digits()

        for length in range(self.minlength, self.maxlength + 1):
            for element in product((self.iterables), repeat = length):
                self.directories.append(''.join('{0}'.format(''.join(element)))) 

        for extension in self.extensions:
            for element in product((self.iterables), repeat = length):
                self.files.append(''.join('{0}.{1}'.format(''.join(element), extension))) 