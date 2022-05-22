from timer import Timer

class Expense:
    def __init__(self, name, cost, period = Timer(month=1)):
        self.name = name
        self.cost = cost
        self.period = period
