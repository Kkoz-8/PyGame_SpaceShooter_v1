import pygame, sys

class Events:

    def __init__(self, TheGame):
        self.thegame = TheGame
        self.ship = TheGame.ship #grab the class "TheGame" attribute "self.ship", reference it to "self.ship" attribute here
        self.bullet = TheGame.bullet #same as above

    def events(self):
        #check for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown(event)
            elif event.type == pygame.KEYUP:
                self._keyup(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._mousebuttondown(event)
            elif event.type == pygame.MOUSEBUTTONUP:
                self._mousebuttonup(event)
                
    def _keydown(self, event):
        if event.key == pygame.K_d:
            self.ship.right = True
        if event.key == pygame.K_a:
            self.ship.left = True
        if event.key == pygame.K_s:
            self.ship.down = True
        if event.key == pygame.K_w:
            self.ship.up = True
        if event.key == pygame.K_q:
                sys.exit()

    def _mousebuttondown(self, event):
        if event.button == 1:
            self.bullet.up = True            
    
    def _mousebuttonup(self, event):
        if event.button == 1:
            self.bullet.up = False

    def _keyup(self, event):
        if event.key == pygame.K_d:
            self.ship.right = False
        if event.key == pygame.K_a:
            self.ship.left = False
        if event.key == pygame.K_s:
            self.ship.down = False
        if event.key == pygame.K_w:
            self.ship.up = False