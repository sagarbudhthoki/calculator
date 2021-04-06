import random
randomNumber = random.randrange(1,10)
#print randomNumber #check if it's working
tries = 0

# rules
print('Hello and welcome to the guess game !')
print('The number is between 1 and 10')

guessed = False
tries += 1

while guessed==False:

    userInput = int(input("Please enter your guess: "))

    if userInput==randomNumber:
        guessed = True
        tries = str(tries)
        print("Congratulations ! You win after " + tries + " tries ! ")

    elif userInput>10:
        print("The guess range is between 1 and 10, please try again")
        tries = tries + 1

    elif userInput<1:
        print("The guess range is between 1 and 10, please try again")
        tries = tries + 1

    elif userInput>randomNumber:
        print("Your guess is too large")
        tries = tries + 1

    elif userInput < randomNumber:
        print("Your guess is too small")
        tries = tries + 1

print("End of the game, please play again")