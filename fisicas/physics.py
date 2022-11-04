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
  UP = pygame.Vector2(0,-1)
  DOWN = pygame.Vector2(0,1)
  LEFT = pygame.Vector2(-1,0)
  RIGHT = pygame.Vector2(1,0)
  def __init__(self):
    pass
  def betweenRect(point, rect):
    return (Physics.between(point.x,(rect.x,rect.x+rect.w))
      and Physics.between(point.y,(rect.y,rect.y+rect.h))
    )

  def between(n,r):
    return n>=r[0] and n<=r[1]
  def CompPosition(dt,acc,vel,pos):
    pos += ((acc/2)*dt*dt)+(vel*dt)
    return pos
  def CompVelocity(dt, acc, vel):
    vel += acc*dt
    return vel

  def MParabolico():
    pass
  def getVectorByDir(degrees):
    rad = math.radians(degrees)
    return pygame.Vector2(
      math.cos(rad),
      math.sin(rad)
    )
  def VelDirection(vec):
    return math.degrees(math.atan2(vec.y,vec.x))
    
  def CalcPotencia(dir)->pygame.Vector2:
    return (POTENCIA*dir)

  def CalcVecDir(mouse:pygame.Vector2,center:pygame.Vector2):
    return center-mouse