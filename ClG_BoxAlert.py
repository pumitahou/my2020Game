# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: ClG_BoxAlert.py
import pygame
Mouse_Pos_X = 0
Mouse_Pos_Y = 0

def MenuButton_Start(screen, font, Text_D, X, Y, AntiAlias):
    MSG = font.render(Text_D, AntiAlias, (234, 240, 205))
    screen.blit(MSG, (X, Y))


def MenuButton_Start_S(screen, font, Text_D, X, Y, AntiAlias):
    MSG = font.render(Text_D, AntiAlias, (234, 5, 205))
    screen.blit(MSG, (X, Y))


def Print_Blit(screen, font, Text_D, X, Y, AntiAlias):
    MSG = font.render(Text_D, AntiAlias, (234, 105, 205))
    screen.blit(MSG, (X, Y))


def ChatBox_Pause(screen, font, Text_D, X, Y, AntiAlias, R, G, B):
    Chat = True
    while Chat:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    Chat = False

        MSG = font.render(Text_D, AntiAlias, (R, G, B))
        screen.blit(MSG, (X, Y))
        pygame.display.update()


def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [ word.split(' ') for word in text.splitlines() ]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space

        x = pos[0]
        y += word_height


def blit_text_Paused(BG, PosGB, surface, text, pos, font, color=pygame.Color('black')):
    Chat = True
    while Chat:
        try:
            xbg, ybg = PosGB
            surface.blit(BG, (xbg, ybg))
        except:
            surface.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    Chat = False

        words = [ word.split(' ') for word in text.splitlines() ]
        space = font.size(' ')[0]
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height
                surface.blit(word_surface, (x, y))
                x += word_width + space

            x = pos[0]
            y += word_height
            pygame.display.update()