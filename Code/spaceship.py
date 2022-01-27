import pygame

from variables import width, height, spaceship_image

class SpaceShip:

    def __init__(self, TheGame):
        self.window = TheGame.window #access game window 
        self.window_rect = TheGame.window.get_rect() #get rect of game window
        self.spaceship_image = spaceship_image #loads spaceship image
        self.spaceship_rect = self.spaceship_image.get_rect() #gets the rect of the spaceship image
        self.spaceship_rect.midbottom = self.window_rect.midbottom #positions spaceship midbottom to the window rect midbottom
        self.right = False 
        self.left = False 
        self.down = False 
        self.up = False 
        self.speed = 8 #speed at which ship will move at

    def blitme(self):
        #constantly blits the spaceship image to the window
        self.window.blit(self.spaceship_image, self.spaceship_rect)

    def movement(self):
        #updates ship position based on user input
        if self.spaceship_rect.x < 0:
            self.spaceship_rect.x = 0
        if self.spaceship_rect.x > width - 64:
            self.spaceship_rect.x = width - 64

        if self.spaceship_rect.y < height/1.5:
            self.spaceship_rect.y = height/1.5
        if self.spaceship_rect.y > height - 64:
            self.spaceship_rect.y = height - 64

        if self.right:
            self.spaceship_rect.x += self.speed
        if self.left:
            self.spaceship_rect.x -= self.speed
        if self.down:
            self.spaceship_rect.y += self.speed
        if self.up:
            self.spaceship_rect.y -= self.speed