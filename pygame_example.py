
# File: pygame_example.py
# Starter code for pygame lessons.

import pygame, sys, random
from pygame.locals import *


# Constant color definitions
           #R    G    B
ORANGE =   (255, 128, 0)
BLUE =     (0,   0,   255)
GREEN =    (0,   128, 0)
PURPLE =   (128, 0,   128)
RED =      (255, 0,   0)
YELLOW =   (255, 255, 0)
NAVYBLUE = (0,   0,   128)
WHITE =    (255, 255, 255)
BLACK =    (0,   0,   0)  

def init_main_window(dimensions, caption):
    pygame.init()
    pygame.display.set_caption(caption)
    return pygame.display.set_mode(dimensions)
    
def load_cat_images(): #animate cat
    file_names = ['images/nyan-1.gif',
                  'images/nyan-2.gif',
                  'images/nyan-3.gif',
                  'images/nyan-4.gif',
                  'images/nyan-5.gif',
                  'images/nyan-6.gif']
    cat_images = []
    for file_name in file_names:
        cat_img = pygame.image.load(file_name)
        cat_images.append(cat_img)
    return cat_images
      
# Keyboard cat moves
def move_cat(cat, event, dist, disp_surf):
    if event.key == K_RIGHT:
        cat.centerx = min(cat.centerx+dist, disp_surf.get_width())
    elif event.key == K_DOWN:
        cat.centery = min(cat.centery+dist, disp_surf.get_height())
    elif event.key == K_LEFT:
        cat.centerx = max(cat.centerx-dist, 0)
    elif event.key == K_UP:
        cat.centery = max(cat.centery-dist,0)
        
def eats_cupcake(cat, cup, broc):
    if cat.colliderect(cup):
        # cat eats cupcake
        # respawn in new location
        cup.centerx = random.randrange(pygame.display.get_surface().get_width())
        cup.centery = random.randrange(pygame.display.get_surface().get_height())
        broc.centerx = random.randrange(pygame.display.get_surface().get_width())
        broc.centery = random.randrange(pygame.display.get_surface().get_height())
        return True
    else:
        return False

def eats_broccoli(cat, broc, cup):
    if cat.colliderect(broc):
        # cat eats broccoli
        # respawn in new location
        broc.centerx = random.randrange(pygame.display.get_surface().get_width())
        broc.centery = random.randrange(pygame.display.get_surface().get_height())
        cup.centerx = random.randrange(pygame.display.get_surface().get_width())
        cup.centery = random.randrange(pygame.display.get_surface().get_height())
        return True
    else:
        return False

def cup_broc_collide(cup, broc):
    if cup.colliderect(broc):
        # respawn broccoli if it collides with a cupcake
        broc.centerx = random.randrange(pygame.display.get_surface().get_width())
        broc.centery = random.randrange(pygame.display.get_surface().get_height())
 
# Write text on screen, any text in any font, anywhere, on any window
def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, WHITE)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)

# Quit gracefully
def terminate():
    pygame.quit()
    sys.exit()
                           
def play_game():
    DISPLAYSURF = init_main_window((400,300), 'Nyan Cat!')
    
    # optional key holding
    pygame.key.set_repeat(50,50)
    
    FPS = 15
    fps_clock = pygame.time.Clock()
    
    # still cat image:
    # cat_img = pygame.image.load('smallNyan.gif')
    # cat = cat_img.get_rect()
    cat_images = load_cat_images()
    cat = cat_images[0].get_rect()
    # loading a cupcake
    cupcake = pygame.image.load('images/cupcake.gif')
    cup = cupcake.get_rect()
    cup.centerx = random.randrange(pygame.display.get_surface().get_width())
    cup.centery = random.randrange(pygame.display.get_surface().get_height())
    # loading a broccoli
    broccoli = pygame.image.load('images/broccoli.gif')
    broc = broccoli.get_rect()
    broc.centerx = random.randrange(pygame.display.get_surface().get_width())
    broc.centery = random.randrange(pygame.display.get_surface().get_height())
    
    score = 0
    num_broccoli = 0
    font = pygame.font.SysFont(None, 20)
    
    while True: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                else:
                    move_cat(cat, event, 10, DISPLAYSURF)
            elif event.type == MOUSEMOTION:
                cat.center = event.pos
        # draw a clean background before drawing images
        DISPLAYSURF.fill(BLUE)
        # display cat
        # DISPLAYSURF.blit(cat_img, cat)
        DISPLAYSURF.blit(cat_images[0], cat)
        # check if cupcake eaten
        if eats_cupcake(cat, cup, broc):
            score += 1
        # check if broccoli eaten
        if eats_broccoli(cat, broc, cup):
            score -= 1
            num_broccoli += 1
        # if three broccoli eaten, terminate()
        if num_broccoli == 3:
            terminate()
        # actions taken if broccoli and cupcakes colide
        cup_broc_collide(cup, broc)
        # update score
        draw_text("Score: "+str(score), font, DISPLAYSURF,10,0)
        # display cupcake
        DISPLAYSURF.blit(cupcake, cup)
        # display broccoli
        DISPLAYSURF.blit(broccoli, broc)
        # update display
        pygame.display.update()
        # circular queue
        cat_images.append(cat_images.pop(0))
        # slow down loop, clock for next loop
        fps_clock.tick(FPS)
        # make cupcake move
        # cup.x = cup.x+5 if cup.x < DISPLAYSURF.get_width() else -cupcake.get_width()

if __name__=='__main__':
    play_game()
