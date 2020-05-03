from snake import *

from bruteForce import BruteForce
from BFS import BFS

import os
import neat

from utils import get_inputs, get_checkpoint_filename, pause
import pickle


pygame.font.init()




HEIGHT, WIDTH = 800, 800 
#(each block is 50x50 px)
size_of_game = 16#int(input("Input size of the game(8x8, 16x16, 32x32, 80x80)\n:"))

SIZE_OF_BLOCK = HEIGHT // size_of_game  #TODO
H = size_of_game
W = size_of_game

screen = pygame.display.set_mode((HEIGHT, WIDTH))








def manual_control():
	global dt
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			exit()

		#Button pressed
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_p:
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



dt = 0
fps = 30


def main(genomes, config):

	global dt, fps

	#NEAT RL:
	snakes = []
	ge = []
	nets = []
	for _, g in genomes:
		net = neat.nn.FeedForwardNetwork.create(g, config)
		nets.append(net)
		snakes.append(Snake(H, W))
		g.fitness = 0
		ge.append(g)

	
	clock = pygame.time.Clock()
	while True:

		#For pausing, speeding up and down
		manual_control()


		#Training NEAT
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
			if reward == "Game over" or ge[x].fitness < -1:
				ge[x].fitness -= 10
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
		fps += dt
		clock.tick(fps)
		





def train(config_file):
	"""
	runs the NEAT algorithm to train a neural network to play snake.
	:param config_file: location of config file
	:return: None
	"""
	
	# Load configuration.
	config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
								neat.DefaultSpeciesSet, neat.DefaultStagnation,
								config_file)

	# Create the population, which is the top-level object for a NEAT run.

	restart = "n"#input("Restart? [Y/n]:\n")
	if restart == "Y":
		print("Restarting...")
		p = neat.Population(config)
	else:
		try:
			filename = get_checkpoint_filename(size_of_game)
			p = neat.Checkpointer.restore_checkpoint(filename)
			print(f"Restored {filename}")
		except:
			p = neat.Population(config)


	p.add_reporter(neat.StdOutReporter(True))
	p.add_reporter(neat.StatisticsReporter())

	#Saves checkpoint with interval of 100 generations
	filename_prefix = 'neat-checkpoints/neat-checkpoint-' + str(size_of_game) + "-"
	p.add_reporter(neat.Checkpointer(1, filename_prefix=filename_prefix))


	#Run for 2000 generations
	winner = p.run(main, 1)

	winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
	
	with open(f"best_phenotypes/phenotype-{size_of_game}", 'wb') as output:
		pickle.dump(winner_net, output, pickle.HIGHEST_PROTOCOL)



if __name__ == '__main__':
	# Determine path to configuration file. This path manipulation is
	# here so that the script will run successfully regardless of the
	# current working directory.
	local_dir = os.path.dirname(__file__)
	config_path = os.path.join(local_dir, 'config-feedforward.txt')
	train(config_path)




	
