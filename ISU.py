from math import sqrt
from random import randint
import pygame
import time
pygame.init()
WIDTH = 800
HEIGHT= 600
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))

#Define boundaries, colour, font, and time
TOP = 0
LEFT = 0
RIGHT = 800
BOTTOM = 600
RED =(170,0,0)
WHITE  = (255,255,255)
YELLOW = (255,255,  0)
BLACK  = (  0,  0,  0)
LIGHT_BLUE =(0,205,205)
LIGHT_PINK =(255,192,203)
GREEN =(0,160,0)
outline=0
BULLET_PERIOD = 1
BEGIN = time.time()
MONEY_PERIOD = 2
font = pygame.font.SysFont("Courier New Bold",40)

#Define images
menuScreen = pygame.image.load("menuscreenISU.png")
intro = pygame.image.load("instructionscreen.png")
background = pygame.image.load("ISU BACKGROUND.png")
header = pygame.image.load("header.png")
winScreen = pygame.image.load("win.png")
endScreen = pygame.image.load("endscreenISU.png")
enemy = pygame.image.load("enemy.png")
turret1 = pygame.image.load("peashooterss.png")
turret2 = pygame.image.load("wallnut.png")
bomb = pygame.image.load("cherrybomb.png")
picX = 0
picY = 0

#---------------------------------------#
# functions                             #
#---------------------------------------#
#Create functions
def redrawMenuWindow():
    gameWindow.fill(BLACK)
    gameWindow.blit(menuScreen, (picX,picY))
    pygame.display.update()

def redrawIntroWindow():
    gameWindow.fill(BLACK)
    gameWindow.blit(intro, (picX,picY))
    pygame.display.update()

def redrawEndWindow():
    gameWindow.fill(BLACK)
    gameWindow.blit(endScreen, (picX,picY))
    pygame.display.update()

def redrawWinWindow():
    gameWindow.fill(BLACK)
    gameWindow.blit(winScreen, (picX,picY))
    pygame.display.update()
    
def redrawGameWindow():
    gameWindow.fill(BLACK)
    gameWindow.blit(background, (picX,picY))
    graphics = font.render(str(money),2,RED)
    gameWindow.blit(graphics,(610,25))
    graphics = font.render(str(timer),2,BLACK)
    gameWindow.blit(graphics,(600,70))
    drawTurret1()
    drawTurret2()
    drawBullets()
    drawEnemys()
    drawBomb()
    gameWindow.blit(header, (picX,picY))
    pygame.display.update()

def drawTurret1():
    for i in range(len(turret1X)):
        gameWindow.blit(turret1, (turret1X[i]-25,turret1Y[i]-15))

def drawTurret2():
    for i in range(len(turret2X)):
        gameWindow.blit(turret2, (turret2X[i]-25,turret2Y[i]-20))
        
def drawBomb():
    for i in range(len(bombX)):
        gameWindow.blit(bomb, (bombX[i]-25,bombY[i]-23))

def drawBullets():
    for i in range(len(bulletX)):
        if bulletVisible[i]:
            for j in range(len(bulletX[i])):
                pygame.draw.ellipse(gameWindow,bulletCLR,(bulletX[i][j],bulletY[i][j],bulletW,bulletH),outline)
    

def drawEnemys():
    for i in range(numEnemys):
        if enemyVisible[i]:
            gameWindow.blit(enemy, (enemyX[i],enemyY[i]-70))
#---------------------------------------#
# main program                          #
#---------------------------------------#
#Create time variables
timer = 0
elasped = time.time() - BEGIN
timeRemaining=0
spawnEnemy = elasped
spawnMoney = elasped
timeLeft = time.time() - BEGIN
bulletReferenceTime = BEGIN
moneyReferenceTime = BEGIN
enemyPosition = WIDTH
money = 0

# enemy properties
numEnemys = 50
enemyR = 20
enemyX = []
enemyY = []
enemyVisible = []
enemyStep = []
enemyCLR=[]
enemyHealth=[]

