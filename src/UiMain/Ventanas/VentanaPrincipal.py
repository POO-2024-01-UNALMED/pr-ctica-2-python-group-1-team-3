# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero

import tkinter as tk

from tkinter import Menu, messagebox, BOTH, Frame
from UiMain.Funcionalidades.EvaluacionOperacion import EvaluacionOperacion
from UiMain.Funcionalidades.AnadirCliente import AnadirCliente
from UiMain.Funcionalidades.AnadirProducto import AnadirProducto
from UiMain.Funcionalidades.ProveerTiendas import ProveerTiendas
from UiMain.Funcionalidades.PagoDeNomina import PagoDeNomina
from UiMain.Funcionalidades.EnviarPedido import EnviarPedido
from UiMain.Funcionalidades.Devoluciones import Devoluciones
from UiMain.Ventanas.VentanaEntrada import VentanaEntrada
from baseDatos.Serializador import Serializador

import sys

from baseDatos.Deserializador import Deserializador
sys.path.append('../')


class VentanaPrincipal(tk.Tk):
    def __init__(self):
        Deserializador.deserializar()
        super().__init__()
        self.configurar_ventana()

        # Barra de menú superior
        self.menuBar = Menu(self)
        self.crear_menus()

        # Ventana de entrada
        interfaz_inicio = VentanaEntrada(self)
        interfaz_inicio.pack(fill=BOTH, expand=True)

        self.config(menu=self.menuBar)

    def configurar_ventana(self):
        """Configuración inicial de la ventana principal."""
        self.geometry("700x900+150+5")
        self.title("Delicia Fresca")
        self.config(bg="#f391e8")

    def crear_menus(self):
        """Creación de menús y submenús."""
        self.menu_archivo()
        self.menu_procesos()
        self.menu_ayuda()

    def menu_archivo(self):
        """Crea el menú 'Archivo'."""
        menu_archivo = Menu(self.menuBar, tearoff=0)
        menu_archivo.add_command(label='Aplicación', command=self.aplicacion)
        menu_archivo.add_command(label='Salir y guardar', command=self.salir_y_guardar)
        self.menuBar.add_cascade(menu=menu_archivo, label='Archivo')

    def menu_procesos(self):
        """Crea el menú 'Procesos y Consultas'."""
        menu_procesos = Menu(self.menuBar, tearoff=0)
        menu_procesos.add_command(label='Enviar pedido', command=self.enviar_pedido)
        menu_procesos.add_command(label='Proveer tiendas', command=self.proveerTiendas)
        menu_procesos.add_command(label='Pago de nomina', command=self.pago_nomina)
        menu_procesos.add_command(label='Devoluciones', command=self.devoluciones)
        menu_procesos.add_command(label='Evaluacion operacion', command=self.evaluacion_operacion)
        menu_procesos.add_command(label='Añadir producto', command=self.anadir_producto)
        menu_procesos.add_command(label='Añadir cliente', command=self.anadir_cliente) 
        self.menuBar.add_cascade(menu=menu_procesos, label='Procesos y Consultas')

    def menu_ayuda(self):
        """Crea el menú 'Ayuda'."""
        menu_ayuda = Menu(self.menuBar, tearoff=0)
        menu_ayuda.add_command(label='Acerca de', command=self.acerca_de)
        self.menuBar.add_cascade(menu=menu_ayuda, label='Ayuda')

    # Funciones asociadas a las acciones del menú
    def proveerTiendas(self):
        self.cambiar_pantalla(ProveerTiendas(self))

    def pago_nomina(self):
        self.cambiar_pantalla(PagoDeNomina(self))

    def enviar_pedido(self):
        self.cambiar_pantalla(EnviarPedido(self))

    def devoluciones(self):
        self.cambiar_pantalla(Devoluciones(self))

    def evaluacion_operacion(self):
        self.cambiar_pantalla(EvaluacionOperacion(self))

    def anadir_producto(self):
        self.cambiar_pantalla(AnadirProducto(self))

    def anadir_cliente(self):
        """Abre la ventana de 'Añadir Cliente'."""
        self.cambiar_pantalla(AnadirCliente(self))

    def cambiar_pantalla(self, nueva_funcionalidad):
        """Limpia la ventana actual y muestra la nueva funcionalidad."""
        for widget in self.winfo_children():
            widget.pack_forget()
        nueva_funcionalidad.pack(fill=BOTH, expand=True)

    def aplicacion(self):
        """Muestra información sobre la aplicación."""
        info = """Este es un programa diseñado para llevar el control de la empresa Delicia Fresca, un supermercado que vende productos frescos, de alta calidad y fabricados en su propia fábrica. La administración de esta contiene funcionalidades como:

        - Enviar pedido 
        - Proveer tiendas 
        - Pago de nomina
        - Gestionar devoluciones 
        - Evaluación operación
        - Añadir productos
        - Añadir clientes"""

        messagebox.showinfo("Aplicación", info)

    def salir_y_guardar(self):
        """Guarda los datos y sale de la aplicación."""
        self.destroy()
        Serializador.serializar()

    def acerca_de(self):
        """Muestra la información de los desarrolladores."""
        messagebox.showinfo("Desarrolladores", 
                            "Valentina Luján Robledo\nSebastian Estrada Villa\nSantiago Ochoa Quintero\n")


# Uso de la ventana principal
if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()
