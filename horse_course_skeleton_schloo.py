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
RED = (255, 0, 0)
BRIGHTRED = (0,255,0)
YELLOW = (255, 255, 0)
NAVYBLUE = (0, 0, 128)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 15 #frames per second
W, H = 600, 400 #window width (pixels), window height (pixels)
HW, HH = W / 2, H / 2
AREA = W * H
CLOCK = pygame.time.Clock()

AFPS = 0 #animated horse FPS
horse_animation = 0 #images from spritesheet 

dispersment_obs = 0 #dispersment of obstacles
obs_speed = 0 #speed of obstacles

score = 0 #score based on stars collected
num_hits = 0 #number of obstacles hit
life_point = 0 #number of hearts collected/lives player still has

class spritesheet:
	def __init__(self, filename, cols, rows):
		self.sheet = pygame.image.load(filename).convert_alpha()
		
		self.cols = cols
		self.rows = rows
		self.totalCellCount = cols * rows
		
		self.rect = self.sheet.get_rect()
		w = self.cellWidth = self.rect.width / cols
		h = self.cellHeight = self.rect.height / rows
		hw, hh = self.cellCenter = (w / 2, h / 2)
		
		self.cells = list([(index % cols * w, index % rows * h, w, h) for index in range(self.totalCellCount)])
		self.handle = list([
			(0, 0), (-hw, 0), (-w, 0),
			(0, -hh), (-hw, -hh), (-w, -hh),
			(0, -h), (-hw, -h), (-w, -h),])
		
	def draw(self, surface, cellIndex, x, y, handle = 0):
		surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])

s = spritesheet("brown_horse.png", 6, 1)

CENTER_HANDLE = 4

index = 0

# initiate main window
def init_main_window(dimensions, caption):
    pygame.init()
    pygame.display.set_caption(caption)
    return pygame.display.set_mode(dimensions)


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
    textobj = font.render(text, 1, BLACK)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Displaying Text to PyGame Screen [Internet]. Python Programming; [cited 2018 Nov 13]. 
    # Available from: https://pythonprogramming.net/displaying-text-pygame-screen/?
    # completed=/adding-boundaries-pygame-video-game/
#button for main menu
"""
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            #action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
"""



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
    DISPLAYSURF = init_main_window((W,H),"Horse Course!")
    # loading intro backdrop
    # Landscape of Grass Field and Green Environment Public Park Use as Natural Background, 
        # Backdrop [Internet]. 2017. iStock; [cited 2018 Nov 13]. Available from: 
        # https://www.istockphoto.com/photo/landscape-of-grass-field-and-green-environment-
        # public-park-use-as-natural-background-gm827580726-134543307
    intro_background = pygame.image.load('field.jpg')
    intro_pic = intro_background.get_rect()
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
        
        # draw a clean background
        DISPLAYSURF.fill(GREEN)
        # display background
        DISPLAYSURF.blit(intro_background,intro_pic)
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
        draw_text("Horse Course", largeText, DISPLAYSURF, (WW/2),300)
        draw_text("GO", smallText, DISPLAYSURF, (100+100/2),(10+50/2))
        draw_text("QUIT", smallText, DISPLAYSURF, (400+100/2),(10+50/2))

        # if GO clicked, initiate game
        # if Quit clicked, terminate game

        #button("GO!", 150, 450, 100, 50, GREEN, BRIGHTGREEN, play_game)
        #button("Quit", 550, 450, 100, 50, RED, BRIGHTRED, terminate)

        pygame.display.update()
        fps_clock.tick(FPS)


# Main program
def play_game():
    pass
    # window size
    DISPLAYSURF = init_main_window((W, H), 'Horse Course!')

    # optional key holding
    pygame.key.set_repeat(50, 50)

    FPS = 15
    fps_clock = pygame.time.Clock()

    # Load horse
    # horse_img = load_horse_sprite()
    # horse = horse_img[0].get_rect()
    s.draw(DISPLAYSURF, index % s.totalCellCount, HW, HH, CENTER_HANDLE)
	index += 1
	
	#pygame.draw.circle(DS, WHITE, (HW, HH), 2, 0)
	
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)

    # Load jumps
    # obstacle = pygame.draw.rect(surface, color, rect, width=0)
    # obs = obstacle.get_rect()

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
                    pass

        # draw a clean background before drawing images
        DISPLAYSURF.fill(GREEN)
        # Display horse
        # DISPLAYSURF.blit(horse_img,horse)

        # make Obstacle (jumps) move left
        # obs.x = obs.x-5 if obs.x < DISPLAYSURF.get_width() else -obstacle.get_width()
        # determine dispersment of obstacles and speed of obstacles


        # if collides with three jumps, terminate()
        if num_hits == 3:
            terminate()

        # update score
        draw_text("Score: " + str(score), font, DISPLAYSURF, 10, 0)

        # Display Obstacle to be jumped
        # DISPLAYSURF.blit(obstacle, obs)

        # update display
        pygame.display.update()

        # slow down loop, clock for next loop
        fps_clock.tick(FPS)


if __name__ == '__main__':
    game_intro()
    # initiate play_game() if GO button selected
