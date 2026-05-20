import helpers 
from objects import Pet # type: ignore
    
string = '''What would you like to do with the pet:
1.Feed him 
2.Make him play 
3.Put him to sleep
'''
def main ():
    name = input('Enter the name of your Pet:')
    animal_type = helpers.text_inp('Enter the type of animal:' , 'Parrot' , 'Dog' , 'Cat' , 'Hamster' )
    
    pet = Pet(name , animal_type , 70 , 70 ,True)
    while pet.alive:
        print(string)
        num = helpers.get_ope('Your choice:' , 1 , 4)

        if num == 1:
            pet.eat()
        elif num == 2:
            pet.play()
        elif num == 3:
            pet.sleep()
    print('Your pet died...')
        
main()
