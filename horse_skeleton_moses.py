# File: pygame_example.py
# Starter code for pygame lessons.

import pygame, sys, random, math
from pygame.locals import *

# Constant color definitions
# R    G    B
ORANGE = (255, 128, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
BRIGHTGREEN = (0,255,0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
BRIGHTRED = (0,255,0)
YELLOW = (255, 255, 0)
NAVYBLUE = (0, 0, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def init_main_window(dimensions, caption):
    pygame.init()
    pygame.display.set_caption(caption)
    return pygame.display.set_mode(dimensions)


# Animate horse
def load_horse_sprite():
    #displaying sprite is within the code
    pass


# horse moves, control speed
def horse_player_move(current_coordinate):
    """
    Process player key input and return new coordinates based on current_coordinate
    and the move made.
    """
    pass
    return (0,0)

# function for collision with obstacle
def unsuccessful_jump(horse,obstacle):
    """
    if horse.colliderect(obstacle):
    #life count decreases by 1
    #horse changes color red to indicate damage
    """
    pass
    return life_count

# function for collision with stars
def successful_star(horse,star):
    """
    if horse.colliderect(star):
    #score count increases by 1
    else:
        continue
    :param horse:
    :param star:
    """
    pass
    return score_count

# function for life point (hearts)
def successful_heart(horse, heart):
    """
    if horse.collidrect(heart)
    life point increases by 1 with maximum of 5 hearts only
    :param horse:
    :param heart:
    """
    pass
    return life_point

# function for distance tracking
def distance_track(heart,time):
    """
    while heart > 0:
    time keeps running and translates to distance in meters
    :param heart:
    :param time:
    """
    pass 
    return distance_run

# Write text on screen, any text in any font, anywhere, on any window
def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#https://pythonprogramming.net/displaying-text-pygame-screen/?completed=/adding-boundaries-pygame-video-game/
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

#button for main menu
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

# Quit gracefully
def terminate():
    pygame.quit()
    sys.exit()

# Main Menu
# https://pythonprogramming.net/pygame-buttons-part-1-button-rectangle/?completed=/pygame-start-menu-tutorial/
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        DISPLAYSURF.fill(WHITE)
        largeText = pygame.font.SysFont("comicsansms", 115)
        TextSurf, TextRect = text_objects("Horse Course", largeText)
        TextRect.center = ((800 / 2), (600 / 2))
        DISPLAYSURF.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, GREEN, BRIGHTGREEN, play_game)
        button("Quit", 550, 450, 100, 50, RED, BRIGHTRED, terminate)

        pygame.display.update()
        fps_clock.tick(15)


# Play game
def play_game():
    # window size
    DISPLAYSURF = init_main_window((800, 600), 'Horse Course!')

    # optional key holding
    pygame.key.set_repeat(50, 50)

    FPS = 15
    fps_clock = pygame.time.Clock()

    # Load horse

    # Load jumps
    pygame.draw.rect(surface, color, rect, width=0)

    # Keep score
    score = 0
    num_hits = 0
    font = pygame.font.SysFont(None, 20)

    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                else:

        # draw a clean background before drawing images
        DISPLAYSURF.fill(GREEN)
        # Display horse

        # check if horse jumped the obstacle

        # check if horse collided with obstacle

        # if collides with three jumps, terminate()
        if num_hits == 3:
            terminate()

        # update score
        draw_text("Score: " + str(score), font, DISPLAYSURF, 10, 0)

        # Display Obstacle to be jumped

        # update display
        pygame.display.update()

        # slow down loop, clock for next loop
        fps_clock.tick(FPS)

        # make Obstacle (jumps) move


if __name__ == '__main__':
    play_game()
