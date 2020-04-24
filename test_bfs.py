from collections import deque
class BFS:
	def __init__(self, game_h, game_w):
		self.game_h = game_h
		self.game_w = game_w
		### TODO BOARD

	def find_vertex(self, x, y):
		q = deque([[x,y]])
		used = [[False] * self.game_w for _ in range(self.game_h)] # visited vertecies
		self.p = [[0] * self.game_w for _ in range(self.game_h)]
		
		used[x][y] = True
		self.p[x][y] = -1
		while q:
			c_x, c_y = q.popleft()
			for dx, dy, move in [[0,1, "right"],[0,-1, "left"],[1,0, "down"],[-1,0, "up"]]:
				if (0 <= c_x + dx < self.game_h) and (0 <= c_y + dy < self.game_w):
					if board[c_x+dx][c_y+dy] == 2: #Found food
						self.target = [c_x+dx, c_y+dy, move]
						self.p[c_x+dx][c_y+dy] = [c_x, c_y, move]
						return
					if board[c_x+dx][c_y+dy] == 0: #Empty cell
						if used[c_x+dx][c_y+dy] == False: #And not visited
							used[c_x+dx][c_y+dy] = True 
							q.append([c_x+dx, c_y+dy])
							self.p[c_x+dx][c_y+dy] = [c_x, c_y, move]


	def find_path(self):
		path = []
		x, y, move = self.target
		while True:
			path.append(move)
			prev = self.p[x][y]
			if prev == -1:
				break
			elif prev == 0:
				return "No path"
			else:
				x, y, move = prev
		return path

	def generator(self):
		while True:
			path = find_path()
			while path:
				yield path.pop()

board = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0]
]

bfs = BFS(16, 16)
bfs.find_vertex(11, 10)
print(bfs.find_path())