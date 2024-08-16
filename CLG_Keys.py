# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: CLG_Keys.py
import pygame
Mouse_Pos_X = 0
Mouse_Pos_Y = 0
WX = 1280
WY = 720
width, height = WX, WY
def Press_Close():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


def Click():
    for event in pygame.event.get():
        if event.type == pygame.mouse.get_pressed:
            return False

def PresedKey():
    # global FullScreen
    # global Mouse_Pos_X
    # global Mouse_Pos_Y
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