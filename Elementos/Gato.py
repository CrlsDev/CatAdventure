
import pygame
from elementos.element import PhysicElement
from utiles.loader import Loader
L = Loader("./Assets")
L.loadImages()
class Gato(PhysicElement):
  def __init__(self, *grupos):
    PhysicElement.__init__(self,(400,400,100,100),L.getImage("CAT"),grupos)
    # self.acc.y=10
    # self.vel.x = 10
  def update(self,dt):
    super().update(dt)
  
  
    
  

  

    

    