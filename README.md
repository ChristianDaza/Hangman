# Hangman

An interactive Python based version of the hangman game.   

## Description

Hangman is a Python script that allows the user to play the hangman game in the command line. When the script is run the user is prompted to enter a letter to try to guess a randomly selected word, one letter at the time. The user begins the game with a predetermine number of lives the number of lives, which will decreases after each wrong guess. The game ends when the user correctly guesses all the letters of the random word before running out of lives or the user's lives reaches 0. The aim of this project was to solidify the Python, command line and GitHub skills from the AiCore courses by applying them into a project. From this project I learned that is better to break down a function, creating the individual lines of code and then combining them. I also learned that you don't need large or many additions to your project to make it unique, refining your code to be easily undertood or adapting certain areas of your code with the end user in mind, creates the greates results.



## Table of content

- [Description](#Description)
- [Main Features](#Main_Features)
- [Intallation](#Intallation)
- [Usage](#Usage)
- [File structure](#File_structure)
- [Lincence](#Licence)

## Main Featues

- Requires minimal coding from the user.
- Already comes with a list of words with varying degrees of difficulties.
- Displays number of letter to the user as underscores: "_".
- Gives feedback to the user based on the guess.
- Substitutes undercores with the correclty guessed letters, in their orignal position from the random word.
- If a letter have more than one occurence in the random word all the occurences will be display when the letter is gueesed.
- Displays and updates the number of lives the user has after each wrong guess.
- Number of lives adapts to the difficulty of the word.
    

## Installation

The source of this code is currently hosted at: https://github.com/ChristianDaza/Hangman.git

Clone this git repository into your machine using the following code:
```
git clone https://github.com/ChristianDaza/Hangman.git
```


## Usage

Once cloned, use the command line to navigate to the clone repository. Once inside run:
```
python3 Milestone_5.py
```
Upon runnign the file the lenght of the word represented by individual undercores and number of unquie letters in the word will be shown to the user. Then the user will be asked to enter a guess in the form of a singular alpahbetical character. The script accepts the guess immediate after the prompt message or with a space between the message and the actual guess.

If the guess is correct the corresponding underscore will be switched to guessed letter, if not the user will lose a live. The game will end when the user correclty guesses all the letters of the random word before running out of lives or if the user's lives reaches 0.

## Licence
[MIT](https://github.com/ChristianDaza/Hangman/blob/main/LICENSE)

