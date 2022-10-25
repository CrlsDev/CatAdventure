
import utiles
from abc import ABC, abstractmethod
class AbstractState(ABC):
  def __init__(self):
    self.EvnMng = utiles.EventManager()
  
  def handle_events(self):
    self.EvnMng.Update()
  
  def update(self):
    pass

  def render(self):
    pass