import pygame, sys

from variables import window, menu_image, icon, title, clock, fps

class Menu:

    def __init__(self):
        #initialize pygame modules
        pygame.init()

        self.window = window
        self.window_rect = self.window.get_rect()
        self.icon = icon
        self.menu_image = menu_image
        self.title = title

    def menu(self):
        menu = True

        while menu:
            self.window.blit(self.menu_image, self.window_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    menu = False

            clock.tick(fps)
            pygame.display.flip()