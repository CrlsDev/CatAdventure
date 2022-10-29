import pygame
from pygame.sprite import Sprite
pygame.sprite.Group
class Element(Sprite):
  """
  Una clase que será usada como una interfaz para la creación de diferentes
  elementos en el juego
  """
  def __init__(self, *grps):
    Sprite.__init__(self,grps)
  

class PhysicElement(Element):
  
  def __init__(self,hitbox,imagen, *grps):
    Element.__init__(self,grps)
    self.rect = pygame.Rect(hitbox)
    self.image=pygame.transform.scale(imagen,self.rect.size)
    self.pos = pygame.Vector2()
    self.vel = pygame.Vector2()
    self.acc = pygame.Vector2()