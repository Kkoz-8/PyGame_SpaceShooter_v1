import pygame, random, math

from variables import *
from functions import *

class Mobs:

    def __init__(self, TheGame):
        self.bullet = TheGame.bullet
        self.ship_rect = TheGame.ship.spaceship_rect

        self.window = TheGame.window
        self.window_rect = TheGame.window.get_rect()

        self.hp = hp #tiny image of spaceship
        self.hp_count = 5
        self.tiny_ships = 40
        self.stop_call = True
        self.get_lives = []

        self.mob_image = mob_image
        self.mob_image = pygame.transform.scale(self.mob_image, (33, 33))
        self.mob_image_rect = self.mob_image.get_rect()
        self.speed = 1
        self.number_of_mobs = 3
        self.MOB_LIST = []
        self.THE_END = False

    def mob_blit(self):
        self.create_mob()
        R_KEY = pygame.key.get_pressed()

        if self.stop_call: #call to get amount of lives
            self.get_lives = self.hp_tracker()

        for rect_values in self.get_lives: #blits the lives to screen
            self.window.blit(self.hp, rect_values)

        try:
            for index, mob in enumerate(self.MOB_LIST):
                #distance calculation formula used to detect collision
                detect_collision_bullet = collision_function_bullet(mob[1][0], mob[1][1], self.bullet.bullet_rect.x, self.bullet.bullet_rect.y)
                detect_collision_ship = collision_function_ship(mob[1][0], mob[1][1], self.ship_rect.x, self.ship_rect.y)

                #check if mob hits ship
                if detect_collision_ship <= 27:
                    self.MOB_LIST.clear()
                    self.hp_count -= 1
                    self.stop_call = True
                    self.tiny_ships = 40
                    if self.hp_count == 0:
                        self.THE_END = True
                        self.speed = 0

                #display game over to screen
                if self.THE_END:
                    game_over()
                    self.number_of_mobs = 3 #reset number of spawning mobs
                    self.bullet.speed = 20 #reset bullet speed
                    if R_KEY[pygame.K_r]:
                        self.THE_END = False
                        self.speed = 1
                        self.create_mob()
                        self.hp_count = 5
                        self.stop_call = True
                        score_tracker(True)

                #check if bullet and mob comes within a certain distance of each other, remove that mob from list if true
                if detect_collision_bullet <= 27:
                    explosion_audio.play()
                    self.MOB_LIST.remove(self.MOB_LIST[index])
                    self.bullet.bullet_rect.x = width

                #each time a mob hits bottom of game window, remove it from the list
                if self.MOB_LIST[index][1][1] >= height:
                    self.MOB_LIST.remove(self.MOB_LIST[index])

                #check is at least 1 mob object is still in the list, blit the mob to game window and continue updating its movements
                if len(self.MOB_LIST) >= 1:
                    self.window.blit(self.mob_image, (mob[1][0], mob[1][1]))
                    self.MOB_LIST[index][1][1] += self.speed
        
        #when iterating the list, if the list updates during iteration, we get an IndexError. expect the error and call method "create_mob()" to handle it
        except IndexError:
            self.create_mob()

    def create_mob(self):
        if len(self.MOB_LIST) == 0:
            for element in range(self.number_of_mobs): #range here to specify how many mobs to spawn
                if not self.THE_END:
                    mob_x = random.randint(0, width - 40)
                    mob_y = random.randint(0, height - (0.7 * height))
                else: #if THE_END is True, shifts all mobs offscreen
                    mob_x = width
                    mob_y = height
                self.MOB_LIST.append((self.mob_image, [mob_x, mob_y]))
            
            #increase mob count and bullet speed each time the "if" statement is True (that is, self.MOB_LIST == 0)
            self.number_of_mobs += 1
            self.bullet.speed += 1

    def hp_tracker(self):
        temp = []
        for i in range(self.hp_count):
            temp.append(self.window.blit(self.hp, (width - self.tiny_ships, 0)))
            self.tiny_ships += 40
        self.stop_call = False
        return temp