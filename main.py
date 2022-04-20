from WordleGame.game import Game
from WordleGame.solver import Solver
from WordleGame.utility import read_words

# initialize the words
word_list = read_words("WordleWordList.txt")

game = Game(word_list)
solver = Solver(game)

while not game.is_over():
    game.display()
    game.make_guess(str(input("Make a guess: ")))

game.display()