# Imports
import random 

# %%
# List of words for hangman
word_list = ["Mango", "Coconut", "Kiwi", "Orange", "Grapes"]
print(word_list)


# Random selector function
def random_choice(word_list):
    """ 
    This fucntion selects a random word from a list of words.
    
    Arg:
        word_list: list of words for the function to choose from.
    
    Returns:
        str: random word choosen from the list.
    """
    word = random.choice(word_list)
    return print(word)

#%%
# Get user imput
def user_guess():
    """ 
    This function takes a single letter from user guess.

    Args:
        guess (str): take a single letter from the user.

    Returns:
        str: letter guess by the user
    """
    guess = input("Please enter a lette")

    while True:
        if guess.isalpha() == False or len(guess) != 1:
            print("Oops! that is not a valid input, Please try again")
            guess = input("Please enter a lette")
        else:
            break
    print(f"{guess} is a good guess!")


# %%
user_guess()
# %%