# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: CLG v 0.4.0.py
import pygame, time, random
from CLG_Keys import *
from P_CLG import *
from ClG_BoxAlert import *
from CLG_Lana import *
from CLG_Math import *
Windows_X = 1280
Windows_Y = 720
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Windows_X, Windows_Y))
font = pygame.font.Font('Fonts//animeace2_bld.ttf', 72)
FPS = pygame.font.Font('Fonts//animeace2_bld.ttf', 16)
CB = pygame.font.Font('Fonts//animeace2_bld.ttf', 16)
CB2 = pygame.font.Font('Fonts//animeace2_bld.ttf', 162)
pygame.mixer.music.load('Mana Two - Part 1.mp3')
BG_test = pygame.image.load('images//BG_Test.png').convert()
Intro = pygame.image.load('images//Intro.png').convert()
Mouse_Pos_X = 0
Mouse_Pos_Y = 0
Fps_Start = 0
FPS_TXT = 'init'
Debug = True
Game = True
pygame.display.set_caption('CLG v 0.2.0')
clock = pygame.time.Clock()
Init_Menu = True
pygame.mixer.music.play(-1, 0.0)
while Init_Menu == True:
    Fps_Start = time.time()
    Delay = time.time()
    screen.fill((0, 0, 0))
    Press_Close()
    Mouse_Pos_X, Mouse_Pos_Y = pygame.mouse.get_pos()
    Particle_Spawn_Rv(5, 1000, random.randint(0, Windows_X), random.randint(0, Windows_Y), random.randint(0, 40), random.randint(0, 40), random.randint(0, 40), -1, -1, 1, 1, random.randint(1, 4))
    Particle_Move()
    Particle_Death(True)
    blit_text(screen, 'Culpable', (random.randint(0, Windows_X), random.randint(0, Windows_Y)), CB, (10,
                                                                                                     10,
                                                                                                     10))
    blit_text(screen, 'Eres un error', (random.randint(0, Windows_X), random.randint(0, Windows_Y)), CB, (10,
                                                                                                          10,
                                                                                                          10))
    blit_text(screen, 'No deviste haver nacido', (random.randint(0, Windows_X), random.randint(0, Windows_Y)), CB, (10,
                                                                                                                    10,
                                                                                                                    10))
    blit_text(screen, 'Acaso alguien te ama lincoln?', (random.randint(0, Windows_X), random.randint(0, Windows_Y)), CB, (10,
                                                                                                                          10,
                                                                                                                          10))
    blit_text(screen, 'porque existes', (random.randint(0, Windows_X), random.randint(0, Windows_Y)), CB, (10,
                                                                                                           10,
                                                                                                           10))
    blit_text(screen, 'Hay una razon por la que tienes que vivir?', (random.randint(0, Windows_X), random.randint(0, Windows_Y)), CB, (10,
                                                                                                                                       10,
                                                                                                                                       10))
    blit_text(screen, 'Acaso te respetan?', (random.randint(0, Windows_X), random.randint(0, Windows_Y)), CB, (10,
                                                                                                               10,
                                                                                                               10))
    Particle_Render(True)
    if Mouse_Pos_X > 640 and Mouse_Pos_X < 936 and Mouse_Pos_Y > 372 and Mouse_Pos_Y < 460:
        MenuButton_Start_S(screen, font, 'Start', 640, 360, False)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                Init_Menu = False

    else:
        MenuButton_Start(screen, font, 'Start', 640, 360, False)
    if Debug == True:
        FPS_TXT = str(int(1 / (time.time() - Fps_Start)))
        Print_Blit(screen, FPS, FPS_TXT, 0, 0, False)
    clock.tick(120)
    pygame.display.update()

while Game:
    CB_1 = True
    while CB_1:
        for i in range(3000):
            Particle_Death(True)

        ChatBox_Pause(screen, CB, 'Con la E avanzas las cajas de texto...', 10, 10, False, 200, 200, 234)
        ChatBox_Pause(screen, CB, 'Hola...', 10, 10, False, 200, 200, 234)
        ChatBox_Pause(screen, CB, 'Como estas..', 10, 10, False, 200, 200, 234)
        ChatBox_Pause(screen, CB, 'Aun puedes cerrar...', 10, 10, False, 200, 20, 23)
        ChatBox_Pause(screen, CB2, 'Ok...', 10, 10, False, 200, 0, 2)
        blit_text_Paused(Intro, (0, 0), screen, 'Toda esta historia comienza en un dia comum...', (10,
                                                                                                   10), CB, color=pygame.Color('white'))
        blit_text_Paused(Intro, (0, 0), screen, 'Como todos sabran o talvez no es una de las mas trajicas del momento, pero lincoln', (10,
                                                                                                                                       10), CB, color=pygame.Color('white'))
        blit_text_Paused(Intro, (0, 0), screen, 'El esta Arto de esta situacion y hara lo posible por cambiar la balanza a su favor...', (10,
                                                                                                                                          10), CB, color=pygame.Color('white'))
        blit_text_Paused(Intro, (0, 0), screen, 'Esta vercion esta a un 13% completa por lo que solo tiene este modo de juego sin proposito pero luego tendra proposito, arrastra el mouse hacia las esferas para quitarles vida', (10,
                                                                                                                                                                                                                                    10), CB, color=pygame.Color('white'))
        CB_1 = False

    CB_3 = True
    while CB_3:
        screen.fill((0, 0, 0))
        Press_Close()
        Mouse_Pos_X_Lana, Mouse_Pos_Y_Lana = pygame.mouse.get_pos()
        if Lana_Count() <= 10:
            summon_Lana_Mud(True, random.randint(0, Windows_X), random.randint(0, int(Windows_Y / 8)), random.randint(15, 25), random.randint(79, 129), random.randint(46, 78), random.randint(9, 14))
        else:
            None
        for i in range(Lana_Count()):
            N, L, X_L, Y_L, R, red, green, blue = Lana_Data_R(i)
            if distance(Mouse_Pos_X_Lana, Mouse_Pos_Y_Lana, X_L, Y_L) < R:
                Damage_Lana(N, 10)
                Particle_Spawn_Rv(1, 300, Mouse_Pos_X_Lana, Mouse_Pos_Y_Lana, random.randint(200, 240), random.randint(200, 240), random.randint(200, 240), -1, -3, 1, 0.2, random.randint(int(R / 16), int(R / 2)))

        for i in range(Lana_Count()):
            try:
                N, L, X_L, Y_L, R, red, green, blue = Lana_Data_R(i)
                if L <= 0:
                    Kill_Lana(i)
            except:
                None

        for i in range(Lana_Count()):
            try:
                N, L, X_L, Y_L, R, red, green, blue = Lana_Data_R(i)
                if Y_L > Windows_Y:
                    Kill_Lana(i)
            except:
                None

        for i in range(Lana_Count()):
            N, L, X_L, Y_L, R, red, green, blue = Lana_Data_R(i)
            Move_Lana(N - 1, 0.2)
            pygame.draw.circle(screen, (red, green, blue), (X_L, int(Y_L)), R)

        Particle_Move()
        Particle_Death(True)
        Particle_Render(True)
        pygame.display.update()
        clock.tick(120)