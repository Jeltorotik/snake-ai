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




attempt = 0
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




		#Controlling snake manually
		#keys =	pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()

			#Button pressed
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					if snake.is_valid_move("left"):
						snake.next_move = "left"
				elif event.key == pygame.K_RIGHT:
					if snake.is_valid_move("right"):
						snake.next_move = "right"
				elif event.key == pygame.K_UP:
					if snake.is_valid_move("up"):
						snake.next_move = "up"
				elif event.key == pygame.K_DOWN:
					if snake.is_valid_move("down"):
						snake.next_move = "down"

		#########
		#Here we can control snake with algorithms:
		#1)Brute force:
		#snake.next_move = next(bf.generator)
		#2)BFS
		move, path = bfs.find_path(*snake.get_head(), snake.board)
		if snake.is_valid_move(move):
			snake.next_move = move
		


		#Rewaring snake
		reward = snake.move()

		if reward == "Game over":
			print_str(screen, "Game Over", 165, 350, 120, (255,255,255))
			pygame.display.update()
			pygame.time.wait(1000)
			running = False

		snake.draw(screen, SIZE_OF_BLOCK)

		print_str(screen, "attempt: " + str(attempt), 0, 55, 50, (255,255,255))


		clock.tick(15)










	
#Todo
"""
- [+]  Fix bfs (when there's no possible path just go the longest available)
- [ ]  Add RL algorithm
- [ ]  Add A* path Finding
- [+]  Split code into blocks and make it mode readable
- [ ]  Add Documentation
- [ ]  Add Ability to change speed and algorithm in-game
- [ ]  Make beautiful edges of snake
"""