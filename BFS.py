from collections import deque

class BFS:

	def bfs(self, x, y, board):
		h, w = len(board), len(board[0])

		q = deque([[x,y]])

		used = [[False] * w for _ in range(h)] # visited vertecies
		used[x][y] = True

		self.p = [[0] * w for _ in range(h)] # path
		self.p[x][y] = [-1,-1,-1]

		while q:
			c_x, c_y = q.popleft()
			for dx, dy, move in [[0,1, "down"],[0,-1, "up"],[1,0, "right"],[-1,0, "left"]]:

				if (0 <= c_x + dx < h) and (0 <= c_y + dy < w): #Within borders

					if board[c_x+dx][c_y+dy] == 2: #Found food			
						target = [c_x+dx, c_y+dy, move]
						self.p[c_x+dx][c_y+dy] = [c_x, c_y, move]
						return target


					if board[c_x+dx][c_y+dy] == 0: #Empty cell
						if used[c_x+dx][c_y+dy] == False: #And not visited
							used[c_x+dx][c_y+dy] = True 
							q.append([c_x+dx, c_y+dy])
							self.p[c_x+dx][c_y+dy] = [c_x, c_y, move]

		return "No path"


	def find_path(self, x, y, board):

		result = self.bfs(x, y, board)
		if result == "No path":
			h, w = len(board), len(board[0])
			#Just move randomly, until it will find a path or will be trapped
			for dx, dy, move in [[0,1, "down"],[0,-1, "up"],[1,0, "right"],[-1,0, "left"]]:
				if (0 <= x + dx < h) and (0 <= y + dy < w): #Within borders
					if board[x+dx][y+dy] == 0:
						return move, []
			#Actually, this returns just random move because snake trapped
			return move, []


		path = []
		x, y, move = result
		while True:
			path.append([x,y])
			prev = self.p[x][y]
			if prev == [-1,-1,-1]:
				break
			# elif prev == 0:
			# 	return "No path", []
			else:
				x, y, move = prev
		

		return move, path
