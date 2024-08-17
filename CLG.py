# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: CLG v 0.4.0.py
import pygame, time, random
from CLG_Keys import *
import Resources
from RenderEngine import RenderPipeLine
from Entities import EntityManager
from P_CLG import *
import Resources
from ClG_BoxAlert import *
from Entities import *
from CLG_Math import *
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Resources.windowlength, Resources.windowheight))

pygame.mixer.music.load('Mana Two - Part 1.mp3')
BG_test = pygame.image.load('images//BG_Test.png').convert()
Intro = pygame.image.load('images//Intro.png').convert()
Mouse_Pos_X = 0
Mouse_Pos_Y = 0
Fps_Start = 0
FPS_TXT = 'init'
Debug = True
Game = True
mediumFont = pygame.font.Font('Fonts//animeace2_bld.ttf', 72)
smallFont = pygame.font.Font('Fonts//animeace2_bld.ttf', 16)
bigFont = pygame.font.Font('Fonts//animeace2_bld.ttf', 162) 
pygame.display.set_caption('CLG v 0.2.0')
clock = pygame.time.Clock()
pygame.mixer.music.play(-1, 0.0)
def callbackDamage(particlemManager : ParticleManager, entityManager : EntityManager):
    if entityManager.getCount() <= 10:
        entityManager.summon_Lana_Mud(
            random.randint(0, Resources.windowlength),
            random.randint(0, int(Resources.windowheight / 8)),
            random.randint(15, 25),
            random.randint(79, 129), #red
            random.randint(46, 78),  #green
            random.randint(9, 14)    #blue
            )
    entityManager.updateEnemys(Resources.positionX,Resources.positionY,particlemManager)
    entityManager.updatePhysics()
def main():
    Init_Menu = True
    particleManager = ParticleManager()
    entityManager = EntityManager()
    renderPipeline = RenderPipeLine(screen)
    renderPipeline.setParticleManager(particleManager)
    renderPipeline.setEnemyManager(entityManager)

    while Init_Menu == True:
        Fps_Start = time.time()
        Delay = time.time()
        screen.fill((0, 0, 0))
        Press_Close()
        
        Resources.positionX, Resources.positionY = pygame.mouse.get_pos()
        particleManager.Particle_Spawn_Rv(5, 1000, random.randint(0, Resources.windowlength), random.randint(0, Resources.windowheight), random.randint(0, 40), random.randint(0, 40), random.randint(0, 40), -1, -1, 1, 1, random.randint(1, 4))
        particleManager.Particle_Move()
        particleManager.Particle_Death()
        
        for dialog in Resources.InitialDialogs:
            blit_text(screen, dialog, (random.randint(0, Resources.windowlength), random.randint(0, Resources.windowheight)), smallFont, (10,10,10))
            
        
        renderPipeline.renderParticles()
        if Resources.positionX > 640 and Resources.positionX < 936 and Resources.positionY > 372 and Resources.positionY < 460:
            MenuButton_Start_S(screen, mediumFont, 'Start', 640, 360, False)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    Init_Menu = False

        else:
            MenuButton_Start(screen, mediumFont, 'Start', 640, 360, False)
        if Debug == True:
            if((time.time() - Fps_Start) != 0):
                FPS_TXT = str(int(1.0 / (time.time() - Fps_Start)))
            Print_Blit(screen, smallFont, FPS_TXT, 0, 0, False)
        clock.tick(120)
        pygame.display.update()

    while Game:
        CB_1 = True
        while CB_1:
            for dialog in range(3000):
                particleManager.Particle_Death()

            ChatBox_Pause(screen, smallFont, 'Con la E avanzas las cajas de texto...', 10, 10, False, 200, 200, 234)
            ChatBox_Pause(screen, smallFont, 'Hola...', 10, 10, False, 200, 200, 234)
            ChatBox_Pause(screen, smallFont, 'Como estas..', 10, 10, False, 200, 200, 234)
            ChatBox_Pause(screen, smallFont, 'Aun puedes cerrar...', 10, 10, False, 200, 20, 23)
            ChatBox_Pause(screen, bigFont, 'Ok...', 10, 10, False, 200, 0, 2)
            blit_text_Paused(Intro, (0, 0), screen, 'Toda esta historia comienza en un dia comum...', (10,
                                                                                                    10), smallFont, color=pygame.Color('white'))
            blit_text_Paused(Intro, (0, 0), screen, 'Como todos sabran o talvez no es una de las mas trajicas del momento, pero lincoln', (10,
                                                                                                                                        10), smallFont, color=pygame.Color('white'))
            blit_text_Paused(Intro, (0, 0), screen, 'El esta Arto de esta situacion y hara lo posible por cambiar la balanza a su favor...', (10,
                                                                                                                                            10), smallFont, color=pygame.Color('white'))
            blit_text_Paused(Intro, (0, 0), screen, 'Esta vercion esta a un 13% completa por lo que solo tiene este modo de juego sin proposito pero luego tendra proposito, arrastra el mouse hacia las esferas para quitarles vida', (10,
                                                                                                                                                                                                                                        10), smallFont, color=pygame.Color('white'))
            CB_1 = False

        CB_3 = True
        while CB_3:
            Resources.positionX, Resources.positionY = pygame.mouse.get_pos()
            screen.fill((0, 0, 0))
            Press_Close()
            callbackDamage(particleManager,entityManager)
            
            entityManager.kill_if_die()
            
            renderPipeline.renderEnemies()
            particleManager.Particle_Move()
            particleManager.Particle_Death()
            renderPipeline.renderParticles()
            renderPipeline.renderEnemies()
            pygame.display.update()
            clock.tick(120)
    pass
if __name__ == "__main__":
    main()