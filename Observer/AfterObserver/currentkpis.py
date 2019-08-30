from observer.observer_abc import AbsObserver

class CurrentKPIs(AbsObserver):
    open_tickets=-1
    closed_tickets=-1
    new_tickets=-1
    
    def __init__(self,kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()
    
    def display(self):
        print('current open tickets: {}'.format(self.open_tickets))
        print("New tickets : {}".format(self.new_tickets))
        print('The closed tickets are : {} '.format(self.closed_tickets))
    