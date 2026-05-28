import random as r 
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
        self.update_stats(r.randint(a , b)
                          , r.randint(c , d)
                          , r.randint(e , f))

    def play(self): # energy - 40 - -10 , hunger = -15 - -30 
        self.update_stats(r.randint(g , h)  
                          , r.randint(i , j)
                          , r.randint(k , l))

    def sleep(self): # energy +20 - +30 , hunger - 10 - -30
        self.update_stats(r.randint(m , n)
                          , r.randint(o , p)
                          , r.randint(q , s))
    
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

class Dog(Pet):# make the dog work , work on the gamplay loop and iteration thing - when these are stable only then any new feature 
    def __init__(self , name):
      super().__init__(name, 'Dog', 70 ,  70 , 0 , True )  
      self.bath_turn = 0 

    def fetch(self):
        self.update_stats(r.randint(-45 , -30) , r.randint( -50 , -20) , r.randint(20 , 50))
    def run(self):
        self.update_stats(r.randint(-40 , - 25) , r.randint(- 10 , -20) , r.randint(40 , 70 ))
    def guard(self):
        self.update_stats(r.randint(-20 , -10) , r.randint(-10 , -5 ) , r.randint(20 , 40 ))
    def bath(self):
        self.update_stats(r.randint(-20 , -10) , r.randint(-10 , - 5) , r.randint(-80 , -40))
    def vet_visit(self):
        self.update_stats(r.randint(-30 , -15) , r.randint(-20 , -10) , r.randint( -150 , - 100))


class Cat(Pet):
    def __int__(self):
        pass
    def nap(self):
        pass
    def scratch(self):
        pass
    def ignore(self):
        pass 

class Hamster(Pet):
    def __init__(self):
        pass
    def run_wheel(self):
        pass 
    def hide(self):
        pass 
    def collect_food(self):
        pass 

class Parrot(Pet):
    def __int__(self):
        pass
    def mimic(self):
        pass 
    def scream(self):
        pass
    def fly(self):
        pass 

def declare_values():
    global a , b , c , d , e ,f , g , h, i, j , k , l , m , n , o , p , q , s
    if Pet.animal_type == 'Dog':
        a = 10 
        b = 20
        c = 20 
        d = 35 
        e = 10
        f = 20
        g = -40
        h = -20 
        i = -30
        j = -15
        k = 25
        l = 40
        m = 25 
        n = 40 
        o = -15
        p = -5 
        q = 5
        s = 15 
    

