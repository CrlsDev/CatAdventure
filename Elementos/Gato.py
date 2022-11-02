
import pygame
from elementos.element import PhysicElement
from utiles.loader import Loader
L = Loader("./Assets")
L.loadImages()
class Gato(PhysicElement):
  def __init__(self, *grupos):
    print(L.container.check_images("CAT"))
    PhysicElement.__init__(self,(400,400,100,100),L.getImage("CAT"),grupos)
  
  def update(self):
    pass
  

  

    

    