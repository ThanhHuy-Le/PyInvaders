import sys

import pygame
from pygame.sprite import Group
import sounds

from settings import Settings
from ship import Ship
from alien import Alien
from background import Background
from alien_bullet import Alien_Bullet
from game_stats import GameStats
from info_board import Info_Board
from red_screen import Red_Screen
from button import Button
import game_functions as gf


def run_game():
	#Initialize game and make a screen object
	pygame.init()
	sounds.playsound('theme1')

	infrompy_settings = Settings()
	screen = pygame.display.set_mode((infrompy_settings.screen_width, infrompy_settings.screen_height))
	screenRect = screen.get_rect()
	pygame.display.set_caption("Invaders")
	background = Background(infrompy_settings, screen)
	red_screen = Red_Screen(infrompy_settings, screen)

	# Make play button and replay button
	play_button = Button(infrompy_settings, screen, "Play")
	play_again_button = Button(infrompy_settings, screen, "Your ship ded lol. Play Again ?")
	# Make an instance to store game stats
	stats = GameStats(infrompy_settings)
	# Make a ship, group of bullets and group of aliens
	ship = Ship(infrompy_settings, screen)
	ship_explosions = Group()
	bullets = Group()
	bullet_explosions = Group()
	aliens = Group()
	alien_explosions = Group()
	alien_bullets = Group()
	alien_bullet_explosions = Group()
	background = Background(infrompy_settings, screen)
	

	# Level board
	info_board = Info_Board(infrompy_settings,screen)
	# Bullets group
	gf.create_fleet(infrompy_settings, screen, ship, aliens)


	while True:
		background.blitme()
		gf.check_events(infrompy_settings, screen, ship, bullets, bullet_explosions, play_button)
		if infrompy_settings.game_active:
		
			gf.update_aliens(infrompy_settings, aliens, screen, ship, alien_explosions, alien_bullet_explosions, red_screen)
			gf.update_alien_explosions(aliens, screen, alien_explosions)

			gf.update_ship(infrompy_settings, screen, ship, ship_explosions)
			gf.update_ship_explosions(ship, screen, ship_explosions)

			gf.update_bullet_explosions(aliens, screen, bullets, bullet_explosions)
			gf.update_bullets(infrompy_settings, aliens, screen, ship, bullets, bullet_explosions, alien_explosions, alien_bullets)

			gf.update_alien_bullets(infrompy_settings, aliens, screen, ship, alien_bullets, alien_bullet_explosions, red_screen)
			gf.update_alien_bullet_explosions(aliens, screen, alien_bullet_explosions)
			gf.update_red_screen(infrompy_settings, red_screen)

		gf.update_screen(infrompy_settings, screen, ship, ship_explosions, aliens, bullets, bullet_explosions, alien_explosions, alien_bullets, alien_bullet_explosions, info_board, play_button, play_again_button,red_screen)
		

		#print(len(bullets))
 



run_game()