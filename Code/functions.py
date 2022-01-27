import math, pygame

from variables import score, window
pygame.font.init()

score_font = pygame.font.Font("freesansbold.ttf", 24)
gameover_font = pygame.font.Font("freesansbold.ttf", 64)

def collision_function_bullet(mob_x, mob_y, bullet_x, bullet_y):
    global score
    distance = math.sqrt((math.pow(mob_x - bullet_x, 2)) + (math.pow(mob_y - bullet_y, 2)))

    #if distance <= 27, which we use to detect collision, increase score by 1
    if distance <= 27:
        score += 1
    return distance

def collision_function_ship(mob_x, mob_y, ship_x, ship_y):
    distance = math.sqrt((math.pow(mob_x - ship_x, 2)) + (math.pow(mob_y - ship_y, 2)))
    return distance

def score_tracker(reset_score = None):
    global score
    if reset_score:
        score = 0
    display_score = score_font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(display_score, (10, 10))

def game_over():
    game_over_text = gameover_font.render("GAME OVER", True, (255, 255, 255))
    game_over_text_2 = gameover_font.render("R = Retry", True, (255, 255, 255))
    game_over_text_3 = gameover_font.render("Q = Exit", True, (255, 255, 255))
    window.blit(game_over_text, (205, 180))
    window.blit(game_over_text_2, (205, 250))
    window.blit(game_over_text_3, (205, 320))