import pygame
from settings import Settings

infrompy_settings = Settings()

def playsound(soundname):
	if soundname == 'theme1':
		pygame.mixer.music.load('sound effects/theme1.wav')
		pygame.mixer.music.set_volume(0.2 * infrompy_settings.music_volume)
		pygame.mixer.music.play(-1)
	if soundname == 'explosion1':
		explosion1 = pygame.mixer.Sound('sound effects/explosion1.wav')
		explosion1.set_volume(0.05 * infrompy_settings.sound_effect_volume)
		explosion1.play()
	elif soundname == 'explosion2':
		explosion1 = pygame.mixer.Sound('sound effects/explosion2.wav')
		explosion1.set_volume(0.07 * infrompy_settings.sound_effect_volume)
		explosion1.play()
	elif soundname == 'laser1':
		explosion1 = pygame.mixer.Sound('sound effects/laser1.wav')
		explosion1.set_volume(0.1 * infrompy_settings.sound_effect_volume)
		explosion1.play()
	elif soundname == 'laser2':
		explosion1 = pygame.mixer.Sound('sound effects/laser2.wav')
		explosion1.set_volume(0.1 * infrompy_settings.sound_effect_volume)
		explosion1.play()