import pygame
from pygame.sprite import Sprite


class Background(pygame.sprite.Sprite):
	def __init__(self, infrompy_settings, screen):
		super(Background, self).__init__()
		self.screen = screen
		self.infrompy_settings = infrompy_settings
		self.screen_rect = screen.get_rect()

		self.image = pygame.image.load('images/background.png')
		self.rect = self.image.get_rect()
		
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
	def blitme(self):
		self.screen.blit(self.image, self.rect)
