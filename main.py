from WordleGame.game import Game
from WordleGame.solver import Solver
from WordleGame.utility import read_words

# initialize the words
word_list = read_words("WordleWordList.txt")

games_solved = 0
guesses_taken = []

game = Game(word_list)
solver = Solver(game)

for i in range(1000):
    game = Game(word_list)
    solver = Solver(game)
    while not game.is_over():
        game.make_guess(solver.generate_guess())
        solver.update(game)
    if game.won:
        guesses_taken.append(game.words_guessed)
        games_solved += 1

print("Solve Rate: " + str(games_solved/10) + "%")
print("Average Guesses Taken: " + str(sum(guesses_taken)/len(guesses_taken)))