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
	btns = [Button("Manual","Manual",                  200, 150, h, w, (0,0,0),(255, 255, 255)), 
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
				print
				if event.key == pygame.K_p:
					paused = False
