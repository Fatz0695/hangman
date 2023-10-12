import random
word_list = ["apple", "mango", "orange" , "strawberry", "melon","banana" ]

class Hangman:
    def __init__(self, word_list, num_lives ):
        self.word = random.choice(word_list) #word to be guessed
        self.word_guessed = ["_" for letter in self.word] #A list of the letters of the word, with _ for each letter not yet guessed.
        self.num_letters = len(self.word) - len(set(self.word_guessed)) #The number of UNIQUE letters in the word that have not been guessed yet
        self.num_lives = num_lives #The number of lives the player has at the start of the game.
        self.word_list = word_list # A list of words
        self.list_of_guesses =[] #A list of the guesses that have already been tried. Set this to an empty list initially

        print("The mystery word has " + str(len(self.word)) + " characters")
        print(f"{self.word_guessed}")

    def check_guess(self, guess):
        guess = guess.lower()
    # checking whether  guess is in the word:
        if guess in list(self.word): 
            print(f'Good guess! {guess} is in the word')
            
            #If the letter is in the word, replace the '_' in the word_guessed list with the letter
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess
           
            self.num_letters = self.num_letters - 1
            print(self.word_guessed)
            print(self.num_letters)
            #return self.num_letters
            
         #If the letter is not in the word, reduce the number of lives by 1    
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
            self.check_num_lives(self)
            
    
    #Ask the user for a letter iteratively until the user enters a valid letter
    def ask_for_input(self): 
        while True:
            print("Please enter a value: ")
            guess = input()
            if len(guess) != 1 or (guess.isalpha()) != True:
                print("Invalid input. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
            self.list_of_guesses.append(guess)
    
        

def play_game(word_list):
    num_lives = 5
    game= Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print(f"Sorry, You lost! The word was {game.word}")
            
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_lives != 0 and game.num_letters == 0:
            print("Congratulations. You won the game!")

if __name__ == '__main__':
    play_game(word_list)