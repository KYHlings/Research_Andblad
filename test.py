import pygame
#Starta pygame
pygame.init()
#skapa skärm ruta               (bredd, höjd)
screen = pygame.display.set_mode((800, 600))

#Titel
pygame.display.set_caption("Testing,testing")
#icon = pygame.image.load("") # för att ladda en icon.
#pygame.display.set_icon(icon)# för att visa icon i fönsterrutans hörn.

#Spelare
#player_img = pygame.image.load('')
#player_X = 370
#player_Y = 480

#def player():
    #screen.blit(player_img,(player_x,player_y))

#Game loop
running = True
while running:
    #screen.fill behöver ligga överst i loopen, för att först ladda backgrunden.
    #RGB=red,green,blue value 0 -> 255(max)
    screen.fill((150,150,150))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False



    #player()
    pygame.display.update()

