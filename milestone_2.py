import random
Fruit_list = ["Apple", "Mango", "Orange" , "Strawberry", "Melon" ]
Fruits = random.choice(Fruit_list)

#Checks if random word is generated
#print(word)

#asking the user fo input
print("Please enter a single letter")
guess = input()
print(guess)

#Checking if input is single character using if/else statements
if len(guess) == 1 and (guess.isalpha()) == True:
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')