import pygame
from pygame.sprite import Group

class GrupoRenderizar(Group):
  def __init__(self,*Sprites:pygame.sprite.Sprite):
    super().__init__(Sprites)


class GrupoFisico(GrupoRenderizar):

  def __init__(self,*Sprites:pygame.sprite.Sprite):
    super().__init__(Sprites)