# This module validates the input provided by the user
# in terms of mathematical correctness of an expression
# intended to be integrated, as well as validity of
# entered integration options (integral limits, step size)

from Polynomial import *
import re


errordict = {0: 'Empty data',  # key=error code, value=error description
             1: 'Function formula contain illegal character(s)',
             6: 'Function formula contain illegal pattern(s) (e.g. \"--\" or floating point power)',
             2: 'Options are of invalid type or contain illegal characters',
             3: 'Too short option list',
             4: 'Too long option list',
             5: 'Step size larger than integration range'}

class InputValidator:
    def __init__(self, inputdata=((), ())):
        self.inputdata = inputdata
        self.isvalid = False
        self.parameters = {}
        self.opts = []

    def run(self, indata=((), ())):
        positives, negatives = [], []  # lists with positive and negative elements of polynomial
        if self.validateinput(indata):  # validation successful, extract function parameters
            params = re.split(r'\+', self.inputdata[0])  # extraction of positive and negative polynomial elements
            for i in params:
                j = re.split(r'\-', i)
                if j[0]:
                    positives.append(j[0])
                for t in j[1:]:
                    negatives.append(t)
            self.extractparameters(positives, 1)
            self.extractparameters(negatives, -1)
            self.opts = [float(x) for x in self.inputdata[1]]

    def extractparameters(self, parliststr, sign):
        for i in parliststr:
            if re.search('x', i) is None:  # possible only if x^0
                self.addparameter(sign*float(i), 0)
            else:  # higher order polynomial elements
                j = re.split(' |x|\*x|\* *x|x *|\^|\^ *', i)
                firstBlank = False
                if j[0] == '' or j[0] == ' ':
                    firstBlank = True
                j = [x for x in j if x is not '']
                if len(j) == 0:
                    self.addparameter(1, 1)
                elif len(j) == 1:
                    if firstBlank:
                        self.addparameter(sign, int(j[0]))
                    else:
                        self.addparameter(sign*float(j[0]), 1)
                else:
                    self.addparameter(sign*float(j[0]), int(j[1]))

    def addparameter(self, coef, power):
        if self.parameters.has_key(power):
            self.parameters[power] += coef
        else:
            self.parameters[power] = coef

    def validateinput(self, inputdata=((), ())):
        errorsfound = []  # initialize (empty) list of errors found during validation
        if inputdata != ((), ()):  # method invoked with some input, store it in this instance
            self.inputdata = inputdata
        if self.inputdata == ((), ()):  # empty data
            errorsfound.append(0)
        else:  # data not empty, proceed with checks
            if re.sub('[0-9]|\*|x|\^| |\+|\-|\.', '', self.inputdata[0]) != '':
                errorsfound.append(1)  # input contains disallowed chars
            if re.search('\^\+|\^\-|[0-9]*\.[0-9]*\.[0-9]*|\.\.|\-\-|\^[0-9]*\.[0-9]*|xx', self.inputdata[0]) is not None:
                errorsfound.append(6)  # input contains disallowed pattern
            if len(self.inputdata[1]) < 2:  # too short option list
                errorsfound.append(3)
            elif len(self.inputdata[1]) > 3:  # too long option list
                errorsfound.append(4)
            else:  # correct number of options, can perform additional checks
                allnumbers = True
                for i in self.inputdata[1]:  # loop over opts to check if they are numbers
                    try:
                        float(i)
                    except ValueError:  # exception thrown, not a number
                        errorsfound.append(2)
                        allnumbers = False
                        break
                if allnumbers and len(self.inputdata[1]) == 3:  # check for valid step size, only possible if provided options are numbers
                    if abs(float(self.inputdata[1][0])-float(self.inputdata[1][1])) < abs(float(self.inputdata[1][2])):
                        errorsfound.append(5)
        if len(errorsfound) == 0:  # no errors
            self.isvalid = True
            print 'Input data successfully passed validation check'
        else:
            self.isvalid = False  # validation failed, print list of errors
            print 'Errors have been found during input validation:'
            for i in errorsfound:
                print ' -> ' + errordict[i]
        return self.isvalid

    def function(self):
        return Polynomial(self.parameters.items())

    def options(self):
        return tuple(self.opts)
