from snake import *

from bruteForce import BruteForce
from BFS import BFS

import os
import neat

from utils import get_inputs


pygame.font.init()




HEIGHT, WIDTH = 800, 800 
#(each block is 50x50 px)
size_of_game = 8#int(input("Input size of the game(8x8, 16x16, 32x32, 80x80)\n:"))

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





def main(genomes, config):

	global dt
	dt = 0
	fps = 30

	# Initialization of snake
	
	# Solution algorithims:
	#1) Brute force
	#bf = BruteForce(H, W, *snake.get_head())
	#2) BFS
	#bfs = BFS()
	#3) NEAT RL:
	snakes = []
	ge = []
	nets = []
	for _, g in genomes:
		net = neat.nn.FeedForwardNetwork.create(g, config)
		nets.append(net)
		snakes.append(Snake(0, 0, H, W))
		g.fitness = 0
		ge.append(g)

	
	clock = pygame.time.Clock()
	while True:

		#Here we can control snake with algorithms:
		#1)Manually:
		#move = manual_control()

		#2)Brute force:
		#move = next(bf.generator)

		#3)BFS
		#move, path = bfs.find_path(*snake.get_head(), snake.board)

		#4)LR
		rewards = []
		for x, snake in enumerate(snakes):
			inputs = get_inputs(*snake.get_head(), snake.board)
			output = nets[x].activate(inputs)
			argmax = output.index(max(output))
			move = ["left","right","up","down"][argmax]
			if snake.is_valid_move(move):
				snake.next_move = move
			else:
				ge[x].fitness -= 0.01
			rewards.append(snake.move())

		for x, reward in enumerate(rewards):
			if reward == "Game over":
				ge[x].fitness -= 1
				rewards.pop(x)
				snakes.pop(x)
				nets.pop(x)
				ge.pop(x)
			elif reward == "Food":
				ge[x].fitness += 1
			else:
				ge[x].fitness -= 0.01

		if len(snakes) == 0:
			break

		snakes[0].draw(screen, SIZE_OF_BLOCK)
		clock.tick(fps)
		
		"""
		#Validation of the move
		 if snake.is_valid_move(move):
		 	snake.next_move = move

		#Rewaring snake
		reward = snake.move()

		if reward == "Game over":

			g.fitness -= 1
			break
		
			print_str(screen, "Game Over", 165, 350, 120, (255,255,255))
			pygame.display.update()
			pygame.time.wait(1000)
			running = False
			
		if reward == "Food":
			g.fitness += 1

		snake.draw(screen, SIZE_OF_BLOCK)

		fps += dt
		fps = max(1, fps)
		fps = min(100, fps)
		clock.tick(fps)
		"""

#main()



def run(config_file):
	"""
	runs the NEAT algorithm to train a neural network to play flappy bird.
	:param config_file: location of config file
	:return: None
	"""
	config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
								neat.DefaultSpeciesSet, neat.DefaultStagnation,
								config_file)

	p = neat.Population(config)

	p.add_reporter(neat.StdOutReporter(True))
	stats = neat.StatisticsReporter()
	p.add_reporter(stats)

	winner = p.run(main, 2000)



if __name__ == '__main__':
	# Determine path to configuration file. This path manipulation is
	# here so that the script will run successfully regardless of the
	# current working directory.
	local_dir = os.path.dirname(__file__)
	config_path = os.path.join(local_dir, 'config-feedforward.txt')
	run(config_path)




	
#Todo
"""
- [+]  Fix bfs (when there's no possible path just go the longest available)
- [+]  Add RL algorithm
- [ ]  Add A* path Finding
- [+]  Split code into blocks and make it mode readable
- [ ]  Add Documentation
- [+]  Add Ability to change speed and algorithm in-game; set game on pause
- [ ]  Make beautiful edges of snake
"""