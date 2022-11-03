import pygame
from pygame.sprite import Group
from  fisicas.physics import Physics
from elementos import Element
class RenderGroup(Group):
  def __init__(self,*Sprites:Element):
    super().__init__(Sprites)
  def update(self,dt):
    super().update(dt=dt)
  def render(self,ventana):
    self.draw(ventana)
  def draw(self,ventana:pygame.Surface):
    for s in self.sprites():
      s.render(ventana)

class PhysicGroup(RenderGroup):

  def __init__(self,*Sprites:pygame.sprite.Sprite):
    super().__init__(Sprites)
    self.pengine = Physics()

  def update(self,dt):
    super().update(dt)
  
    
