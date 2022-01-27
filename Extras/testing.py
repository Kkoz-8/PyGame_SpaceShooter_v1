# import pygame


# def game_loop():
#     pygame.init()
#     gameDisplay = pygame.display.set_mode((640, 480))
#     clock = pygame.time.Clock()
#     bulletpicture = pygame.Surface((10, 5))
#     bulletpicture.fill(pygame.Color('sienna1'))
#     bullets = []
#     x = 50
#     y = 240
#     previous_time = pygame.time.get_ticks()

#     gameExit = False
#     while not gameExit:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 gameExit = True

#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_SPACE]:
#             current_time = pygame.time.get_ticks()
#             # We're ready to fire when 500 ms have passed.
#             if current_time - previous_time > 500:
#                 previous_time = current_time
#                 bullets.append([x+25, y+24])

#         remaining_bullets = []
#         for bullet in bullets:
#             bullet[0] += 6  # Move the bullet.
#             if bullet[0] < 500:  # Filter out the bullets.
#                 remaining_bullets.append(bullet)
#         bullets = remaining_bullets

#         gameDisplay.fill((30, 30, 30))

#         for bullet in bullets:
#             gameDisplay.blit(bulletpicture, pygame.Rect(bullet[0], bullet[1], 0, 0))

#         pygame.display.update()
#         #clock.tick(120)

# game_loop()
# pygame.quit()
import copy

x = 20

x2 = copy.copy(x)
x = 300000

print(x, x2)