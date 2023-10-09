import random
Fruit_list = ["apple", "mango", "orange" , "strawberry", "melon" ]
Fruits = random.choice(Fruit_list)


#functions to run checks
def check_guess(guess):
    #guess.lowercase()
    # checking whether  guess is in the word:
    if guess in Fruits:
        print('Good guess! {guess} is in the word')
    else:
        print ('Sorry, {guess} is not in the word. Try again.')

def ask_for_input():
    # checking if input is a valid guess 
    while True:
        guess = input()
        if len(guess) == 1 and (guess.isalpha()) == True:
            break
        else: 
            print("Invalid input. Please, enter a single alphabetical character.")
            continue
    check_guess(guess)

ask_for_input()