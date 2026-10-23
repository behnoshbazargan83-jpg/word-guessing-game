# word-guessing-game

A Hangman-style word guessing game in Python that runs in the terminal.

## Features

- Random word picked from 4 categories: animals, fruits, colors, misc
- A hint at the start: the category and the number of letters
- 6 lives: a wrong guess costs one life
- Input validation: only a single letter is accepted, repeated guesses are ignored
- Score that is kept between rounds (more lives left = more points)
- Play again option after every round

## How to run

1. Install Python 3.
2. Download word-game.py.
3. Run it in a terminal:

python word-game.py
## Example

game number: 1
fruits 5
_ _ _ _ _ | lives: 6
enter a letter: a
## Concepts used

- Recursion (count_letter)
- Closures and nonlocal (score keeper)
- global variable (games counter)
- *args and **kwargs (show_message)
- Lists, tuples and dictionaries
- Packing and unpacking
- while loops, for loops over strings, nested functions

## Author

Behnosh
