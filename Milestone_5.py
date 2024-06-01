
# %%
#Class
import random
class  Hangman:
    """ 
    A hangman game that ask the user for a letter and then checks if the letter in in the word.
    The game starts with a default number of lives and a ramdomly selected word from a list.
    
    Parameters:
        word_list (list): 
            List of words to be used in the game.
        num_lives (int): 
            Number of lives the player has.

    Attributes:
        word (str): 
            The word to be guess by the user selected ramdomly from word_list.
        word_guessed (list): 
            A list of letters of the word, with "_" for each letter no yet guessed.
        num_letters (int): 
            Number of unique letter in the word that has not been guessed yet.
        num_lives (int): 
            Number of lives the player has.
        list_letters (list): 
            A list of letter that have laready been tried.
    
    Methods:
    check_guess(letter):
        Checks if the guess is in the word.
    ask_for_input()
        Asks the user for a letter.
    """
     
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
             Checks if the user letter is in the randomly chosen word.
             If it is, it replaces the "_" in the word_guessed list wiht the letter.
             If is not, it reduces the number of lives by 1.

        Prameters:
            guess (str):
                The letter to be checked.
        
        Returns: 
            str: 
                string confirming if the user guess was right or wrong.
            list: 
                List with the correctly guessed letters, in their correct positions.
            int: 
                Number of remaining lives after each wrong guess.
        """

        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
        
            for num in range(0,len(self.word)):
                if(guess==self.word[num]):
                    self.word_guessed[num] = guess      
            self.num_letters = self.num_letters -1
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
print(hang_1.word) 
print(hang_1.num_letters) 
print(hang_1.list_letters)

# %%
hang_1.ask_for_input()

# %%
print(hang_1.num_letters) 
print(hang_1.list_letters)
print(hang_1.num_lives)

# %%
word = "coconut"
# %%
word = "coconut"
guess = "o"

list_doubles = []
for num in range(0,len(word)):
    if(guess==word[num]):
        list_doubles.append(num)
print(list_doubles)
# %%
list_doubles = []
word = "coconut"
guess = "o"
for letters in word:
    if  letters == guess and word.count(letters)>1:
        list_doubles.append(letters)
print(list_doubles)

# %%
