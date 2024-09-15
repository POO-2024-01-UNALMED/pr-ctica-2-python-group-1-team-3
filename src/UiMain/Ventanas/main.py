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

from VentanaPrincipal import VentanaPrincipal
#
# import VentanaPrincipal


from setuptools.command.setopt import edit_config

#from src.gestorAplicacion.externo.TipoTransporte import TipoTransporte


from pathlib import Path

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
ventanaMain.geometry('800x800')
ventanaMain.title('Inicio')

#Funciones Eventos

#Evento click  - Cambio hoja de vida
def mensaje(Evento):
    texto = hojaDeVida.cget("text")

    if (texto == "Valentina Luján Robledo" or texto == "Descripcion de Proyecto"):
        hojaDeVida.config(text="Sebastian Estrada Villa")
        hojaDeVida2.config(text="Estudio Ingeniería de Sistemas \ne Informática \nMe gusta el deporte, la música  \ny los acertijos.")
        global imagen1v
        imagen1v = tk.PhotoImage(file=ruta_sebastian1)
        labelImagen1.config(image=imagen1v)

        global imagen2v
        imagen2v = tk.PhotoImage(file=ruta_sebastian2)
        labelImagen2.config(image=imagen2v)

        global imagen3v
        imagen3v = tk.PhotoImage(file=ruta_sebastian3)
        labelImagen3.config(image=imagen3v)

        global imagen4v
        imagen4v = tk.PhotoImage(file=ruta_sebastian4)
        labelImagen4.config(image=imagen4v)



    if (texto == "Sebastian Estrada Villa"):
        hojaDeVida.config(text='Santiago Ochoa Quintero')
        hojaDeVida2.config(text="Texto2 Texto2 Texto2 Texto2 Texto2 \nTexto2 Texto2 Texto2 Texto2 Texto2 \nTexto2 Texto2 Texto2")
    if (texto == "Santiago Ochoa Quintero"):
        hojaDeVida.config(text='Valentina Luján Robledo')
        hojaDeVida2.config(text="Estudio Ingeniería de Sistemas \ne Informática \nMe gusta la música, bailar y \naprender cosas nuevas ")

        global imagen1s
        imagen1s = tk.PhotoImage(file=ruta_valentina1)
        labelImagen1.config(image=imagen1s)

        global imagen2s
        imagen2s = tk.PhotoImage(file=ruta_valentina2)
        labelImagen2.config(image=imagen2s)

        global imagen3s
        imagen3s = tk.PhotoImage(file=ruta_valentina3)
        labelImagen3.config(image=imagen3s)

        global imagen4s
        imagen4s = tk.PhotoImage(file=ruta_valentina4)
        labelImagen4.config(image=imagen4s)




#Funcion para crear una nueva ventana y cerra la anterior

def nueva_ventana():
    ventanaMain.withdraw()
    #Deserializador.deserializar() # Para cargar los objetos serializados
    ventana2.deiconify()

def descripcion_proyecto():
    hojaDeVida.config(text='Descripcion de Proyecto')
    hojaDeVida2.config(text="Delicia fresca es un supermercado que \nse encarga de ofrecer productos de la \nmejor calidad \n\nEste programa nos permite llevar el control de \ntodos los procesos del mercado.")


rutasImagenesSistema = [
    ruta_tienda,
    ruta_carrito,
    ruta_productos,
    ruta_cajera,
    ruta_precio,
]

image_index = 0

def cambiarImagen(Event):
    global imagenSistema, image_index
    image_index = (image_index + 1) % len(rutasImagenesSistema)
    img = tk.PhotoImage(file=rutasImagenesSistema[image_index])  # Cargar la nueva imagen
    labelImagenSistema.config(image=img)
    labelImagenSistema.image = img


#Frame 1 - Parte izquierda de la pantalla
frame1 = tk.Frame(ventanaMain, bg="pink", borderwidth=2, relief="sunken")
frame1.place(relx=0, rely=0, relwidth=0.5, relheight=1)

subFrame1_1 = tk.Frame(frame1, bg="pink", borderwidth=2, relief="sunken")
subFrame1_1.place(relx=0.05, rely=0.05, relheight=0.20, relwidth=0.9)

saludoBienvenida = tk.Label(subFrame1_1, font=("Helvetica", 15), text="Bienvenido a Delicia Fresca", bg="pink", borderwidth=2, relief="sunken")
saludoBienvenida.place(relx=0.15, rely=0.4)

#Subframe 1 Frame parte derecha Boton para avanzar a la siguiente ventana

