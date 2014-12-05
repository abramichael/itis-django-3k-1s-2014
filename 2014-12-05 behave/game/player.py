class Player:
	def __init__(self, name):
		self.name = name
		self.hp = 100

	def kicks(self, p, d):
		p.hp -= d
