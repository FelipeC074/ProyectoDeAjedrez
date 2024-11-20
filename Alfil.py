from ClasesYObjetos import Piezas

class Alfil(Piezas):
    def __init__(self, color, posX, posY):
        self.alto = 6
        self.ancho = 5
        super().__init__(color, posX, posY)
    def Moverse(self, tabl, LDePizs):
        ListMovimtos = []
        Terminar = True
        SumatCalcul = 10
        for fila in tabl:
            SumatCalcul += 10
            for i in fila:
             if i.posX - SumatCalcul == self.posX and i.posX - SumatCalcul:
                SubList = [i.posX, i.posY]
                ListMovimtos.append(SubList)
        for i in range(len(ListMovimtos)):
            if ListMovimtos[i].posX == self.posX:
                PosDeAlfil = i
        for i in range(PosDeAlfil, len(ListMovimtos)):
            for Piez in LDePizs:
                if ListMovimtos[i].posX == Piez.posX and ListMovimtos[i].posY == Piez.posY and Terminar:
                    if Piez.color == self.color:
                        Terminar = False
                    else:
                        ListMovimtos[i].Movible = True
                        Terminar = False
                elif Terminar:
                    ListMovimtos[i].Movible = True
        ListMovimtos = []
        Terminar = True
        SumatCalcul = 10
        for fila in tabl:
            SumatCalcul += 10
            for i in fila:
             if i.posX + SumatCalcul == self.posX and i.posX - SumatCalcul:
                SubList = [i.posX, i.posY]
                ListMovimtos.append(SubList)
        for i in range(len(ListMovimtos)):
            if ListMovimtos[i].posX == self.posX:
                PosDeAlfil = i
        for i in range(PosDeAlfil, len(ListMovimtos)):
            for Piez in LDePizs:
                if ListMovimtos[i].posX == Piez.posX and ListMovimtos[i].posY == Piez.posY and Terminar:
                    if Piez.color == self.color:
                        Terminar = False
                    else:
                        ListMovimtos[i].Movible = True
                        Terminar = False
                elif Terminar:
                    ListMovimtos[i].Movible = True
        ListMovimtos = []
        Terminar = True
        SumatCalcul = 10
        for fila in tabl:
            SumatCalcul += 10
            for i in fila:
             if i.posX + SumatCalcul == self.posX and i.posX + SumatCalcul:
                SubList = [i.posX, i.posY]
                ListMovimtos.append(SubList)
        for i in range(len(ListMovimtos)):
            if ListMovimtos[i].posX == self.posX:
                PosDeAlfil = i
        for i in range(PosDeAlfil, len(ListMovimtos)):
            for Piez in LDePizs:
                if ListMovimtos[i].posX == Piez.posX and ListMovimtos[i].posY == Piez.posY and Terminar:
                    if Piez.color == self.color:
                        Terminar = False
                    else:
                        ListMovimtos[i].Movible = True
                        Terminar = False
                elif Terminar:
                    ListMovimtos[i].Movible = True
        ListMovimtos = []
        Terminar = True
        SumatCalcul = 10
        for fila in tabl:
            SumatCalcul += 10
            for i in fila:
             if i.posX - SumatCalcul == self.posX and i.posX + SumatCalcul:
                SubList = [i.posX, i.posY]
                ListMovimtos.append(SubList)
        for i in range(len(ListMovimtos)):
            if ListMovimtos[i].posX == self.posX:
                PosDeAlfil = i
        for i in range(PosDeAlfil, len(ListMovimtos)):
            for Piez in LDePizs:
                if ListMovimtos[i].posX == Piez.posX and ListMovimtos[i].posY == Piez.posY and Terminar:
                    if Piez.color == self.color:
                        Terminar = False
                    else:
                        ListMovimtos[i].Movible = True
                        Terminar = False
                elif Terminar:
                    ListMovimtos[i].Movible = True

