import random 

randNumber = random.randint(1, 100)
# print(randNumber)
userGuess = None 
guesses = 0

while(userGuess != randNumber):

    userGuess = int(input("Enter your guess number between 1 to 100: "))

    guesses +=1

    if(userGuess == randNumber):
        print('\n')
        print("Congratulation!!! You gussed it right!!")
    else: 
        if(userGuess>randNumber):
            print("You gussed it wrong!! Enter a smaller number")
        else:
            print("You gussed it wrong!! Enter a larger number")
    

print(f"You guessed the number in {guesses} guesses") 



with open("high_score.txt", "r") as f:     # Program to note the highscore created by user in file high_score.txt
    high_score = int(f.read())

if(guesses<high_score):

    print("You have just broken the high score!!")
    
    with open("high_score.txt", "w") as f:
        f.write(str(guesses))