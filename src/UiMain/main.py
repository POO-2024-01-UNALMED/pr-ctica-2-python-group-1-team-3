# Este módulo pertenece al paquete 'UIMain' y contiene clases relacionadas con la interfaces de usuario y las funcionalidades
# Incluye la clase 'Main' que representa la interfaz y las interacciones en la aplicacion
# y métodos para su manipulación. 
#  
# Esta clase representa la interfaz de la aplicacion para la interaccion con  el usuario
#  
# 

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

# Seccion p6 - Seccion donde  deben estar 4 imagenes de cada desarrollador usando el posicionamiento grid
# imagenDesarrollador1 = tk.PhotoImage(file='/images/OIP.jfif')
# tk.Label(ventanaMain, image=imagenDesarrollador1).pack()

#Seccion p5


#Boton para entrar al menu de la apliacacion
def open_new_window():
    # Crear una nueva ventana
    new_window = tk.Toplevel(ventanaMain)
    new_window.title("Nueva Ventana")
    
    # Configurar el tamaño de la nueva ventana
    new_window.geometry("300x200")
    
    # Añadir un mensaje a la nueva ventana
    label = tk.Label(new_window, text="¡Esta es una nueva ventana!")
    label.pack(pady=20)

botonMenu = tk.Button(ventanaMain, text="Abrir Nueva Ventana", command=open_new_window).place(x=50, y=500, height=50, width=150)

ventanaMain.mainloop()