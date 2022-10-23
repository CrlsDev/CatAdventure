import pygame
import sys

def singleton(cls):
  instanced = dict() 
  def intern(*args, **kwargs):
    if cls not in instanced: 
      instanced[cls] = cls(*args,**kwargs)
    
    return instanced[cls]

  return intern
