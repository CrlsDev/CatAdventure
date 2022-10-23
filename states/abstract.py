
import utiles

class AbstractState():
  def __init__(self):
    self.EvnMng = utiles.EventManager()

  def handle_events(self):
    pass

  def update(self):
    pass

  def render(self):
    pass