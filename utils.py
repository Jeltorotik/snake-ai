import os
import pygame


def get_inputs(x, y, board):
	"""
	Generates 8x3 input values for RL algorithm.
	For each of 8 sides of head calculates 3 vales:
	1) Distance from the wall
	2) Distance from the body
	3) Distance form the food
	UL U UR 
	L    R
	DL D DR
	:param head - position of the head - x, y; board
	:return: list of 24 values: 
	[upper-left-wall, upper-left-body, upper-left-food upper-wall, etc..]
	"""
	h, w = len(board), len(board[0])
	sides = [[-1,-1], [-1, 0],[-1, 1],[0,  1],[1,  1], [1, 0], [1, -1],[0, -1]]


	result = []

	for dx, dy in sides:
		temp_x, temp_y = x, y
		dist = 0
		triple = [-1,-1,-1] # wall, body, food
		while True:
			dist += abs(dx)
			dist += abs(dy)
			temp_x += dx
			temp_y += dy
			#wall
			if not ((0 <= temp_x < h) and (0 <= temp_y < w)):
				triple[0] = dist
				break
			#body
			if board[temp_x][temp_y] == 1 and triple[1] == -1:
				triple[1] = dist
			#food
			if board[temp_x][temp_y] == 2:
				triple[2] = dist

		result += triple[:]

	return result



def get_checkpoint_filename(size_of_game):
	"""
	Takes integer size_of_game
	returns filenamethe best available checkpoint for this size
	"""

	path = "neat-checkpoints"
	filenames = os.listdir(path)

	filenames = [name.split("-") for name in filenames]

	check_size = lambda x: x[2] == str(size_of_game) 
	filenames = list(filter(check_size, filenames))


	filenames = [int(name[3]) for name in filenames]

	name = str(max(filenames))
	name = "neat-checkpoint-" + str(size_of_game) + "-" + name

	return path + "/" + name




def pause():
	print("PAUSE")
	paused = True
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_p:
					paused = False
				if event.type == pygame.QUIT:
					exit()

