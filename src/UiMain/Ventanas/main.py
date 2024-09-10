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
from tkinter import messagebox

#Creacion ventana
ventanaMain = tk.Tk()
ventanaMain.geometry('600x600')
ventanaMain.title('Inicio')

#Funciones Eventos

#Evento click  - Cambio hoja de vida
def mensaje(Evento):
    texto = hojaDeVida.cget("text")

    if (texto == "Valentina Luján Robledo" or texto == "Descripcion de Proyecto"):
        hojaDeVida.config(text="Sebastian Estrada Villa")
        hojaDeVida2.config(text="Estudio Ingeniería de Sistemas \ne Informática \nMe gusta el deporte, la música  \ny los acertijos.")

        imagen1 = tk.PhotoImage(file="../imagenes/sebastian1.png")
        labelImagen1.config(image=imagen1)

        imagen2 = tk.PhotoImage(file="../imagenes/sebastian2.png")
        labelImagen2.config(image=imagen2)

        imagen3 = tk.PhotoImage(file="../imagenes/sebastian3.png")
        labelImagen3.config(image=imagen3)

        imagen4 = tk.PhotoImage(file="../imagenes/sebastian4.png")
        labelImagen4.config(image=imagen4)



    if (texto == "Sebastian Estrada Villa"):
        hojaDeVida.config(text='Nombre desarrollador 3')
        hojaDeVida2.config(text="Texto2 Texto2 Texto2 Texto2 Texto2 \nTexto2 Texto2 Texto2 Texto2 Texto2 \nTexto2 Texto2 Texto2")
    if (texto == "Nombre desarrollador 3"):
        hojaDeVida.config(text='Valentina Luján Robledo')
        hojaDeVida2.config(text="Estudio Ingeniería de Sistemas \ne Informática \nMe gusta la música, bailar y \naprender cosas nuevas ")


#Funcion para crear una nueva ventana y cerra la anterior

def nueva_ventana():
    ventanaMain.withdraw()
    ventana2.deiconify()

def descripcion_proyecto():
    hojaDeVida.config(text='Descripcion de Proyecto')
    hojaDeVida2.config(text="Text Text Text Text Text \nText Text Text Text Text \nText Text Text")

def cambiarImagen(Event):
    imagen2 = tk.PhotoImage(file="../imagenes/valentina1.png")
    labelImagenSistema.config(image=imagen2)


#Frame 1 - Parte izquierda de la pantalla
frame1 = tk.Frame(ventanaMain, bg="white", width=300, height=600, borderwidth=2, relief="sunken")
frame1.pack(side="left", fill="y")

subFrame1_1 = tk.Frame(frame1, bg="white")
subFrame1_1.place(relx=0.05, rely=0.05, relheight=0.20, relwidth=0.9)

saludoBienvenida = tk.Label(subFrame1_1, font=("Helvetica", 12), text="Bienvenido a Delicia Fresca", bg="white", borderwidth=2, relief="sunken")
saludoBienvenida.place(x=30, y=50)

#Subframe 1 Frame parte derecha Boton para avanzar a la siguiente ventana

subFrame1_2 = tk.Frame(frame1, bg="white")
subFrame1_2.place(relx=0.05, rely=0.35, relheight=0.60, relwidth=0.9)

siguienteVentana = tk.Button(subFrame1_2, text="Nueva ventana", command=nueva_ventana)
siguienteVentana.place(relx=0.05, rely=0.7, relheight=0.15, relwidth=0.9)

imagenSistema = tk.PhotoImage(file="../imagenes/valentina1.png")
labelImagenSistema = tk.Label(subFrame1_2, image=imagenSistema, width=125, height=125)
labelImagenSistema.place(relx=0.1, rely=0.05, relheight=0.4, relwidth=0.8)
labelImagenSistema.bind("<Leave>", cambiarImagen)



#Frame 2 - Parte derecha de la ventana
frame2 = tk.Frame(ventanaMain, bg="white", width=300, height=600, borderwidth=2, relief="sunken")
frame2.pack(side="right", fill="y")

subFrame2_1 = tk.Frame(frame2, bg="white")
subFrame2_1.place(relx=0.05, rely=0.05, relheight=0.25, relwidth=0.9)


hojaDeVida = tk.Label(subFrame2_1, bg="white",text="Valentina Luján Robledo", font=("Helvetica", 14))
hojaDeVida.place(x=30, y=10)

