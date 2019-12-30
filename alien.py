import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from AlienExplosion import Alien_Explosion
import random
class Alien(Sprite):
	
	def __init__(self, infrompy_settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.infrompy_settings = infrompy_settings

		# Load Alien image (different levels have diffrent images)

		self.level = infrompy_settings.alien_level
		if infrompy_settings.alien_level % 4 == 1:
			self.image = pygame.image.load('images/alien.png')
		elif infrompy_settings.alien_level % 4 == 2:
			self.image = pygame.image.load('images/alien2.png')
		elif infrompy_settings.alien_level % 4 == 3:
			self.image = pygame.image.load('images/alien3.png')
		elif infrompy_settings.alien_level % 4 == 0:
			self.image = pygame.image.load('images/alien4.png')

		self.rect = self.image.get_rect()

		# Start each new alien near the top left of the screen
		self.rectx = self.rect.width
		self.rect.y = self.rect.height

		# Store the alien's position

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Aliens firing tick
		self.current_tick = 0
		self.firing_tick = int(infrompy_settings.alien_start_firing_tick) + random.randint(0, int(infrompy_settings.alien_firing_interval))

		# Alien's health points
	
		self.health = infrompy_settings.alien_level * infrompy_settings.alien_max_health 
		
		# Alien's ticks before death
		self.death_ticks = 0
		# Alien's score when killed
		self.score = 100*self.level
	

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		# Return true if alien touches edge of screen
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def update(self):
		self.current_tick += 1
		# Increase death ticks (makes alien linger after death)
		if self.health <= 0:
			self.death_ticks += 1 
		# Move aliens to the right
		self.x += (self.infrompy_settings.alien_speed_factor * self.infrompy_settings.fleet_direction)
		self.rect.x = self.x


