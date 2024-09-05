# Este módulo pertenece al paquete 'UIMain' y contiene clases relacionadas con la interfaces de usuario y las funcionalidades
# Incluye la clase 'Main' que representa la interfaz y las interacciones en la aplicacion
# y métodos para su manipulación. 
#  
# Esta clase representa la interfaz de la aplicacion para la interaccion con  el usuario
#  
#
from dataclasses import field
# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero


#Importacion tkinter
from tkinter import *
import tkinter as tk

#Creacion ventana
ventanaMain = tk.Tk()
ventanaMain.geometry('600x600')
ventanaMain.title('Inicio')

#Funciones Eventos

#Evento click  - Cambio hoja de vida
def mensaje(Evento):
    texto = hojaDeVida.cget("text")

    if (texto == "Nombre desarrollador" or texto == "Descripcion de Proyecto"):
        hojaDeVida.config(text="Nombre desarrollador 2")
        hojaDeVida2.config(text="Texto1 Texto1 Texto1 Texto1 Texto1 \nTexto1 Texto1 Texto1 Texto1 Texto1 \nTexto1 Texto1 Texto1")
    if (texto == "Nombre desarrollador 2"):
        hojaDeVida.config(text='Nombre desarrollador 3')
        hojaDeVida2.config(text="Texto2 Texto2 Texto2 Texto2 Texto2 \nTexto2 Texto2 Texto2 Texto2 Texto2 \nTexto2 Texto2 Texto2")
    if (texto == "Nombre desarrollador 3"):
        hojaDeVida.config(text='Nombre desarrollador')
        hojaDeVida2.config(text="Texto Texto Texto Texto Texto \nTexto Texto Texto Texto Texto \nTexto Texto Texto")

#Frame 1 - Parte izquierda de la pantalla
frame1 = tk.Frame(ventanaMain, bg="white", width=300, height=600, borderwidth=2, relief="sunken")
frame1.pack(side="left", fill="y")

saludoBienvenida = tk.Label(frame1, font=("Helvetica", 12), text="Bienvenido a Delicia Fresca", bg="white", borderwidth=2, relief="sunken")
saludoBienvenida.place(x=50, y=100)

#Frame 2 - Parte derecha de la ventana
frame2 = tk.Frame(ventanaMain, bg="white", width=300, height=600, borderwidth=2, relief="sunken")
frame2.pack(side="right", fill="y")

hojaDeVida = tk.Label(frame2, bg="white",text="Nombre desarrollador", font=("Helvetica", 14))
hojaDeVida.place(x=50, y=50)

hojaDeVida.bind("<Button-1>", mensaje)

hojaDeVida2 = tk.Label(frame2, bg="white", text="Texto Texto Texto Texto Texto \nTexto Texto Texto Texto Texto \nTexto Texto Texto", font=("Helvetica", 10), justify="left")
hojaDeVida2.place(x=50, y=100)
hojaDeVida.bind("<Button-1>", mensaje)

subFrame2 = tk.Frame(frame2, bg="white")
subFrame2.place(relx=0.05, rely=0.35, relheight=0.60, relwidth=0.9)

# imagen1 = tk.PhotoImage(file=" imagenes/gato.jpg")


menubar = Menu(ventanaMain)
ventanaMain.config(menu=menubar)

def descripcion_proyecto():
    hojaDeVida.config(text='Descripcion de Proyecto')
    hojaDeVida2.config(text="Text Text Text Text Text \nText Text Text Text Text \nText Text Text")

file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Salir", command=ventanaMain.quit)
file_menu.add_command(label="Descripcion del Proyecto",
                      command=descripcion_proyecto)
menubar.add_cascade(
    label="Menu",
    menu=file_menu
)


ventanaMain.mainloop()


