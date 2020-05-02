from snake import *

from bruteForce import BruteForce
from BFS import BFS



pygame.font.init()




HEIGHT, WIDTH = 800, 800 
#(each block is 50x50 px)
size_of_game = int(input("Input size of the game(8x8, 16x16, 32x32, 80x80)\n:"))

SIZE_OF_BLOCK = HEIGHT // size_of_game  #TODO
H = size_of_game
W = size_of_game

screen = pygame.display.set_mode((HEIGHT, WIDTH))




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



def manual_control():
	global dt
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			exit()

		#Button pressed
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				return "left"
			elif event.key == pygame.K_RIGHT:
				return "right"
			elif event.key == pygame.K_UP:
				return "up"
			elif event.key == pygame.K_DOWN:
				return "down"

			elif event.key == pygame.K_p:
				pause()
			elif event.key == pygame.K_LSHIFT:
				dt = 1
			elif event.key == pygame.K_LCTRL:
				dt = -1

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LSHIFT:
				dt = 0
			if event.key == pygame.K_LCTRL:
				dt = 0




attempt = 0
fps = 60
dt = 0
while True:
	attempt += 1

	# Initialization of snake
	snake = Snake(0, 0, H, W)
	# Solution algorithims:
	#1) Brute force
	bf = BruteForce(H, W, *snake.get_head())
	#2) BFS
	bfs = BFS()
	# Gameloop
	running = True
	clock = pygame.time.Clock()
	
	while running:

		#Here we can control snake with algorithms:
		#1)Manually:
		move = manual_control()

		#2)Brute force:
		#move = next(bf.generator)

		#3)BFS
		#move, path = bfs.find_path(*snake.get_head(), snake.board)

		#Validation of the move
		if snake.is_valid_move(move):
			snake.next_move = move


		#Rewaring snake
		reward = snake.move()

		if reward == "Game over":
			print_str(screen, "Game Over", 165, 350, 120, (255,255,255))
			pygame.display.update()
			pygame.time.wait(1000)
			running = False

		snake.draw(screen, SIZE_OF_BLOCK, attempt)



		fps += dt
		fps = max(1, fps)
		fps = min(100, fps)
		clock.tick(fps)








	
#Todo
"""
- [+]  Fix bfs (when there's no possible path just go the longest available)
- [ ]  Add RL algorithm
- [ ]  Add A* path Finding
- [+]  Split code into blocks and make it mode readable
- [ ]  Add Documentation
- [+]  Add Ability to change speed and algorithm in-game; set game on pause
- [ ]  Make beautiful edges of snake
"""