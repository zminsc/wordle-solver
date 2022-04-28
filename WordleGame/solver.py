from WordleGame import color_codes

class Solver:
    def __init__(self, game):
        self.game = game
        self.possible_guesses = game.valid_words
        self.must_have_letters = []

    def update(self, game):
        self.game = game
        self.update_possible_guesses(game)

    def generate_guess(self):
        if self.game.words_guessed == 0:
            return "PHONY"
        elif self.game.words_guessed == 1:
            return "CAMEL"
        elif self.game.words_guessed == 2:
            return "DUITS"
        else:
            guess_values = self.assign_values(self.create_letter_frequency_table(), self.game.words_guessed)
            return self.possible_guesses[guess_values.index(max(guess_values))]

    def create_letter_frequency_table(self):
        frequency_table = {}
        for i in range(130):
            frequency_table[chr(ord('A')+int(i/5))+str(i%5)] = 0
        for i in range(len(self.possible_guesses)):
            for j in range(5):
                frequency_table[self.possible_guesses[i][j]+str(j)] += 1
        return frequency_table

    def create_pair_frequency_table(self):
        frequency_table = {}
        for i in range(26):
            for j in range(26):
                frequency_table[str(chr(ord('A')+i)+chr(ord('A')+j))] = 0
        for i in range(len(self.possible_guesses)):
            for j in range(4):
                frequency_table[str(self.possible_guesses[i][j]+self.possible_guesses[i][j+1])] += 1
        return frequency_table

    def assign_values(self, frequency_table, cur_guess):
        value_list = []
        for word in self.possible_guesses:
            value = 0
            unique_letters = list(set(word))
            keys = []
            for unique_letter in unique_letters:
                for i in range(len(word)):
                    if word[i] == unique_letter:
                        keys.append(str(unique_letter)+str(i))
            for i in range(len(keys)):
                value += frequency_table[keys[i]]
            value_list.append(value)
        return value_list

    def update_possible_guesses(self, game):
        new_possible_guesses = []
        # remove all words with yellow letter in wrong position
        yellowed_letters = []
        yellowed_letters_indexes = []
        for i in range(5):
            if self.game.guesses_colors[self.game.words_guessed - 1][i] == color_codes.yellow:
                yellowed_letter = self.game.guesses[self.game.words_guessed - 1][i]
                yellowed_letters.append(yellowed_letter)
                yellowed_letters_indexes.append(i)
                if yellowed_letter not in self.must_have_letters:
                    self.must_have_letters.append(yellowed_letter)
        if len(yellowed_letters) != 0:
            for guess in self.possible_guesses:
                okay = True
                for i in range(len(yellowed_letters)):
                    if yellowed_letters[i] in guess:
                        if yellowed_letters[i] == guess[yellowed_letters_indexes[i]]:
                            okay = False
                    else:
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
                green_letter = self.game.guesses[self.game.words_guessed - 1][i]
                green_letters.append(green_letter)
                green_letters_indexes.append(i)
                if green_letter not in self.must_have_letters:
                    self.must_have_letters.append(green_letter)
        if (len(green_letters)) != 0:
            for guess in self.possible_guesses:
                okay = True
                for i in range(len(green_letters)):
                    if guess[green_letters_indexes[i]] != green_letters[i] or green_letters[i] not in guess:
                        okay = False
                if okay:
                    new_possible_guesses.append(guess)
            self.possible_guesses = new_possible_guesses
            new_possible_guesses = []

        blacked_letters = []
        blacked_letters_indexes = []
        for i in range(5):
            if self.game.guesses_colors[self.game.words_guessed-1][i] == color_codes.black:
                blacked_letters.append(self.game.guesses[self.game.words_guessed-1][i])
                blacked_letters_indexes.append(i)
        for guess in self.possible_guesses:
            okay = True
            for i in range(len(blacked_letters)):
                if blacked_letters[i] in guess:
                    if blacked_letters[i] in self.must_have_letters:
                        if guess[blacked_letters_indexes[i]] == blacked_letters[i]:
                            okay = False
                    else:
                        okay = False
            if okay:
                new_possible_guesses.append(guess)
        self.possible_guesses = new_possible_guesses