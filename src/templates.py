import abc


class Calculator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self):
        pass


class Assistant(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def assist(self):
        pass
