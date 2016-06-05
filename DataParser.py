import re

class DataParser:

    def __init__(self):
        self.s = None

    def set_data(self, s):
        self.s = s

    def parse(self):
        if(self.s is not None):
            m = re.search('.*"top":(\d+),"left":(\d+),"width":(\d+),"height":(\d+).*', self.s)
            return {'top':int(m.group(1)),'left':int(m.group(2)),'width':int(m.group(3)),'height':int(m.group(4))}
