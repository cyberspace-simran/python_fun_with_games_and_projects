# This is the program which a small game so thet the user can guess the number
# importing module to generate random number 
import random

# initialising variables

playerGuess = None
guesses = 0

randNumber = random.randint(1, 100)
print(randNumber) # we do not need to print this it is just for checking.


while playerGuess != randNumber:        
    playerGuess =  int(input("Enter the number you guess : "))
    guesses +=1
       
    if playerGuess == randNumber:
        print("Congratulations, You gussed it right!!")
    else:
        if (randNumber < playerGuess) :
            print("Wrong!! Guess a smaller number!!")
        else:
            print("Wrong!! Guess a larger number!!")

print(f'You guessed the Number in {guesses} guesses')

# adding the highscore facility to the game on a new file.

with open ('highscore.txt' ,  "r") as f:
    highscore = int (f.read())

if (guesses < highscore):
    print(" You have broken the HighScore ")

    with open ("highscore.txt" ,"w") as f:
        f.write(str(guesses))