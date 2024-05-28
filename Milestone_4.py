#%%
# Imports
import random 

# %%
# List of words for hangman
word_list_1 = ["Mango", "Coconut", "Kiwi", "Orange", "Grapes"]

#%%
# Random selector function
def random_choice(word_list):
    """ 
    This fucntion selects a random word from a list of words.
    
    Arg:
        word_list: list of words for the function to choose from.
    
    Returns:
        str: random word choosen from the list.
    """
    global random_word
    random_word = random.choice(word_list)
    return print(random_word)

#%%

def check_guess(guess):
    """" 
    This function check if the user guess is in the randomly chosen word.
    
    Returns: 
        str: confirming if the user guess was right or wrong.
    """
    guess = guess.lower()
    if guess in random_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
#%%
# Get user imput
def user_guessx():
    """ 
    This function takes a single letter from user guess and also checks if the guess in in the word.

    Args:
        guess (str): take a single letter from the user.

    Returns:
        str: letter guess by the user
    """

    while True:
        guess = input("Please enter a lette")
        if guess.isalpha() == False or len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
            guess = input("Please enter a lette")
        else:
            break
    print(f"{guess} is a good guess!")
    check_guess(guess)



# %%
#Class
import random
class  Hangman:
     
    def __init__(self, word_list:list[str], num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives if num_lives != 5 else 5 
        self.word = random.choice(word_list)
        self.word_guessed = ["_"]*len(self.word)
        self.num_letter = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        """" 
        This function check if the user guess is in the randomly chosen word.
        
        Returns: 
            str: confirming if the user guess was right or wrong.
        """

        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input(self):
        """ 
        This function takes a single letter from user guess and also checks if the guess in in the word.

        Args:
            guess (str): take a single letter from the user.

        Returns:
            str: letter guess by the user
        """
        
        while True:
            guess = input("Please enter a lette")
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
                guess = input("Please enter a lette")
                
            elif guess in self.list_of_guesses:
                print("guess in list_of_guesses")
                
            else:
                check_guess(guess)
                self.list_of_guesses.append(guess)
                break
# %%
hang_1 = Hangman(word_list_1)
print(hang_1.word)

# %%
hang_1.ask_for_input()
# %%
print(hang_1.list_of_guesses)
# %%
