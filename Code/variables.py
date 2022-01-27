import glob
import pygame
pygame.mixer.init()

width = 800
height = 600

#will be used to set game fps
clock = pygame.time.Clock() 

#frames per second value
fps = 60

#score tracker
score = 0

#images
BULLET_IMAGE = glob.glob("Extras/bullet.png")
SPACESHIP_IMAGE = glob.glob("Extras/pewpew.png")
HEALTH_SHIPS = glob.glob("Extras/pewpewsmall.png")
MOB_IMAGE = glob.glob("Extras/mob.png")
ICON_IMAGE = glob.glob("Extras/icon.png")
BACKGROUND_IMAGE = glob.glob("Extras/background.png")
MENU_IMAGE = glob.glob("Extras/menu.png")
EXPLOSION_IMAGE = glob.glob("Extras/big_boom.png")

#audio
BACKGROUND_AUDIO  = glob.glob("Extras/background_sound.ogg")
SHOOTING_AUDIO  = glob.glob("Extras/shoot_sound.ogg")
EXPLOSION_AUDIO  = glob.glob("Extras/explode_1.ogg")

#window size, will be used to represent the surface upon which we draw
window = pygame.display.set_mode((width, height))

#window title
title = pygame.display.set_caption("Space Shooter")

#window icon
icon = pygame.image.load(ICON_IMAGE[0])
pygame.display.set_icon(icon)

#background image for game window
background_image = pygame.image.load(BACKGROUND_IMAGE[0])
background_image = pygame.transform.scale(background_image, (width, height)) #Resize image

#menu image
menu_image = pygame.image.load(MENU_IMAGE[0])
menu_image = pygame.transform.scale(menu_image, (width, height)) #Resize image

#spaceship image
spaceship_image = pygame.image.load(SPACESHIP_IMAGE[0])

#HP
hp = pygame.image.load(HEALTH_SHIPS[0])

#mob image
mob_image = pygame.image.load(MOB_IMAGE[0])

#bullet_audio
bullet_audio = pygame.mixer.Sound(SHOOTING_AUDIO[0])
bullet_audio.set_volume(0.05)

#explosion_audio
explosion_audio = pygame.mixer.Sound(EXPLOSION_AUDIO[0])
explosion_audio.set_volume(0.05)