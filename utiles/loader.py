import pygame
import os
from enum import Enum

ats = ["images","sounds","fonts","music"]

class Admited():
  IMG = [".png",".jpg"]

class AssetsContainer():
  def __init__(self):
    for at in ats:
      self.__setattr__(at,{})
      self.__create_check_function(at)
  
  def check(self,key):
    return key in self.__dict__.keys()
  def __create_check_function(self,objetive):
    self.__setattr__(f"check_{objetive}",lambda key: key in self.__dict__[str(objetive)].keys())
  def __repr__(self) -> str:
    return str(self.__dict__)
  
  def __str__(self) -> str:
    return self.__repr__()

class Loader():
  
  def __init__(self,assets_dir):
    self.assets_dir = assets_dir
    self.container = AssetsContainer()

    
  def getImage(self,image:str):
    if self.container.check_images(image):
      return self.container.images[image]
  def __getDir(self,key):
    return os.path.join(self.assets_dir,key)

  def loadAll(self):
    self.loadImages()
    self.loadAudios()
    self.loadFonts()

  def loadImages(self):
    self.__load(ats[0],Admited.IMG)
  def loadAudios(self):
    self.__load(self.sounds)
  def loadFonts(self):
    self.__load(self.fonts)

  def __load(self,key,admited=None,forced = False):
    container = self.container.__getattribute__(key)
    dir = self.__getDir(key)
    for asset in os.listdir(dir):
      n,e = os.path.splitext(asset)
      if ((e.lower() in admited or admited is None) and (not self.container.check(n) or forced)):
        container[n] = pygame.image.load(os.path.join(dir,asset)).convert_alpha()


