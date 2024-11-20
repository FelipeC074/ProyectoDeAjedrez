ListaDePiezas =  []
Turno = True
Turno_Jugado = 0

def redondear(pos):  #Para redondear la posición del cursor a las posiciones terminadas en cero donde estaran las piezas y casillas
    pos = float(pos / 10)
    pos += 0.50
    pos //= 1
    pos = int(pos)
    return pos

class Piezas:
    def __init__(self, color, posX, posY):
        self.color = color
        self.posX = posX
        self.posY = posY
        self.Vivo = True
    def Tocar_Pieza(self):    #Si toca una pieza de otro color la pieza se deja de imprimir
        for i in ListaDePiezas:
            if i.posX == self.posX and i.posY == self.posY and self.color != i.color:
                    i.Morir()
    def Morir(self):
        self.Vivo = False
import Rey
import Peon
import Torre
import Alfil
import Reina
import Caballo

class Casilla:
    def __init__(self, color, Par, posX, posY, Movible):
        self.color = color
        self.Par = Par
        self.posX = posX
        self.posY = posY
        self.Movible = Movible
        self.ancho = 10
        self.alto = 10
    def SerMovible(self):
        self.Movible = True

# Creamos todas las piezas 
# Reyes
ReyBlanco = Rey(True, 50, 80)
ReyNegro = Rey(False, 50, 10)

# Reinas
ReinaBlanca = Reina(True, 40, 80)
ReinaNegra = Reina(False, 40, 10)
ListaDePiezas.append(ReinaBlanca)
ListaDePiezas.append(ReinaNegra)

# Alfiles
Alf_BlancoPar = Alfil(True, 60, 80)
Alf_BlancoImpar = Alfil(True, 30, 80)
Alf_NegroPar = Alfil(False, 60, 10)
Alf_NegroImpar = Alfil(False, 30, 10)

ListaDePiezas.append(Alf_BlancoPar)
ListaDePiezas.append(Alf_BlancoImpar)
ListaDePiezas.append(Alf_NegroPar)
ListaDePiezas.append(Alf_NegroImpar )
# Torres
Torre_BlncDecha = Torre(True, 80, 80)
Torre_BlncIzqda = Torre(True, 10, 80)
Torre_NegDecha = Torre(False, 80, 10)
Torre_NegIzqda = Torre(False, 10, 10)

ListaDePiezas.append(Torre_BlncDecha)
ListaDePiezas.append(Torre_BlncIzqda)
ListaDePiezas.append(Torre_BlncDecha)
ListaDePiezas.append(Torre_NegIzqda )
# Caballos
Caballo_BlncDecho = Caballo(True, 70, 80)
Caballo_BlncIzqdo = Caballo(True, 20, 80)
Caballo_NegDecho = Caballo(False, 70, 10)
Caballo_NegIzqdo = Caballo(False, 20, 10)
                     
ListaDePiezas.append(Caballo_BlncDecho)
ListaDePiezas.append(Caballo_BlncIzqdo)
ListaDePiezas.append(Caballo_NegDecho)
ListaDePiezas.append(Caballo_NegIzqdo)
# Peones

# Blancos
Peon_B1 = Peon(True, 10, 70)
Peon_B2 = Peon(True, 20, 70)
Peon_B3 = Peon(True, 30, 70)
Peon_B4 = Peon(True, 40, 70)
Peon_B5 = Peon(True, 50, 70)
Peon_B6 = Peon(True, 60, 70)
Peon_B7 = Peon(True, 70, 70)
Peon_B8 = Peon(True, 80, 70)
                     
ListaDePiezas.append(Peon_B1)
ListaDePiezas.append(Peon_B2)
ListaDePiezas.append(Peon_B3)
ListaDePiezas.append(Peon_B4)
ListaDePiezas.append(Peon_B5)
ListaDePiezas.append(Peon_B6)
ListaDePiezas.append(Peon_B7)
ListaDePiezas.append(Peon_B8)
# Negros
Peon_N1 = Peon(False, 10, 20)
Peon_N2 = Peon(False, 20, 20)
Peon_N3 = Peon(False, 30, 20)
Peon_N4 = Peon(False, 40, 20)
Peon_N5 = Peon(False, 50, 20)
Peon_N6 = Peon(False, 60, 20)
Peon_N7 = Peon(False, 70, 20)
Peon_N8 = Peon(False, 80, 20)
                     
ListaDePiezas.append(Peon_N1)
ListaDePiezas.append(Peon_N2)
ListaDePiezas.append(Peon_N3)
ListaDePiezas.append(Peon_N4)
ListaDePiezas.append(Peon_N5)
ListaDePiezas.append(Peon_N6)
ListaDePiezas.append(Peon_N7)
ListaDePiezas.append(Peon_N8)
ListaDePiezas.append(ReyBlanco)
ListaDePiezas.append(ReyNegro)

# Definimos Las Casillas
tablero = []
for fila in range(1, 9):  # Fila 1 a 8
    fila_casillas = []
    for columna in range(1, 9):  # Columna 1 a 8
        # Alterna el color: True si la casilla es blanca, False si es negra
        color_blanco = (fila + columna) % 2 == 0
        # Calcula las coordenadas X e Y basadas en la columna y fila
        x = columna * 10
        y = fila * 10
        # Crea la casilla y la añade a la fila actual
        casilla = Casilla(color_blanco, not color_blanco, x, y, False)
        fila_casillas.append(casilla)
    tablero.append(fila_casillas)