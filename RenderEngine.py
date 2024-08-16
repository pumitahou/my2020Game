import pygame
from P_CLG import ParticleManager

class RenderPipeLine:
    def __init__(self,screen):
        self.screen = screen
        pass
    def setParticleManager(self,particleManager : ParticleManager):
        self.particleManager = particleManager
        
    def renderParticles(self):
        for p in self.particleManager.getParticles():
            pygame.draw.circle(self.screen, p.color, (p.positionX,p.positionY), p.radius)