# add enemy
for i in range(numEnemys):
    enemyX.append(enemyPosition+300)  
    enemyY.append(randint(1,5)*90+90)  
    enemyVisible.append(True)
    enemyStep.append(1)
    enemyCLR.append(WHITE)
    enemyHealth.append(5)
    enemyPosition = enemyPosition + 300
    
# turret1 properties
turret1W = 30
turret1H = 50
turret1X = []
turret1Y = []
turret1CLR = WHITE
turret1Health = []
selected = []
clickedY = []
clickedX = []
shooting = []
placed = []

#create menu turret1
for i in range(1):                
    turret1X.append(20) 
    turret1Y.append(20)  
    turret1Health.append(30)
    selected.append(False)
    clickedY.append(True)
    clickedX.append(True)
    shooting.append(False)
    placed.append(False)

# turret2 propertie
turret2W = 30
turret2H = 50
turret2X = []
turret2Y = []
turret2CLR = LIGHT_BLUE
turret2Health = []
selected2 = []
clickedY2 = []
clickedX2 = []

#create menu turret2
for i in range(1):                
    turret2X.append(130)  
    turret2Y.append(20)  
    turret2Health.append(100)
    selected2.append(False)
    clickedY2.append(True)
    clickedX2.append(True)


#Bomb properties
bombR = []
bombX = []
bombY = []
bombCLR = LIGHT_PINK
selectedBomb = []
clickedBomb = []
bombDamage = []

#create menu bomb
for i in range(1):               
    bombX.append(90) 
    bombY.append(40)  
    bombR.append(30)
    selectedBomb.append(False)
    clickedBomb.append(True)
    bombDamage.append(False)
    
# bullet properties
bulletW = 20
bulletH = 20
bulletX = []
bulletY = []
bulletVisible = []
bulletStep = 10
bulletCLR= GREEN

clock = pygame.time.Clock()
FPS = 40

#---------------------------------------#
#Create different windows
inPlay = False
menu = True
introScreen = False
end = False
win = False
#draw menu screen
while menu:
    redrawMenuWindow()
    pygame.time.delay(2)
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        inPlay = True
        menu = False
    if keys[pygame.K_i]:
        introScreen = True
        menu = False
#draw intro screen
while introScreen:
    redrawIntroWindow()
    pygame.time.delay(2)
    pygame.event.clear()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        inPlay = True
        introScreen = False
#draw game screen
while inPlay:
    redrawGameWindow()
    clock.tick(FPS)
    timeLeft = time.time() - BEGIN
    timeLeft = round(timeLeft,2)
    timer = 100 - timeLeft
    if timer <= 0:
        win = True
        inPlay = False
    for i in range(len(turret1X)):
        for event in pygame.event.get():    
    
#check if player picked turret1        
            if event.type == pygame.MOUSEBUTTONDOWN and money>=20 and mouseY>=turret1Y[0] and mouseY<=turret1Y[0]+turret1H and mouseX>=turret1X[0] and mouseX<=turret1X[0]+turret1W:
                print ("YAY")
                selected[i] = True
                turret1X.append(mouseX)  
                turret1Y.append(mouseY)
                turret1Health.append(30)
                selected.append(False)
                shooting.append(True)
                placed.append(False)

#check if player picked turret2   
            if event.type == pygame.MOUSEBUTTONDOWN  and money>=15 and mouseY>=turret2Y[0] and mouseY<=turret2Y[0]+turret2H and mouseX>=turret2X[0] and mouseX<=turret2X[0]+turret2W:
                selected2[i] = True
                turret2X.append(mouseX)  
                turret2Y.append(mouseY) 
                turret2Health.append(100)
                selected2.append(False)

#check if player picked bomb  
            if event.type == pygame.MOUSEBUTTONDOWN  and money>=25 and clickedBomb[-1] == True and mouseY>=bombY[0]-bombR[i] and mouseY<=bombY[0]+bombR[i] and mouseX>=bombX[0]-bombR[i] and mouseX<=bombX[0]+bombR[i]:
                selectedBomb[i] = True
                bombX.append(mouseX)  
                bombY.append(mouseY)  
                bombR.append(30)
                selectedBomb.append(False)
                clickedBomb.append(True)
                bombDamage.append(False)

