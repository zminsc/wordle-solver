import color_codes
from random import randint

class Game:
    def __init__(self, valid_words):
        self.valid_words = valid_words
        self.correct_word = valid_words[randint(0, len(valid_words))]
        self.yellow_letters = list(set(self.correct_word))
        self.words_guessed = 0
        self.guesses = [""] * 6
        self.guesses_colors = [[""]*5 for i in range(6)]
        self.alphabet_colors = [""]*26
        print(self.correct_word)

    def make_guess(self, guess):
        guess = guess.upper()
        if self.validate_guess(guess):
            self.guesses[self.words_guessed] = guess
            self.update_guesses_colors()
            self.update_alphabet_colors()
            self.words_guessed += 1

    def validate_guess(self, guess):
        if len(guess) != 5:
            return False
        elif guess not in self.valid_words:
            return False
        else:
            return True

    def update_guesses_colors(self):
        for i in range(0, 5):
            self.guesses_colors[self.words_guessed][i] = color_codes.black
        for i in range(0, len(self.yellow_letters)):
            for j in range(0, 5):
                if self.guesses[self.words_guessed][j] == self.yellow_letters[i]:
                    self.guesses_colors[self.words_guessed][j] = color_codes.yellow
        for i in range(0, 5):
            if self.guesses[self.words_guessed][i] == self.correct_word[i]:
                self.guesses_colors[self.words_guessed][i] = color_codes.green

    def update_alphabet_colors(self):
        for i in range(0, 5):
            self.alphabet_colors[ord(self.guesses[self.words_guessed][i])-ord('A')] = self.guesses_colors[self.words_guessed][i]

    def display(self):
        self.display_guesses()
        self.display_alphabet()

    def display_guesses(self):
        print("======== WORDLE ========")
        for i in range(0, self.words_guessed):
            print(" " + str(i+1) + ". ", end="")
            for j in range(0, 5):
                print(self.guesses_colors[i][j] + " " + self.guesses[i][j] + " " + color_codes.flush, end=" ")
            print()
        for i in range(self.words_guessed, 6):
            print(" " + str(i+1) + ".  _   _   _   _   _  ")
        print("========================")

    def display_alphabet(self):
        print("  ", end="")
        for i in range(0, 26):
            print(self.alphabet_colors[i] + " " + chr(i+ord('A')) + " " + color_codes.flush, end=" ")
            if i % 5 == 4:
                print("   ")
                print("  ", end="")
        print()

    def is_over(self):
        if self.words_guessed >= 6:
            return True
        if self.guesses[self.words_guessed-1] == self.correct_word:
            return True
        return False