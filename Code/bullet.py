import pygame

from variables import bullet_audio, BULLET_IMAGE, SHOOTING_AUDIO
import spaceship

class Bullet:

    def __init__(self, TheGame):
        self.window = TheGame.window
        self.window_rect = TheGame.window.get_rect()
        self.ship = TheGame.ship.spaceship_rect

        self.bullet_image = pygame.image.load(BULLET_IMAGE[0])
        self.bullet_audio = bullet_audio
        self.bullet_rect = self.bullet_image.get_rect()
        self.bullet_rect.midbottom = self.window_rect.midbottom
        self.bullet_rect.x = self.ship.x + 20
        self.bullet_rect.y = self.ship.y + 20
        self.up = False
        self.speed = 20

    def blitbullet(self):
        self.window.blit(self.bullet_image, self.bullet_rect)

    def movement(self):
        if self.up is True:
            self.bullet_rect.y -= self.speed
        if self.up is True and self.bullet_rect.y >= self.ship.y - 20:
            bullet_audio.play()
            self.bullet_rect.y -= self.speed
        if self.bullet_rect.y <= 0:
            self.bullet_rect.y = self.ship.y + 20
            self.bullet_rect.x = self.ship.x + 20
        
        if self.up is False:
            if self.bullet_rect.y > 0 and self.bullet_rect.y < self.ship.y + 1:
                self.bullet_rect.y -= self.speed
            else:
                self.bullet_rect.x = self.ship.x + 20
                self.bullet_rect.y = self.ship.y + 20