#check if player released turret1
            elif event.type == pygame.MOUSEBUTTONUP  and money>=15 and clickedY[-1] == True and mouseY>=turret1Y[-1] and mouseY<=turret1Y[-1]+turret1H and mouseX>=turret1X[-1] and mouseX<=turret1X[-1]+turret1W:
                selected[i] = False
                clickedY[-1] = False
                clickedX[-1] = False
                placed[-1] = True
                money = money - 15

#check if player released bomb
            elif event.type == pygame.MOUSEBUTTONDOWN  and money>=25 and clickedBomb[-1] == True and mouseY>=bombY[-1]-bombR[i] and mouseY<=bombY[-1]+bombR[i] and mouseX>=bombX[-1]-bombR[i] and mouseX<=bombX[-1]+bombR[i]:
                selectedBomb[i] = False
                clickedBomb[i] = False
                bombR[-1] = 100
                bombDamage[-1] = True
                money = money - 25

#check if player released turret2
            elif event.type == pygame.MOUSEBUTTONUP  and money>=15 and clickedY2[-1] == True and mouseY>=turret2Y[-1] and mouseY<=turret2Y[-1]+turret2H and mouseX>=turret2X[-1] and mouseX<=turret2X[-1]+turret2W:
                selected2[i] = False
                clickedY2[-1] = False
                clickedX2[-1] = False
                money = money - 15
                
            elif event.type == pygame.MOUSEMOTION:
                mouseX,mouseY = pygame.mouse.get_pos()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    inPlay = False
    
# move the asteroids
    for i in range(numEnemys):            
        enemyX[i] = enemyX[i] - enemyStep[i]

#Make sure items follow mose when picked

    for i in range(len(turret1X)-1,-1,-1):
        if selected[i]:
            turret1X[-1] = mouseX-15
            turret1Y[-1] = mouseY-25
        elif selected[i] != True:
            turret1X[-1] = turret1X[-1]
            turret1Y[-1] = turret1Y[-1]

    for i in range(len(bombX)-1,-1,-1):
        if selectedBomb[i]:
            bombX[-1] = mouseX
            bombY[-1] = mouseY
        elif selectedBomb[i] != True:
            bombX[-1] = bombX[-1]
            bombY[-1] = bombY[-1]

    for i in range(len(turret2X)-1,-1,-1):
        if selected2[i]:
            turret2X[-1] = mouseX-15
            turret2Y[-1] = mouseY-25
        elif selected2[i] != True:
            turret2X[-1] = turret2X[-1]
            turret2Y[-1] = turret2Y[-1]

#create money system to give money every few seconds
    spawnMoney = round(time.time() - moneyReferenceTime, 1)
    if spawnMoney > MONEY_PERIOD:
        money = money + 5
        moneyReferenceTime = time.time()

#createbullets that shoot for a specific turret
    for l in range(len(turret1X)):
        spawnBullet = round(time.time() - bulletReferenceTime, 1)
        if placed[-1]:
            if shooting[l]:
                if spawnBullet > BULLET_PERIOD:

                    for i in range(2):
                        bulletX.append([])
                        bulletY.append([])
                        bulletVisible.append([])
                    for i in range(len(turret1X)):
                        bulletX[i].append(turret1X[i])
                        bulletY[i].append(turret1Y[i])
                        bulletVisible[i].append(False)
                    bulletReferenceTime = time.time()

#move bullet
    for l in range(len(turret1X)):
        if placed[l]:
            if shooting[l]:
                for j in range(len(bulletX[l])):
                    bulletX[l][j] = bulletX[l][j] + bulletStep

#don't allow bullet to go past window
    for l in range(len(turret1X)):
        if placed[-1]:
            if shooting[l]:
                for n in range(len(bulletX[l])):
                    if bulletX[l][0] > 700:
                        bulletVisible[l].pop(0)
                        bulletX[l].pop(0)
                        bulletY[l].pop(0)
                
