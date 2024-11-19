import Proyecto_PyCurso_Funciones as clases
import tkinter as tk

pantalla = tk.Tk()
Ancho, Alto = 80, 80
Lienzo = tk.Canvas(pantalla, width=Ancho, height=Alto, bg="gray")
Lienzo.pack()

casilla_tamaño = 80
#Bucle Ppal.
def Clic_Hecho(event):
        if clases.Turno_Jugado == 0:
              event.x = clases.redondear(event.x)
              event.y = clases.redondear(event.y)
              for i in clases.ListaDePiezas:
                  if i.posX == event.x and i.posY == event.y:
                      i.Moverse()
                      Pieza = i
                      clases.ListaDePiezas.remove(i)
                      clases.Turno_Jugado += 1
        elif clases.Turno_Jugado == 1:
                event.x = clases.redondear(event.x)
                event.y = clases.redondear(event.y)
                for fila in clases.tablero:
                    for cas in fila:
                        if cas.posX == event.x and cas.posY == event.y and cas.Movible:
                            Pieza = type(Pieza)(Pieza.color, cas.posX, cas.posY)
                            clases.ListaDePiezas.append(Pieza)

def Dibujar():
    Lienzo.delete("all")
    for i in clases.ListaDePiezas:
        i.clases.Tocar_Pieza()
        if i.color and i.Vivo:
            x0 = i.posX * casilla_tamaño
            y0 = i.posY * casilla_tamaño
            x1 = x0 + casilla_tamaño
            y1 = y0 + casilla_tamaño
            Lienzo.create_rectangle(x0,y0, x1, y1, fill = "white")
        elif not i.color and i.Vivo:
            x0 = i.posX * casilla_tamaño
            y0 = i.posY * casilla_tamaño
            x1 = x0 + casilla_tamaño
            y1 = y0 + casilla_tamaño
            Lienzo.create_rectangle(x0, y0, x1, y1, fill= "black")

if not clases.ReyBlanco.Vivo:
        clases.ReyNegro.Terminar()

if not clases.ReyNegro.Vivo:
        clases.ReyBlanco.Terminar()
        

Lienzo.bind("<Button-1>", Clic_Hecho)

pantalla.after(50, Dibujar)

pantalla.mainloop()
