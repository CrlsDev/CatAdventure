import math
import sys
import pygame
from elementos import * 
import constantes as c
from metodos import *

pygame.init()
ventana = pygame.display.set_mode(c.RESOLUCION);
reloj = pygame.time.Clock()

while True:
  dt = reloj.tick(c.FPS)/1000
  # print(dt)
  # if (mouse[0])
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: cerrar()
    if event.type == pygame.MOUSEMOTION:
      pass

  ventana.fill((0,0,0))
  pygame.display.update()
