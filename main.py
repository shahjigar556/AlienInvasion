import pygame
import sys
import random
import math
from pygame import mixer
# Anything to be displayed on the screen must be included in while loop
# initialise a Game
pygame.init()

# create a screen
screen = pygame.display.set_mode((800,600)) # 800 px wide and 600 ps tall

running=True

#backGround music

mixer.music.load("background.wav")
mixer.music.play(-1)

# setCaption
pygame.display.set_caption("space Invador")
icon=pygame.image.load("ufo.png")

# setIcon
pygame.display.set_icon(icon)

bimg=pygame.image.load("background.png")

playerImg=pygame.image.load("player.png")
playerX=370
playerY=480
playerX_change=0

def player(x,y):
    screen.blit(playerImg,(x,y))

enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6

for i in range(0,num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(0)

bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=7
bulletState='ready'

# function for enemy
def enemy(X,Y):
    screen.blit(enemyImg[0],(X,Y))

def fireBullet(x,y):
    screen.blit(bulletImg,(x,y))
    global bulletState
    bulletState='fire'

def collision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance <27:
        return  True
    else:
        return False

# score
score=0
font=pygame.font.Font("freesansbold.ttf",32)
scoreX=10
scoreY=10

def show_score(x,y):
    scoreCard=font.render("Score: "+str(score),True,(255,255,255)) #(text,True,(255,255,255))
    screen.blit(scoreCard,(x,y))

#Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)
gameX=200
gameY=250

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


# Game Loop
while running:

    # filling the surface
    screen.fill((0,0,0))  #RGB Values


    screen.blit(bimg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # Leaving the Game
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:   # Moving to left
                print("Left Key is Pressed")
                playerX_change=-5

            elif event.key == pygame.K_RIGHT:  # Moving to right
                print("Right Key is Pressed")
                playerX_change=5

            elif event.key==pygame.K_SPACE:
                print("space key is pressed")
                if bulletState == 'ready':
                    bulletX = playerX
                    fireBullet(bulletX + 16, bulletY + 10)
                    bulletSound=mixer.Sound("laser.wav")
                    bulletSound.play()


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key is released")
                playerX_change=0

# algorithm for player
    playerX= playerX+playerX_change
    if playerX>=736:
        playerX=736
    elif playerX<=0:
        playerX=0
    player(playerX,playerY)

    # algorithm for enemy
    for i in range(0,num_of_enemies):
        if enemyX[i] <= 0:
            enemyX_change[i]=4
            enemyY_change[i]=40
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i]=-4
            enemyY_change[i]=40
            enemyY[i]+=enemyY_change[i]

        enemyX[i]+=enemyX_change[i]

    # algorithm for bullet fire
    if bulletY<=0:
        bulletY=480
        bulletState='ready'

    if bulletState == 'fire':
        fireBullet(bulletX+16,bulletY)
        bulletY-=bulletY_change


    for i in range(num_of_enemies):
        if (collision(enemyX[i],enemyY[i],bulletX,bulletY)):
            score+=1  # collision is successfull
            bulletY=480
            bulletState="ready"
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)
            expolsion_sound=mixer.Sound("explosion.wav")
            expolsion_sound.play()

        if enemyY[i]>440:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()

    for i in range(num_of_enemies):
        enemy(enemyX[i],enemyY[i])

    show_score(scoreX,scoreY)
    pygame.display.update()



