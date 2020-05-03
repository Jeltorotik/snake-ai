import pygame
from collections import deque
import random


def draw_a_block(screen, x, y, type_of_block, color, size):
	#Scaling
	shell = size // 25
	x *= size
	y *= size
	h, w = size, size

	if type_of_block == "horizontal":
		y += shell
		w -= shell*2
	elif type_of_block == "vertical":
		x += shell
		h -= shell*2
	elif type_of_block in ["empty","food"]:
		x += shell
		y += shell
		h -= shell*2
		w -= shell*2
	pygame.draw.rect(screen, color, [x, y, h, w])



def show_text(screen,text, x, y, font_size, color):
	myfont1 = pygame.font.SysFont('Comic Sans MS', font_size)
	myfont2 = pygame.font.SysFont('Comic Sans MS', font_size+2)
	textsurface1 = myfont1.render(text, False, color)
	textsurface2 = myfont2.render(text, False, (0,0,0))
	
	screen.blit(textsurface2,(x+1,y+1))
	screen.blit(textsurface1,(x,y))



class Snake():

	def __init__(self, h, w):
		"""
		x, y - initial position of a snake 
		h, w - height and width of the board

		Board:
		0 - empty block
		1 - snake block
		2 - food block
		"""
		self.score = 0

		self.h = h
		self.w = w
		x, y = random.randint(0, self.h-1), random.randint(0, self.w-1)
		self.body = deque([[x, y, "standing"]])

		self.last_move = "right"
		self.next_move = "right"

		self.board = [[0] * h for _ in range(w)]
		self.board[x][y] = 1

		self.spawn_food()

		self.moves = {"right":  [1, 0, "horizontal"],
						"left": [-1, 0, "horizontal"],
						"up":   [0, -1, "vertical"],
						"down": [0, 1, "vertical"]}

	def get_head(self):
		return self.body[0][0], self.body[0][1]


	def is_valid_move(self, move):
		if move not in self.moves.keys():
			return False
		if move in ["up", "down"] and self.last_move in ["up", "down"]:
			return False
		if move in ["left", "right"] and self.last_move in ["left", "right"]:
			return False
		return True


	def move(self):
		"""
		moves snake's head, updates board and returns reward:
		1) "Game over" (Out of border or ate itself)
		2) "Food" (snake ate food)
		3) None (snake just succesfully moves)
		"""
		self.last_move = self.next_move
		dx, dy, block = self.moves[self.next_move]

		x, y = self.get_head()
		if (0 <= x+dx < self.h) and (0 <= y+dy < self.w):

			self.body.appendleft([x+dx, y+dy, block])
			#Poping tail
			x_tail, y_tail, _ = self.body[-1]

			self.board[x_tail][y_tail] = 0

			if self.board[x+dx][y+dy] == 1:
				return "Game over"

			elif self.board[x+dx][y+dy] == 0:
				self.board[x+dx][y+dy] = 1
				self.body.pop()
				return None
			else:
				self.board[x+dx][y+dy] = 1
				self.board[x_tail][y_tail] = 1
				self.score += 1
				if self.score == self.h * self.w - 1:
					return "Game over"
				else:
					self.spawn_food()
					return "Food"
		else:
			return "Game over"




	def spawn_food(self):
		"""
		spawns food at random free block of board
		"""
		x = random.randint(0, self.h-1)
		y = random.randint(0, self.w-1)
		while self.board[x][y] != 0:
			x = random.randint(0, self.h-1)
			y = random.randint(0, self.w-1)
		self.board[x][y] = 2
		self.food = [x, y]



	def draw(self, screen, size):
		"""
		Draws board, snake and food
		"""

		SNAKE_COLOR = (20, 255, 50)
		FOOD_COLOR = (200, 20, 40)

		screen.fill((255, 255, 255))

		#Board
		for i in range(self.h):
			for j in range(self.w):
				draw_a_block(screen, i, j, "empty", (0,0,0), size)

		#Snake
		for block in self.body:
			draw_a_block(screen, *block, SNAKE_COLOR, size)

		draw_a_block(screen, *self.food, "food", FOOD_COLOR, size)

		show_text(screen, "score: " + str(self.score), 0, 0, 50, (255,255,255))

		