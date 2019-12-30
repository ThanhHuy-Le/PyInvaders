import pygame
import random
from pygame.sprite import Sprite


class Alien_Bullet_Explosion(Sprite):
	# Bulltets from our spaceship

	def __init__(self, screen, alien_bullet):
		super(Alien_Bullet_Explosion,self).__init__()
		self.screen = screen
		self.image = pygame.image.load('images/explosion/Explosion1.png')
		self.image1 = pygame.image.load('images/explosion/Explosion1.png')
		self.image2 = pygame.image.load('images/explosion/Explosion2.png')
		self.image3 = pygame.image.load('images/explosion/Explosion3.png')
		self.image4 = pygame.image.load('images/explosion/Explosion4.png')
		self.image5 = pygame.image.load('images/explosion/Explosion5.png')
		self.image6 = pygame.image.load('images/explosion/Explosion6.png')
		self.image7 = pygame.image.load('images/explosion/Explosion7.png')
		self.rect = self.image1.get_rect()
		self.rect.centerx = alien_bullet.rect.centerx
		self.rect.centery = alien_bullet.rect.centery + 2 * alien_bullet.speed + random.randint(0, alien_bullet.speed)
		#self.rect.top = bullet.rect.top +10

		self.tick = 0
		self.y = float(self.rect.centery)

	
	def update(self):
		# Change explosion states
		self.tick += 1
		if self.tick == 1:
			self.image = self.image1
		elif self.tick == 2:
			self.image = self.image2
		elif self.tick == 3:
			self.image = self.image3
		elif self.tick == 4:
			self.image = self.image4
		elif self.tick == 5:
			self.image = self.image5
		elif self.tick == 6:
			self.image = self.image6
		elif self.tick == 7:
			self.image = self.image7	

	def draw_alien_bullet_explosion(self):
		self.screen.blit(self.image, self.rect)

