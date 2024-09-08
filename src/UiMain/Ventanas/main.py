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

#Funcion para crear una nueva ventana y cerra la anterior

def nueva_ventana():
    ventanaMain.destroy()

    ventanaMenu = tk.Tk()
    ventanaMenu.geometry('600x600')
    ventanaMenu.title('Delicia Fresca')
    ventanaMenu.mainloop()

def descripcion_proyecto():
    hojaDeVida.config(text='Descripcion de Proyecto')
    hojaDeVida2.config(text="Text Text Text Text Text \nText Text Text Text Text \nText Text Text")


#Frame 1 - Parte izquierda de la pantalla
frame1 = tk.Frame(ventanaMain, bg="white", width=300, height=600, borderwidth=2, relief="sunken")
frame1.pack(side="left", fill="y")

saludoBienvenida = tk.Label(frame1, font=("Helvetica", 12), text="Bienvenido a Delicia Fresca", bg="white", borderwidth=2, relief="sunken")
saludoBienvenida.place(x=50, y=100)

#Subframe 1 Frame parte derecha Boton para avanzar a la siguiente ventana
siguienteVentana = tk.Button(frame1, text="Hola", command=nueva_ventana)
siguienteVentana.place(relx=0.05, rely=0.5, relheight=0.20, relwidth=0.3)

imagenSistema = tk.PhotoImage(file="imagenes/gato.png")
labelImagenSistema = tk.Label(frame1, image=imagenSistema, width=125, height=125)
labelImagenSistema.place(relx=0.05, rely=0.5, relheight=0.20, relwidth=0.3)






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

imagen1 = tk.PhotoImage(file="imagenes/gato.png")
labelImagen1 = tk.Label(subFrame2, image=imagen1, width=125, height=125)
labelImagen1.grid(row=0, column=0, padx=1, pady=1)

imagen2 = tk.PhotoImage(file="imagenes/blanco.png")
labelImagen2 = tk.Label(subFrame2, image=imagen2, width=125, height=125)
labelImagen2.grid(row=0, column=1, padx=1, pady=1)

imagen3 = tk.PhotoImage(file="imagenes/blanco.png")
labelImagen3 = tk.Label(subFrame2, image=imagen3, width=125, height=125)
labelImagen3.grid(row=1, column=0, padx=1, pady=1)

imagen4 = tk.PhotoImage(file="imagenes/gato.png")
labelImagen4 = tk.Label(subFrame2, image=imagen4, width=125, height=125)
labelImagen4.grid(row=1, column=1, padx=1, pady=1)







menubar = Menu(ventanaMain)
ventanaMain.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Salir", command=ventanaMain.quit)
file_menu.add_command(label="Descripcion del Proyecto",
                      command=descripcion_proyecto)
menubar.add_cascade(
    label="Menu",
    menu=file_menu
)

ventanaMain.mainloop()



