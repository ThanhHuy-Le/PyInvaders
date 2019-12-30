import pygame
from pygame.sprite import Sprite


class Red_Screen(pygame.sprite.Sprite):
	def __init__(self, infrompy_settings, screen):
		super(Red_Screen, self).__init__()
		self.screen = screen
		self.infrompy_settings = infrompy_settings
		self.screen_rect = screen.get_rect()

		self.image = pygame.image.load('images/red_screen.png')
		self.rect = self.image.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery

		self.on = False
		self.duration = infrompy_settings.red_screen_duration
		self.tick = 0
	def blitme(self):
		self.screen.blit(self.image, self.rect)
	def turn_on(self):
		self.on = True
	def turn_off(self):
		self.on = False