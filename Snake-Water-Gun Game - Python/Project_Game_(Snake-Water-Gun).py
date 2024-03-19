import random     # NOTE: "Random" module is imported to give the random number command i.e. "random.randint(NUMBER, NUMBER)"

def game(p1, p2):
    if(p1 == p2):
        return None 
    elif(p1 == 's'):
        if(p2 == 'w'):
            return False  
        elif(p2 == 'g'):
            return True
    elif(p1 == 'w'):
        if(p2 == 's'):
            return True  
        elif(p2 == 'g'):
            return False     
    elif(p1 == 'g'):
        if(p2 == 'w'):
            return True  
        elif(p2 == 's'):
            return False                


print("Computer's Turn: Snake(s), Water(w) or Gun(g)? \n")

randnum = random.randint(1,3)    # Gentrating a random number using Random module from 1, 2 & 3  
if(randnum == 1):                # NOTE: Number generated is without including "ZERO" and including the second number in bracket    
    comp = 's'
elif(randnum == 2):
    comp = 'w'
else:
    comp = 'g'

you = input("Your Turn: Snake(s), Water(w) or Gun(g)? \n")

result = game(comp, you)
print(f'Computer chose {comp} \n')
print(f'You chose {you} \n')

if(result==None):
    print("It's a TIE !! \n")
elif(result):
    print("You WIN !! \n")
else:
    print("You LOOSE !! \n")
