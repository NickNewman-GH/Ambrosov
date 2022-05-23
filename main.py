import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
happy_recommend_prob = 0.2

consecutive_client_decrease = 0
consecutive_client_decrease_thresh = 3


#arrays for plots

profit = []
client_num = []

min_sat_arr = []
max_sat_arr = []

x = 0
x_vals = []

last_week = Timer(day=0)
last_year = 0

while True:

    if (canteen.working_hours[0].hour < world.global_timer.hour < canteen.working_hours[1].hour):
        free_potential_clients = [c for c in potential_clients if c.visiting_time == None]
        new_clients = [c for c in free_potential_clients if random.random()*3 < c.visiting_prob]

        count_people += len(new_clients)

        canteen.add_client(new_clients,world.global_timer)
        canteen.cook_orders()
        canteen.serve_orders(world.global_timer)
        canteen.remove_clients(world.global_timer)

        if (last_week + Timer(day=7)).day == world.global_timer.day:
            min_sat = min([c.satisfaction for c in potential_clients])
            max_sat = max([c.satisfaction for c in potential_clients])
            
            max_sat_arr.append(max_sat)
            min_sat_arr.append(min_sat)
            last_week += Timer(day=7)
            x_vals.append(x)
            x+=1
            

        

        if world.global_timer.month != last_month:
            min_sat = min([c.satisfaction for c in potential_clients])
            max_sat = max([c.satisfaction for c in potential_clients])

            very_happy_clients = [c for c in potential_clients if c.satisfaction > 0.92]
            very_unhappy_clients = len(potential_clients)

            last_clients_num = len(potential_clients)
            
            potential_clients = [c for c in potential_clients if c.satisfaction > 0.3]

            very_unhappy_clients -= len(potential_clients)
            
            potential_clients += [Client() for i in range(len(very_happy_clients)) if random.random() < happy_recommend_prob]

            cur_clients_num = len(potential_clients)

            if (last_clients_num > cur_clients_num):
                consecutive_client_decrease += 1

            if (consecutive_client_decrease >= consecutive_client_decrease_thresh):
                mean_workability = sum([c.workability for c in cooks])/len(cooks)

                cooks_to_fire = [c for c in cooks if c.workability < mean_workability]

                for cook in cooks_to_fire:
                    cook.workability = random.randint(6,10)/10

                consecutive_client_decrease = 0

            client_num.append(cur_clients_num)
                    

            
            print(world.global_timer)
            print("Balance before: ", canteen.balance)
            canteen.subtract_montly_loss()
            last_month = world.global_timer.month
            print("Balance after: ", canteen.balance)
            print("Profit:", canteen.balance - last_balance)
            print("Clients per month: ", count_people)
            print("Max sat: ", max_sat)
            print("Min sat: ", min_sat)
            print("very happy: ", len(very_happy_clients))
            print("very unhappy: ", very_unhappy_clients)
            print(len(potential_clients))
            print()

            profit.append(canteen.balance - last_balance)
            
            count_people = 0
            last_balance = canteen.balance


        if (world.global_timer.month + 1) % 12 == 0 and last_year != (world.global_timer.month + 1) // 12 :
            fig = plt.figure()
            ax1 = fig.add_subplot(1, 3, 1)
            ax2 = fig.add_subplot(1, 3, 2)
            ax3 = fig.add_subplot(1, 3, 3)
            ax1.clear()
            
            ax1.plot(x_vals,max_sat_arr, linestyle="--")
            ax1.plot(x_vals,min_sat_arr, linestyle="--")

            ax1.legend(["Max sat","Min sat"])
            ax1.set_xlabel("Weeks")
            ax1.set_ylabel("Values")


            ax2.clear()
            ax2.plot([i for i in range(len(client_num))],client_num)
            ax2.legend(["client num"])
            ax2.set_xlabel("Months")
            ax2.set_ylabel("Values")

            ax3.clear()
            ax3.plot([i for i in range(len(profit))],profit)
            ax3.legend(["profit"])
            ax3.set_xlabel("Months")
            ax3.set_ylabel("Values")
            
            plt.show()

            last_year = (world.global_timer.month + 1) // 12
            

              
        for p in potential_clients:
            p.calculate_visiting_prob(world.global_weather)
            
    world.update()

            
    
