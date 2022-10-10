import pygame
import constantes as c
class Resortera:
  imagen = pygame.image.load(c.img_resortera)
  def __init__(self, pos):
    self.tam = pygame.Vector2(100,100)
    self.imagen = pygame.transform.scale(Resortera.imagen, self.tam)
    self.pos = pygame.Vector2(pos)

  def obtCentro(self):
    return pygame.Vector2(self.pos.x+(self.tam.x/2),self.pos.y+(self.tam.y/2))
  