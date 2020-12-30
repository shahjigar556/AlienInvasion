import pygame
import sys

# initialise a Game
pygame.init()

# create a screen
screen = pygame.display.set_mode((800,600))# 800 px wide and 600 ps tall

running = True

# setCaption
pygame.display.set_caption("space Invador")
icon=pygame.image.load("ufo.png")

# setIcon
pygame.display.set_icon(icon)


playerImg=pygame.image.load("player.png")
playerX=370
playerY=480


def player(x,y):
    screen.blit(playerImg,(x,y))

# Game Loop
while running:

    # filling the surface
    screen.fill((0,0,0))  #RGB Values

    for event in pygame.event.get():
        if event.type== pygame.QUIT:   # Leaving the Game
            sys.exit()

    if playerX < float(800):
        playerX += 0.1
    elif playerX > float(800):
        playerX -= 0.1


    print(playerX)

    player(playerX,playerY)
    pygame.display.update()

