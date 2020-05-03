class BruteForce():
	def __init__(self, game_h, game_w, x, y):
		self.game_h = game_h
		self.game_w = game_w
		self.x = 0
		self.y = 0
		
		self.generator = self.move()
		while self.x != x or self.y != y:
			next(self.generator)
		

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