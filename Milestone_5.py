
# %%
import random

class  Hangman:
    """ 
    A hangman game that ask the user for a guess in the form of a letter and then checks if the letter in the word.
    The game starts with a default number of lives and a ramdomly selected word from a list.
    
    Parameters:
        word_list (list): 
            List of words to be used in the game.

    Attributes:
        word (str): 
            The word to be guess by the user, selected ramdomly from the word_list.
        word_guessed (list): 
            A list of letters of the word, with "_" for each letter no yet guessed.
        num_letters (int): 
            Number of unique letters in the word that has not been guessed yet.
        num_lives (int): 
            Number of lives the player has.
        list_letters (list): 
            A list of letters that have already been tried.
    
    Methods:
    check_guess(guess):
        Checks if the guess is in the word.
    ask_for_input()
        Asks the user for to guess a letter.
    """
    def __init__(self, word_list):
        self.word = random.choice(word_list)
        self.word_guessed = ["_"]*len(self.word)
        self.word_list = word_list
        self.num_letters = len(set(self.word))
        self.num_lives = self.num_lives =  self.num_letters if self.num_letters > 5 else 5
        self.list_letters = []

        print(f"The mistery word has {self.num_letters} characters.")
        print(self.word_guessed)

    def check_guess(self, guess):
        """" 
        This function:
             Checks if the user guess is in the randomly chosen word.
             If it is, it replaces the "_" in the word_guessed list with the guessed letter.
             If is not, it reduces the number of lives by 1.

        Prameters:
            guess (str):
                The letter to be checked.
        
        Returns: 
            str: 
                String confirming if the user guess was right or wrong.
            list: 
                List with the correctly guessed letters, in their correct positions.
            int: 
                Number of remaining lives after each wrong guess.
        """
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
            for index in range(0,len(self.word)):
                if(guess == self.word[index]):
                    self.word_guessed[index] = guess      
            self.num_letters = self.num_letters -1
            print(self.word_guessed)  
        else:
            print(f"Sorry, {guess} is not in the word.")
            self.num_lives = self.num_lives -1
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        """ 
        This function:
             Checks if the user guess is a single alphabetical character.
             Pass the guess that fulfils the above conditions into the check_guess().

        Parameters:
            guess (str): 
                Takes a single letter from the user.

        Returns:
            str: 
                A string telling the user the guess is invalid and to try again.
            str: 
                A string telling the user that the letter had alrady being used for a previous guess.
        """
        while True:
            guess = input("Please enter a letter:").replace(" ", "")
            if guess.isalpha() == False or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
                guess 
                
            elif guess in self.list_letters:
                print("You already tried that letter!")
                
            else:
                self.check_guess(guess)
                self.list_letters.append(guess)
                break

# %%
def play_game(word_list):
        """
        This function:
            Creates a Hangman class instance.
            Calls the Hangman methods.
            Allows the user to play Hangman.

        Parameter:
        word_list (list):
            List of words to be used in the game.

        Returns:
            str:
                Telling the user he or she has lost the game.
            ask_for_input():
                Calls this method to continue playing hangman.
            str:
                Telling the user he or she has won the game.
        """
        game = Hangman(word_list)

        while True:
            if game.num_lives == 0:
                print("You lost!")
                break

            elif game.num_letters > 0: 
                game.ask_for_input()

            elif game.num_lives != 0 and game.num_letters <= 0:
                print("Congratulations. You won the game!")
                break

#%%
if __name__ == "__main__":
    word_list = ["mango", "lute", "incomprehensibilities", "floccinaucinihilipilification", "unimaginatively"]
    play_game(word_list)