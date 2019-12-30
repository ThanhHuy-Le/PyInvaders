import pygame

class Info_Board():
	def __init__(self,infrompy_settings, screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.infrompy_settings = infrompy_settings
		self.white = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 50) 
		

	def prep_level(self):
		self.level_string = str(self.infrompy_settings.alien_level)
		self.level_image = self.font.render('Level '+ self.level_string, True, self.white)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right - 20
		self.level_rect.top = 20
	def display_level(self):
		self.screen.blit(self.level_image, self.level_rect)

