import pygame

ventana = pygame.display.set_mode((100,100));

pygame.init()

ejecutar = True

while ejecutar:

  for event in pygame.event.get():
    if event.type == pygame.QUIT: ejecutar = False
