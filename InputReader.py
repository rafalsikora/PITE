# This module is responsible for reading
# the input file/input from console

import os.path

class InputReader:
    def __init__(self, args):
        self.datalist, self.filename = ['', []], ''
        if len(args) > 1:
            self.filename = args[1]
            self.readfile()
            self.datalist[1] = tuple(args[2:])
        else:
            self.readconsole()

    def readfile(self):
        if os.path.isfile(self.filename):
            print "Reading a file " + self.filename
            f = open(self.filename)
            self.datalist[0] = f.read()
            print "File content: " + self.datalist[0]
        else:
            print "Couldn't find a file " + self.filename + ". Switching to console..."
            self.readconsole()

    def readconsole(self):
        self.datalist[0] = raw_input("Please enter polynomial expression: ")
        options = raw_input("Please enter integration limits"
                            "(and optionally step size) separated with blanks: ").split()
        self.datalist[1] = tuple(options)

    def data(self):
        return tuple(self.datalist)
