import abc
from .observer_abc import AbsObserver

class AbsSubject:
    __metaclass__=abc.ABCMeta
    _observers = set()
    
    def attach(self,observer):
        if not isinstance(observer,AbsObserver):
            raise TypeError('Observer not derived from AbsObserver')
        self._observers.add(observer)
    
    def detach(self,observer):
        self._observers -= {observer}

    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.notify()
            else:
                observer.notify(value)