hojaDeVida.bind("<Button-1>", mensaje)

hojaDeVida2 = tk.Label(subFrame2_1, bg="white", text="Estudio Ingeniería de Sistemas \ne Informática \nMe gusta la música, bailar y \naprender cosas nuevas ", font=("Arial", 10), justify="left")
hojaDeVida2.place(x=30, y=50)
hojaDeVida.bind("<Button-1>", mensaje)





subFrame2_2 = tk.Frame(frame2, bg="white")
subFrame2_2.place(relx=0.05, rely=0.35, relheight=0.60, relwidth=0.9)

imagen1 = tk.PhotoImage(file="../imagenes/valentina1.png")
labelImagen1 = tk.Label(subFrame2_2, image=imagen1, width=125, height=125)
labelImagen1.grid(row=0, column=0, padx=1, pady=1)

imagen2 = tk.PhotoImage(file="../imagenes/valentina2.png")
labelImagen2 = tk.Label(subFrame2_2, image=imagen2, width=125, height=125)
labelImagen2.grid(row=0, column=1, padx=1, pady=1)

imagen3 = tk.PhotoImage(file="../imagenes/valentina3.png")
labelImagen3 = tk.Label(subFrame2_2, image=imagen3, width=125, height=125)
labelImagen3.grid(row=1, column=0, padx=1, pady=1)

imagen4 = tk.PhotoImage(file="../imagenes/valentina4.png")
labelImagen4 = tk.Label(subFrame2_2, image=imagen4, width=125, height=125)
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



ventana2 = tk.Tk()
ventana2.geometry('1000x500')
ventana2.title('Delicia Fresca')

def ventana2Info():
    messagebox.showinfo("Delicia Fresca", "¡Hola, esta es una ventana emergente!")

def ventanaPrincipal():
    ventana2.withdraw()
    ventanaMain.deiconify()

def acercaDeFunction():
    messagebox.showinfo("Delicia Fresca", "¡Hola, esta es una ventana emergente!")



menu2 = Menu(ventana2)
ventana2.config(menu=menu2)

file_menu = Menu(menu2, tearoff=0)
file_menu.add_command(label="Aplicacion", command=ventana2Info)
file_menu.add_command(label="Salir", command=ventanaPrincipal)

menu2.add_cascade(
    label="Archivo",
    menu=file_menu
)

file_menu2 = Menu(menu2, tearoff=0)
file_menu2.add_command(label="Funcionalidad 1", command=ventana2Info)
file_menu2.add_command(label="Funcionalidad 2", command=ventanaPrincipal)
file_menu2.add_command(label="Funcionalidad 3", command=ventanaPrincipal)
file_menu2.add_command(label="Funcionalidad 4", command=ventanaPrincipal)
file_menu2.add_command(label="Funcionalidad 5", command=ventanaPrincipal)

menu2.add_cascade(
    label="Procesos y consultas",
    menu=file_menu2
)

file_menu3 = Menu(menu2, tearoff=0)
file_menu3.add_command(label="Acerca de:", command=acercaDeFunction)

menu2.add_cascade(
    label="Ayuda",
    menu=file_menu3
)

ventana2frame1 = tk.Frame(ventana2, bg="white", width=300, height=600, borderwidth=2, relief="sunken")
ventana2frame1.place(x=100, y=20, height=200, width=800)

ventana2subframe1 = tk.Frame(ventana2frame1, bg="white")
ventana2subframe1.place(relx=0.05, rely=0.05, relheight=0.25, relwidth=0.9)

nombreDelProceso = tk.Label(ventana2subframe1, text="Nombre del proceso")
nombreDelProceso.place(relx=0.05, rely=0.1, relheight=1, relwidth=0.9)

ventana2subframe2 = tk.Frame(ventana2frame1, bg="white")
ventana2subframe2.place(x=50, y=70, height=100, width=700)

descripcionProceso = tk.Label(ventana2subframe2, text="Descripcion del Proceso del detalle de la consulta", font=("Arial", 15))
descripcionProceso.place(relx=0.05, rely=0.1, relheight=1, relwidth=0.9)


#Interfaz Funcionalidad

ventana2funcionalidad = tk.Frame(ventana2, bg="white")
ventana2funcionalidad.place(x=100, y=250, height=200, width=800)



ventana2.withdraw()


ventanaMain.mainloop()



