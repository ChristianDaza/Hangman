# Hangman
Hangman: interactive python base version of the hangman game.

## Description
The Hangman project allows the a user to play a python version of the hangman game, in which a random unkown word is selected, and the user tries to guess unkown word, by entering one letter at the time. The game end when the user correctly gueses all the letter in the word before runnign out of lives or the live count reaches 0. The game will end if the user runs out of lives or correctly guesses the word. This project aimed at solidifying my python, command line, GitHub and conda skills from the AiCore courses by applying them into a project.

## Table of content
- [Description](#Description)
- [Main Features](#Main_Features)
- [Intallation](#Intallation)
- [Usage](#Usage)
- [File structure](#File_structure)
- [Lincence](#Licence)

## Main Featues
- Selects a random word from a list.
- Ask the user for input.
- Checks if the input is single alphabetical character.
- Checks if the user input is present in the randomly chosen word:
    - If present the guess will be print in a list, where its position is the same as in the random word.
    - If not present a live will be taken.
    

## Installation
The source of this code is currently hosted at: https://github.com/ChristianDaza/Hangman.git

To install clone this git repository using the following code:
'git clone https://github.com/ChristianDaza/Hangman.git'


## Usage
In the command line run the main.py file from this repository.

The Hangman class requires a list of words and number of lives. If the user does not input a number of lives, the default value of 5 will be used.

Use the ask_for_input() method from the Hangman class to begin the game, this method does not initially require a parameter to run but when run it will as for input from the user.

If the user guess is a single alphabetical character, then it is check. If the guess is present in the random word a list of underscores will be return, with the guess letter occupating the correponding position as in the random word. The number of underscores corresponds to the number of letters in the random word. If the guess is wrong the user will loss a live and a message will be printed with the updated number of lives.

The game will end when the user corretly guesses all the letters within the random word while having lives or if the number of lives reaches 0.



## File struture
## Licence

