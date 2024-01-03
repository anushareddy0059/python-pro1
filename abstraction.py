from abc import ABC,abstractmethod
class Car(ABC):
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
        self.speed=0
        @abstractmethod
        def speed_up():
           pass
        @abstractmethod
        def speed_down():
           pass
        @abstractmethod
        def stop():
           pass
        
    
class Bmw(Car):
    def speed_up(self):
        self.speed+=5
    def speed_down(self):
        self.speed-=5
    def stop(self):
        self.speed=0
    
Bmw=Bmw('x7','black',50000)
