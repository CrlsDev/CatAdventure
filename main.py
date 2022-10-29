from game import *
from states.pruebas import TestState

def main():
  juego = Game(TestState())
  juego.run()



if __name__=="__main__":
  main()