
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
            print(f"Good guess! {guess} is in the word")
            for i in self.word:
                if i == guess:
                    guess_index = self.word.index(i)
                    self.word_guessed[guess_index] = guess
            print(self.word_guessed)
            

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
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
# %%
word_list_1 = ["mango", "coconut", "kiwi", "orange", "grapes"]
hang_1 = Hangman(word_list_1)
print(hang_1.word)

# %%
hang_1.ask_for_input()
# %%

print(hang_1.word_guessed)

# %%
