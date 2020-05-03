import pickle
from utils import get_inputs


class NN():
	def __init__(self, size_of_game):
		with open(f"best_phenotypes/phenotype-{size_of_game}", 'rb') as input:
			self.net = pickle.load(input)

	def get_move(self, x, y, board):
		inputs = get_inputs(x, y, board)
		output = net.activate(inputs)
		argmax = output.index(max(output))
		move = ["left","right","up","down"][argmax]
		return move
