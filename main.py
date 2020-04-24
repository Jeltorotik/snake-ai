import pygame
from collections import deque
import random

class BruteForce:
	def __init__(self, game_h, game_w, x, y):
		self.game_h = game_h
		self.game_w = game_w
		self.x = 0
		self.y = 0
		
		self.generator = self.move()
		while self.x != x or self.y != y:
			next(self.generator)
			print(self.x, self.y)
		

	def move(self):
		while True:
			self.x += 1
			yield "right"
			for i in range(self.game_w//2 - 1):

				for j in range(self.game_h-2):
					self.y += 1
					yield "down"
				self.x += 1
				yield "right"
				for j in range(self.game_h-2):
					self.y -= 1
					yield "up"
				print("asfdsf", self.x, self.y)
				self.x += 1
				yield "right"

			for i in range(self.game_h-1):
				self.y += 1
				yield "down"
			for i in range(self.game_w-1):
				self.x -= 1
				yield "left"
			for i in range(self.game_h-1):
				self.y -= 1
				yield "up"
			





pygame.init()
pygame.font.init()


HEIGHT, WIDTH = 800, 800 
SIZE_OF_BLOCK = 50

SNAKE_COLOR = (20, 255, 50)
FOOD_COLOR = (200, 20, 40)
WHITE = (255, 255, 255)

game_h = HEIGHT // SIZE_OF_BLOCK
game_w = WIDTH // SIZE_OF_BLOCK

#The game is 16x16 (each block is 50x50 px)

screen = pygame.display.set_mode((HEIGHT, WIDTH))

def print_str(string, x, y, font_size, color):
	myfont = pygame.font.SysFont('Comic Sans MS', font_size)
	textsurface = myfont.render(string, False, color)
	screen.blit(textsurface,(x,y))

def draw_a_block(x, y, type_of_block,color, size):
	#Scaling
	shell = size // 25
	x *= size
	y *= size
	if type_of_block == "lying":
		y += shell
		pygame.draw.rect(screen, color, [x, y, size, size - shell*2])
	elif type_of_block == "standing":
		x += shell
		pygame.draw.rect(screen, color, [x, y, size - shell*2, size])
	else:
		x += shell
		y += shell
		pygame.draw.rect(screen, color, [x, y, size - shell*2, size - shell*2])




board = [[0] * game_h for _ in range(game_w)]
for i in board:
	print(i)
"""
0 - empty block
1 - snake
2 - food
"""

class Snake:
	def __init__(self, x, y):
		self.body = deque([[x, y, "standing"]])
		self.next = "right"
		board[x][y] = 1


	def move_head(self):
		print(self.body[0])
		x, y, _ = self.body[0]

		if self.next == "right":
			dx, dy = 1, 0
			type_of_block = "lying"
		elif self.next == "left":
			dx, dy = -1, 0
			type_of_block = "lying"
		elif self.next == "up":
			dx, dy = 0, -1
			type_of_block = "standing"
		else:
			dx, dy = 0, 1
			type_of_block = "standing"

		self.body.appendleft([x+dx, y+dy, type_of_block])
		
		if (x+dx < 0 or game_h <= x+dx) or \
			(y+dy < 0 or game_w <= y+dy) or \
			 board[x+dx][y+dy] == 1:
			#Game over
			return 1

		elif board[x+dx][y+dy] == 0:
			#Nothing
			self.pop_tail()
			board[x+dx][y+dy] = 1
			return 0
		else:
			#Food
			board[x+dx][y+dy] = 1
			return 2



	def pop_tail(self):
		x, y, _ = self.body.pop()
		board[x][y] = 0


def spawn_food():
	x, y = random.randint(0, game_h-1), random.randint(0, game_w-1)
	while board[x][y] != 0:
		x, y = random.randint(0, game_h-1), random.randint(0, game_w-1)
	board[x][y] = 2
	return x, y



snake = Snake(0, 0)
food = spawn_food()

#### Solution algorithims:
#1) Brute force
bf = BruteForce(game_h, game_w, snake.body[0][0], snake.body[0][1])




### GAMELOOP
running = True
score = 0
clock = pygame.time.Clock()
dt = 0
next_move = "right"
state = False
while running:


		#Controlling snake manually
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		#Button pressed
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				if snake.next in ["up", "down"]:
					next_move = "left"
			elif event.key == pygame.K_RIGHT:
				if snake.next in ["up", "down"]:
					next_move = "right"
			elif event.key == pygame.K_UP:
				if snake.next in ["left", "right"]:
					next_move = "up"
			elif event.key == pygame.K_DOWN:
				if snake.next in ["left", "right"]:
					next_move = "down"
	#########
	#Here we can control snake with algorithms:
	#1)Brute force:
	next_move = next(bf.generator)
	
	print(bf.x, bf.y)

	

	#Moving snake
	snake.next = next_move
	reward = snake.move_head()

	#Rewaring snake
	if reward == 2:
		score += 1
		food = spawn_food()
	elif reward == 1:
		print_str("Game Over", 165, 350, 120, WHITE)

		pygame.display.update()
		pygame.time.wait(30000)
		running = False

		######## VISUAL PART
	# Drawing stuff:
	screen.fill((255, 255, 255))
	for i in range(game_h):
		for j in range(game_w):
			draw_a_block(i, j, "empty", (0,0,0), SIZE_OF_BLOCK)

	for block in snake.body:
		draw_a_block(*block, SNAKE_COLOR, SIZE_OF_BLOCK)
	draw_a_block(*food, "food", FOOD_COLOR, SIZE_OF_BLOCK)

	print_str("score: " + str(score), 0, 0, 50, WHITE)

	pygame.display.update()

	clock.tick(100)
	####################
	
#Todo
"""
1) Angle parts of snake drawings
2) Brute force - Done
3) Figure out how to make game more smooth
"""