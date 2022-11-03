import pygame
from enum import Enum
import sys
from abc import ABC, abstractmethod

class EventType():
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
    self.MBEvents = {}
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
      if evn.type in EventType.KBEvent:
        pass
      if evn.type in EventType.MBEvent:
        pass
      
      

  def Bindear(self, tipo: EventType=1):
    EventFactory().Create(tipo)

class EventFactory():
  def __init__(self):
    self.objetives = [
      MBEvent
    ]
  def Create(self, id):
    if (id<=0 or id>self.objetives.__len__()): raise Exception()
    return self.objetives[id-1]()
class Event:
  
  _id: str=0
  action:int
  def __init__(self,action):
    self.action = action
  @property
  def id(self): return self.__class__._id

class MBEvent(Event):
  _id = 1
  def __init__(self):
    pass

    
