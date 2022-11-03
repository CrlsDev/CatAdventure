import math
import sys
import pygame
from elementos import *
from states import *
import constantes as c
from metodos import *
from utiles import *



@singleton
class Game():
  estado: None
  def __init__(self,state):
    self.ventana = pygame.display.set_mode(c.RESOLUCION);
    self.reloj = pygame.time.Clock()
    self.state:AbstractState = state
  def run(self):
    pygame.init()
    self.state.init(self.ventana.get_rect())
       
    self.game_loop()  
  def game_loop(self):
    while True:
      dt = self.reloj.tick(c.FPS)/1000
      # print(dt)
      # if (mouse[0])
      self.state.handle_events()
      self.state.update(dt)
      self.state.render(self.ventana)
      pygame.display.update()

    

a = EventManager()
