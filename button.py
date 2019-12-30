import pygame.font

class Button():
	def __init__(self, infrompy_settings, screen, msg):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = 200,50

		self.button_color = (255,255,255)
		self.text_color = (0,0,0)
		self.font = pygame.font.SysFont(None,48)
		self.rect = pygame.Rect(0,0, self.width, self.height)
		self.rect.center = self.screen_rect.center

		# Button message only need to be prepped once
		#self.prep_msg(self, msg)
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center


	def prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect_center


	def draw_button(self):
		# Draw button then draw message
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)

