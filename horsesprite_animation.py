
# File: pygame_example.py
# Starter code for pygame lessons.

import math, sys, random
import pygame
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

# exit the program
def events():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

# define display surface			
W, H = 1920, 1080
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("code.Pylet - Sprite Sheets")
FPS = 15

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
		
		self.cells = list([(index % cols * w, index / cols * h, w, h) for index in range(self.totalCellCount)])
		self.handle = list([
			(0, 0), (-hw, 0), (-w, 0),
			(0, -hh), (-hw, -hh), (-w, -hh),
			(0, -h), (-hw, -h), (-w, -h),])
		
	def draw(self, surface, cellIndex, x, y, handle = 0):
		surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])

s = spritesheet("Horse Gallop Brown.png", 6, 4)

CENTER_HANDLE = 4

index = 0

# main loop
while True:
	events()

	s.draw(DS, index % s.totalCellCount, HW, HH, CENTER_HANDLE)
	index += 1
	
	#pygame.draw.circle(DS, WHITE, (HW, HH), 2, 0)
	
	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)
