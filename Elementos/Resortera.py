import pygame
import constantes as c
class Resortera:
  imagen = pygame.image.load(c.img_resortera)
  def __init__(self, pos):
    self.imagen = pygame.transform.scale(Resortera.imagen, (500,500))
    self.pos = pos