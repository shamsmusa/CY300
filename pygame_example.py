
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

def load_cat_images():
	file_names = ['images/nyan-1.gif',
				'images/nyan-2.gif',
				'images/nyan-3.gif',
				'images/nyan-4.gif',
				'images/nyan-4.gif',
				'images/nyan-5.gif',
				'images/nyan-6.gif']
	cat_images=[]
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
		cat.centerx = max(cat.centerx-dist,0)
	elif event.key == K_UP:
		cat.centery = max(cat.centery-dist,0)
		
def eats_cupcake(cat,cup):
	if cat.colliderect(cup):
		# cat eats cupcake
		# respawn in new location
		cup.centerx =  random.randrange(pygame.display.get_surface().get_width())
		cup.centery = random.randrange(pygame.display.get_surface().get_height())
		return True
	else:
		return False

def eats_broccoli(broccoli,broc):
	if broccoli.colliderect(broc):
		broc.centerx =  random.randrange(pygame.display.get_surface().get_width())
		broc.centery = random.randrange(pygame.display.get_surface().get_height())
		return True
	else:
		return False

# Write text on the screen
def draw_text(text,font,subject,x,y):
	textobj = font.render(text,1,WHITE)
	textrect = textobj.get_rect()
	textrect.topleft = (x,y)
	subject.blit(textobj, textrect)

# Quit gracefully
def terminate():
	pygame.quit()
	sys.exit()
	
def play_game():	
	DISPLAYSURF = init_main_window((400,300), 'Nyan Cat!') #the window in which the game exists

	#optional key holding
	pygame.key.set_repeat(50,50)

	FPS = 15
	fps_clock = pygame.time.Clock()

#	cat_img = pygame.image.load('smallNyan.gif')
#	cat = cat_img.get_rect() #gives the rectangle that is the size of the image. how you can determine colllision
	cat_images = load_cat_images()
	cat = cat_images[0].get_rect()

	cupcake = pygame.image.load('images/cupcake.gif')
	cup = cupcake.get_rect()
	cup.move_ip(100,10)
	
	broccoli = pygame.image.load('images/broccoli.gif')
	broc = broccoli.get_rect()
	broc.move_ip(150,10)

	score = 0
	font = pygame.font.SysFont(None,20)

	while True: #main game loop
		for event in pygame.event.get(): #event are "happenings" within the game.
			if event.type == QUIT:
			  terminate()
			elif event.type == KEYDOWN:
			  if event.type == K_ESCAPE:
			    terminate()
			  else:
			    move_cat(cat,event,10,DISPLAYSURF)
			elif event.type == MOUSEMOTION:
			  cat.center == event.pos
		# draw a clean background before drawing images
		DISPLAYSURF.fill(BLUE)
		# display cat
#		DISPLAYSURF.blit(cat_img,cat) #block image transfer
		DISPLAYSURF.blit(cat_images[0], cat) #l.append(l.pop(0)) took the front index and put it in the end AKA circular loop
		# display cupcake
		DISPLAYSURF.blit(cupcake, cup)
		DISPLAYSURF.blit(broccoli,broc)
		#check if cupcake eaten
		if eats_cupcake(cat, cup):
			score += 1
			print(score)
		if eats_broccoli(cat,broc):
			score -= 1
		# update score
		draw_text("Score: "+str(score), font, DISPLAYSURF, 10, 0)
		
		# update display
		pygame.display.update()

		# update cat and clock for next loop
		cup.x = cup.x+10 if cup.x < DISPLAYSURF.get_width() else cupcake.get_width()
		cat_images.append(cat_images.pop(0))
		fps_clock.tick(FPS) #tick does the math to do the FPS


if __name__=='__main__':
    play_game()
