#Esta clase se encarga de la interfaz princiapl del usuario

# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero


#Importacion tkinter
from tkinter import *
import tkinter as tk

#Creacion ventana principal
ventanaMain = tk.Tk()
ventanaMain.title("Inicio")
ventanaMain.geometry("1000x800")

#Seccion p3 - Saludo de bienvenida en la esquina superior derecha
bienvenidaP3 = tk.Label(ventanaMain, text="Bienvenid@ usuari@ a \n Delicia fresca ", width=30, height=10, font=('Helvetica', 14)).grid(row=2, column=0, padx=2, pady=1)

#Seccion p5 - Esquina superior derecha donde estara cada hoja de vida de cada desarrollador

#Funcion para cambiar el texto de las hojas de vida
def mensaje(Evento):
    texto = textoHojaDeVida1.cget("text")
    
    print(texto)
    
    if (texto == "Nombre desarrollador 1"):
        textoHojaDeVida1.config(text="Nombre desarrollador 2")
    if (texto == "Nombre desarrollador 2"):
        textoHojaDeVida1.config(text='Nombre desarrollador 3')
    if (texto == "Nombre desarrollador 3"):
        textoHojaDeVida1.config(text='Nombre desarrollador 1')

#Frame principal 
hojaDeVidap5 = tk.Frame(ventanaMain, bg="#f8f8f8", height=100).place(relx=0.5, rely=0, relheight=0.5, relwidth=0.5)

#Widget principal
textoHojaDeVida1 = tk.Label(hojaDeVidap5, text="Nombre desarrollador 1", bg="#f8f8f8", font=('Helvetica', 14), cursor="hand1")
textoHojaDeVida1.place(relx=0.55, rely=0.27)
textoHojaDeVida1.bind("<Button-1>", mensaje)

textoHojaDeVida2 = tk.Label(hojaDeVidap5, 
                            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nNullam vestibulum mollis urna eget vehicula. \nFusce tempus erat vitae semper egestas. \nQuisque mollis erat leo, sit amet interdum ante eleifend sed.",
                            bg="#f8f8f8", font=('Helvetica', 10), cursor="hand1", justify=tk.LEFT)
textoHojaDeVida2.place(relx=0.55, rely=0.32)
textoHojaDeVida2.bind("<Button-2>", mensaje)



ventanaMain.mainloop()