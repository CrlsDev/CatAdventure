import math
import sys
import pygame
from Elementos.Gato import Gato
from fisicas.Arrow import Arrow
import constantes as c
from utiles import loader

loader.inicio()
print(loader.IMGS)
a = Gato()
pygame.init()
ventana = pygame.display.set_mode(c.RESOLUCION);
reloj = pygame.time.Clock()
flecha = Arrow(pygame.Vector2(c.RESOLUCION)/2,length=200)
print(Arrow.__dict__.keys())
def cerrar():
  pygame.quit()
  sys.exit()

ca = False
cm = False
while True:
  dt = reloj.tick(c.FPS)/1000
  # print(dt)
  # if (mouse[0])
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT: cerrar()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        ca = True
      if event.key == pygame.K_DOWN:
        cm = True
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_UP:
        ca = False
      if event.key == pygame.K_DOWN:
        cm = False

  if ca:
    flecha.setAngle(flecha.angle-(math.radians(15)))
  if cm:
    flecha.setLength(flecha.length-5)
  ventana.fill((0,0,0))
  flecha.render_lines(ventana)
  pygame.display.update()
