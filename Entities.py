# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: CLG_Lana.py
import Resources
import random
from CLG_Math import distance
from typing import List
class Enemy:
    def __init__(self,life,position,radium,color):
        self.Life = life
        self.Pos_X ,self.Pos_Y  = position
        self.radium = radium
        self.color = color
    def move(self,x,y):
        self.Pos_X += x
        self.Pos_Y += y
    
    def Damage_Lana(self,Damage):
        self.Life -= Damage

class EntityManager:
    def __init__(self):
        self.__listEnemy : List[Enemy] = []

    #kills the enemy if has low life or exit of window margin
    def kill_if_die(self):
        for i in range(len(self.__listEnemy) - 1, -1, -1):
            enemy = self.__listEnemy[i]
            if enemy.Life <= 0 or enemy.Pos_Y > Resources.windowheight:
                self.__listEnemy.pop(i)
    def summon_Lana_Mud(self,X, Y, R, RED, GREEN, BLUE):
        newEnemy = Enemy(100,(X,Y),R,(RED,GREEN,BLUE))
        self.__listEnemy.append(newEnemy)

    def updatePhysics(self):
        for enemy in self.__listEnemy:
            #gravity
            # the original code uses the number of list to move, a bug with multiple times
            enemy.move(0,0.2*10)
    def updateEnemys(self,positionX,positionY,particlemManager):
        for entity in self.__listEnemy:
                if distance(positionX, positionY, entity.Pos_X, entity.Pos_Y) < entity.radium:
                    entity.Damage_Lana(10)
                    particlemManager.Particle_Spawn_Rv(1,300,positionX, positionY, random.randint(200, 240), random.randint(200, 240), random.randint(200, 240), -1, -3, 1, 0.2, random.randint(int(entity.radium / 16), int(entity.radium / 2)))
    def getCount(self):
        return len(self.__listEnemy)
    def getEntities(self):
        return self.__listEnemy

