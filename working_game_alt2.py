
from pygame import *
import random, pygame, sys, random

X, Y = 600, 400

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

init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Horse Course!')

FPS = 15 #frames per second
ground = Y - 70

gravity = 1


#https://pastebin.com/NwhQtsVJ

class PlayerClass:
    def __init__(self, scale, imageChangeSpeed, terminalVelocity):
        self.run1 = transform.scale(image.load('Horse_Ice/ice-horse-run-00.png'), (15 * scale, 14 * scale))
        self.run2 = transform.scale(image.load('Horse_Ice/ice-horse-run-01.png'), (15 * scale, 14 * scale))
        self.run3 = transform.scale(image.load('Horse_Ice/ice-horse-run-02.png'), (15 * scale, 14 * scale))
        self.run4 = transform.scale(image.load('Horse_Ice/ice-horse-run-03.png'), (15 * scale, 14 * scale))
        self.run5 = transform.scale(image.load('Horse_Ice/ice-horse-run-04.png'), (15 * scale, 14 * scale))

        self.scale = scale
        self.imageChangeSpeed = imageChangeSpeed
        self.terminalVelocity = terminalVelocity

        self.height = 14 * scale
        self.width = 7 * scale

    dead = False

    def update(self):
        self.physics()

        if self.touchingobstacle():
            self.dead = True

        if not self.dead:
            self.playerInput()

        self.y += self.velocityY

        self.show()

    def touchingobstacle(self):
        for obstacle in obstacleManager.obstacleList:
            if self.x + self.width > obstacle.x:
                if self.x < obstacle.x + obstacle.width:
                    if self.y + self.height > obstacle.y:
                        return True




    x = 100
    y = 100

    velocityY = 0

    def playerInput(self):
        pressedKeys = key.get_pressed()

        if pressedKeys[K_SPACE]:
            if self.y + self.height == ground:
                self.velocityY -= 10
            else:
                self.velocityY -= gravity / 2

    def physics(self):
        if self.dead:
            if self.y < Y:
                self.velocityY += 1


        elif self.y + self.height < ground:
            if self.velocityY < self.terminalVelocity:
                self.velocityY += gravity


        elif self.velocityY > 0:
            self.velocityY = 0
            self.y = ground - self.height

    runTick = 0

    def show(self):
        if self.runTick <= self.imageChangeSpeed:
            img = self.run1
        elif self.runTick <= self.imageChangeSpeed * 2:
            img = self.run2
        elif self.runTick <= self.imageChangeSpeed * 3:
            img = self.run3
        elif self.runTick <= self.imageChangeSpeed * 4:
            img = self.run4
        else:
            img = self.run5


        self.runTick += 1

        if self.runTick >= self.imageChangeSpeed * 5:
            self.runTick = 0

        window.blit(img, (self.x, self.y))



player = PlayerClass(5, 6, 10)


class obstacleManager:
    def __init__(self, scale, spawnRange):
        self.img = transform.scale(image.load('Game_Jumps/fence1.png'), (15 * scale, 15 * scale))

        self.spawnRange = spawnRange
        self.obstacleList = []
        self.scale = scale


    def update(self, doSpawn, moveSpeed):
        if doSpawn:
            self.spawn()
        self.manage(moveSpeed)

    def manage(self, moveSpeed):
        obstacles2 = []

        for obstacle in self.obstacleList:
            obstacle.update(moveSpeed)

            if obstacle.onScreen():
                obstacles2.append(obstacle)
        self.obstacleList = obstacles2
    spawnTick = 0

    def spawn(self):
        if self.spawnTick >= self.spawnRange[1]:
            newobstacle = ObstacleClass(X, self.img, 7 * self.scale, 15 * self.scale)
            self.obstacleList.append(newobstacle)
            self.spawnTick = 0

        elif self.spawnTick > self.spawnRange[0]:
            if random.randint(0, self.spawnRange[1] - self.spawnRange[0]) == 0:
                newobstacle = ObstacleClass(X, self.img, 7 * self.scale, 15 * self.scale)
                self.obstacleList.append(newobstacle)
                self.spawnTick = 0

        self.spawnTick += 1

obstacleManager = obstacleManager(3, (45, 90))

