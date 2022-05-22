from timer import Timer
from weather import Weather


class World:
    
    adder=Timer(mins=10)
    
    def __init__(self):
        self.global_timer=Timer()
        self.global_weather=Weather()
        
    def update(self):
        self.global_timer=self.global_timer+self.adder
        self.global_weather.changeWeather(global_timer=self.global_timer)
        
    def get_weather(self):
        return {'temp':self.global_weather.get_temp(),'pres':self.global_weather.get_pres(),'next_change':self.global_weather.next_change}
    
    def get_global_timer(self):
        return self.global_timer.copy()
    
if __name__=='__main__':   
    my_world=World()
    for i in range(100):
        print(my_world.get_global_timer(), end='=> ')
        weather=my_world.get_weather()
        print('temp: ',weather['temp'],', pres: ',weather['pres'],', next_change: ',weather['next_change'])
        my_world.update()