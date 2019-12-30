import pygame
from pygame.sprite import Sprite
from BulletExplosion import Bullet_Explosion

class Bullet(Sprite):
	# Bulltets from our spaceship

	def __init__(self, infrompy_settings, screen, ship, bullet_explosions):
		super(Bullet,self).__init__()
		self.screen = screen
		self.image = pygame.image.load('images/bullet1.png')
		self.rect = self.image.get_rect()
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top


		self.exploded = False
		self.y = float(self.rect.centery)
		self.color = infrompy_settings.bullet_color
		self.speed = infrompy_settings.bullet_speed
	
		self.damage = infrompy_settings.bullet_base_damage

	def update(self):
		# Move bullet up the screen
		# Update y position
		self.y -= self.speed
		self.rect.centery = self.y

	def draw_bullet(self):
		self.screen.blit(self.image, self.rect)


			
