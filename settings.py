class Settings():

	def __init__(self):
		#Game settings and game settings
		self.screen_width = 1200
		self.screen_height = 600
		self.bg_color = (0,0,150)

		# Game active or not
		self.game_active = False

		# Ship settings
		self.ship_speed = 6
		self.shoot_delay = 5 # Lower means higher sustained shotting speed
		self.ship_health = 10
		self.ship_limit = 3
		self.ship_dead = False
		self.ship_invul_time = 30

		# Bullet settings
		self.bullet_base_damage = 5
		self.bullet_speed = 6
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = 200,200,200

		# Alien Bullet settings
		self.bullet_speed_alien = 5
		self.bullet_damage_alien = 1

		# Alien Bullet firing delay
		self.alien_firing_interval = 100
		self.alien_start_firing_tick = 10

		# Alien Settings
		self.alien_max_health = 5
		self.alien_speed_factor = 2
		self.fleet_drop_speed = 10
		self.alien_level = 1
		self.alien_bullet_base_damage = 1

		# Sound settings
		self.music_volume = 1.0
		self.sound_effect_volume = 1.0

		# Fleet direction of 1 represents right; -1 left
		self.fleet_direction = 1

		# Red_screen settings
		self.red_screen_duration = 30

		# Score stat
		self.score = 0
	def add_score_alien_dead(self):
		self.score  += 100 * self.alien_level
	def add_score_level_clear(self):
		self.score  += 1000 * self.alien_level
