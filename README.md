# Hangman
This code represents the classic game of "Hangman." The player's objective is to guess a word based on hints. They can choose from various categories of words or input their own word. Then, they play according to the rules of Hangman, where they have a certain number of attempts to guess the correct letters.

## Table of Contents
- [Usage](#usage)
- [Files](#files) 
- [Functions](#functions)
- [Learnings and Takeaways](#learnings-and-takeaways)
- [Contact](#contact)

## USAGE
#### Running the Program:
To start the game, execute the script in Python.  
```bash
    python hangman.py
```
#### Choosing a Category:
After starting the game, the player has the option to choose a category from which the word will be guessed. Categories include countries, food, jobs, and sports.

#### Inputting a Custom Word:
Alternatively, the player can input their own word. It must be a single word of their choice.

#### Gameplay:
Once the word and category are selected, the game proceeds to the main phase, where the player guesses individual letters of the word. They have a certain number of attempts to guess all the correct letters. After exhausting attempts, the game ends, and the player learns whether they won or lost.

## Files:
- hangman.py: Main script for launching the game.

## Functions:
- **hangman()**: Function to display the hangman image based on the remaining attempts.  
- **choosing_category()**: Function to select the word category for guessing.  
- **check_answer()**: Function to verify whether the player wants to choose a category or input a custom word.  
- **communication()**: Function for communication with the player and obtaining information about the chosen category or custom word.  
- **contains_num()**: Function to check if the input contains numbers.  
- **choose_word()**: Function to select a random word from the chosen category.  
- **check_difficulty()**: Function to verify the game difficulty.  
- **check_letter()**: Function to validate whether the entered letter is valid.  
- **type_attempts()**: Function to select the number of attempts based on the chosen difficulty.  
- **print_hint()**: Function to print hints for the player.  
- **game()**: Main function for the gameplay.  
- **final()**: Function to display the game result.  
- **clear_terminal()**: Function to clear the terminal before starting the game.  

## Learnings and Takeaways:
- **Handling User Input**: Improved ability to communicate with users and process their inputs.  
- **Terminal Manipulation**: Acquired experience in clearing the terminal before starting the game, which can enhance the user experience.  

## Contact:
For any inquiries or issues, please feel free to contact the developer via email: adelanavratova@seznam.cz. Enjoy the game!
