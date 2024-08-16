# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
# [GCC 9.4.0]
# Embedded file name: P_CLG.py

#thats will relocated in other File
import random, math
from typing import List
#_________________________________________

class Particle:
    def __init__(self,life = 100,position=(0,0),color=(0,0,0),velocity=(0,0),radius=3):
        self.velocityX,self.velocityY = velocity
        self.positionX,self.positionY = position
        self.life = life
        self.color = color
        self.radius = radius
        self.angle = 0
    def setAngle(self,angle):
        self.angle
    def move(self):
        self.positionX += self.velocityX
        self.positionY += self.velocityY
        self.life -= random.randint(0, 3)

class ParticleManager:
    def __init__(self):
        self.particles : List[Particle] = []
        pass
    def Particle_Spawn(self, P_Num, Life, posX, posY, R, G, B, VX, VY, Rad):
        for i in range(P_Num):
            theNewParticle = Particle(Life,(posX,posY),(R,G,B),(VX,VY),Rad)
            self.particles.append(theNewParticle)


    def Particle_Spawn_angle(self, P_Num, Life, posX, posY, R, G, B, Force, Angle, Rad):
        for i in range(P_Num):
            velocityXangle=math.cos(Angle) * Force
            velocityYangle=math.sin(Angle) * Force
            theNewParticle = Particle(Life,(posX,posY),(R,G,B),(velocityXangle,velocityYangle),Rad)
            self.particles.append(theNewParticle)

    def Particle_Move(self):
        for particle in self.particles:
            particle.move()

    def Particle_Death(self):
        #recorre la lista de forma inversa para evitar que se salga del indice
        for i in range(len(self.particles) -1, -1,-1):
            if self.particles[i].life <= 0 :
                self.particles.pop(i)

    def Particle_Spawn_Rv(self, P_Num: int, Life, posX, posY, R, G, B, minVelocityX, minVelocityY, maxVelocityX, maxVelocityY, Radius):
            for i in range(P_Num):
                velocityXangle=random.uniform(minVelocityX, maxVelocityX)
                velocityYangle=random.uniform(minVelocityY, maxVelocityY)
                theNewParticle = Particle(Life,(posX,posY),(R,G,B),(velocityXangle,velocityYangle),Radius)
                self.particles.append(theNewParticle)

    def getParticles(self):
        return self.particles
