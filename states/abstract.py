
from pygame import Surface
import utiles
from abc import ABC, abstractmethod
from utiles.loader import Loader
class AbstractState(ABC):
  def __init__(self):
    self.EvnMng = utiles.EventManager()
    self.loader = Loader("./Assets")
    self.loader.loadImages()
  def init(self):
    """
    Este metodo sirve como un constructor secundario para inicializar parametros del estado
    """
  def handle_events(self):
    self.EvnMng.handle()
  
  def update(self,dt):
    pass

  def render(self, ventana:Surface):
    pass