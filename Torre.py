from ClasesYObjetos import Piezas
class Torre(Piezas):
    def __init__(self, color, posX, posY):
        self.alto = 8
        self.ancho = 5
        super().__init__(color, posX, posY)
    def Moverse(self, tabl, LDePizs):
        #Filas
        ListMovimtos = []
        Terminar = True
        for fila in tabl:
            for i in fila:
             if i.posX == self.posX:
                SubList = [i.posX, i.posY]
                ListMovimtos.append(SubList)
        for i in range(len(ListMovimtos)):
            if ListMovimtos[i].posY == self.posY:
                PosDeTorre = i
        for i in range(PosDeTorre, len(ListMovimtos)):
            for Piez in LDePizs:
                if ListMovimtos[i].posX == Piez.posX and ListMovimtos[i].posY == Piez.posY and Terminar:
                    if Piez.color == self.color:
                        Terminar = False
                    else:
                        ListMovimtos[i].Movible = True
                        Terminar = False
                else:
                    ListMovimtos[i].Movible = True
        Terminar = True
        for i in range(PosDeTorre,0, -1):
            for Piez in LDePizs:
                if ListMovimtos[i].posX == Piez.posX and ListMovimtos[i].posY == Piez.posY and Terminar:
                    if Piez.color == self.color:
                        Terminar = False
                    else:
                        ListMovimtos[i].Movible = True
                        Terminar = False
                elif Terminar:
                    ListMovimtos[i].Movible = True
        #Columnas
        ListMovimtos = []
        Terminar = True
        for fila in tabl:
            for i in fila:
             if i.posY == self.posY:
                SubList = [i.posX, i.posY]
                ListMovimtos.append(SubList)
        for i in range(len(ListMovimtos)):
            if ListMovimtos[i].posX == self.posX:
                PosDeTorre = i
        for i in range(PosDeTorre, len(ListMovimtos)):
            for Piez in LDePizs:
                if ListMovimtos[i].posX == Piez.posX and ListMovimtos[i].posY == Piez.posY and Terminar:
                    if Piez.color == self.color:
                        Terminar = False
                    else:
                        ListMovimtos[i].Movible = True
                        Terminar = False
                elif Terminar:
                    ListMovimtos[i].Movible = True
        Terminar = True
        for i in range(PosDeTorre,0, -1):
            for Piez in LDePizs:
                if ListMovimtos[i].posX == Piez.posX and ListMovimtos[i].posY == Piez.posY and Terminar:
                    if Piez.color == self.color:
                        Terminar = False
                    else:
                        ListMovimtos[i].Movible = True
                        Terminar = False
                elif Terminar:
                    ListMovimtos[i].Movible = True