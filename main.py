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

canteen = Company(capacity=50,potential_clients=500,profit_margin=0.12)

cooks = [Cook() for i in range(5)]

canteen.add_workers(cooks)
workers = [Casher(),Casher(),Administrator(),Cleaner(),Cleaner()]
canteen.add_workers(workers)

for w in workers:
    w.workability=random.randint(6,10)/10


expenses = [Expense('water',40000),Expense('Electricity',40000),Expense('Security',50000)]

potential_clients = [Client() for i in range(canteen.potential_clients)]

canteen.working_hours = [Timer(hour=10),Timer(hour=20)]


last_month = world.global_timer.month
count_people = 0
happines = 0

while True:
    #print(world.global_timer)
    #print("Clients waiting: ",len(canteen.clients))
    #print("Clients being served: ", len(canteen.being_cooked))
    #print("Clients eating: ", len(canteen.eating))
    #print("Balance: ", canteen.balance)
    #print()
    if (canteen.working_hours[0].hour < world.global_timer.hour < canteen.working_hours[1].hour):
        free_potential_clients = [c for c in potential_clients if c.visiting_time == None]
        new_clients = [c for c in free_potential_clients if random.random()*5 < c.visiting_prob]

        count_people += len(new_clients)

        canteen.add_client(new_clients,world.global_timer)
        canteen.cook_orders()
        canteen.serve_orders(world.global_timer)
        canteen.remove_clients(world.global_timer)
        

        if world.global_timer.month != last_month:
            print("Balance before: ", canteen.balance)
            canteen.subtract_montly_loss()
            last_month = world.global_timer.month
            print("Balance after: ", canteen.balance)
            print("Clients per month: ", count_people)
            happines = sum([c.satisfaction for c in potential_clients]) / count_people
            print("Happines: ", happines)
            count_people = 0
            
              
        for p in potential_clients:
            p.calculate_visiting_prob(world.global_weather)
            
    world.update()

            
    
