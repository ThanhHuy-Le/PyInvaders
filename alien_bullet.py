import pygame
from pygame.sprite import Sprite
from BulletExplosion import Bullet_Explosion

class Alien_Bullet(Sprite):
	# Bulltets from our spaceship

	def __init__(self, infrompy_settings, screen, ship, alien):
		super(Alien_Bullet,self).__init__()
		self.screen = screen
		if alien.level <= 4:
			self.image = pygame.image.load('images/bullet2.png')
			self.damage = infrompy_settings.alien_bullet_base_damage
		elif alien.level >= 4:
			self.image = pygame.image.load('images/bullet3.png')
			self.damage = infrompy_settings.alien_bullet_base_damage * 2
		elif alien.level >= 4:
			self.image = pygame.image.load('images/bullet3.png')
			self.damage = infrompy_settings.alien_bullet_base_damage * 2
		self.rect = self.image.get_rect()
		self.rect.centerx = alien.rect.centerx
		self.rect.centery = alien.rect.centery


		self.exploded = False
		self.y = float(self.rect.centery)
		
		self.speed = infrompy_settings.bullet_speed_alien
	
		#self.damage = infrompy_settings.alien_bullet_base_damage #* infrompy_settings.alien_level

	def update(self):
		# Move bullet up the screen
		# Update y position
		self.y += self.speed
		self.rect.centery = self.y

	def draw_alien_bullet(self):
		self.screen.blit(self.image, self.rect)


			
