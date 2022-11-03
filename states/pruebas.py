import pygame

from states.abstract import AbstractState
from utiles.grupos import RenderGroup
from elementos.gato import Gato

class TestState(AbstractState):
  renderGroup:RenderGroup
  def __init__(self):
    super().__init__()
    self.g = Gato()
    self.renderGroup = RenderGroup(self.g)

  def initRenderGroup(self,*sprites):
    self.renderGroup.add(*sprites)
  def render(self,ventana:pygame.Surface):
    self.renderGroup.draw(ventana)
    pygame.draw.rect(ventana,(255,0,0),self.g.rect,1)

  def update(self,dt):
    self.renderGroup.update(dt)

