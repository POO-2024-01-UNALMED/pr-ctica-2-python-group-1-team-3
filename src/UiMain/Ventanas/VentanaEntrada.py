# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero

import tkinter as tk
from tkinter import scrolledtext

# Texto de bienvenida con instrucciones
texto_bienvenida = """Bienvenido al menú principal del supermercado Delicia Fresca

En esta aplicación podrá encontrar las siguientes opciones:

1. Archivo: En esta sección de desplegarán dos opciones:
    - Aplicacion: Para ver información acerca del programa
    - Salir: Para volver a la ventana principal

2. Procesos y consultas: En esta sección se desplegarán las 7 opciones de funcionalidades del sistema. Estas son:
    - Enviar pedido
    - Proveer tiendas
    - Pago de nomina
    - Devoluciones
    - Evaluacion operacion
    - Añadir producto
    - Añadir cliente

3. Ayuda: En esta sección se desplegará la opción donde podra consultar información acerca de los desarrolladores.
"""

class VentanaEntrada(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configurar_texto()

    def configurar_texto(self):
        # Crear área de texto con barra de desplazamiento
        area_texto = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        area_texto.insert(tk.END, texto_bienvenida)
        area_texto.tag_configure('center', justify='center')  # Centrar texto
        area_texto.configure(state='disabled')  # Hacer el texto no editable
        area_texto.pack(expand=True, fill='both')

