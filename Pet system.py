import helpers 
from objects import * 
from loops import *

def win():
    print('You Won the game!')

def loop(x , pet):
    while pet.alive:
        x(pet)
        if pet.happiness == 1000:
            win()
            break
    if pet.happiness != 1000:
        print('Ur pet died')




def main ():
    name = input('Enter the name of your Pet:')
    animal_type = helpers.text_inp('Enter the type of animal[Parrot , Dog , Cat , Hamster]' , 'Parrot' , 'Dog' , 'Cat' , 'Hamster' )
    declare_values()

    if animal_type == 'Dog':
        pet = Dog(name)
        loop(dog_loop , pet)     
        
main()
