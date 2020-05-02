board =[
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
	[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
]

x, y = 12, 6


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

