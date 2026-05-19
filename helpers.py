def text_inp(y,a,b,c,d):
    while True:
        try:
            x = input(y)
            if x not in [a,b,c,d]:
                print('Invalid operation.')
                continue
            return x
        except :
            print('Enter a valid operation.')

def clamp(x):
    if x < 0 :
        return 0
    elif x > 100:
        return 100
    else :
        return x 

def get_ope(y,a,b):
    while True:
        try:
            x = int(input(y))
            if x not in range(a,b):
                print('Invalid operation.')
                continue
            return x
        except ValueError:
            print('Enter a valid number.')