import pygame
import os

IMGS = {}
IMGS_ACCEPTED = [".jpg",".png"]


def inicio():
  cargar_imagenes()


def cargar_imagenes():
  
  for img in os.listdir("./Assets"):
    n,e = os.path.splitext(img)
    
    if (e.lower() in IMGS_ACCEPTED):
      IMGS[n] = pygame.image.load(os.path.join("./Assets",img))

