from ClasesYObjetos import Piezas

class Rey(Piezas):
    def __init__(self,color, posX, posY):  
        self.alto = 8
        self.ancho = 8
        super().__init__(color, posX, posY)
    def Terminar(self):  #Imprime en Pantalla quien ganó
        print(f"Ganó el jugador {self.color}")
    def Moverse(self, tabl, LDePizs):
        for fila in tabl:
          for i in fila:
              if i.posX == self.posX - 10:
                  if i.posY == self.posY -10:
                      i.Movible()
                  if i.posY == self.posY:
                      i.Movible()
                  if i.posY == self.posY +10:
                      i.Movible()
              if i.posX == self.posX + 10:
                  if i.posY == self.posY -10:
                      i.Movible()
                  if i.posY == self.posY:
                      i.Movible()
                  if i.posY == self.posY +10:
                      i.Movible()
              if i.posX == self.posX:
                  if i.posY == self.posY -10:
                      i.Movible()
                  if i.posY == self.posY +10:
                      i.Movible()  