import pygame 

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
				print("hey")
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
