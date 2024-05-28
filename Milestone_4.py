#%%
# Imports
import random 

# %%
# List of words for hangman
word_list = ["Mango", "Coconut", "Kiwi", "Orange", "Grapes"]

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
def user_guess():
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