subFrame1_2 = tk.Frame(frame1, bg="pink", borderwidth=2, relief="sunken")
subFrame1_2.place(relx=0.05, rely=0.35, relheight=0.60, relwidth=0.9)

siguienteVentana = tk.Button(subFrame1_2, text="Nueva ventana", command=nueva_ventana)
siguienteVentana.place(relx=0.05, rely=0.7, relheight=0.15, relwidth=0.9)

imagenSis = tk.PhotoImage(file=ruta_carrito)
labelImagenSistema = tk.Label(subFrame1_2, image=imagenSis, bg="pink", borderwidth=2, relief="sunken")
labelImagenSistema.place(relx=0.1, rely=0.05, relheight=0.6, relwidth=0.8)
labelImagenSistema.bind("<Leave>", cambiarImagen)



#Frame 2 - Parte derecha de la ventana
frame2 = tk.Frame(ventanaMain, bg="pink", borderwidth=2, relief="sunken")
frame2.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

subFrame2_1 = tk.Frame(frame2, bg="pink", borderwidth=2, relief="sunken")
subFrame2_1.place(relx=0.05, rely=0.05, relheight=0.25, relwidth=0.9)


hojaDeVida = tk.Label(subFrame2_1, bg="pink",text="Valentina Luján Robledo", font=("Helvetica", 16))
hojaDeVida.place(relx=0.20, rely=0.20)

hojaDeVida.bind("<Button-1>", mensaje)

hojaDeVida2 = tk.Label(subFrame2_1, bg="pink", text="Estudio Ingeniería de Sistemas e Informática \n\nMe gusta la música, bailar y aprender \ncosas nuevas ", font=("Georgia", 12), justify="left")
hojaDeVida2.place(relx=0.10, rely=0.40)
hojaDeVida2.bind("<Button-1>", mensaje)





subFrame2_2 = tk.Frame(frame2, bg="pink", borderwidth=2, relief="sunken")
subFrame2_2.place(relx=0.125, rely=0.35, relheight=0.40, relwidth=0.8)

imagen1 = tk.PhotoImage(file=ruta_valentina1)
labelImagen1 = tk.Label(subFrame2_2, image=imagen1, width=150, height=150, borderwidth=2, relief="solid")
labelImagen1.grid(row=0, column=0, padx=1, pady=1)

imagen2 = tk.PhotoImage(file=ruta_valentina2)
labelImagen2 = tk.Label(subFrame2_2, image=imagen2, width=150, height=150, borderwidth=2, relief="solid")
labelImagen2.grid(row=0, column=1, padx=1, pady=1)

imagen3 = tk.PhotoImage(file=ruta_valentina3)
labelImagen3 = tk.Label(subFrame2_2, image=imagen3, width=150, height=150, borderwidth=2, relief="solid")
labelImagen3.grid(row=1, column=0, padx=1, pady=1)

imagen4 = tk.PhotoImage(file=ruta_valentina4)
labelImagen4 = tk.Label(subFrame2_2, image=imagen4, width=150, height=150, borderwidth=2, relief="solid")
labelImagen4.grid(row=1, column=1, padx=1, pady=1)


menubar = Menu(ventanaMain)
ventanaMain.config(menu=menubar)

file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Salir", command=ventanaMain.quit)
file_menu.add_command(label="Descripcion del Proyecto",command=descripcion_proyecto)
menubar.add_cascade(
    label="Inicio",
    menu=file_menu
)



# ventana2 = tk.Tk()
# ventana2.geometry('1000x1000')
# ventana2.title('Delicia Fresca')

# def ventana2Info():
#     messagebox.showinfo("Delicia Fresca", "¡Hola, esta es una ventana emergente!")

# def ventanaPrincipal():
#     # ventana2.withdraw(
#     ventanaMain.deiconify()




#Interfaz Funcionalidad


#Lista de clientes - Tienda - Productso con una cantidad menor que 5 - Transporte - Envio gratis

