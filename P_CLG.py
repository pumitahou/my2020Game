# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: P_CLG.py
import pygame, time, random, math
startTime = time.time()
WX = 1280
WY = 720
pygame.init()
width, height = WX, WY
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
pygame.display.set_caption('CLG v 0.0')
clock = pygame.time.Clock()
FullScreen = True
intro = True
running = True
Game = True
Mouse_Pos_X = 0
Mouse_Pos_Y = 0
clock = pygame.time.Clock()
particles = 0
life_P = []
V_X = []
V_Y = []
Pos_X = []
Pos_Y = []
P_R = []
P_G = []
P_B = []
P_Radius = []
Anglo = 0

def PresedKey():
    global FullScreen
    global Mouse_Pos_X
    global Mouse_Pos_Y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            Mouse_Pos_X, Mouse_Pos_Y = pygame.mouse.get_pos()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if FullScreen == True:
                    FullScreen = False
                    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
                elif FullScreen == False:
                    screen = pygame.display.set_mode((width, height))
                    FullScreen = True


def Particle_Spawn(P_Num, Life, posX, posY, R, G, B, VX, VY, Rad):
    global P_B
    global P_G
    global P_R
    global P_Radius
    global Pos_X
    global Pos_Y
    global V_X
    global V_Y
    global life_P
    global particles
    particles += P_Num
    try:
        for i in range(P_Num):
            life_P.append(Life)
            V_X.append(VX)
            V_Y.append(VY)
            Pos_X.append(posX)
            Pos_Y.append(posY)
            P_R.append(R)
            P_G.append(G)
            P_B.append(B)
            P_Radius.append(Rad)
            if Debug == True:
                print (
                 'Summon:', i, 'Pos_X:', Pos_X[i], 'Pos_Y', Pos_Y[i], 'V_X', V_X[i], 'V_Y', V_Y[i])

    except:
        None

    return


def Particle_Spawn_angle(P_Num, Life, posX, posY, R, G, B, Force, Angle, Rad):
    global particles
    particles += P_Num
    try:
        for i in range(P_Num):
            life_P.append(Life)
            V_X.append(math.cos(Angle) * Force)
            V_Y.append(math.sin(Angle) * Force)
            Pos_X.append(posX)
            Pos_Y.append(posY)
            P_R.append(R)
            P_G.append(G)
            P_B.append(B)
            P_Radius.append(Rad)

    except:
        None

    return


def Particle_Move():
    try:
        for i in range(particles):
            Pos_X[i] += V_X[i]
            Pos_Y[i] += V_Y[i]
            life_P[i] -= random.randint(0, 3)

    except:
        None

    return


def Particle_Render(P_rander_off_or_On):
    if P_rander_off_or_On == True:
        try:
            for i in range(particles):
                pygame.draw.circle(screen, (P_R[i], P_G[i], P_B[i]), (int(Pos_X[i]), int(Pos_Y[i])), P_Radius[i])

        except:
            for i in range(particles):
                pygame.draw.circle(screen, (P_R[i], P_G[i], P_B[i]), (int(Pos_X[i]), int(Pos_Y[i])), P_Radius[i])


def Particle_Death(OFF_On):
    global particles
    for i in range(particles):
        try:
            if life_P[i] <= 0 and OFF_On == True:
                particles -= 1
                life_P.pop(i)
                V_X.pop(i)
                V_Y.pop(i)
                Pos_X.pop(i)
                Pos_Y.pop(i)
                P_R.pop(i)
                P_G.pop(i)
                P_B.pop(i)
                P_Radius.pop(i)
        except:
            None

    return


def Void_Space_Particle():
    for i in range(particles):
        if Pos_Y[i] <= 0:
            Pos_Y[i] = WY
        elif Pos_Y[i] >= WY:
            Pos_Y[i] = 0
        if Pos_X[i] <= 0:
            Pos_X[i] = WX
        elif Pos_X[i] >= WX:
            Pos_X[i] = 0


def Particle_Spawn_Rv(P_Num, Life, posX, posY, R, G, B, VX, VY, VXM, VYM, Rad):
    global particles
    particles += P_Num
    try:
        for i in range(P_Num):
            life_P.append(Life)
            V_X.append(random.uniform(VX, VXM))
            V_Y.append(random.uniform(VY, VYM))
            Pos_X.append(posX)
            Pos_Y.append(posY)
            P_R.append(R)
            P_G.append(G)
            P_B.append(B)
            P_Radius.append(Rad)

    except:
        None

    return