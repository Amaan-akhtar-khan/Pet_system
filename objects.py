import random
from helpers import clamp

class Pet:
    def __init__(self, name, animal_type, energy, hunger, happiness , alive):
        self.name = name 
        self.animal_type = animal_type
        self.energy = energy
        self.hunger = hunger
        self.happiness = happiness
        self.alive = alive

    def eat(self): # hunger + 15 - 30 , energy + 10 - 20
        self.update_stats(random.randint(10,20) 
                          , random.randint(15 , 30)
                          )

    def play(self): # energy - 40 - -10 , hunger = -15 - -30 
        self.update_stats(random.randint(-40 , -10) , 
                          random.randint(-15 , -30)
                          )

    def sleep(self): # energy +20 - +30 , hunger - 10 - -30
        self.update_stats(random.randint(20 , 30) ,
                           random.randint(-10 , -30)
                           )
    
    def update_stats(self , a , b , c ):#a is for energy and b is for hunger and c is for happiness 
        self.energy = clamp(self.energy + a , 100)
        self.hunger = clamp(self.hunger + b , 100)
        self.happiness = clamp(self.happiness + c , 1000)
        self.check_status()
        self.status()

    def check_status(self):
        if self.energy == 0 or self.hunger == 0:
            self.alive = False

    def status(self):
        print(f'\nName:{self.name}\nType of animal:{self.animal_type}\nEnergy:{self.energy}\nHunger level:{self.hunger}\nHappiness level :{self.happiness}\n')