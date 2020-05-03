import pygame

class Button:
	def __init__(self, text,val, x, y, w, h, color, text_color):
		self.text = text
		self.val = val
		self.x = x
		self.y = y
		self.W = w 
		self.H = h
		self.color = color
		self.text_color = text_color


	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.W, self.H))
		font = pygame.font.SysFont("comicsans", 40)
		text = font.render(self.text, 5, self.text_color)
		win.blit(text, (self.x + round(self.W/2)-round(text.get_width()/2), 
						self.y + round(self.H/2)-round(text.get_height()/2) ) )


	def click(self, pos):
		x1 = pos[0]
		y1 = pos[1]
		if (self.x <= x1 <= self.x + self.W) and (self.y <= y1 <= self.y + self.H):
			return True
		else:
			return False



def wait_for_click(screen, btns):

	screen.fill((255, 255, 255))
	for btn in btns:
		btn.draw(screen)
	pygame.display.update()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				for btn in btns:
					if btn.click(pos):
						return btn.val



def choose_size(screen):
	h, w = 400, 125
	btns = [Button("8x8",    8, 200, 150, h, w, (0,0,0),(255, 255, 255)), 
			Button("16x16", 16, 200, 300, h, w, (0,0,0),(255, 255, 255)), 
			Button("32x32", 32, 200, 450, h, w, (0,0,0),(255, 255, 255)),
			Button("80x80", 80, 200, 600, h, w, (0,0,0),(255, 255, 255))]

	return wait_for_click(screen, btns)


def choose_control(screen):
	h, w = 400, 125
<<<<<<< HEAD
	btns = [Button("Arrow Keys","Manual",              200, 150, h, w, (0,0,0),(255, 255, 255)), 
=======
	btns = [Button("Manual","Manual",                  200, 150, h, w, (0,0,0),(255, 255, 255)), 
>>>>>>> b532d065b97acebe7664c4e288d754cc043e7727
			Button("Brute Force","Brute Force",        200, 300, h, w, (0,0,0),(255, 255, 255)), 
			Button("BFS", "BFS",                       200, 450, h, w, (0,0,0),(255, 255, 255)),
			Button("Neural Network", "Neural Network", 200, 600, h, w, (0,0,0),(255, 255, 255))]

	return wait_for_click(screen, btns)


def pause(screen):
	paused = True

	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			if event.type == pygame.KEYDOWN:
<<<<<<< HEAD
				paused = False


def show_text(screen,text, x, y, font_size, color, out=True):
	myfont1 = pygame.font.SysFont('Comic Sans MS', font_size)
	myfont2 = pygame.font.SysFont('Comic Sans MS', font_size+2)
	textsurface1 = myfont1.render(text, False, color)
	textsurface2 = myfont2.render(text, False, (0,0,0))
	if out:
		screen.blit(textsurface2,(x+1,y+1))
	screen.blit(textsurface1,(x,y))


def display_intro(screen):
	screen.fill((255,255,255))
	show_text(screen, "Press a key", 275, 360, 60, (0,0,0), out=False)
	pygame.display.update()
	pause(screen)


def display_info(screen):
	INFO = pygame.image.load("info.png")
	screen.blit(INFO, (0, 0))
	pygame.display.update()
	pause(screen)
=======
				print
				if event.key == pygame.K_p:
					paused = False
>>>>>>> b532d065b97acebe7664c4e288d754cc043e7727
