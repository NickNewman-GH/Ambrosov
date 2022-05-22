
class Timer:
    
    def __init__(self, sec=0, min=0, hour=0,day=0,month=0):
        self.hour=hour
        self.min=min
        self.sec=sec
        self.day=day
        self.month=month
        
    def addTime(self, sec=0, min=0, hour=0,day=0,month=0):
        self.sec+=sec
        if(self.sec>=60):
            self.min=int(self.min+(self.sec/60))
            self.sec=self.sec%60
        self.min+=min
        if(self.min>=60):
            self.hour=int(self.hour+(self.min/60))
            self.min=self.min%60
        self.hour+=hour
        if(self.hour>=24):
            self.day=int(self.day+(self.hour/24))
            self.hour=self.hour%24
        self.day+=day
        if(self.day>=30):
            self.month=int(self.month+(self.day/30))
            self.day=self.day%30
        self.month+=month
        
    def __str__(self):
        resultstring=str(self.sec)+":"+str(self.min)+":"+str(self.hour)+" day:"+str(self.day)+", month:"+str(self.month)
        return resultstring
    
    def __eq__(self, timer_2):
        if(not isinstance(timer_2, Timer)):
            return False
        if(self.sec!=timer_2.sec):
            return False
        if(self.min!=timer_2.min):
            return False
        if(self.hour!=timer_2.hour):
            return False
        if(self.day!=timer_2.day):
            return False
        if(self.month!=timer_2.month):
            return False
        return True
    
    def __gt__(self, timer_2):
        if(not isinstance(timer_2, Timer)):
            return False
        if(self.month>timer_2.month):
            return True
        if(self.month<timer_2.month):
            return False
        
        if(self.day>timer_2.day):
            return True
        if(self.day<timer_2.day):
            return False
        
        if(self.hour>timer_2.hour):
            return True
        if(self.hour<timer_2.hour):
            return False
        
        if(self.min>timer_2.min):
            return True
        if(self.min<timer_2.min):
            return False
        
        if(self.sec>timer_2.sec):
            return True
        if(self.sec<timer_2.sec):
            return False
        
        return False
    
    def __lt__(self, timer_2):
        if(not isinstance(timer_2, Timer)):
            return False
        
        if(self>timer_2):
            return False
        
        if(self==timer_2):
            return False
        
        return True
    
    def __ge__(self, timer_2):
        if(not isinstance(timer_2, Timer)):
            return False
        if(self>timer_2 or self==timer_2):
            return True
        return False
    
    def __le__(self, timer_2):
        if(not isinstance(timer_2, Timer)):
            return False
        if(self<timer_2 or self==timer_2):
            return True
        return False
    
    def copy(self):
        copy=Timer(sec=self.sec, min=self.min, hour=self.hour, day=self.day, month=self.month)
        return copy
    
    def __add__(self, timer_2):
        if(not isinstance(timer_2, Timer)):
            raise Exception("wrong type, use Timer()")
        result=self.copy()
        result.addTime(sec=timer_2.sec, min=timer_2.min, hour=timer_2.hour, day=timer_2.day, month=timer_2.month)
        return result