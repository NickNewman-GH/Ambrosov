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
        self.max_comfort_pres = random.choice(Weather.pres_states)
        
    def enter_a_place(self, current_time):
        self.visiting_time = current_time
        self.order_waiting_time = Timer(min=random.randint(5, 59), hour=random.randint(0, 1))
        self.eating_time = Timer(min=random.randint(5, 59))
        self.state = "Waiting for order"

    def exit_a_place(self, is_order_done, is_mistake):
        self.change_satisfaction(is_order_done, is_mistake)
        self.visiting_time = None
        self.order_waiting_time = None
        self.eating_time = None
        self.state = "Potential client"

    def change_satisfaction(self, is_order_done, is_mistake):
        if is_order_done:
            self.satisfaction += (1 - self.satisfaction)*0.10
        else: 
            self.satisfaction -= (self.satisfaction)*0.25

        if is_mistake:
            self.satisfaction -= (self.satisfaction)*0.2


    def tell_about_experience_to_other_client(self, client):
        if isinstance(client, Client):
            client.satisfaction += (self.satisfaction - client.satisfaction) * 0.025

    def calculate_visiting_prob(self, weather):
        visiting_prob_base = 0.01
        if self.temp_preferences == weather.temperature:
            visiting_prob_base *= 1.5
        else: visiting_prob_base /= 1.5
        if Weather.pres_states.index(self.max_comfort_pres) >= Weather.pres_states.index(weather.presipitation):
            visiting_prob_base *= 1.5
        else: visiting_prob_base /= 1.5
        self.visiting_prob = visiting_prob_base * self.satisfaction

    def __str__(self) -> str:
        return f"Temp prefs: {self.temp_preferences}, max comfort pres: {self.max_comfort_pres}"