#Check for collision between enemy and bullet
    for i in range(len(enemyX)):
        lastIndexBomb = len(bombX)-1
        for l in range(len(turret1X)):
            if placed[l]:
                if shooting[l]:
                    for n in range(len(bulletX[l])):
                        if enemyVisible[i] and enemyX[i]<800:
                            if bulletX[l][n-1] - bulletW/2 <= enemyX[i] + enemyR and bulletX[l][n-1] + bulletW/2 >= enemyX[i] - enemyR:
                                if bulletY[l][n-1]-bulletH <= enemyY[i] and bulletY[l][n-1]+bulletH >=enemyY[i]:
                                    enemyHealth[i] = enemyHealth[i] - 1
                                    bulletVisible[l].pop(n-1)
                                    bulletX[l].pop(n-1)
                                    bulletY[l].pop(n-1)

#check for collision between enemy and turret1          
            for k in range(len(turret2X)):
                if l < len(turret1X) and l < len(turret1Y) and l < len(turret1Health):
                    if enemyVisible[i] and enemyX[i]+enemyR >= turret1X[l]-turret1W and enemyX[i]-enemyR <= turret1X[l]+turret1W and turret1Y[l] <= enemyY[i] and turret1Y[l]+turret1H >= enemyY[i]:
                        turret1Health[l] = turret1Health[l] - 1
                        enemyX[i] = enemyX[i] + 10

#check for collision between enemy and turret2  
                if enemyVisible[i] and enemyX[i]+enemyR >= turret2X[k]-turret2W and enemyX[i]-enemyR <= turret2X[k]+turret2W and turret2Y[k] <= enemyY[i] and turret2Y[k]+turret2H >=enemyY[i]:
                    turret2Health[k] = turret2Health[k] - 1
                    enemyX[i] = enemyX[i] + 10

#Make turrets disappear when killed
                for l in range(len(turret1X) - 1, -1, -1):
                    if turret1Health[l] <= 0:
                        # Pop the elements from all lists
                        turret1X.pop(l)
                        turret1Y.pop(l)
                        turret1Health.pop(l)
                        selected.pop(l)
                        clickedY.pop(l)
                        clickedX.pop(l)
                        shooting.pop(l)
                        placed.pop(l)

                for l in range(len(turret2X) - 1, -1, -1):
                    if turret2Health[l] <= 0:
                        # Pop the elements from all lists
                        turret2X.pop(l)
                        turret2Y.pop(l)
                        turret2Health.pop(l)
                        selected2.pop(l)
                        clickedY2.pop(l)
                        clickedX2.pop(l)

