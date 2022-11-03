import pygame
import math
# from elementos import PhysicElement
from fisicas.constantes import POTENCIA
""""
TODO:

1. Funciones para lanzamiento
2. Colisiones
3. Calculos para rebotes
4. Fluidos
5. 
"""
class Physics():
  def __init__(self):
    pass

  def MParabolico(PE,dt:float):
    PE.vel += PE.acc*dt
    print(PE.vel)
    PE.pos += ((PE.acc/2)*dt*dt)+(PE.vel*dt)
  def VelDirection(PE):
    return math.atan2(PE.vel.y,PE.vel.x)
    
  def CalcPotencia(PE, vector_director:pygame.Vector2):
    PE.vel = POTENCIA*vector_director

  def CalcVecDir(mouse:pygame.Vector2,center:pygame.Vector2):
    return center-mouse