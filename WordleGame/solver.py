class Solver:
    def __init__(self, game):
        self.game = game
        self.frequency_table = {}
        self.possible_guesses = game.valid_words

    def update(self, game):
        self.game = game
        self.update_possible_guesses(game)

    def generate_guess(self):
        guess = "ADIEU"
        return guess

    def update_frequency_table(self):
        return {}

    def assign_values(self, frequency_table):
        # return values of each possible guess as a list
        return []

    def update_possible_guesses(self, game):
        # go through the list of possible guesses and update it
        return self.possible_guesses