from timer import Timer
import random

class Worker:
    
    def __init__(self):
        self.payment = 0
        self.state = "Ready"
        self.workability=1
        
    def get_payment(self):
        return self.payment
    
    def something_happened(self):
        chance=random.randint(0,100)
        if(chance<5):
            self.state="ill"
            
    def get_state(self):
        return self.state
    
    def __str__(self):
        return("state="+str(self.state)+", payment="+str(self.payment)+", workability="+str(self.workability))
        
    
class Cook(Worker):
    
    def __init__(self):
        super().__init__()
        self.payment=40000
        self.cooking=False
        
class Administrator(Worker):
    
    def __init__(self):
        super().__init__()
        self.payment=50000
        
    def DoNothing(self):
        pass
        
class Casher(Worker):
        
        def __init__(self):
            super().__init__()
            self.payment=30000
            
class Cleaner(Worker):
    
    def __init__(self):
        super().__init__()
        self.payment=20000
        
        
        
if __name__=="__main__":
    cook=Cook()
    cook.cooking()
    print(cook)
    