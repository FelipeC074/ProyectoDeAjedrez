from ClasesYObjetos import Piezas

class Caballo(Piezas):
    def __init__(self, color, posX, posY):
        self.alto = 7
        self.ancho = 4
        super().__init__(color,posX,posY)
    def Moverse(self, tabl, LDePizs):
        for fila in tabl:
            for Cas in fila:
               if Cas.posX == self.posX + 10 and Cas.posY == self.posY + 20:
                   Cas.Movible()
               if Cas.posX == self.posX + 20 and Cas.posY == self.posY + 10:
                   Cas.Movible()
               if Cas.posX == self.posX + 20 and Cas.posY == self.posY - 10:
                   Cas.Movible()
               if Cas.posX == self.posX + 10 and Cas.posY == self.posY - 20:
                   Cas.Movible() 
               if Cas.posX == self.posX -10 and Cas.posY == self.posY - 20:
                   Cas.Movible()
               if Cas.posX == self.posX - 20 and Cas.posY == self.posY - 10:
                   Cas.Movible()
               if Cas.posX == self.posX - 20 and Cas.posY == self.posY +10:
                   Cas.Movible()
               if Cas.posX == self.posX - 10 and Cas.posY == self.posY + 20:
                   Cas.Movible()  
