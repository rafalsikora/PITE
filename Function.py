# An abstract class representing one-dimensional function
# of a mathematical form y = f(x)

import abc


class Function:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        return

    @property
    def expression(self):
        assert isinstance(self.expressionstr, str)
        return self.expressionstr

    @abc.abstractmethod
    def __call__(self, x):
        return

    @abc.abstractmethod
    def __str__(self):
        return