#Place turrets onto grid

                if clickedY[-1] != True and turret1Y[-1] <=180 and turret1Y[-1] >0:
                    turret1Y[-1] = 180
                    clickedY[l] = True

                elif clickedY[-1] != True and turret1Y[-1] >450 and turret1Y[-1] <=600:
                    turret1Y[-1] = 540
                    clickedY[l] = True

                elif clickedY[-1] != True and turret1Y[-1] >360 and turret1Y[-1] <=450:
                    turret1Y[-1] = 450
                    clickedY[l] = True
                    
                elif clickedY[-1] != True and turret1Y[-1] >270 and turret1Y[-1] <=360:
                    turret1Y[-1] = 360
                    clickedY[l] = True
                    
                elif clickedY[-1] != True and turret1Y[-1] >180 and turret1Y[-1] <=270:
                    turret1Y[-1] = 270
                    clickedY[l] = True

                elif clickedX[-1] != True and turret1X[-1] <=140:
                    turret1X[-1] = 140
                    clickedX[l] = True

                elif clickedX[-1] != True and turret1X[-1] >650 and turret1X[-1] <=720:
                    turret1X[-1] = 720
                    clickedX[l] = True

                elif clickedX[-1] != True and turret1X[-1] >580 and turret1X[-1] <=650:
                    turret1X[-1] = 650
                    clickedX[l] = True

                elif clickedX[-1] != True and turret1X[-1] >510 and turret1X[-1] <=580:
                    turret1X[-1] = 580
                    clickedX[l] = True

                elif clickedX[-1] != True and turret1X[-1] >440 and turret1X[-1] <=510:
                    turret1X[-1] = 510
                    clickedX[l] = True

                elif clickedX[-1] != True and turret1X[-1] >360 and turret1X[-1] <=440:
                    turret1X[-1] = 440
                    clickedX[l] = True

                elif clickedX[-1] != True and turret1X[-1] >290 and turret1X[-1] <=360:
                    turret1X[-1] = 360
                    clickedX[l] = True
                    
                elif clickedX[-1] != True and turret1X[-1] >210 and turret1X[-1] <=290:
                    turret1X[-1] = 290
                    clickedX[l] = True
                    
                elif clickedX[-1] != True and turret1X[-1] >140 and turret1X[-1] <=210:
                    turret1X[-1] = 210
                    clickedX[l] = True


                if clickedY2[-1] != True and turret2Y[-1] <=180 and turret2Y[-1] >0:
                    turret2Y[-1] = 180
                    clickedY2[l] = True

                elif clickedY2[-1] != True and turret2Y[-1] >450 and turret2Y[-1] <=600:
                    turret2Y[-1] = 540
                    clickedY2[l] = True

                elif clickedY2[-1] != True and turret2Y[-1] >360 and turret2Y[-1] <=450:
                    turret2Y[-1] = 450
                    clickedY2[l] = True
                    
                elif clickedY2[-1] != True and turret2Y[-1] >270 and turret2Y[-1] <=360:
                    turret2Y[-1] = 360
                    clickedY2[l] = True
                    
                elif clickedY2[-1] != True and turret2Y[-1] >180 and turret2Y[-1] <=270:
                    turret2Y[-1] = 270
                    clickedY2[l] = True

                elif clickedX2[-1] != True and turret2X[-1] <=140:
                    turret2X[-1] = 140
                    clickedX2[l] = True

                elif clickedX2[-1] != True and turret2X[-1] >650 and turret2X[-1] <=720:
                    turret2X[-1] = 720
                    clickedX2[l] = True

                elif clickedX2[-1] != True and turret2X[-1] >580 and turret2X[-1] <=650:
                    turret2X[-1] = 650
                    clickedX2[l] = True

                elif clickedX2[-1] != True and turret2X[-1] >510 and turret2X[-1] <=580:
                    turret2X[-1] = 580
                    clickedX2[l] = True

                elif clickedX2[-1] != True and turret2X[-1] >440 and turret2X[-1] <=510:
                    turret2X[-1] = 510
                    clickedX2[l] = True

                elif clickedX2[-1] != True and turret2X[-1] >360 and turret2X[-1] <=440:
                    turret2X[-1] = 440
                    clickedX2[l] = True

                elif clickedX2[-1] != True and turret2X[-1] >290 and turret2X[-1] <=360:
                    turret2X[-1] = 360
                    clickedX2[l] = True
                    
                elif clickedX2[-1] != True and turret2X[-1] >210 and turret2X[-1] <=290:
                    turret2X[-1] = 290
                    clickedX2[l] = True
                    
                elif clickedX2[-1] != True and turret2X[-1] >140 and turret2X[-1] <=210:
                    turret2X[-1] = 210
                    clickedX2[l] = True

#check for collition between bomb and enemies
    for i in range(len(enemyX)):
        for j in range(lastIndexBomb,-1,-1):
            if bombDamage[-1] and enemyVisible[i] and enemyX[i]-enemyR<=bombX[-1]+bombR[-1] and enemyX[i]+enemyR>=bombX[-1]-bombR[-1] and enemyY[i]+enemyR>=bombY[-1]-bombR[-1] and enemyY[i]-enemyR<=bombY[-1]+bombR[-1]:
                enemyHealth[i] = enemyHealth[i] - 10
                bombX.pop(-1)
                bombY.pop(-1)
                bombR.pop(-1)

#Make enemy go invisible and end Play if enemy reaches your house
        if enemyHealth[i] <= 0:
            enemyVisible[i] = False
        if enemyVisible[i] and enemyX[i]<0 and enemyHealth[i]>0:
            end = True
            inPlay = False
#Draw win window
    while win:
        redrawWinWindow()
        pygame.time.delay(2)
        pygame.event.clear()

#Draw end window
    while end:
        redrawEndWindow()
        pygame.time.delay(2)
        pygame.event.clear()
#---------------------------------------#
pygame.quit()


