
from pygame import Surface
import utiles
from abc import ABC, abstractmethod
class AbstractState(ABC):
  def __init__(self):
    self.EvnMng = utiles.EventManager()
  
  def handle_events(self):
    self.EvnMng.handle()
  
  def update(self):
    pass

  def render(self, ventana:Surface):
    pass