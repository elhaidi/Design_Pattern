import abc

class AbsOrderCommand:
    __metaclass__= abc.ABCMeta

    @abc.abstractproperty
    def name(self):
        pass
    

    @abc.abstractproperty
    def description:
        pass