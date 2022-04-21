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
        for i in range(0, 26):
            frequency_table[chr(ord('A')+i)] = 0
        for i in range(0, len(self.possible_guesses)):
            for j in range(0, 5):
                frequency_table[self.possible_guesses[i][j]] += 1
        return frequency_table

    def assign_values(self, frequency_table):
        # return values of each possible guess as a list
        return []

    def update_possible_guesses(self, game):
        # go through the list of possible guesses and update it
        return self.possible_guesses