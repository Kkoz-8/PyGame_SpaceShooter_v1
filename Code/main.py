import pygame

import game, menu
from variables import BACKGROUND_AUDIO
pygame.mixer.init()

#background audio
pygame.mixer.music.load(BACKGROUND_AUDIO[0])
pygame.mixer.music.play(-1) #plays the audio, "-1" loops the audio

#create instances
start_game = game.TheGame()
menu_screen = menu.Menu()

#start main game loop
menu_screen.menu()
start_game.run_game()