import pygame

ventana = pygame.display.set_mode((1280,720));

pygame.init()

ejecutar = True

fondo = pygame.image.load("./Assets/fondo.jpg")


while ejecutar:

  for event in pygame.event.get():
    if event.type == pygame.QUIT: ejecutar = False
  ventana.blit(fondo,(0,0))

  pygame.display.update()