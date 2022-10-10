import pygame



class Pajaro:
  def __init__(self, resor):
    self.tam = pygame.Vector2(25,25)
    self.imagen = pygame.Surface(self.tam)
    self.imagen.fill((0,255,0))
    self.resor = resor
    self.pos = pygame.Vector2()
    self.ac = pygame.Vector2(0,100)
    self.v = pygame.Vector2()
  

    

    