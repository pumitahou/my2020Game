import pygame
from P_CLG import ParticleManager
from Entities import EntityManager

class RenderPipeLine:
    def __init__(self,screen):
        self.screen = screen
        pass
    def setParticleManager(self,particleManager : ParticleManager):
        self.particleManager = particleManager
    def setEnemyManager(self,entityManager : EntityManager):
        self.entityManager = entityManager
        
    def renderParticles(self):
        for p in self.particleManager.getParticles():
            pygame.draw.circle(self.screen, p.color, (p.positionX,p.positionY), p.radius)
    
    def renderEnemies(self):
        for enemy in self.entityManager.getEntities():
            pygame.draw.circle(self.screen, enemy.color, (enemy.Pos_X,enemy.Pos_Y), enemy.radium)