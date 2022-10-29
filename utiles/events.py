import pygame
from enum import Enum
import sys
from abc import ABC, abstractmethod

class EventTypes():
  KBEvent = [pygame.KEYDOWN, pygame.KEYUP]
  MBEvent = [pygame.MOUSEBUTTONDOWN,pygame.MOUSEBUTTONUP]
  
class AbstractEvent(ABC):
  def __init__(self,active = False):
    self.active = active
  @abstractmethod
  def check(self, evn):
    raise NotImplementedError()


class EventManager():
  KBEvents:dict[AbstractEvent]
  def __init__(self):
    self.KBEvents = {}
    
  def cerrar(self):
    pygame.quit()
    sys.exit()
  
  def handle_quit_events(self,evn):
    if evn.type==pygame.QUIT: self.cerrar()
    
  @staticmethod
  def __handle_dict(evn,events_dict):
    for denv in events_dict:
      denv.check(evn)

  def handle(self):
    for evn in pygame.event.get():
      self.handle_quit_events(evn)
      
      

  def Bindear(self, tipo: type):
    pass