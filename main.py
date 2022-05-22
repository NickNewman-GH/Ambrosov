import random
import time

from timer import Timer
from company import Company
from world import World
from expense import Expense
from client import Client
from worker import Worker, Cook, Administrator, Casher, Cleaner


world = World()

world.change_adder(Timer(min=10))

canteen = Company(capacity=50,potential_clients=500,profit_margin=0.15)

cooks = [Cook() for i in range(5)]

for c in cooks:
    c.workability=random.randint(6,10)/10

canteen.add_workers(cooks)
workers = [Casher(),Casher(),Administrator(),Cleaner(),Cleaner()]
canteen.add_workers(workers)



expenses = [Expense('water',40000),Expense('Electricity',40000),Expense('Security',50000)]

potential_clients = [Client() for i in range(canteen.potential_clients)]

canteen.working_hours = [Timer(hour=10),Timer(hour=20)]


last_month = world.global_timer.month
last_balance = 0
count_people = 0
happines = 0
happy_recommend_prob = 0.15

while True:
    #print(world.global_timer)
    #print("Clients waiting: ",len(canteen.clients))
    #print("Clients being served: ", len(canteen.being_cooked))
    #print("Clients eating: ", len(canteen.eating))
    #print("Balance: ", canteen.balance)
    #print()
    if (canteen.working_hours[0].hour < world.global_timer.hour < canteen.working_hours[1].hour):
        free_potential_clients = [c for c in potential_clients if c.visiting_time == None]
        new_clients = [c for c in free_potential_clients if random.random()*3 < c.visiting_prob]

        count_people += len(new_clients)

        canteen.add_client(new_clients,world.global_timer)
        canteen.cook_orders()
        canteen.serve_orders(world.global_timer)
        canteen.remove_clients(world.global_timer)
        

        if world.global_timer.month != last_month:
            min_sat = min([c.satisfaction for c in potential_clients])
            max_sat = max([c.satisfaction for c in potential_clients])

            very_happy_clients = [c for c in potential_clients if c.satisfaction > max_sat-max_sat*0.05]
            very_unhappy_clients = len(potential_clients)
            
            potential_clients = [c for c in potential_clients if c.satisfaction > min_sat + min_sat*0.5]

            very_unhappy_clients -= len(potential_clients)
            
            potential_clients += [Client() for i in range(len(very_happy_clients)) if random.random() < happy_recommend_prob]

            
            print(world.global_timer)
            print("Profit:", canteen.balance - last_balance)
            print("Balance before: ", canteen.balance)
            canteen.subtract_montly_loss()
            last_month = world.global_timer.month
            print("Balance after: ", canteen.balance)
            print("Clients per month: ", count_people)
            print("Max sat: ", max_sat)
            print("Min sat: ", min_sat)
            print("very happy: ", len(very_happy_clients))
            print("very unhappy: ", very_unhappy_clients)
            print(len(potential_clients))
            print()
            count_people = 0
            last_balance = canteen.balance
            
              
        for p in potential_clients:
            p.calculate_visiting_prob(world.global_weather)
            
    world.update()

            
    