class ObstacleClass:
    def __init__(self, x, img, width, height):
        self.x = x
        self.img = imghttps://pastebin.com/NwhQtsVJ
        self.width = width
        self.height = height
        self.y = ground - height

    def update(self, moveSpeed):
        self.move(moveSpeed)
        self.show()

    def move(self, moveSpeed):
        self.x -= moveSpeed

    def show(self):
        window.blit(self.img, (self.x, self.y))

    def onScreen(self):
        if self.x + self.width > 0:
            return True
        else:
            return False


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
    window.blit(TextSurf, TextRect)

# Displaying Text to PyGame Screen [Internet]. Python Programming; [cited 2018 Nov 13].
    # Available from: https://pythonprogramming.net/displaying-text-pygame-screen/?
    # completed=/adding-boundaries-pygame-video-game/
#button for main menu

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(window, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    window.blit(textSurf, textRect)



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
    DISPLAYSURF = init_main_window((X, Y),"Horse Course!")
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
    horse.centerx = X/2
    horse.centery = 175

    while intro: # intro loopield
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
        draw_text("Horse Course", largeText, DISPLAYSURF, (X/2),300)
        draw_text("GO", smallText, DISPLAYSURF, (100+100/2),(10+50/2))
        draw_text("QUIT", smallText, DISPLAYSURF, (400+100/2),(10+50/2))

        # if GO clicked, initiate game
        # if Quit clicked, terminate game

        button("GO!", 100, 10, 100, 60, GREEN, BRIGHTGREEN, game)
        button("Quit", 400, 10, 100, 60, RED, BRIGHTRED, terminate)

        pygame.display.update()
        clock.tick(FPS)




def play_game():
    for events in event.get():
        if events.type == KEYDOWN:
            if events.key == K_ESCAPE:
                quit()

groundImg = transform.scale(image.load('greengrass.jpg'), (X, int(Y - ground)))

font1 = pygame.font.Font('freesansbold.ttf', 50)
font2 = pygame.font.Font('freesansbold.ttf', 40)
deathMessage1 = font1.render('You Fell Over!', True, (255, 255, 255))
deathMessage1Shadow = font1.render('You Fell Over!', True, (0, 0, 0))
deathMessage2 = font2.render('Press Space', True, (255, 255, 255))
deathMessage2Shadow = font2.render('Press Space', True, (0, 0, 0))

message1Rect = deathMessage1.get_rect()
message1x = X / 2 - message1Rect.width / 2

message2Rect = deathMessage2.get_rect()
message2x = X / 2 - message2Rect.width / 2

def showMessage(y):
    window.blit(deathMessage1, (message1x, y))
    window.blit(deathMessage1Shadow, (message1x + 5, y + 5))

    window.blit(deathMessage2, (message2x, y + message1Rect.height))
    window.blit(deathMessage2Shadow, (message2x, message1Rect.height + 5 + y))


score = {'gameScore': 0}

def game():
    player.update()
    while True:
        if player.dead:
            fall(scoreStr)

        play_game()
        window.fill((200, 240, 250))

        player.update()


        obstacleManager.update(True, score['gameScore'] / 50 + 3)
        window.blit(groundImg, (0, ground))

        clock.tick(60)

        scoreStr = font2.render(str(round(score['gameScore'])), True, (0, 0, 0))
        window.blit(scoreStr, (50, 50))

        display.update()

        score['gameScore'] += 0.1



def fall(scoreStr):
    space = 0
    while True:
        pressedKeys = key.get_pressed()

        oldSpace = space
        space = pressedKeys[K_SPACE]

        play_game()
        window.fill((200, 240, 250))

        player.update()


        obstacleManager.update(False, score['gameScore'] / 50 + 3)
        window.blit(groundImg, (0, ground))

        clock.tick(60)

        showMessage(50)

        window.blit(scoreStr, (50, 50))
        display.update()

        spaceEvent = space - oldSpace

        if spaceEvent == 1:
            #Reset Everything

            obstacleManager.obstacleList = []
            player.velocityY = 0
            player.dead = False
            player.y = ground - player.height
            score['gameScore'] = 0

            break



if __name__ == '__main__':
    game_intro()
