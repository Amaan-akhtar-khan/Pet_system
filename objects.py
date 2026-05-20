from helpers import clamp

class Pet:
    def __init__(self, name, animal_type, energy, hunger, alive):
        self.name = name 
        self.animal_type = animal_type
        self.energy = energy
        self.hunger = hunger
        self.alive = alive

    def eat(self): # hunger + 30 , energy + 20
        self.update_stats(20 , 30)

    def play(self): # energy - 40 , hunger = -30 
        self.update_stats(-40 , -30)

    def sleep(self): # energy +30 , hunger - 10
        self.update_stats(30 , -10)
    
    def update_stats(self , a , b ):#a is for energy and b is for hunger
        self.energy = clamp(self.energy + a)
        self.hunger = clamp(self.hunger + b)
        self.check_status()
        self.status()

    def check_status(self):
        if self.energy == 0 or self.hunger == 0:
            self.alive = False

    def status(self):
        print(f'\nName:{self.name}\nType of animal:{self.animal_type}\nEnergy:{self.energy}\nHunger level:{self.hunger}\nAlive:{self.alive}\n')