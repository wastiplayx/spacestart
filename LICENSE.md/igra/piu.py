import pygame
import random
import time
pygame.init()
#хуйня
okno = pygame.display.set_mode((500, 500))
run = False
sup = True
idk = False
x = 50
y = 350
python = False
left = False
right = False
blue = True
#это комментарий и  я хочу сказать майнкрафт говнооо а пятерка тоже говно)
damage1 = pygame.image.load("player_dl1.png")
damage2 = pygame.image.load("player_dl2.png")
damage3 = pygame.image.load("player_dl3.png")
kolvoanim = 0
pula = pygame.Surface((10,10))
p_x = 1000
p_y = 1000
noni = None
enemy = True
moving = True
nez = False
red = True
t = True
d1 = True
d2 = True
d3 = True
count = 0
amount = 3
global time
speed = 8
time = 60
a = False
#хуйня №2
pula = pygame.mixer_music.load("puli.mp3")
background_music = pygame.mixer_music.load("back.mp3")
pygame.mixer_music.play()
igrok = pygame.image.load("player.png")
fon = pygame.image.load("fon.jpg")
meteor = pygame.image.load("enemy.png")
pygame.display.set_caption("SpaceStar")
while run == False: #коменты ничего коду не делают а это 80 количество фпс
    pygame.time.delay(60)
    for emm in pygame.event.get():
        if emm.type == pygame.QUIT:
            run = True   
    ris =  pygame.draw.circle(okno,(255,0,0),(p_x,p_y),5)
    hearth = pygame.font.SysFont("bold",20)
    life = hearth.render("Жизни:"+str(amount),0,(255,0,0))
    vrag = pygame.font.SysFont("bold",20)
    mom = vrag.render("Очки:"+str(count),0,(0,0,100))
    loose = pygame.font.SysFont("MK-90 Regular",50)
    if a:
        l =  loose.render("Game Over",0,(0,0,255))
        okno.blit(l,(160,1))
    okno.blit(mom,(0,0))
    okno.blit(life,(430,0))
    if t:
        okno.blit(igrok,(x,y))
    pygame.display.update()
    okno.blit(fon, (0,0))
    knopka = pygame.key.get_pressed()
    if d1:
        if amount == 2:
            t = False
            okno.blit(damage1,(x,y))
    if d2:
        if amount == 1:
            d1 = False
            okno.blit(damage2,(x,y))
    if d3:
        if amount == 0:
            d2 = False
            okno.blit(damage3,(x,y))
    #event on if player get pressed on button
    if moving:
        if knopka[pygame.K_d] and x<420:
            x += 10
        if knopka[pygame.K_a] and x>10:
            x-= 10
        if knopka[pygame.K_RIGHT] and x<420:
            x += 10
        if knopka[pygame.K_LEFT] and x>10:
            x-= 10
        if sup:
            if knopka[pygame.K_f]:
                noni = True
                p_x = x + 30
                p_y = y - 10
                sup = False

    if red:
        vx = random.randrange(20,400)
        vy = -10
        red = False
        nez = True
    if nez:
        okno.blit(meteor,(vx,vy))
        vy += speed
    if p_y<vy - 20 and vx<p_x<vx + 60:
        red = True
        nez = False
        count += 10
        speed += 0.2
    elif vy>470:
        red = True
        nez = False
        count -= 20
    elif vx - 65<x<vx + 85 and vy>y - 40:
        red = True
        nez = False
        if amount == 0:
            hearth = pygame.font.SysFont("bold",20)
            life = hearth.render("Жизни:0",0,(255,0,0))
            okno.blit(life,(430,0))
            moving = False
            nez = False
            red = False
            a = True
            dead  = pygame.mixer_music.load("smert.mp3")
            pygame.mixer_music.play()
        
        else:
            amount -= 1
        
    if count == (count - 1) + 1:
        time -= 0.1
        
            

        
#other function
    if noni:
        p_y -= 15
        if p_y < 0  :
            sup = True
            noni = False
        else:
            p_y -= 25
            if p_y < 1:
                noni = False 
                sup = True         
pygame.quit()