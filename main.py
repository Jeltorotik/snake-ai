import pygame
from collections import deque
import random

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 50)

HEIGHT, WIDTH = 800, 800 
SIZE_OF_BLOCK = 25
SNAKE_COLOR = (20, 255, 50)
FOOD_COLOR = (200, 20, 40)

game_h = HEIGHT // SIZE_OF_BLOCK
game_w = WIDTH // SIZE_OF_BLOCK

#The game is 16x16 (each block is 50x50 px)

screen = pygame.display.set_mode((HEIGHT, WIDTH))


def draw_a_block(x, y, color, size):
	shell = size // 25
	x *= size
	y *= size
	x += shell
	y += shell
	pygame.draw.rect(screen, color, [x, y, size - shell*2, size - shell*2])


board = [[0] * game_h for _ in range(game_w)]
"""
0 - empty block
1 - snake
2 - food
"""

class Snake:
	def __init__(self, x, y):
		self.body = deque([[x, y]])
		self.next = "right"
		board[x][y] = 1


	def move_head(self):
		x, y = self.body[0]
		if self.next == "right":
			dx, dy = 1, 0
		elif self.next == "left":
			dx, dy = -1, 0
		elif self.next == "up":
			dx, dy = 0, -1
		else:
			dx, dy = 0, 1

		self.body.appendleft([x+dx, y+dy])

		if (x+dx < 0 or game_h <= x+dx) or \
			(y+dy < 0 or game_w <= y+dy) or \
			 board[x+dx][y+dy] == 1:
			#Game over
			return 1

		elif board[x+dx][y+dy] == 0:
			#Nothing
			board[x+dx][y+dy] = 1
			return 0
		else:
			#Food
			board[x+dx][y+dy] = 1
			return 2



	def pop_tail(self):
		x, y = self.body.pop()
		board[x][y] = 0


def spawn_food():
	x, y = random.randint(0, game_h-1), random.randint(0, game_w-1)
	while board[x][y] != 0:
		x, y = random.randint(0, game_h-1), random.randint(0, game_w-1)
	board[x][y] = 2
	return x, y



snake = Snake(5, 3)
food = spawn_food()


### GAMELOOP
running = True
score = 0
clock = pygame.time.Clock()
while running:

	#Controlling snake
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		#Button pressed
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				if snake.next in ["up", "down"]:
					snake.next = "left"
			elif event.key == pygame.K_RIGHT:
				if snake.next in ["up", "down"]:
					snake.next = "right"
			elif event.key == pygame.K_UP:
				if snake.next in ["left", "right"]:
					snake.next = "up"
			elif event.key == pygame.K_DOWN:
				if snake.next in ["left", "right"]:
					snake.next = "down"
	

	#Rewaring snake
	reward = snake.move_head()
	if reward == 0:
		snake.pop_tail()
	elif reward == 2:
		score += 1
		food = spawn_food()
	else:

		endfont = pygame.font.SysFont('Comic Sans MS', 120)
		gameover = endfont.render("Game Over", False, (255, 255, 255))
		screen.blit(gameover,(165,350))
		pygame.display.update()

		pygame.time.wait(3000)
		running = False

	# Drawing stuff:
	screen.fill((0, 0, 0))
	for block in snake.body:
		draw_a_block(*block, SNAKE_COLOR, SIZE_OF_BLOCK)
	draw_a_block(*food, FOOD_COLOR, SIZE_OF_BLOCK)

	textsurface = myfont.render("score: " + str(score), False, (255, 255, 255))
	screen.blit(textsurface,(0,0))

	pygame.display.update()
	
	clock.tick(3.7)