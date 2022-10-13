import pygame
from pygame.sprite import Sprite

class Sujeto(Sprite):
  def __init__(self, *grps):
    Sprite.__init__(self,grps)
    self.rect
    self.image

class SujetoFisico(Sujeto):
  def __init__(self, *grps):
    Sujeto.__init__(self,grps)
    self.dim = pygame.Vector2()
    self.pos = pygame.Vector2()
    self.vel = pygame.Vector2()
    