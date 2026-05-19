from helpers import text_inp , clamp , get_ope

class Pet:
    def __init__(self, name, animal_type, energy, hunger, alive):
        self.name = name 
        self.animal_type = animal_type
        self.energy = energy
        self.hunger = hunger
        self.alive = alive

    def eat(self): # hunger + 30 , energy + 20
        self.hunger += 30
        self.hunger = clamp(self.hunger)
        self.energy += 20 
        self.energy = clamp(self.energy)
        self.check_status()
        self.status()

    def play(self): # energy - 40 , hunger = -30 
        self.hunger -= 30
        self.hunger = clamp(self.hunger)
        self.energy -= 40
        self.energy = clamp(self.energy)
        self.check_status()
        self.status()

    def sleep(self): # energy +30 , hunger - 10
        self.energy += 30
        self.energy = clamp(self.energy)
        self.hunger -= 10
        self.hunger = clamp(self.hunger)
        self.check_status()
        self.status()
    
    def check_status(self):
        if self.energy == 0 or self.hunger == 0:
            self.alive = False

    def status(self):
        print(f'\nName:{self.name}\nType of animal:{self.animal_type}\nEnergy:{self.energy}\nHunger level:{self.hunger}\nAlive:{self.alive}\n')
    
string = '''What would you like to do with the pet:
1.Feed him 
2.Make him play 
3.Put him to sleep
'''
def main ():
    name = input('Enter the name of your Pet:')
    animal_type = text_inp('Enter the type of animal:' , 'Parrot' , 'Dog' , 'Cat' , 'Hamster' )
    
    pet = Pet(name , animal_type , 70 , 70 ,True)
    while pet.alive is True:
        print(string)
        num = get_ope('Your choice:' , 1 , 4)

        if num == 1:
            pet.eat()
        elif num == 2:
            pet.play()
        elif num == 3:
            pet.sleep()
    print('Your pet died...')
        
main()
