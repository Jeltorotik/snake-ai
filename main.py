from snake import *

from gui import choose_size, choose_control, pause

from bruteForce import BruteForce
from BFS import BFS
from NN import NN



def manual_control():
	global dt
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			exit()

		#Button pressed
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				print("hey")
				return "left"
			elif event.key == pygame.K_RIGHT:
				return "right"
			elif event.key == pygame.K_UP:
				return "up"
			elif event.key == pygame.K_DOWN:
				return "down"

			elif event.key == pygame.K_p:
				pause(screen)
			elif event.key == pygame.K_LSHIFT:
				dt = 1
			elif event.key == pygame.K_LCTRL:
				dt = -1

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LSHIFT:
				dt = 0
			if event.key == pygame.K_LCTRL:
				dt = 0


def main(screen, speed, control):
	
	global dt
	dt = 0

	# Initialization of snake
	snake = Snake(H, W)

	# Solution algorithims:
	#1) Brute force
	bf = BruteForce(H, W, *snake.get_head())
	#2) BFS
	bfs = BFS()
	#3) RL
	try:
		net = NN(size_of_game)
	except:
		pass # TODO

	# Gameloop
	clock = pygame.time.Clock()
	
	while True:


		#Here we can control snake
		move = manual_control()
		if control == "Manual":
			#1)Manually:
			pass
		if control == "Brute Force":
			#2)Brute force:

			move = next(bf.generator)
		elif control == "BFS":
			#3)BFS
			move, path = bfs.find_path(*snake.get_head(), snake.board)
		elif control == "Neural Network":
			#4) NN
			try:
				move = net.get_move(*snake.get_head(), snake.board)
			except:
				pass




		#Validation of the move
		if snake.is_valid_move(move):
			snake.next_move = move

		#Rewaring snake
		reward = snake.move()
		if reward == "Game over":
			show_text(screen, "Game Over", 165, 350, 120, (255,255,255))
			pygame.display.update()
			pygame.time.wait(1000)
			break


		snake.draw(screen, SIZE_OF_BLOCK)
		show_text(screen, "speed: " + str(speed), 0, 25, 50, (255,255,255))

		speed += dt
		speed = max(1, speed)
		speed = min(100, speed)

		clock.tick(speed)

		pygame.display.update()



#Basic initialization
pygame.init()
pygame.font.init()
HEIGHT, WIDTH = 800, 800 
screen = pygame.display.set_mode((HEIGHT, WIDTH))


while True:
	size_of_game = choose_size(screen)
	SIZE_OF_BLOCK = HEIGHT // size_of_game  
	H = size_of_game
	W = size_of_game
	control = choose_control(screen)
	main(screen, speed=20, control = control)
	














	
#Todo
"""
- [+]  Fix bfs (when there's no possible path just go the longest available)
- [+]  Add RL algorithm
- [ ]  Add A* path Finding
- [+]  Split code into blocks and make it mode readable
- [ ]  Add Documentation
- [+]  Add Ability to change speed and algorithm in-game; set game on pause
- [ ]  Make beautiful edges of snake
- [ ]  Random Spawn postion of snake, and direction
- [+]  Make training file for NEAT. Organize checkpoints
- [ ]  !!! Organize GUI. Make add ability ot user to choose solution algorithm.
- [ ]  Configure and improve StdOutReporter
- [ ]  Add hybrid: when bfs can't find path - turn on Neural network
"""