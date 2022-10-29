import pygame
from pygame.sprite import Group

class RenderGroup(Group):
  def __init__(self,*Sprites:pygame.sprite.Sprite):
    super().__init__(Sprites)

  

class PhysicGroup(RenderGroup):

  def __init__(self,*Sprites:pygame.sprite.Sprite):
    super().__init__(Sprites)
    
