import random
from timer import Timer

class Client():
    def __init__(self):
        self.age = random.randint(14, 95)
        self.avg_check = random.randint(300, 3000)
        self.state = "Potential"
        self.eating_time = None
        self.visiting_prob = None
        self.satisfaction = 0
        self.visiting_time = None
        self.order_waiting_time = None

    def enter_a_place(self, current_time):
        ...

    def exit_a_place(self):
        ...

    def calculate_visiting_prob(self):
        ...

    def change_satisfaction(self, is_order_done):
        ...

    def calculate_visiting_prob(self, temp, precipitation):
        ...