"""
This is a skeleton for the Horse Course game. The smaller functions
involved in the overall game are represented as stub functions below. The 
stub functions provide an idea for how the program will implement the actual
functions. The idea of the game is to have an animated horse jump obstacles
that will be panning from right to left. The dispersment and speed of the 
fences will be determined, so the game will not be unbeatable. While jumping,
the player will have the opportunity to collect stars, which will increase the
player's score. The distance will be calculated based on time. The player will
only be allowed to collide with three obstacles before the player runs out of
lives. The player can collect hearts, a life, which will appear occasionally 
in the game. The player will only be able to have a maximum of five life points, 
lives, at any one time. There will be different locations a player can ride in.
The object of the game is to collect the most points and go as far as possible. 

"""

# File: horse_course_skeleton_schloo.py
# Name: CDT Rachael Schloo and CDT Moses Sun

import pygame, sys, random, math
from pygame.locals import *

# Constant color definitions
# R    G    B
ORANGE = (255, 128, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
BRIGHTGREEN = (0,255,0)
PURPLE = (128, 0, 128)
RED = (180, 0, 0)
BRIGHTRED = (255,0,0)
YELLOW = (255, 255, 0)
NAVYBLUE = (0, 0, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 15 #frames per second
W, H = 600, 400 #window width (pixels), window height (pixels)
HW, HH = W / 2, H / 2
gameDisplay = pygame.display.set_mode((W,H))
AREA = W * H
fps_clock = pygame.time.Clock()

AFPS = 0 #animated horse FPS
horse_animation = 0 #images from spritesheet 

dispersment_obs = 0 #dispersment of obstacles
obs_speed = 0 #speed of obstacles

score = 0 #score based on stars collected
num_hits = 0 #number of obstacles hit
life_point = 0 #number of hearts collected/lives player still has

def load_horse_run(): #animate horse
    file_names = ['Horse_Ice/ice-horse-run-00.png',
                  'Horse_Ice/ice-horse-run-01.png',
                  'Horse_Ice/ice-horse-run-02.png',
                  'Horse_Ice/ice-horse-run-03.png',
                  'Horse_Ice/ice-horse-run-04.png',
                  'Horse_Ice/ice-horse-run-05.png',
                  'Horse_Ice/ice-horse-run-06.png']
    horse_images = []
    for file_name in file_names:
        horse_img = pygame.image.load(file_name)
        horse_images.append(horse_img)
    return horse_images

def load_horse_jump(): #animate horse
    file_names = ['Horse_Ice/ice-horse-jump-00.png',
                  'Horse_Ice/ice-horse-jump-01.png',
                  'Horse_Ice/ice-horse-jump-02.png',
                  'Horse_Ice/ice-horse-jump-03.png',
                  'Horse_Ice/ice-horse-jump-04.png',
                  'Horse_Ice/ice-horse-jump-05.png',
                  'Horse_Ice/ice-horse-jump-06.png']
    horse_images = []
    for file_name in file_names:
        horse_img = pygame.image.load(file_name)
        horse_images.append(horse_img)
    return horse_images

# initiate main window
def init_main_window(dimensions, caption):
    pygame.init()
    pygame.display.set_caption(caption)
    return pygame.display.set_mode(dimensions)

# Write text on screen, any text in any font, anywhere, on any window
def draw_text(text, font, surface, x, y):
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

#https://pythonprogramming.net/pygame-start-menu-tutorial/
def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

# Displaying Text to PyGame Screen [Internet]. Python Programming; [cited 2018 Nov 13].
    # Available from: https://pythonprogramming.net/displaying-text-pygame-screen/?
    # completed=/adding-boundaries-pygame-video-game/
#button for main menu

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
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
# PyGame Buttons, Part 1, Drawing the Rectangle [Internet]. Python Programming; [cited 2018 
    # Nov 13]. Available from: https://pythonprogramming.net/pygame-buttons-part-1-button-
    # rectangle/

def game_intro():
    intro = True
    DISPLAYSURF = init_main_window((W, H),"Horse Course!")
    # loading intro backdrop
    # Landscape of Grass Field and Green Environment Public Park Use as Natural Background, 
        # Backdrop [Internet]. 2017. iStock; [cited 2018 Nov 13]. Available from: 
        # https://www.istockphoto.com/photo/landscape-of-grass-field-and-green-environment-
        # public-park-use-as-natural-background-gm827580726-134543307
    background_pic = pygame.image.load('field.jpg')
    background = background_pic.get_rect()
    # loading horse
    # Clipart Brown Horse PNG Image Picture [Internet]. 2017. Stickeroid; [cited 2018 Nov 14]. 
        # Available from: https://stickeroid.com/?q=clipart%20brown%20horse%20png%20image%20
        # picture,%20transparent%20background%2048
    horse_img = pygame.image.load('horse_pic.png')
    horse = horse_img.get_rect()
    horse.centerx = W/2
    horse.centery = 175

    while intro: # intro loop
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
                sys.exit()
        
        # display background
        DISPLAYSURF.blit(background_pic,background)
        # display horse
        DISPLAYSURF.blit(horse_img,horse)
        # display Go button
        pygame.draw.rect(DISPLAYSURF,GREEN,[100, 10, 100, 60])
        # display Quit button
        pygame.draw.rect(DISPLAYSURF,RED,[400, 10, 100, 60])
        # display text
        largeText = pygame.font.SysFont("comicsansms", 90)
        smallText = pygame.font.SysFont("comicsansms", 20)
        # text
        draw_text("Horse Course", largeText, DISPLAYSURF, (W/2),300)
        draw_text("GO", smallText, DISPLAYSURF, (100+100/2),(10+50/2))
        draw_text("QUIT", smallText, DISPLAYSURF, (400+100/2),(10+50/2))

        # if GO clicked, initiate game
        # if Quit clicked, terminate game

        button("GO!", 100, 10, 100, 60, GREEN, BRIGHTGREEN, play_game)
        button("Quit", 400, 10, 100, 60, RED, BRIGHTRED, terminate)

        pygame.display.update()
        fps_clock.tick(FPS)

# Animate horse
def load_horse_sprite():
    #animate horse by using sprite sheet
    pass
    return horse_animation


# horse moves, control speed
def horse_player_move(current_coordinate,horse,event,dist,disp_surf):
    """
    Process player key input and return new coordinates based on current_coordinate
    and the move made.
    if event.key == K_RIGHT:
        horse.centerx = min(horse.centerx+dist, disp_surf.get_width())
    elif event.key == K_SPACE: #space initiates jump
        # will need formula for parabola
    """
    pass
    return (0,0)
    
def move_horse(horse, event, dist, disp_surf):
    if event.key == K_RIGHT:
        horse.centerx = min(horse.centerx+dist, disp_surf.get_width())
    elif event.key == K_DOWN:
        horse.centery = min(horse.centery+dist, disp_surf.get_height())
    elif event.key == K_LEFT:
        horse.centerx = max(horse.centerx-dist, 0)
    elif event.key == K_UP:
        horse.centery = max(horse.centery-dist,0)

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
    
# Main program
def play_game():
    pass
    # window size
    DISPLAYSURF = init_main_window((W, H), 'Horse Course!')
    # background image
    # Landscape of Grass Field and Green Environment Public Park Use as Natural Background, 
        # Backdrop [Internet]. 2017. iStock; [cited 2018 Nov 13]. Available from: 
        # https://www.istockphoto.com/photo/landscape-of-grass-field-and-green-environment-
        # public-park-use-as-natural-background-gm827580726-134543307
    background_pic = pygame.image.load('field.jpg')
    background = background_pic.get_rect()
    # optional key holding
    pygame.key.set_repeat(50, 50)
    # loading an obstacle
    obs_images =  ['Game_Jumps/fence1.png',
                  'Game_Jumps/fence2.png',
                  'Game_Jumps/fence3.png',
                  'Game_Jumps/fence4.png',
                  'Game_Jumps/fence5.png',
                  'Game_Jumps/fence6.png',
                  'Game_Jumps/fence7.png',
                  'Game_Jumps/fence8.png',
                  'Game_Jumps/fence9.png',
                  'Game_Jumps/fence10.png',
                  'Game_Jumps/fence11.png',
                  'Game_Jumps/fence12.png']
    obstacle = pygame.image.load(random.choice(obs_images))
    obs = obstacle.get_rect()
    obs.centerx = W-10
    obs.centery = HH+100
    

    FPS = 15
    fps_clock = pygame.time.Clock()

    # Load horse
    running_horse = load_horse_run()
    horse = running_horse[0].get_rect()
    horse.centerx = 100
    horse.centery = HH+100
    jumping_horse = load_horse_jump()
    horsej = jumping_horse[0].get_rect()

    # Load stars
    # stars = pygame.image.load('star.gif')
    # star = stars.get_rect()

    # Load hearts
    # hearts = pygame.image.load('heart.gif')
    # heart = hearts.get_rect()

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
                    move_horse(horse, event, 10, DISPLAYSURF)
                    move_horse(horsej, event, 10, DISPLAYSURF)

        # display background
        DISPLAYSURF.blit(background_pic,background)
        # Display horse
        DISPLAYSURF.blit(running_horse[0], horse)
        DISPLAYSURF.blit(jumping_horse[0], horsej)
        # circular queue for horse animation
        running_horse.append(running_horse.pop(0))
        jumping_horse.append(jumping_horse.pop(0))

        # make Obstacle (jumps) move left
        #obstacle = pygame.draw.rect(DISPLAYSURF, BLUE, [W-10,HH+100,10,30])
        #obstacle = pygame.image.load(random.choice(obs_images))
        #obs = obstacle.get_rect()
        DISPLAYSURF.blit(obstacle, obs)
        if obs.x > 0:
            obs.x = obs.x-random.randrange(5,15)  
        else:
            obstacle = pygame.image.load(random.choice(obs_images))
            obs = obstacle.get_rect()
            obs.centerx = W-10
            obs.centery = HH+100
        # determine dispersment of obstacles and speed of obstacles


        # if collides with three jumps, terminate()
        if num_hits == 3:
            terminate()

        # update score
        draw_text("Score: " + str(score), font, DISPLAYSURF, 550, 20)

        # Display Obstacle to be jumped
        # DISPLAYSURF.blit(obstacle, obs)

        # update display
        pygame.display.update()

        # slow down loop, clock for next loop
        fps_clock.tick(FPS)


if __name__ == '__main__':
    game_intro()
