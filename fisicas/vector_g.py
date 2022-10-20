from math import *

import pygame


class Arrow():
  points: tuple[pygame.Vector2]
  TIP_VALUES = (8,8)
  def __init__(self,root=(0,0),angle=0, length=0, width=1, scale=1,color=(255,255,255)):
    self.root = pygame.Vector2(root)
    self.angle = radians(angle)
    self.length = length
    self.width = width
    self.scale = scale
    self.color = color
    self.lines = []

  def new_set(self,root=(0,0),angle=0, length=0, width=1, scale=1,color=(255,255,255)):
    self.root = pygame.Vector2(root)
    self.angle = radians(angle)
    self.length = abs(length)
    self.width = width
    self.scale = scale
    self.color = color
    self.lines = []
    self.update()
  def setRoot(self,root):
    self.root = root
    self.update()
  def setAngle(self,angle):
    self.angle = angle
    self.update()
  def setLength(self,length):
    self.length = abs(length)
    self.update()
  def setWidth(self,width):
    self.width = width
    self.update()
  def setScale(self,scale):
    self.scale = scale
    self.update()
  def setColor(self,color):
    self.color = color
    self.update()


  def update(self):
    self.lines.clear()
    self.compute_unitary()
    self.compute_mainv()
    self.compute_end()
    self.compute_lines()

  def render_lines(self,ventana):
    for i in self.lines:
      pygame.draw.line(ventana,self.color,i[0],i[1],self.scale*self.width)

  def compute_unitary(self):
    self.unitary = self.scale*pygame.Vector2(
      cos(self.angle),
      sin(self.angle)
    )
  def compute_mainv(self):
    self.vec = self.unitary*self.length
  def compute_end(self):
    self.end = self.root+self.vec
  def compute_lines(self):
    self.compute_mainline()
    self.compute_tip()
  
  def compute_mainline(self):
    self.lines.append((self.root,self.end))
  
  def compute_tip(self):

    directriz = self.end-(self.unitary*Arrow.TIP_VALUES[0])
    normal = self.unitary.rotate(90)*Arrow.TIP_VALUES[1]

    self.lines.append(
      (
        directriz+normal,
        self.end
      )
    )
    self.lines.append(
      (
        directriz-normal,
        self.end
      )
    )
  
