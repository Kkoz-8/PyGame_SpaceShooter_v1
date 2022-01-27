import pygame

from variables import window, background_image, icon, title, clock, fps
import spaceship, bullet, events, mobs
from functions import score_tracker

class TheGame:

    def __init__(self):
        #initialize pygame modules
        pygame.init()

        self.window = window
        self.window_rect = self.window.get_rect()
        self.icon = icon
        self.background_image = background_image
        self.title = title

        #These need to be in a correct order
        self.ship = spaceship.SpaceShip(self) #same as "self.bullet" comment
        self.bullet = bullet.Bullet(self) #"self.bullet" to represent instance of class "Bullet", while passing instance of class "TheGame" to class "Bullet" as parameter "self"
        self.events = events.Events(self) #same as "self.bullet" comment
        self.mobs = mobs.Mobs(self) #same as "self.bullet" comment

    def run_game(self):
        
        while True:
            self.events.events()
            self.ship.movement()
            self.bullet.movement()
            self.updates()
            
            clock.tick(fps) #game fps
            score_tracker() #score tracker
            pygame.display.flip() #make the most recently drawn screen visible

    def updates(self):
        self.window.blit(self.background_image, self.window_rect)
        self.bullet.blitbullet()
        self.ship.blitme()
        self.mobs.mob_blit()