import sys 
from bullet import Bullet
import pygame
import sounds
import random
from alien import Alien
from background import Background
from BulletExplosion import Bullet_Explosion
from AlienExplosion import Alien_Explosion
from AlienBulletExplosion import Alien_Bullet_Explosion
from ShipExplosion import Ship_Explosion
from alien_bullet import Alien_Bullet
from red_screen import Red_Screen


def check_keydown_events(event, infrompy_settings, screen, ship, bullets, bullet_explosions):
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
		ship.moving_left = True
	elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
		ship.moving_down = True
	elif event.key == pygame.K_UP or event.key == pygame.K_w:
		ship.moving_up = True
	elif event.key == pygame.K_SPACE:
		ship.shooting = True



def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
		ship.moving_left = False
	elif event.key == pygame.K_UP or event.key == pygame.K_w:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
		ship.moving_down = False
	elif event.key == pygame.K_SPACE:
		ship.shooting = False
		ship.shooting_tick = 0

def check_events(infrompy_settings, screen, ship, bullets, bullet_explosions, play_button):
	#respond to key presses and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		# Moving
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, infrompy_settings, screen, ship, bullets, bullet_explosions)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(infrompy_settings, play_button, mouse_x, mouse_y)

def check_play_button(infrompy_settings, play_button, mouse_x, mouse_y):
	# Start new game when play button is clicked
	if play_button.rect.collidepoint(mouse_x,mouse_y):
		infrompy_settings.game_active = True

def update_screen(infrompy_settings, screen, ship, ship_explosions, aliens, bullets, bullet_explosions, alien_explosions, alien_bullets, alien_bullet_explosions, info_board, play_button,play_again_button, red_screen):
	

	# Redraw old bullets behind aliens and ship
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	for alien_bullet in alien_bullets:
		alien_bullet.draw_alien_bullet()

	ship.blitme()
	aliens.draw(screen)

	if not infrompy_settings.game_active and infrompy_settings.ship_dead == False:
		play_button.draw_button()
	elif infrompy_settings.ship_dead == True:
		play_again_button.draw_button()


	for bullet_explosion in bullet_explosions:
		bullet_explosion.draw_bullet_explosion()

	for alien_bullet_explosion in alien_bullet_explosions:
		alien_bullet_explosion.draw_alien_bullet_explosion()

	for alien_explosion in alien_explosions:
		alien_explosion.draw_alien_explosion()

	for ship_explosion in ship_explosions:
		ship_explosion.draw_ship_explosion()

	# Check redscreen on
	if red_screen.on:
		red_screen.blitme

	# Check whether to shoot:
	if ship.shooting_tick == 2:
		sounds.playsound('laser1')
		new_bullet = Bullet(infrompy_settings, screen, ship, bullet_explosions)
		bullets.add(new_bullet)
	# Check whether aliens shoot
	for alien in aliens:
		if alien.current_tick == alien.firing_tick:
			sounds.playsound('laser2')
			new_alien_bullet = Alien_Bullet(infrompy_settings, screen, ship, alien)
			alien_bullets.add(new_alien_bullet)
		elif alien.current_tick >= infrompy_settings.alien_start_firing_tick + infrompy_settings.alien_firing_interval:
			alien.current_tick = 0

	info_board.prep_info()
	info_board.display_info()
	
	#Make most recent screen visible
	pygame.display.flip()

def update_bullets(infrompy_settings, aliens, screen, ship, bullets, bullet_explosions, alien_explosions, alien_bullets):
	# Update positions of bullets and remove old bullets
	# CHeck for bullets that have hit aliens
	# Get rid of bullet and alien

	for bullet in bullets:
		for alien in aliens:
			if pygame.sprite.collide_rect(alien, bullet):
				bullet.exploded = True
				new_bullet_explosion = Bullet_Explosion(screen, bullet)
				bullet_explosions.add(new_bullet_explosion)
				sounds.playsound('explosion1')
				bullets.remove(bullet)
				alien.health -= bullet.damage
	
	if len(aliens) == 0:
		bullets.empty()
		alien_bullets.empty()
		infrompy_settings.add_score_level_clear()
		infrompy_settings.alien_level += 1
		infrompy_settings.alien_firing_interval = max(50, infrompy_settings.alien_firing_interval - 50)
		create_fleet(infrompy_settings, screen, ship, aliens)
	

	#colisions = pygame.sprite.groupcollide(bullets, aliens, True, False)

	bullets.update()
	# Remove bullets
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def update_alien_bullets(infrompy_settings, aliens, screen, ship, alien_bullets, alien_bullet_explosions, red_screen):

	alien_bullets.update()
	for alien_bullet in alien_bullets:
		if pygame.Rect.colliderect(ship.hitbox,alien_bullet):
			alien_bullet.exploded = True
			new_alien_bullet_explosion = Alien_Bullet_Explosion(screen, alien_bullet)
			alien_bullet_explosions.add(new_alien_bullet_explosion)
			sounds.playsound('explosion1')
			alien_bullets.remove(alien_bullet)
			if not ship.invul:
				ship.health -= alien_bullet.damage
				red_screen.turn_on()
				infrompy_settings.ship_health = ship.health
				ship.invul = True
				ship.invul_tick = infrompy_settings.ship_invul_time

	for alien_bullet in alien_bullets.copy():
		if alien_bullet.rect.top >= infrompy_settings.screen_height:
			alien_bullets.remove(alien_bullet)


