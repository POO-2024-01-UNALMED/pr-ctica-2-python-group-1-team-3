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
from tkinter import messagebox
from PIL import Image, ImageTk  # Para redimensionar imágenes
from pathlib import Path

#Importacion de clases
from UiMain.Ventanas.VentanaPrincipal import VentanaPrincipal
from baseDatos.Serializador import Serializador

#Rutas de las imagenes
directorio_script = Path(__file__).parent

ruta_tienda = directorio_script / "imagenes" / "tienda.png"
ruta_carrito = directorio_script / "imagenes" / "carrito.png"
ruta_precio = directorio_script / "imagenes" / "precio.png"
ruta_cajera = directorio_script / "imagenes" / "cajera.png"
ruta_productos = directorio_script / "imagenes" / "productos.png"
ruta_sebastian1 = directorio_script / "imagenes" / "sebastian1.png"
ruta_sebastian2 = directorio_script / "imagenes" / "sebastian2.png"
ruta_sebastian3 = directorio_script / "imagenes" / "sebastian3.png"
ruta_sebastian4 = directorio_script / "imagenes" / "sebastian4.png"
ruta_valentina1 = directorio_script / "imagenes" / "valentina1.png"
ruta_valentina2 = directorio_script / "imagenes" / "valentina2.png"
ruta_valentina3 = directorio_script / "imagenes" / "valentina3.png"
ruta_valentina4 = directorio_script / "imagenes" / "valentina4.png"


#Creacion ventana
ventanaMain = tk.Tk()
ventanaMain.title('Inicio - Delicia Fresca')

# Ajustar ventana principal al tamaño de la pantalla
ventanaMain.state('zoomed')

# Redimensiona imágenes
def redimensionar_imagen(ruta_imagen, ancho, alto):
    img = Image.open(ruta_imagen)
    img = img.resize((ancho, alto), Image.LANCZOS)
    return ImageTk.PhotoImage(img)


#Funciones Eventos
#Evento click  - Cambio hoja de vida
def mensaje(Evento):
    texto = hojaDeVida.cget("text")

    if texto == "Valentina Luján Robledo" or texto == "Descripcion de Proyecto":
        hojaDeVida.config(text="Sebastian Estrada Villa", anchor="center")
        hojaDeVida2.config(text="Estudio Ingeniería de Sistemas e Informática \n\nMe gusta el deporte, la música y los acertijos.", anchor="center")

        # Redimensionar las imágenes antes de asignarlas
        global imagen1v
        imagen1v = redimensionar_imagen(ruta_sebastian1, 200, 200)
        labelImagen1.config(image=imagen1v)

        global imagen2v
        imagen2v = redimensionar_imagen(ruta_sebastian2, 200, 200)
        labelImagen2.config(image=imagen2v)

        global imagen3v
        imagen3v = redimensionar_imagen(ruta_sebastian3, 200, 200)
        labelImagen3.config(image=imagen3v)

        global imagen4v
        imagen4v = redimensionar_imagen(ruta_sebastian4, 200, 200)
        labelImagen4.config(image=imagen4v)

    elif texto == "Sebastian Estrada Villa":
        hojaDeVida.config(text='Santiago Ochoa Quintero', anchor="center")
        hojaDeVida2.config(text="Texto2 Texto2 Texto2 Texto2 Texto2 \n\nTexto2 Texto2 Texto2 Texto2 Texto2 \nTexto2 Texto2 Texto2", anchor="center")

    elif texto == "Santiago Ochoa Quintero":
        hojaDeVida.config(text='Valentina Luján Robledo', anchor="center")
        hojaDeVida2.config(text="Estudio Ingeniería de Sistemas e Informática \n\nMe gusta la música, bailar y aprender cosas nuevas", anchor="center")

        global imagen1s
        imagen1s = redimensionar_imagen(ruta_valentina1, 200, 200)
        labelImagen1.config(image=imagen1s)

        global imagen2s
        imagen2s = redimensionar_imagen(ruta_valentina2, 200, 200)
        labelImagen2.config(image=imagen2s)

        global imagen3s
        imagen3s = redimensionar_imagen(ruta_valentina3, 200, 200)
        labelImagen3.config(image=imagen3s)

        global imagen4s
        imagen4s = redimensionar_imagen(ruta_valentina4, 200, 200)
        labelImagen4.config(image=imagen4s)


#Funcion para crear una nueva ventana y cerra la anterior
def nueva_ventana():
    ventanaMain.withdraw()
    #Deserializador.deserializar() # Para cargar los objetos serializados
    ventana2 = VentanaPrincipal()  # Crea una instancia de la ventana principal
    ventana2.deiconify()

def descripcion_proyecto():
    hojaDeVida.config(text='Descripcion de Proyecto')
    hojaDeVida2.config(text="""Delicia fresca es un supermercado que se encarga de ofrecer 
productos de la mejor calidad.
Este programa nos permite llevar el control de todos los 
procesos necesarios para la correcta administración del 
supermercado.""", anchor="center")


rutasImagenesSistema = [
    ruta_carrito,
    ruta_productos,
    ruta_cajera,
    ruta_precio,
    ruta_tienda
]

image_index = 0

def cambiarImagen(Event):
    global imagenSistema, image_index
    image_index = (image_index + 1) % len(rutasImagenesSistema)
    img = tk.PhotoImage(file=rutasImagenesSistema[image_index])  # Cargar la nueva imagen
    labelImagenSistema.config(image=img)
    labelImagenSistema.image = img


def salir_y_guardar():
        """Guarda los datos y sale de la aplicación."""
        Serializador.serializar()
        ventanaMain.destroy()
        

