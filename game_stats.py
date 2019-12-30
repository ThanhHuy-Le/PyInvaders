class GameStats():
	# Track stats
	def __init__(self,infrompy_settings):
		self.infrompy_settings = infrompy_settings
		self.reset_stats()

	def reset_stats(self):
		self.ships_left = self.infrompy_settings.ship_limit
