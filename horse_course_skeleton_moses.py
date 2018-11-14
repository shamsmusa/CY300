# File: pygame_example.py
# Starter code for pygame lessons.

import pygame, sys, random, math
from pygame.locals import *

# Constant color definitions
# R    G    B
ORANGE = (255, 128, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
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


# horse moves, control speed
def horse_player_move(current_coordinate):
    """
    Process player key input and return new coordinates based on current_coordinate
    and the move made.
    """
    return (0,0)

# function for collision with obstacle
def unsuccessful_jump(horse,obstacle):
    """
    if horse.colliderect(obstacle):
    #life count decreases by 1
    #horse changes color red to indicate damage
    """

# function for collision with stars
def successful_star(horse,star):
    """
    if horse.colliderect(star):
    #score count increases by 1
    else:
        continue
    :param horse:
    :param star:
    :return:
    """

# function for life point (hearts)
def successful_heart(horse, heart):
    """
    if horse.collidrect(heart)
    life point increases by 1 with maximum of 5 hearts only
    :param horse:
    :param heart:
    :return:
    """

# function for distance tracking
def distance_track(heart,time):
    """
    while heart > 0:
    time keeps running and translates to distance in meters
    :param heart:
    :param time:
    :return:
    """
# Write text on screen, any text in any font, anywhere, on any window
def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Quit gracefully
def terminate():
    pygame.quit()
    sys.exit()


# Play game
def play_game():
    # window size
    DISPLAYSURF = init_main_window((400, 300), 'Horse Course!')

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
