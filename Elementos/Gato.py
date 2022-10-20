
import pygame
from elementos.sujeto import SujetoFisico
from utiles import loader

class Gato(SujetoFisico):
  def __init__(self, *grupos):
    SujetoFisico.__init__(self,(0,0,25,25),loader.IMGS["CAT"],grupos)
    
  

    

    