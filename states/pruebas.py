import pygame

from states.abstract import AbstractState
from utiles.grupos import RenderGroup


class TestState(AbstractState):
  renderGroup:RenderGroup
  def __init__(self):
    super().__init__()
    self.renderGroup = RenderGroup()

  def initRenderGroup(self,*sprites):
    self.renderGroup.add(*sprites)
  def render(self,ventana):
    self.renderGroup.draw(ventana)
