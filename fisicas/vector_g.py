from math import *
from elementos.element import Element,PhysicElement
from fisicas.physics import Physics
import pygame

import math
class Arrow(Element):
  points: tuple[pygame.Vector2]
  TIP_VALUES = (8,8)
  def __init__(self,vec=pygame.Vector2(),root=pygame.Vector2(), width=1, scale=1,color=(255,0,255),*grps):
    Element.__init__(self,grps)
    self.root = root
    self.vec = vec
    self.width = width
    self.scale =scale
    self.color = color
    self.font = pygame.font.Font(pygame.font.get_default_font(),int(scale*70))
    self.lines = []
    self.obj = None
  def bind_object(self,obj:PhysicElement):
    self.obj = obj
    return self  
  def update_vec(self):
    self.vec = self.obj.vel
    line:pygame.Vector2 = self.root+(self.vec*self.scale)  

    
    self.lines.append(line)
    
    
  def compDraw(self,ventana):
    
    pygame.draw.lines(ventana,self.color,False,
      self.lines,self.width
    )
  def update(self,dt):
    self.lines.clear()
    self.root = self.obj.rect.center
    self.lines.append(self.root)
    self.update_vec()
  def render(self,ventana:pygame.Surface):
    # super().render(ventana)
    self.compDraw(ventana)
    
    text = self.font.render(f"{round(self.vec.magnitude(),2)}",True,pygame.Vector3(self.color)*0.7)
    # rotation = -Physics.VelDirection(self.vec)
    # if rotation%360>=90 and rotation%360<=270: rotation-=180
    # text = pygame.transform.rotate(text,rotation)
    ventana.blit(text,pygame.Vector2(self.obj.rect.center)+((Physics.UP*self.obj.rect.h/1.5)))

    
    
  
