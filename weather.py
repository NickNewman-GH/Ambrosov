import random
from timer import Timer

class Weather:
    
    temp_states=['Super Cold', 'Cold', 'Normal','Hot', 'Super Hot']
    #presipitation
    pres_states=['No', 'Low', 'Medium', 'High']
    
    def __init__(self):
        self.temperature=self.temp_states[2]
        self.presipitation=self.pres_states[0]
        self.next_change=Timer(min=random.randint(10,59),hour=random.randint(1,2))
        
    def __str__(self):
        result='temperature: '+self.temperature+', presipitation: '+self.presipitation
        return(result)
        
    def changeWeather(self, global_timer=Timer(), mode='Unforce'):
        if(self.next_change<=global_timer or mode=='Force'):
            change_weather=random.randint(0,100)
            if(self.temperature=='Super Cold'):
                if(change_weather<=30):
                    self.temperature='Super Cold'
                else:
                    self.temperature='Cold'
            elif(self.temperature=='Cold'):
                if(change_weather<=20):
                    self.temperature='Super Cold'
                elif(change_weather<=60):
                    self.temperature='Cold'
                else:
                    self.temperature='Normal'
            elif(self.temperature=='Normal'):
                if(change_weather<=30):
                    self.temperature='Cold'
                elif(change_weather<=70):
                    self.temperature='Normal'
                else:
                    self.temperature='Hot'
            elif(self.temperature=='Hot'):
                if(change_weather<=20):
                    self.temperature='Super Hot'
                elif(change_weather<=60):
                    self.temperature='Hot'
                else:
                    self.temperature='Normal'
            else:
                if(change_weather<=30):
                    self.temperature='Super Hot'
                else:
                    self.temperature='Hot'
                    
            change_pres=random.randint(0,100)
            if(self.presipitation=='No'):
                if(change_weather<=30):
                    self.presipitation='Low'
            elif(self.presipitation=='Low'):
                if(change_pres<=40):
                    self.presipitation='Medium'
                else:
                    self.presipitation='No'
            elif(self.presipitation=='Medium'):
                if(change_pres<=30):
                    self.presipitation='Hard'
                else:
                    self.presipitation='Low'
            else:
                if(change_pres<=80):
                    self.presipitation='Medium'
            if(mode!='Force'):
                self.next_change.addTime(min=random.randint(0,59),hour=5)
            else:
                self.next_change=global_timer.addTime(min=random.randint(0,59),hour=5)
        return str(self)
    
    def get_temp(self):
        return self.temperature
    
    def get_pres(self):
        return self.presipitation
    
    def get_values(self):
        return(self.temp_states, self.pres_states)