class Dictionary(object):
    def __init__(self, dictionaryfile, extensions = []):
        self.dictionaryfile = open(dictionaryfile, 'r')
        self.extensions = extensions
        self.generate()

    def generate(self):
        self.directories = []
        self.files = []
        for line in self.dictionaryfile:
            if line.lstrip().startswith("#"):
                continue
            else:
                self.directories.append(line.rstrip())
                for extension in self.extensions:
                     self.files.append(line.rstrip() + '.{}'.format(extension))