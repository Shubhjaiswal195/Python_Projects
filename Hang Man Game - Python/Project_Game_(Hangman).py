import random
import Diagram_Hang_man

Words = ['fruit', 'table', 'college', 'human', 'computer','instagram', 'restaurant', 'mobile', 'internet']
Word = random.choice(Words)

display = []
game_over = False
lives = 6 

for i in range(0, len(Word)):

    display.append('_')
    i = i + 1
print('\n', display)
    
while not game_over:

    Guessed = (input('Guess any letter : \n')).lower()

    for position in range(len(Word)):

        letter = Word[position]
        
        if (letter == Guessed):
            display[position] = Guessed

    if (Guessed not in Word):
        lives -=1

        if(lives == 0):
            game_over = True 
            print("You Loose !!! Play & try Again")
    
    if ('_' not in display):
        game_over = True
        print("You Win!!!")

    print(display)
    print(f'Lives = {lives}')
    print(Diagram_Hang_man.stages[lives])

print(f'The word is: {Word}')