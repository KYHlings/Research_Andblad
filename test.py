import pygame
#Starta pygame
pygame.init()
#skapa skärm ruta               (bredd, höjd)
width = 800
hight = 600
screen = pygame.display.set_mode((width, hight))

#Titel
pygame.display.set_caption("Testing,testing")
icon = pygame.image.load("rocket.png") # för att ladda en icon.
pygame.display.set_icon(icon)# för att visa icon i fönsterrutans hörn.

#Spelare
player_img = pygame.image.load('space-invaders.png')
player_img = pygame.transform.scale(player_img, (50, 38))



#Fiende
enemy_img = pygame.image.load("lorry.png")
enemy_img = pygame.transform.scale(enemy_img,(50,40))
enemy_X = 760
enemy_Y = 400
enemy_change = -0.1


def player(x,y):
    screen.blit(player_img,(x,y))
def enemy(x,y):
    screen.blit(enemy_img,(x,y))

def enemy_control(enemy_X,enemy_change):

    if enemy_X <= 750 :
        enemy_X = 750
        enemy_change = -0.1

    if enemy_X >= 0:
        enemy_X = 0
        enemy_change = 0.1

    return enemy_X,enemy_change


def player_control():
    player_X = 370
    player_Y = 480
    speed = 0.1
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_X -= speed
        if event.key == pygame.K_RIGHT:
            player_X += speed
        if event.key == pygame.K_UP:
            player_Y -= speed
        if event.key == pygame.K_DOWN:
            player_Y += speed
    if player_X <= 0:
        player_X = 0
    if player_X >= width-50:
        player_X = width-50
    if player_Y <=0:
        player_Y = 0
    if player_Y >= hight-38:
        player_Y = hight-38
    return player_X,player_Y
#Game loop
running = True
while running:

    #screen.fill behöver ligga överst i loopen, för att först ladda backgrunden.
    #RGB=red,green,blue value 0 -> 255(max)
    screen.fill((100,100,150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False

    enemy_change -= 0.1
    player_X, player_Y = player_control()
    enemy_X= enemy_control(enemy_X,enemy_change)
    player(player_X,player_Y)
    enemy(enemy_X,enemy_Y)
    pygame.display.update()

