import pygame

ventana = pygame.display.set_mode((500,500));

pygame.init()

ejecutar = True

while ejecutar:

  for event in pygame.event.get():
    if event.type == pygame.QUIT: ejecutar = False
