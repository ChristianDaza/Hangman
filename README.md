# Hangman
![](https://img.shields.io/badge/platforms%20-macOS--64%20%7C%20win--64-lightgrey) ![](https://img.shields.io/badge/version-1.0.0-blue)

An interactive Python based version of the hangman game.   

## Description

Hangman is a Python script that allows the user to play the hangman game in the command line. When the script is run the user is prompted to enter a letter to try to guess a randomly selected word, one letter at the time. The user begins the game with a predetermine number of lives, which will decreases after each wrong guess. The game ends when the user correctly guesses all the letters of the random word before running out of lives or the user's lives reaches 0. 

The aim of this project was to solidify and impprove my Python, command line and GitHub skills. I learned that you don't need large or many additions to your project to make it unique, refining your code to be easily undertood or adapting certain areas of your code with the end user in mind, creates the greates results.


## Table of content

- [Description](#Description)
- [Intallation](#Intallation)
- [Usage](#Usage)
- [Main Features](#Main_Features)
- [Lincence](#Licence)
- [Contact Information](#Contact_information)


## Installation

 The source of this code is currently hosted at: https://github.com/ChristianDaza/Hangman.git

Clone this git repository into your machine using the following code:
```
git clone https://github.com/ChristianDaza/Hangman.git
```


## Usage

Once cloned, use the command line to navigate to the repository. Then move to the SRC folder and run:
```
python3 Play_hangman.py
```
Upon runnign the file, the number of unique letters in the word will be shown to the user, as well as the lenght of the word  as individual undercores. 
```
The mistery word has 4 characters.
['_', '_', '_', '_']
Please enter a letter: 
```
Then the user will be asked to enter a guess in the form of a singular alpahbetical character. The script accepts the guess immediate after the prompt message or with a space between the message and the actual guess.
```
Please enter a letter: l
Please enter a letter:l 

```
If the guess is correct the corresponding underscore will be switched to the guessed letter, if not the user will lose a live. 
```
Good guess! l is in the word
['l', '_', '_', '_']

Sorry, a is not in the word.
You have 4 lives left.
```
The game will end when the user correclty guesses all the letters of the random word before running out of lives or if the user's lives reaches 0.
```
['l', 'u', 't', 'e']
Congratulations. You won the game!

You have 0 lives left.
You lost!
```

## Main Featues

- Requires minimal coding from the user.
- Already comes with a list of words with varying degrees of difficulty.
- Displays the number of letters to the user as underscores.
- Substitutes undercores with the correclty guessed letters, in their orignal position from the random word.
- If a letter have more than one occurence in the random word all the occurences will be display when the letter is gueesed.
- Displays and updates the number of lives the user has after each wrong guess.
- Number of lives adapts to the difficulty of the random word.
- The code in this Python script can be run as individual cells, when view in Visual Studio Code due to the #%% symbol above the code.
    

## Licence
[MIT](https://github.com/ChristianDaza/Hangman/blob/main/LICENSE)

## Contact Information
- Christian
- ch.arenasdaza@gmail.com
- [GitHub](https://github.com/ChristianDaza)