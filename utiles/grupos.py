import pygame
from pygame.sprite import Group
from  fisicas.physics import Physics

class RenderGroup(Group):
  def __init__(self,*Sprites:pygame.sprite.Sprite):
    super().__init__(Sprites)
  def update(self,dt):
    super().update(dt=dt)
  

class PhysicGroup(RenderGroup):

  def __init__(self,*Sprites:pygame.sprite.Sprite):
    super().__init__(Sprites)
    self.pengine = Physics()

  def update(self,dt):
    super().update()
    