def update_bullet_explosions(aliens, screen, bullets, bullet_explosions):
	bullet_explosions.update()
	for bullet_explosion in bullet_explosions.copy():
		if bullet_explosion.tick >= 8:
			bullet_explosions.remove(bullet_explosion)

def update_alien_bullet_explosions(aliens, screen, alien_bullet_explosions):
	alien_bullet_explosions.update()
	for alien_bullet_explosion in alien_bullet_explosions.copy():
		if alien_bullet_explosion.tick >= 8:
			alien_bullet_explosions.remove(alien_bullet_explosion)

def update_alien_explosions(aliens, screen, alien_explosions):

	alien_explosions.update()
	for alien_explosion in alien_explosions.copy():
		if alien_explosion.tick >= 8:
			alien_explosions.remove(alien_explosion)

def update_ship_explosions(ship, screen, ship_explosions):

	ship_explosions.update()
	for ship_explosion in ship_explosions.copy():
		if ship_explosion.tick >= 8:
			ship_explosions.remove(ship_explosion)


def create_fleet(infrompy_settings, screen, ship, aliens):
	# Create an alien and find number of aliens in a row
	# Spacing between aliens is equal to one alien width
	alien = Alien(infrompy_settings, screen)
	number_aliens_x = get_number_aliens_x(infrompy_settings, alien.rect.width)
	number_rows = get_number_rows(infrompy_settings, ship.rect.height, alien.rect.height)


	# Create fleet
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(infrompy_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(infrompy_settings, alien_width):
	# Find number of aliens (duh)
	available_space_x = infrompy_settings.screen_width - 2*alien_width
	number_aliens_x = int(available_space_x / (1.3*alien_width))
	return number_aliens_x

def create_alien(infrompy_settings, screen, aliens,alien_number, row_number):
	# Create an alien and place it in a row
	alien = Alien(infrompy_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 1.3 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height/2 + 1.3 * alien.rect.height * row_number
	aliens.add(alien)


def get_number_rows(infrompy_settings, ship_height, alien_height):
	# Determine number of rows of aliens that fit on screen
	available_space_y = (infrompy_settings.screen_height - (3 * ship_height))
	number_rows = int(available_space_y / (1.5 *alien_height))
	return number_rows

def check_fleet_edges(infrompy_settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(infrompy_settings, aliens)
			break

def change_fleet_direction(infrompy_settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += infrompy_settings.fleet_drop_speed
	infrompy_settings.fleet_direction *= -1

def update_aliens(infrompy_settings, aliens, screen, ship, alien_explosions, alien_bullets, red_screen):
	

	for alien in aliens:
		if alien.health <= 0:
			if alien.death_ticks == 1:
				sounds.playsound('explosion2')
				new_explosion1 = Alien_Explosion(screen,alien) 
				alien_explosions.add(new_explosion1)
				new_explosion2 = Alien_Explosion(screen,alien) 
				alien_explosions.add(new_explosion2)
			if alien.death_ticks == 3:
				new_explosion1 = Alien_Explosion(screen,alien) 
				alien_explosions.add(new_explosion1)
				new_explosion2 = Alien_Explosion(screen,alien) 
				alien_explosions.add(new_explosion2)
			if alien.death_ticks == 5:
				new_explosion1 = Alien_Explosion(screen,alien) 
				alien_explosions.add(new_explosion1)	
			elif alien.death_ticks >= 6:
				infrompy_settings.add_score_alien_dead()
				aliens.remove(alien)
	# Upate position of all aliens and check if fleet is at edge		
	check_fleet_edges(infrompy_settings, aliens)
	aliens.update()
	
	# Check alien ship collisions
	if pygame.sprite.spritecollideany(ship,aliens) and ship.invul == False:
			red_screen.turn_on()
			ship.health -= 1
			ship.invul = True
			ship.invul_tick = infrompy_settings.ship_invul_time
			infrompy_settings.ship_health = ship.health

def update_red_screen(infrompy_settings, red_screen):
	if red_screen.on:
		red_screen.blitme()
		red_screen.tick += 1
		if red_screen.tick >= red_screen.duration:
			red_screen.on = False
			red_screen.tick = 0

def update_ship(infrompy_settings, screen, ship, ship_explosions):
	ship.update()
	if ship.dead == True:
		ship.moving_right = False
		ship.moving_left = False
		ship.moving_up = False
		ship.moving_down = False
		ship.shoting = False
		ship.death_tick += 1
		if ship.death_tick == 60:
			infrompy_settings.game_active = False
		else:
			sounds.playsound('explosion1')
			new_explosion = Ship_Explosion(screen,ship) 
			ship_explosions.add(new_explosion)









