from ClasesYObjetos import Piezas

class Peon(Piezas):
    def __init__(self, color, posX, posY):
        self.alto = 3
        self.ancho = 3
        super().__init__(color,posX,posY)
    def Moverse(self, tabl, LDePizs):
        pass