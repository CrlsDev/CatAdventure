import pygame
from pygame.sprite import Sprite
from fisicas.physics import Physics
from math import pi


class Element(Sprite):
  """
  Una clase que será usada como una interfaz para la creación de diferentes
  elementos en el juego
  """
  def __init__(self, *grps):
    Sprite.__init__(self,grps)
  def update(self,dt):
    pass
  def render(self,surf:pygame.Surface):
    surf.blit(self.image,self.rect)

class ImageElement():
  def __init__(self,rect,image, *grps):
    print(grps)
    Element.__init__(grps)
    print(self.rect)
    self.rect = pygame.Rect(rect)
    self.image = pygame.transform.scale(image,self.rect.size)

class ChargeIndicator(Element):
  r:int=0
  g:int=0
  b:int=0
  
  def __init__(self,*grps):
    super().__init__(grps)
    self.rad = 15
    self.pos = pygame.Vector2()

  def update(self,dt):
    pass  
  def setColor(self, ratio):
    max_red = 180
    max_green = 150
    self.r = max_red*ratio
    self.g = max_green*(1-ratio)
  def render(self,ventana):
    pygame.draw.circle(ventana,self.color,self.pos, self.rad)
  @property 
  def color(self): return (self.r,self.g,self.b)

  def setPos(self,vec):
    self.pos = vec
class PhysicElement(Element):
  

  def __init__(self,hitbox:pygame.Rect, *grps):
    Element.__init__(self,grps)
    self.rect = hitbox
    self.pos = pygame.Vector2(self.rect.x,self.rect.y)
    self.vel = pygame.Vector2()
    self.acc = pygame.Vector2()
  
  def update_position(self,dt):
    Physics.CompVelocity(dt,self.acc,self.vel)
    Physics.CompPosition(dt,self.acc,self.vel,self.pos)
  def set_velovity(self,vec):
    self.vel = vec
  def update(self,dt):
    
    self.update_position(dt)
    self.rect.x = self.pos.x
    self.rect.y = self.pos.y
    # print(Physics.VelDirection(self.vel))
    
  
  def render(self,ventana):
    super().render(ventana)

  
  
    
    
       