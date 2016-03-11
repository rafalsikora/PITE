# A class representing Nth-order polynomial function y = SUM_i^N{ a_i * x^i }

from Function import *


class Polynomial(Function):
    def __init__(self, parametertuple):
        super(Polynomial, self).__init__()
        self.par = parametertuple
        self.expressionstr = self.formexpression()
        print 'Unified expression for created polynomial: ' + self.expression

    def __call__(self, x):
        res = 0
        for p in self.par:
            res += p[1] * x ** p[0]
        return res

    def __str__(self):
        return self.expression

    def formexpression(self):  # forming a string with unified form of a polynomial
        res = 'f(x) = '
        if len(self.par) == 0:
            return res + '0'
        isfirst = True
        for p in self.par:
            if isfirst:
                prep = str(abs(p[1]))
                isfirst = False
            else:
                prep = ' + ' + str(abs(p[1]))
            if p[1] < 0:
                prep = ' - ' + str(abs(p[1]))
            if p[0] is not 0 and p[0] is not 1:
                res += prep + '*x^' + str(p[0])
            elif p[0] is 1:
                res += prep + '*x'
            else:
                res += prep
        return res