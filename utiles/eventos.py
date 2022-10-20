import pygame
from enum import Enum

class Evento():
  def __init__(self, fnc):
    self.fnc = fnc
    
class EventoPres(Evento):
  def __init__(self, btn, fnc):
    super().__init__(self,fnc)
    self.btn = btn
    self.mant = False



class EventoTeclado(EventoPres):
  def __init__(self, btn, fnc):
    super().__init__(self,btn,fnc)

class TEventoMouse(Enum):
  PRES = 1
  MOV = 2    

class EventoMouse(Evento):
  def __init__(self, tipos,fnc, btn=None):
    super().__init__(self,fnc)
    self.tipos = tipos
    self.pres = EventoPres(btn, fnc) if TEventoMouse.PRES in self.tipos else None
    self.mov = pygame.Vector2() if TEventoMouse.MOV in self.tipos else None


class MnjEventos():
  TEventos = []
  def __init__(self):
    self.eventos = {}

  def TypeByInt(self, tipo):pass
  
  def Bindear(self, tipo: type):
    if issubclass(tipo,Evento):print("a")
    else: print("b")