
import pygame
from elementos.element import PhysicElement,ImageElement

from fisicas.physics import Physics

class Gato(PhysicElement,ImageElement):
  def __init__(self,rect,image, *grupos):
    print(rect,image)
    ImageElement.__init__(rect,image,grupos)
    PhysicElement.__init__(self,self.rect,grupos)
    
    self.oimage = self.image
  def update_rotation(self):
    rotation = Physics.VelDirection(self.vel)
    if rotation>=90 and rotation<=270: rotation*=1
    self.image=pygame.transform.rotate(self.oimage,rotation)

  def update(self,dt):
    super().update(dt)
    self.update_rotation()
  
  
    
  

  

    

    