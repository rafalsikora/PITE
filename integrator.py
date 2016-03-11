#!/usr/bin/python

# This program performs integration of a polynomial with parameters
# provided by the user. It checks correctness of those parameters
# and, if they pass validation test, calculates and prints the result.
# It also compares obtained result with the value of integral returned
# by scipy.integrate.quad module.
#
# You can invoke program twofold:
# 1. ./integrator.py FILENAME LIMIT_DOWN LIMIT_UP [STEP]
# 2. ./integrator.py
#
# FILENAME = path to file with polynomial expression
# LIMIT_DOWN = lower integration limit
# LIMIT_UP = upper integration limit
# STEP = size of integration step

from IntegrationEngine import *
from InputValidator import *
from InputReader import *
from scipy import integrate
import sys

print "Welcome to >>INTEGRATOR 2000<<"

reader = InputReader(sys.argv)  # get input
validator = InputValidator(reader.data())  # initialize validator
validator.run()  # validate input

if validator.isvalid:  # if input is valid, proceed with integral calculation
    func = validator.function()
    opts = validator.options()

    integrator = IntegrationEngine('trapez')  # initialization of an engine
    myintegral = integrator.integrate(func, *opts)  # calculate integral using own algorithm
    scipyintegral = integrate.quad(func, opts[0], opts[1]) # calculate integral using scipy library

    print 'Integral calculated with own algorithm        :\t' + str(myintegral)
    print 'Integral calculated with scipy.integrate.quad :\t' + str(scipyintegral[0])
    print 'Relative difference amounts ' + str(100*(myintegral-scipyintegral[0])/scipyintegral[0]) + '%'

    print "Thank you for using >>INTEGRATOR 2000<<  :-)"
else:
    print "Invalid input parameters, exiting >>INTEGRATOR 2000<<."

