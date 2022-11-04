import pygame

from states.abstract import AbstractState
from utiles.grupos import RenderGroup
from elementos.gato_cosas import Gato,Cama,CatThing
from elementos.element import ChargeIndicator,Element,ImageElement
from fisicas.physics import Physics
from fisicas.vector_g import Arrow
import constantes as c
class TestState(AbstractState):
  renderGroup:RenderGroup
  def __init__(self,*grps):
    super().__init__()
  def init(self,backgroundRect):
    # self.catThing = 
    self.g = Gato((400,400,60,60),self.loader.getImage("CAT"))
    self.v = Arrow(pygame.Vector2(50,50),width=3,scale=0.4).bind_object(self.g)
    
    cama = self.loader.getImage("CAMA")
    cosa = self.loader.getImage("COSODELGATO")
    self.thing =  CatThing(self.g,(1280-200,720-300,*pygame.Vector2(cosa.get_rect().size)/5),cosa)
    self.bed = Cama(self.g,(30,720-150,*pygame.Vector2(cama.get_rect().size)/5),cama)
    self.ind = ChargeIndicator()
    self.background = ImageElement(backgroundRect,self.loader.getImage("BACKGROUND"))
    self.renderGroup = RenderGroup(self.background,self.bed,self.thing,self.g,self.v)
    self.mouse = [
      False,
      pygame.Vector2()
    ]
    self.EvnMng.Bindear()
    self.mode = 0
    self.dist = 0
    self.pres=50
    self.drawWay = False
  def initRenderGroup(self,*sprites):
    self.renderGroup.add(*sprites)
  def render(self,ventana:pygame.Surface):
    ventana.fill((0,0,0))
    self.renderGroup.draw(ventana)
    if (self.drawWay):
      vel = Physics.CalcPotencia(self.dist)
      acc = pygame.Vector2(0,130)
      pos = pygame.Vector2(self.g.rect.center)
      o_color = pygame.Vector3((200,230,70))
      for i in range(0,self.pres):
        # v2 = acc*dt+vel
        dt=0.3*(50/self.pres)
        color = o_color*(1-(i/50))
        rad_vec = pos
        if rad_vec.x+15>=1280: 
          pos.x = 1280-15
          vel.x*=-0.6
        if rad_vec.x-15<=0: 
          pos.x = 15
          vel.x*=-0.6
        if rad_vec.y+15>=720: 
          pos.y = 720-15
          vel.y*=-0.6
        if rad_vec.y-15<=0: 
          pos.y = 15
          vel.y*=-0.6
        pos = Physics.CompPosition(dt,acc,vel,pos)
        vel = Physics.CompVelocity(dt,acc,vel)  
        
        pygame.draw.circle(ventana,color,pos,10)
        pygame.draw.circle(ventana,(0,0,0),pos,10,4)
    

  def update(self,dt):
    if self.g.vel.magnitude()==0:
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
          
          if self.dist.magnitude()>40: self.drawWay = True
          else: self.drawWay=False
          self.ind.setColor(self.dist.magnitude()/c.RADIO_MAX)
          self.ind.setPos(-self.dist+self.g.rect.center)

          
          

          
        
      else:
        if (self.mode==1):
          pygame.mouse.set_pos(self.ind.pos)
          if self.dist.magnitude()>40: 
            self.g.acc.y=130
            self.g.set_velovity(Physics.CalcPotencia(self.dist))
            self.drawWay=False
          
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
        if evn.key == pygame.K_r: self.reset()
        if evn.key == pygame.K_F1: 
          if self.renderGroup.has(self.v):
            self.renderGroup.remove(self.v)
          else:
            self.renderGroup.add(self.v)

        if evn.key == pygame.K_F2: 
          print(self.pres)
          if self.pres==50: self.pres=30
          else: self.pres = 50
        if evn.key == pygame.K_F3: 
          self.thing.toggle_bind()
            # self.renderGroup.add(self.v)
            # self.renderGroup.has(self.g)
            

  def reset(self):
    self.bed.pos_cat()


