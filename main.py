import sys
import pygame
import constantes as c
import Elementos.Resortera

ventana = pygame.display.set_mode(c.RESOLUCION);

pygame.init()

reloj = pygame.time.Clock()

resortera = Elementos.Resortera.Resortera((0,220))

def cerrar():
  pygame.quit()
  sys.exit()

while True:
  dt = reloj.tick(c.FPS)/1000
  # print(dt)
  # if (mouse[0])
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: cerrar()
  
  b_mouse = pygame.mouse.get_pressed()
  p_mouse = pygame.mouse.get_pos()

  ventana.blit(resortera.imagen,resortera.pos)

  pygame.display.update()