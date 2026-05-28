from objects import *
from helpers import *

string_universal = '''1. Eat
2. Play
3. Sleep
'''

def dog_loop(dog):#need to make the auto bath working 

    print(string_universal)
    choice = get_ope('Enter Your chocice:', 1, 9)
    if choice == 1:
        dog.eat()
        print('Dog Ate')
    elif choice == 2:
        dog.play()
        print('Dog Played')
    elif choice == 3:
        dog.sleep()
        print('Dog Slept')
    elif choice == 4:
        dog.fetch()
        print('Dog played Fetch')
    elif choice == 5:
        dog.run()
        print('Dog had a run')
    elif choice == 6:
        dog.guard()
        print('Dog was guarding')
    elif choice == 7:
        dog.bath()
        print('Dog had a bath')
    else :
        dog.vet_visit()
        print('Dog had to visit the vet')

    if dog.bath_turn == 10:
        dog.bath()
        dog.bath_turn = -1
        print('Dog took a bath!')
    else :
        print(f'{10 - dog.bath_turn} turns till the dog auto baths')

    dog.bath_turn += 1


