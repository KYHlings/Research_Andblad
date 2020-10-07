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
player_X = 370
player_Y = 480
speed = 2

#Fiende
enemy_img = pygame.image.load("lorry.png")
enemy_img = pygame.transform.scale(enemy_img,(40,40))
enemy_X = 800
enemy_Y = 400
enemy_speed= 1


def player(x,y):
    screen.blit(player_img,(x,y))
def enemy(x,y):
    screen.blit(enemy_img,(x,y))

def enemy_control():
    global enemy_X
    global enemy_Y
    if enemy_X <= 800 :
        enemy_X -= enemy_speed
    if enemy_X >= 0:
        enemy_X += enemy_speed

    return enemy_X,enemy_Y

def player_control():
    global running
    global player_Y
    global player_X
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    if keys[pygame.K_LEFT]:
        player_X -= speed
    if keys[pygame.K_RIGHT]:
        player_X += speed
    if keys[pygame.K_UP]:
        player_Y -= speed
    if keys[pygame.K_DOWN]:
        player_Y += speed
    if player_X <=0:
        player_X = 0
    if player_X >= width-50:
        player_X = width-50
    if player_Y >= hight-38:
        player_Y = hight-38
    if player_Y <= 0:
        player_Y = 0
    return player_X, player_Y

#Game loop
running = True
while running:
    #screen.fill behöver ligga överst i loopen, för att först ladda backgrunden.
    #RGB=red,green,blue value 0 -> 255(max)
    screen.fill((100,100,150))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False
    enemy(enemy_X,enemy_Y)
    player_X, player_Y = player_control()
    enemy_X, enemy_Y = enemy_control()
    player(player_X,player_Y)
    #enemy(enemy_X,enemy_Y)
    pygame.display.update()

