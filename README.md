# wordle-solver

A Wordle solver that uses letter frequency analysis to guess words efficiently. Uses the following strategy:

1. Starts with initial guesses ("PHONY", then "CAMEL", then "DUITS")
2. For subsequent guesses:
   - Analyze frequency of letters in remaining possible words,
   - Eliminate words that don't match the feedback from previous guesses,
   - Select the word with the highest probability of containing common letters.

## Requirements

- Python 3.6 or higher

## Setup & Usage

Clone the repository:

```
git clone https://github.com/zminsc/wordle-solver.git
cd wordle-solver
```

Then:

```
python main.py
```

This will output:

- The solve rate (% of games where word was guessed in under 6 guesses)
- The average number of guesses across all simulations
