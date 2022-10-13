import sys
import pygame
import constantes as c
from Elementos.Resortera import *
from Elementos.Pajaro import *

pygame.init()
ventana = pygame.display.set_mode(c.RESOLUCION);
reloj = pygame.time.Clock()

def cerrar():
  pygame.quit()
  sys.exit()


while True:
  dt = reloj.tick(c.FPS)/1000
  # print(dt)
  # if (mouse[0])
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: cerrar()

  ventana.fill((0,0,0))

  pygame.display.update()