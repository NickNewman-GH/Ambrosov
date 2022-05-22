import random
import time

from timer import Timer
from world import World
from expense import Expense
from client import Client
from worker import Worker, Cook


class Company:
    
    def __init__(self,name='Canteen',balance=0,capacity=0,potential_clients=0,profit_margin=0.1):
        self.name = name
        self.workers = []
        self.clients = []
        self.eating = []
        self.being_cooked = []
        self.balance = balance
        self.capacity = capacity
        self.profit_margin = profit_margin
        self.potential_clients = potential_clients
        self.is_open = False
        self.working_hours = [Timer(),Timer()]
        self.expenses = []


    def calculate_loss(self,period = Timer(month=1)):
        wages = 0
        other_expenses = 0
        if period.month > 0:
            for i in range(period.month):
                wages += sum([worker.payment for worker in self.workers])

        for exp in self.expenses:
            timer = exp.period
            while timer <= period:
                other_expenses += exp.cost
                timer += exp.period

        return wages + other_expenses

    def subtract_montly_loss(self):
        loss = self.calculate_loss()
        self.balance -= loss


    def add_workers(self,workers):
        if isinstance(workers, list):
            self.workers += workers
        else:
            self.workers.append(workers)

    def add_client(self,clients, time):
        if isinstance(clients, list):
            while (len(self.clients) + len(self.eating) + len(self.being_cooked)) <= self.capacity and len(clients) > 0:
                client = clients.pop(0)
                client.enter_a_place(time)
                self.clients.append(client)
        else:
            if len(self.clients) + len(self.eating) + len(self.being_cooked) + 1 <= self.capacity:
                clients.enter_a_place(time)
                self.clients.append(clients)

    def cook_orders(self):
        available_cooks = [w for w in self.workers if isinstance(w,Cook) and not w.cooking]
        
        for i in range(len(available_cooks)):
            if len(self.clients) > 0:
                order = [self.clients.pop(0),available_cooks[i]]
                self.being_cooked.append(order)
                available_cooks[i].cooking = True
                
    def serve_orders(self,time):
        remaining_orders = []
        for order in self.being_cooked:

            if time >= order[0].order_waiting_time + order[0].visiting_time:
                order[1].cooking = False
                if order[1].workability >= random.random():
                    self.eating.append(order[0])
                else:
                    order[0].exit_a_place(False)
            else:
                remaining_orders.append(order)
                    
        self.being_cooked = remaining_orders
                
                
    def remove_clients(self,time):
        remaining_clients = []
        for client in self.eating:

            if time > client.visiting_time + client.order_waiting_time + client.eating_time:
                self.balance += client.avg_check * self.profit_margin
                client.exit_a_place(True)
            else:
                remaining_clients.append(client)

        self.eating = remaining_clients

        
