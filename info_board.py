import pygame

class Info_Board():
	def __init__(self,infrompy_settings, screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.infrompy_settings = infrompy_settings
		self.white = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 40) 
		

	def prep_info(self):
		self.level_string = str(self.infrompy_settings.alien_level)
		self.level_image = self.font.render('Lvl: '+ self.level_string, True, self.white)
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.screen_rect.right - 20
		self.level_rect.top = 20
	
		self.score_string = str(self.infrompy_settings.score)
		self.score_image = self.font.render('Score: '+ self.score_string, True, self.white)
		self.score_rect = self.level_image.get_rect()
		self.score_rect.left = self.screen_rect.left + 20
		self.score_rect.top = 20

		self.health_string = str(self.infrompy_settings.ship_health)
		self.health_image = self.font.render('HP: '+ self.health_string, True, self.white)
		self.health_rect = self.level_image.get_rect()
		self.health_rect.right = self.screen_rect.right - 20
		self.health_rect.bottom = self.screen_rect.bottom - 20

	def display_info(self):
		self.screen.blit(self.level_image, self.level_rect)
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.health_image, self.health_rect)

