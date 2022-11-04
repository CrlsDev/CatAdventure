
import pygame
from elementos.element import PhysicElement,ImageElement

from fisicas.physics import Physics

class Gato(PhysicElement,ImageElement):
  def __init__(self,rect,image, *grupos):
    ImageElement.__init__(self,rect,image,grupos)
    PhysicElement.__init__(self,grupos)
    
    self.oimage = self.image
  def update_rotation(self):
    rotation = Physics.VelDirection(self.vel)
    
    if rotation%360>=90 and rotation%360<=270: rotation-=180
    self.image=pygame.transform.rotate(self.oimage,-rotation)
  def update_bounds(self):
    if self.pos.x+self.rect.w>=1280:
      self.pos.x = 1280-(self.rect.w+5)
      self.vel.x*=-0.6
    if self.pos.y+self.rect.h>=720:
      self.pos.y = 720-(self.rect.h+5)
      self.vel.y*=-0.6
    if self.pos.x<=0:
      self.pos.x = 4
      self.vel.x*=-0.6
    if self.pos.y<=0:
      self.pos.y=4
      self.vel.y*=-0.6

  def update(self,dt):
    super().update(dt)
    self.update_rotation()
    self.update_bounds()

class Cama(ImageElement):
  def __init__(self,cat:Gato,rect,image, *grupos):
    ImageElement.__init__(self,rect,image,grupos)
    self.cat = cat
    self.pos_cat()
  
  def pos_cat(self):
    self.cat.acc = pygame.Vector2()
    self.cat.vel = pygame.Vector2()
    self.cat.set_position(
      pygame.Vector2(self.rect.center[0]-(self.cat.rect.w/2),
      self.rect.center[1]-(self.cat.rect.h/2))
    )
    
  def render(self,ventana):
    super().render(ventana)
  
class CatThing(Cama):
  def __init__(self,cat:Gato,rect,image, *grupos):
    ImageElement.__init__(self,rect,image,grupos)
    self.cat = cat
    self.pos_cat()
    self.positioned = False
    self.bind = True
  def toggle_bind(self):
    self.bind = not self.bind
  def update(self,dt):
    if self.rect.colliderect(self.cat.rect) and self.bind:
      if not self.positioned:self.pos_cat()
      self.positioned = True
    else: self.positioned = False

      
    
  def render(self,ventana):
    super().render(ventana)
     
  

  

    

    