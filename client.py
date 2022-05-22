import random
from timer import Timer
from weather import Weather

class Client():
    def __init__(self):
        self.age = random.randint(14, 95)
        self.avg_check = random.randint(300, 3000)
        self.state = "Potential client"
        self.eating_time = None
        self.visiting_prob = 0
        self.satisfaction = 0.5
        self.visiting_time = None
        self.order_waiting_time = None
        self.temp_preferences = random.choice(Weather.temp_states[1:-1])
        self.pres_preferences = random.choice(Weather.pres_states)
        
    def enter_a_place(self, current_time):
        self.visiting_time = current_time
        self.order_waiting_time = Timer(min=random.randint(5, 59), hour=random.randint(0, 1))
        self.eating_time = Timer(min=random.randint(5, 59))
        self.state = "Waiting for order"

    def exit_a_place(self, is_order_done):
        self.change_satisfaction(self, is_order_done)
        self.visiting_time = None
        self.order_waiting_time = None
        self.eating_time = None
        self.state = "Potential client"

    def change_satisfaction(self, is_order_done):
        if is_order_done: self.satisfaction += (1 - self.satisfaction)*0.25
        else: self.satisfaction -= (self.satisfaction)*0.25

    def tell_about_experience_to_other_client(self, client):
        if isinstance(client, Client):
            client.satisfaction += (self.satisfaction - client.satisfaction) * 0.1

    def calculate_visiting_prob(self, weather):
        visiting_prob_base = 0.1
        self.visiting_prob = 0
