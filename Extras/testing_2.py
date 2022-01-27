# lightblue=(0,174,255)
# import pygame

# pygame.init()
# screen = pygame.display.set_mode((400, 300))
# done = False
# screen.fill(lightblue)
# images=pygame.image.load('mob_1.png')
# noi=16
# current_image=0
# while not done:
#         for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                         done = True
#                         pygame.quit()
#                         quit()
#         if(current_image>noi-1):
#             current_image=0
#         else:
#             current_image+=1
#         screen.blit(images,(50,100),(current_image*32,0,32,32))
#         pygame.display.flip()

x = 0
for i in range(0, 100):
    print(x)
    x += 1
    if x == 10:
        #pass
        break


