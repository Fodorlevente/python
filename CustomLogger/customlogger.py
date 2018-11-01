from contextlib import contextmanager
from datetime import datetime

class CustomLogger(object):
    def __init__(self,file,mode):
        self.mode = mode
        self.file = file
    
    def __enter__(self):
        self.openfile = open(self.file,self.mode)
        self.openfile.write("Start Date: {}\n" .format(datetime.now()))
        return self.openfile
    
    def __exit__(self, *args):
        self.openfile.write("End Date: {}\n" .format(datetime.now()))
        self.openfile.close()

with CustomLogger("Customlog.txt", "a") as customlog:
    customlog.write('This is my custom log\n')