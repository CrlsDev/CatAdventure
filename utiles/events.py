import pygame
from enum import Enum
import sys
class EventTypes():
  KBEvent = [pygame.KEYDOWN, pygame.KEYUP]
  MBEvent = [pygame.MOUSEBUTTONDOWN,pygame.MOUSEBUTTONUP]
  
  def check(evn):
    pass
class PlayerEvent():
  def __init__(self,active = False):
    self.active = active
  def Update(self, evn):
    pass


class EventManager():
  def __init__(self):
    self.eventos = {}
  def cerrar(self):
    pygame.quit()
    sys.exit()
  def Update(self):
    for evn in pygame.event.get():
      if evn.type==pygame.QUIT:
        self.cerrar()
      if evn.type in EventTypes.KBEvent: print("a")

  def Bindear(self, tipo: type):
    pass