# ventana2funcionalidad = tk.Frame(ventana2, bg="pink")
# ventana2funcionalidad.place(x=100, y=250, relwidth=0.8, relheight=0.5)
#
# ventana2FuncionalidadFrame1 = tk.Frame(ventana2funcionalidad, bg="red")
# ventana2FuncionalidadFrame1.place(relx=0.1, rely=0.6, relheight=0.3, relwidth=0.8)
#
# botonBorrar = tk.Button(ventana2FuncionalidadFrame1, text="Borrar", command=borrarButton)
# botonBorrar.place(relx=0.05, rely=0.1, relheight=0.2, relwidth=0.2)
#
# funcionalidad1frame = tk.Frame(ventana2funcionalidad, bg="red")
# #funcionalidad1frame.place(relx=0.1, rely=0.1, relheight=0.4, relwidth=0.8)
#
#
# productos = {
#     "Frutas y Verduras": [
#         "Manzana", "Zanahoria", "Pepino", "Limon", "Piña", "Pera", "Tomate", "Frambuesa", "Lechuga", "Sandia"
#     ],
#     "Panadería": [
#         "Pan", "Sanduche", "Pandebono", "Pan hojaldrado", "Galletas", "Palito de queso", "Tostada", "Ponque", "Pan tajado", "Almojabana"
#     ],
#     "Salsas y Mermeladas": [
#         "Mermelada de frambuesa", "Mermelada de piña", "Mermelada de mora", "Mayonesa", "Salsa de tomate", "Mermelada de fresa",
#         "Mermelada de kiwi", "Mermelada de frutos rojos", "Salsa BBQ", "Salsa de soya"
#     ],
#     "Bebidas": [
#         "Te verde", "Jugo de naranja", "Leche de almendras", "Leche de avena", "Yogur de soya", "Cafe instantaneo", "Bebida achocolatada",
#         "Leche de coco", "Bebida hidratante", "Jugo de mora"
#     ]
# }
# tiendas = ['Delicia Fresca Norte', 'Delicia Fresca Sur', 'Delicia Fresca Centro']
#
# clientes = [
#     "Esteban Carrillo",
#     "Tiffany Mendoza",
#     "Santiago Perez",
#     "Mariana Lopera",
#     "Jose Manuel Vergara",
#     "Camila Zapata",
#     "Miguel Acosta",
#     "Martin Berrio"
# ]
# opciones = [
#     "SI",
#     "NO"
# ]
# TipoTransporte = [
#     "Camion",
#     "Bicicleta",
#     "Caminando",
#     "Moto",
#     "Carro",
#     "Avion"
# ]
#
#
# # Crear una lista de productos con separadores de categorías
# productos_lista = []
# for categoria, productos_en_categoria in productos.items():
#     productos_lista.append(f"-- {categoria} --")  # Agregar el separador
#     productos_lista.extend(productos_en_categoria)  # Agregar los productos
#
# label = tk.Label(funcionalidad1frame, text="Selecciona un producto", font=('Georgia', 12))
# label.pack(pady=1, padx=0.1)
#
# # Crear el combobox (lista desplegable)
# combo = ttk.Combobox(funcionalidad1frame, values=productos_lista, state="readonly")
# combo.place(relx=0.05, rely=0.1, relheight=0.2, relwidth=0.2)
#
# label2 = tk.Label(funcionalidad1frame, text="Selecciona una tienda", font=('Georgia', 12))
# label2.pack(pady=2, padx=0.1)
#
# # Crear el combobox (lista desplegable)
# combo2 = ttk.Combobox(funcionalidad1frame, values=tiendas, state="readonly")
# combo2.place(relx=0.05, rely=0.3, relheight=0.2, relwidth=0.2)
#
# label3 = tk.Label(funcionalidad1frame, text="Selecciona un cliente", font=('Georgia', 12))
# label3.pack(pady=2, padx=0.1)
#
# # Crear el combobox (lista desplegable)
# combo3 = ttk.Combobox(funcionalidad1frame, values=clientes, state="readonly")
# combo3.place(relx=0.05, rely=0.3, relheight=0.2, relwidth=0.2)
#
# entry = tk.Entry(funcionalidad1frame, width=50)
# entry.pack(pady=2, padx=0.1)
#
# label4 = tk.Label(funcionalidad1frame, text="Selecciona un Tipo de transporte", font=('Georgia', 12))
# label4.pack(pady=2, padx=0.1)
#
# combo4 = ttk.Combobox(funcionalidad1frame, values=TipoTransporte, state="readonly")
# combo4.place(relx=0.05, rely=0.3, relheight=0.2, relwidth=0.2)
#
# label5 = tk.Label(funcionalidad1frame, text="Aplicar envio Gratis?", font=('Georgia', 12))
# label5.pack(pady=2, padx=0.1)
#
# combo5 = ttk.Combobox(funcionalidad1frame, values=opciones, state="readonly")
# combo5.place(relx=0.05, rely=0.3, relheight=0.2, relwidth=0.2)


ventana2 = VentanaPrincipal()  # Crea una instancia de la ventana principal
ventana2.mainloop()


ventana2.withdraw()


ventanaMain.mainloop()



