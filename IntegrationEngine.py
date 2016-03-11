# This is the integration engine, which means set of
# functions calculating integral in given argument limits
# using chosen integration method.

import numpy


class IntegrationEngine:
    def __init__(self, method='trapez', step=0.0001):
        self.integrationMethods = {'trapez': self.trapez,
                                   'rectangle': self.rectangle}
        self.method = method
        self.step = abs(step)

    def setmethod(self, method):
        self.method = method

    def setstep(self, step):
        self.step = step

    # 1-function, 2-limit_down, 3-limit_up, 4-step
    def integrate(self, *args):
        assert(len(args) >= 3)  # make sure that enough args have been provided
        if len(args) == 4:  # set step size if provided
            self.setstep(args[3])
        res, sign = 0.0, 1  # initialize values needed for integration
        a, b = args[1], args[2]

        if a > b:  # if lower limit > upper limit then do some swap
            b, a = a, b
            sign = -1

        for x in numpy.arange(a, b, self.step):  # integration loop
            res += self.integrationMethods[self.method](args[0], x)

        return sign*res

    def trapez(self, func, x):  # single-step integral using trapez method
        return self.step*(func(x)+func(x+self.step))/2

    def rectangle(self, func, x):  # single-step integral using rectangular method
        return self.step*func(x+self.step/2)


# self-test
if __name__ == '__main__':
    xlimit = 100
    kernel = IntegrationEngine("trapez", xlimit/1e3)
    int1 = kernel.integrate(lambda x: x, 0, xlimit)
    int2 = kernel.integrate(lambda x: x, xlimit, 0)
    int3 = kernel.integrate(lambda x: x, xlimit, xlimit)
    assert(numpy.allclose(int1, xlimit**2/2))
    assert(numpy.allclose(int1, -int2))
    assert(numpy.allclose(int3, 0))
    print('Self-test in '+kernel.__class__.__name__+' completed with no errors.')
