import pygame

from states.abstract import AbstractState
from utiles.grupos import RenderGroup
from elementos.gato import Gato
from elementos.element import ChargeIndicator,Element,ImageElement
from fisicas.physics import Physics
import constantes as c
class TestState(AbstractState):
  renderGroup:RenderGroup
  def __init__(self):
    super().__init__()
  def init(self,backgroundRect):
    self.g = Gato((400,400,25,25),self.loader.getImage("CAT"))
    self.ind = ChargeIndicator()
    self.background = ImageElement(backgroundRect,self.loader.getImage("BACKGROUND"))
    self.renderGroup = RenderGroup(self.background,self.g)
    self.mouse = [
      False,
      pygame.Vector2()
    ]
    self.EvnMng.Bindear()
    self.mode = 0
    self.dist = 0
  def initRenderGroup(self,*sprites):
    self.renderGroup.add(*sprites)
  def render(self,ventana:pygame.Surface):
    ventana.fill((0,0,0))
    ventana.blit(self.background,(0,0))
    self.renderGroup.draw(ventana)

  def update(self,dt):
    if (self.mouse[0]):
      
      self.mouse[1] = pygame.Vector2(pygame.mouse.get_pos())

      if (self.mode==0 and Physics.betweenRect(self.mouse[1],self.g.rect)):
        self.renderGroup.add(self.ind)
        pygame.event.set_grab(True)
        pygame.mouse.set_visible(not self.mouse[0])
        self.mode=1
      if (self.mode==1):
        self.dist = Physics.CalcVecDir(self.mouse[1],self.g.rect.center)
        if (self.dist.magnitude()>=c.RADIO_MAX):
          self.dist = self.dist.normalize()*c.RADIO_MAX

        self.ind.setColor(self.dist.magnitude()/c.RADIO_MAX)
        self.ind.setPos(-self.dist+self.g.rect.center)

        
      
    else:
      if (self.mode==1):
        self.g.acc.y=140
        if self.dist.magnitude()>0: self.g.set_velovity(Physics.CalcPotencia(self.dist))
        print(self.dist)
        self.mode=0


    
    self.renderGroup.update(dt)
  def updateMouse(self,evn):
    if (evn.type == pygame.MOUSEBUTTONDOWN):
      self.mouse[0]=True

    elif (evn.type == pygame.MOUSEBUTTONUP or True):
      self.color = [0,0,0]
      self.mouse[0]=False
      pygame.event.set_grab(False)
      self.renderGroup.remove(self.ind)
      pygame.mouse.set_visible(not self.mouse[0])
    

  def handle_events(self):
    for evn in pygame.event.get():
      self.EvnMng.handle_quit_events(evn)
      if evn.type==pygame.MOUSEBUTTONDOWN or evn.type==pygame.MOUSEBUTTONUP:
        
        self.updateMouse(evn)
      if evn.type==pygame.KEYDOWN:
        self.reset()


