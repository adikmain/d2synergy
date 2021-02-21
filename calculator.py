import abc


class Calculator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self):
        pass




