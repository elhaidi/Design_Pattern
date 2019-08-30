import abc

class AbsCommand:
    __metaclass_=abc.ABCMeta

    @abc.abstractmethod
    def execute(self):
        pass