#Frame 1 - Parte izquierda de la pantalla
frame1 = tk.Frame(ventanaMain, bg="#f8d5e1", borderwidth=2, relief="sunken")
frame1.grid(row=0, column=0, sticky="nsew")
ventanaMain.grid_rowconfigure(0, weight=1)
ventanaMain.grid_columnconfigure(0, weight=1)

subFrame1_1 = tk.Frame(frame1, bg="#f2a6c2", borderwidth=2, relief="sunken")
subFrame1_1.pack(fill='both', expand=True, padx=10, pady=10)

saludoBienvenida = tk.Label(subFrame1_1, font=("Georgia", 15), text="Bienvenido a Delicia Fresca", bg="#fbcfe0", borderwidth=2, relief="sunken")
saludoBienvenida.pack(pady=20)


#Subframe 1 Frame parte derecha Boton para avanzar a la siguiente ventana
subFrame1_2 = tk.Frame(frame1, bg="#ff8fc5", borderwidth=2, relief="sunken")
subFrame1_2.pack(fill='both', expand=True, padx=10, pady=10)
ventanaMain.grid_rowconfigure(0, weight=1)
ventanaMain.grid_columnconfigure(1, weight=1)

# Cargar imagen redimensionada
imagenSis = redimensionar_imagen(ruta_carrito, 300, 300)
labelImagenSistema = tk.Label(subFrame1_2, image=imagenSis, bg="#fbcfe0", borderwidth=2, relief="sunken")
labelImagenSistema.pack(pady=20)
labelImagenSistema.bind("<Leave>", cambiarImagen)


# Botón para avanzar a la siguiente ventana
siguienteVentana = tk.Button(subFrame1_2, text="Nueva ventana", command=nueva_ventana, bg="#ff8fc5", font=("Georgia", 14, "bold"), fg="#ffffff", border=3, relief="raised")
siguienteVentana.place(relx=0.05, rely=0.7, relheight=0.15, relwidth=0.9)


#Frame 2 - Parte derecha de la ventana
frame2 = tk.Frame(ventanaMain, bg="#f8d5e1", borderwidth=2, relief="sunken")
frame2.grid(row=0, column=1, sticky="nsew")

subFrame2_1 = tk.Frame(frame2, bg="#f2a6c2", borderwidth=2, relief="sunken")
subFrame2_1.pack(fill='both', expand=True, padx=10, pady=10)

hojaDeVida = tk.Label(subFrame2_1, bg="#fbcfe0",text="Valentina Luján Robledo", font=("Georgia", 16), anchor = "center")
hojaDeVida.pack(pady=10, fill = 'both', expand = True)

hojaDeVida.bind("<Button-1>", mensaje)

hojaDeVida2 = tk.Label(subFrame2_1, bg="#fbcfe0", text="Estudio Ingeniería de Sistemas e Informática \n\nMe gusta la música, bailar y aprender cosas nuevas ", font=("Georgia", 12), justify="center", anchor = "center")
hojaDeVida2.pack(pady=10, fill='both', expand=True)

hojaDeVida2.bind("<Button-1>", mensaje)


# Subframe para las imágenes
subFrame2_2 = tk.Frame(frame2, bg="#ff8fc5", borderwidth=2, relief="sunken")
subFrame2_2.pack(fill='both', expand=True, padx=10, pady=10)

# Configurar el grid para que las imágenes se ajusten correctamente
subFrame2_2.grid_rowconfigure(0, weight=1)
subFrame2_2.grid_rowconfigure(1, weight=1)
subFrame2_2.grid_columnconfigure(0, weight=1)
subFrame2_2.grid_columnconfigure(1, weight=1)


# Imágenes de los integrantes redimensionadas
imagen1 = redimensionar_imagen(ruta_valentina1, 150, 150)
labelImagen1 = tk.Label(subFrame2_2, image=imagen1, borderwidth=2, relief="solid", bg="#ff8fc5")
labelImagen1.grid(row=0, column=0, padx=1, pady=1, sticky="nsew")
labelImagen1.image = imagen1

imagen2 = redimensionar_imagen(ruta_valentina2, 200, 200)
labelImagen2 = tk.Label(subFrame2_2, image=imagen2, borderwidth=2, relief="solid", bg="#ff8fc5")
labelImagen2.grid(row=0, column=1, padx=1, pady=1, sticky="nsew")
labelImagen2.image = imagen2

imagen3 = redimensionar_imagen(ruta_valentina3, 200, 200)
labelImagen3 = tk.Label(subFrame2_2, image=imagen3, borderwidth=2, relief="solid", bg="#ff8fc5")
labelImagen3.grid(row=1, column=0, padx=1, pady=1, sticky="nsew")
labelImagen3.image = imagen3 

imagen4 = redimensionar_imagen(ruta_valentina4, 200, 200)
labelImagen4 = tk.Label(subFrame2_2, image=imagen4, borderwidth=2, relief="solid", bg="#ff8fc5")
labelImagen4.grid(row=1, column=1, padx=1, pady=1, sticky="nsew")
labelImagen4.image = imagen4 

# Configurar el evento de click para cambiar la hoja de vida
menubar = Menu(ventanaMain)
ventanaMain.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Salir", command=salir_y_guardar)
file_menu.add_command(label="Descripcion del Proyecto",command=descripcion_proyecto)
menubar.add_cascade(
    label="Inicio",
    menu=file_menu
)

# Hacer que la ventana se ajuste al tamaño
ventanaMain.grid_columnconfigure(0, weight=1)
ventanaMain.grid_columnconfigure(1, weight=1)
ventanaMain.grid_rowconfigure(0, weight=1)

ventanaMain.mainloop()  # Inicia el bucle de eventos