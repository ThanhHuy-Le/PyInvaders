import pygame 

from settings import Settings

class Ship():
	def __init__(self, infrompy_settings, screen):

		# self.speed = 5 (speed now in settings.py)
		self.infrompy_settings = infrompy_settings
		
		# Stating ship position
		self.screen = screen

		# Load ship image
		self.image = pygame.image.load('images/ship.png')
		self.image_original = pygame.image.load('images/ship.png')
		self.image_invul = pygame.image.load('images/ship_invul.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		# Make ship hitbox smaller than ship.rect
		self.hitbox =  pygame.rect.Rect((0, 0), (int(self.rect.width/2), int(self.rect.height*3/4)))
		self.hitbox.centerx = self.rect.centerx
		self.hitbox.centery = self.rect.centery



		#Start with new ship at bottom
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#storing a decimal value for ship center
		self.center = float(self.rect.centerx)

		# Movement flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		# Shooting flag/ticks
		self.shooting = False
		self.shooting_tick = 0
		self.shoot_delay = infrompy_settings.shoot_delay

		# Invulnerable flag
		self.invul = False
		self.invul_tick = 0

		# Ship health and death status
		self.health = infrompy_settings.ship_health
		self.dead = False
		self.death_tick = 0 





	def update(self):
		# update ship's position based on movement flags
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.infrompy_settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.rect.centerx -= self.infrompy_settings.ship_speed
		if self.moving_up and self.rect.top > 0:
			self.rect.centery -= self.infrompy_settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.rect.centery += self.infrompy_settings.ship_speed

		# Update shooting ticks
		if self.shooting:
			if self.shooting_tick < self.shoot_delay :
				self.shooting_tick += 1
			else:
				self.shooting_tick = 0

		# Update invul ticks
		if self.invul:
			self.invul_tick -= 1
			if self.invul_tick%6 == 0 or self.invul_tick%6 == 1 or self.invul_tick%6 == 2:
				self.image = self.image_invul
			else:
				self.image = self.image_original
			if self.invul_tick <= 0:
				self.invul = False
				self.invul_tick = 0
				self.image = self.image_original

		if self.health <= 0:
			self.dead = True

		self.hitbox.centerx = self.rect.centerx
		self.hitbox.centery = self.rect.centery
		
	def blitme(self):
		#draw ship at current location
		self.screen.blit(self.image, self.rect)





