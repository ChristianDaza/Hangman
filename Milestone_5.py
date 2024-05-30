
# %%
#Class
import random
class  Hangman:
     
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"]*len(self.word)
        self.word_list = word_list
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives if num_lives != 5 else 5 
        self.list_letters = []

        print(f"The mistery word has {self.num_letters} characters")
        print(self.word_guessed)

    def check_guess(self, guess):
        """" 
        This function:
             Checks if the user guess is in the randomly chosen word.
             Saves the correct guess in a list with their correct guess.
             Updates the number of ramaining lives after each guess.


        
        Returns: 
            str: string confirming if the user guess was right or wrong.
            lst: list with the correctly guessed letter, in their position correct positions.
            int: number of remaining lives after each guess.
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
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives = self.num_lives -1
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """ 
        This function:
             Checks that the user guess is a single alphabetical character.
             Pass the guess that fulfils the above conditions into the check_guess().


        Args:
            guess (str): take a single letter from the user.

        Returns:
            str: a string telling the user the guess is invalid and to try again.
            str: a string telling the user that the letter had alrady being used for a previous guess.
        """
        
        while True:
            guess = input("Please enter a lette")
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
                guess = input("Please enter a lette")
                
            elif guess in self.list_letters:
                print("This letter has already being used for a previous guess")
                
            else:
                self.check_guess(guess)
                self.list_letters.append(guess)
                break
    
    def play_game(self, word_list):
        num_lives = 5
        game = Hangman(word_list, num_lives)
        while True:
            if num_lives == 0:
                print("You lost!")

            elif self.num_letters > 0: 
                self.ask_for_input()
            elif num_lives != 0 and self.num_letters <= 0:
                print("Congratulations. You won the game!")


# %%
word_list_1 = ["mango", "coconut", "kiwi", "orange", "grapes"]

hang_1 = Hangman(word_list_1)
# %%


# %%
