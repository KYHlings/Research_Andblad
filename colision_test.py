#functions tester för kolision, och prompt.
import pygame
#import time
from get_quiz import get_quiz

pygame.init()
clock = pygame.time.Clock()
run = True
width = 800
hight = 600

class Player():
    def __init__(self):
        self.player_image = pygame.image.load("rocket.png")
        self.player_img = pygame.transform.scale(self.player_image,(50,50))
        self.player_rect = self.player_img.get_rect(topleft=(100,200))

    def bouncing_img(self):
        global x_speed,y_speed
        self.player_rect.right += x_speed
        self.player_rect.bottom += y_speed

        if self.player_rect.right >= width or self.player_rect.left <= 0:
            x_speed *= -1
        if self.player_rect.bottom >= hight or self.player_rect.top <= 0:
            y_speed *= -1


class Mobs():
    def __init__(self):
        self.mob_image = pygame.image.load('lorry.png')
        self.mob_img = pygame.transform.scale(self.mob_image,(50,50))
        self.mob_rect = self.mob_img.get_rect(topleft=(300,150))

    def bouncing_img(self):
        global mob_x_speed,mob_y_speed
        self.mob_rect.right += mob_x_speed
        self.mob_rect.bottom += mob_y_speed

        if self.mob_rect.right >= width or self.mob_rect.left <= 0:
            mob_x_speed *= -1

        if self.mob_rect.bottom >= hight or self.mob_rect.top <= 0:
            mob_y_speed *= -1
    # Nedan är att spawna mobs från lista upp till vist antal, där n är hur många loopar imellan.
    # if count % n == 0:
    #     Enemylist.append(Enemy(random.randint(0,<YourScreenSize>),0.1))
    # if count > 1000:
    #     count = 0


def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,255))
    return textSurface, textSurface.get_rect()

def message_display(text,text2):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextSurf2, TextRect2 = text_objects(text2,largeText)
    TextRect.center = (int((width/2)),int((hight/2)))
    TextRect2.center =(int((width/2)),int((hight/2+20)))
    message_window = pygame.Surface([400,100])
    screen.blit(message_window,(200,250))
    screen.blit(TextSurf, TextRect)
    screen.blit(TextSurf2, TextRect2)

    pygame.display.update()

    wait(3)



def answer_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',20)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (int((width/2)),int((hight/2)))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()


def crash(text):
    run = True
    while run:
        lista = []
        quiz_promp,quiz_rans,quiz_wans = get_quiz()
        lista.append(quiz_rans)
        for wA in quiz_wans:
            lista.append(wA)
        message_window = pygame.Surface([400,100])
        largeText = pygame.font.Font('freesansbold.ttf',20)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = (int((width/2)),int((hight/2)))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    answer_display("rätt")
                    run = False

                if event.key == pygame.K_n:
                    answer_display("fel")
                    run = False
        screen.blit(message_window,(200,250))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()


def wait(time):
    clock = pygame.time.Clock()
    waiting = True

    while waiting:
        dt = clock.tick(30) / 1000
        time -= dt
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    answer_display("rätt")
                    time = 0

                if event.key == pygame.K_n:
                    answer_display("fel")
                    time = 0
            pygame.display.update()

        if time <= 0:
            waiting = False

screen = pygame.display.set_mode((width,hight))
#second_surface = pygame.Surface([200,100])
#img_rect=second_surface.get_rect(topleft=(100,200))
player = Player()
mob = Mobs()
x_speed = 2
y_speed = 1
mob_x_speed = 2
mob_y_speed = 2

#mob.mob_rect.left += 2
#mob.mob_rect.top += 1
def game_loop():
    run = True
    global x_speed,y_speed,mob_x_speed,mob_y_speed
    while run:
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(player.player_img,player.player_rect)
        screen.blit(mob.mob_img,mob.mob_rect)
        player.bouncing_img()
        mob.bouncing_img()
        tollerance = 10
        if player.player_rect.colliderect(mob.mob_rect):
            if abs(mob.mob_rect.bottom - player.player_rect.top) < tollerance:
                y_speed *= -1
                mob_y_speed *= -1
                crash('Fråga här.')

            if abs(mob.mob_rect.top - player.player_rect.bottom) < tollerance:
                y_speed *= -1
                mob_y_speed *= -1
                crash('Fråga här.')

            if abs(mob.mob_rect.left - player.player_rect.right) < tollerance:
                x_speed *= -1
                mob_x_speed *= -1
                crash('Fråga här.')

            if abs(mob.mob_rect.right - player.player_rect.left) < tollerance:
                x_speed *= -1
                mob_x_speed *= -1
                crash('Fråga här.')


        pygame.display.update()
        clock.tick(60)

game_loop()