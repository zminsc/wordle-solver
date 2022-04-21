from WordleGame import color_codes

class Solver:
    def __init__(self, game):
        self.game = game
        self.possible_guesses = game.valid_words

    def update(self, game):
        self.game = game
        self.update_possible_guesses(game)

    def generate_guess(self):
        if self.game.words_guessed == 0:
            return "ADIEU"
        else:
            self.update_possible_guesses(self.game)
            guess_values = self.assign_values(self.create_frequency_table())
            return self.possible_guesses[guess_values.index(max(guess_values))]

    def create_frequency_table(self):
        frequency_table = {}
        for i in range(26):
            frequency_table[chr(ord('A')+i)] = 0
        for i in range(len(self.possible_guesses)):
            for j in range(5):
                frequency_table[self.possible_guesses[i][j]] += 1
        return frequency_table

    def assign_values(self, frequency_table):
        # return values of each possible guess as a list
        # read possible_guesses
        # assign value using frequency table?
        # consider double letter
        value_list = []
        for word in self.possible_guesses:
            value = 0
            for i in range(len(word)):
                value += frequency_table[(word[i])]
            value_list.append(value)
        return value_list

    def update_possible_guesses(self, game):
        # remove all words containing blacked letters
        new_possible_guesses = []
        blacked_letters = []
        for i in range(5):
            if self.game.guesses_colors[self.game.words_guessed-1][i] == color_codes.black:
                blacked_letters.append(self.game.guesses[self.game.words_guessed-1][i])
        for guess in self.possible_guesses:
            found = False
            for blacked_letter in blacked_letters:
                if blacked_letter in guess:
                    found = True
            if not found:
                new_possible_guesses.append(guess)
        self.possible_guesses = new_possible_guesses
        new_possible_guesses = []

        # remove all words with yellow letter in wrong position
        yellowed_letters = []
        yellowed_letters_indexes = []
        for i in range(5):
            if self.game.guesses_colors[self.game.words_guessed - 1][i] == color_codes.yellow:
                yellowed_letters.append(self.game.guesses[self.game.words_guessed - 1][i])
                yellowed_letters_indexes.append(i)
        if len(yellowed_letters) != 0:
            for guess in self.possible_guesses:
                okay = True
                for i in range(len(yellowed_letters)):
                    if yellowed_letters[i] in guess and yellowed_letters[i] == guess[yellowed_letters_indexes[i]]:
                        okay = False
                if okay:
                    new_possible_guesses.append(guess)
            self.possible_guesses = new_possible_guesses
            new_possible_guesses = []

        # add all words with green letter in correct position
        green_letters = []
        green_letters_indexes = []
        for i in range(5):
            if self.game.guesses_colors[self.game.words_guessed-1][i] == color_codes.green:
                green_letters.append(self.game.guesses[self.game.words_guessed - 1][i])
                green_letters_indexes.append(i)
        if (len(green_letters)) != 0:
            for guess in self.possible_guesses:
                okay = True
                for i in range(len(green_letters)):
                    if guess[green_letters_indexes[i]] != green_letters[i]:
                        okay = False
                if okay:
                    new_possible_guesses.append(guess)
            self.possible_guesses = new_possible_guesses