gimport sys
import pygame
import constantes as c
from Elementos.Resortera import *
from Elementos.Pajaro import *

ventana = pygame.display.set_mode(c.RESOLUCION);

pygame.init()

reloj = pygame.time.Clock()

resort = Resortera((150,400))
paj = Pajaro(resort)
tirando = False
disparo = False
lanzamiento = False

dir = None
dist = None

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
  p_mouse = pygame.Vector2(pygame.mouse.get_pos())
  if (not tirando and not disparo):
    if (p_mouse.x>resort.pos.x and p_mouse.x<resort.pos.x+resort.tam.x and p_mouse.y>resort.pos.y and p_mouse.y<resort.pos.y+resort.tam.y): 
      if (b_mouse[0]):
          tirando = True
  elif not b_mouse[0]: 
    
    disparo = True
    


  
  
  if (tirando): 
    centro = resort.obtCentro()
    v_dist = centro-p_mouse
    dist = v_dist.magnitude()
    if dist==0:
      dir = pygame.Vecto2()
    else: dir = v_dist.normalize()
    
    if (dist>=c.RADIO_MAX): 
      dist = c.RADIO_MAX
      v_dist = dir*c.RADIO_MAX

    paj.pos = (resort.obtCentro()-v_dist)-pygame.Vector2(12.5,12.5)
    if (disparo):
      lanzamiento = True
      tirando = False
      paj.v = c.P*dir*dist
    
  if lanzamiento:
    paj.v+=(paj.ac*dt)
    
    paj.pos += ((1/2)*paj.ac*(dt*dt))+(paj.v*dt)





  ventana.fill((0,0,0))
  ventana.blit(resort.imagen,resort.pos)
  ventana.blit(paj.imagen,paj.pos)

  pygame.display.update()