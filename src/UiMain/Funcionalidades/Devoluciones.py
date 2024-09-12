import tkinter as tk
from tkinter import ttk, Frame, messagebox
import sys
sys.path.append('../')  # Retrocede un nivel al directorio padre

from gestorAplicacion.empresa.Fabrica import Fabrica
from gestorAplicacion.empresa.Factura import Factura
from gestorAplicacion.externo.Cliente import Cliente 
from gestorAplicacion.empresa.Producto import Producto 
from gestorAplicacion.externo.CuentaBancaria import CuentaBancaria
from baseDatos.Deserializador import Deserializador

class Devoluciones(Frame):
    # Atributos de clase
    listaFacturas = []
    clienteElegido: Cliente
    listaProductos = []
    productoElegido = None

    def _init_(self, window):
        super()._init_(window)

        # Deserialización de los datos necesarios
        Deserializador.deserializar()

        # Configuración del fondo y distribución de filas y columnas
        self.config(bg="#f8d5e1")
        for i in range(6):
            self.rowconfigure(i, weight=1)
        for j in range(3):
            self.columnconfigure(j, weight=1)

        # ---- Cabecera ----
        Cabecera = tk.Frame(self, bg="#f8d5e1")
        for k in range(3):
            Cabecera.columnconfigure(k, weight=1)
        Cabecera.rowconfigure(0, weight=1)
        Cabecera.rowconfigure(1, weight=1)
        Cabecera.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

        # Título principal
        tituloCabecera = tk.Label(Cabecera, text='Gestionar Devoluciones', font=("Georgia", 18, "bold"), bg="#f2a6c2", relief="raised", border=4)
        tituloCabecera.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Descripción
        variableD = """En este apartado se pueden realizar devoluciones de los productos
        de una factura en base al nombre del cliente"""
        descripcionCabecera = tk.Label(Cabecera, text=variableD, font=("Georgia", 12), bg="#fbcfe0", border=2, relief="sunken")
        descripcionCabecera.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # ---- Contenedor de Facturas ----
        Facturas = tk.Frame(self, bg="#fbcfe0", relief="raised", border=2)
        Facturas.columnconfigure(0, weight=1)
        Facturas.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # ---- Contenedor de Productos ----
        Productos = tk.Frame(self, bg="#fbcfe0", relief="raised", border=2)
        Productos.columnconfigure(0, weight=1)
        Productos.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
        Productos.grid_remove()  # Se oculta inicialmente hasta que se selecciona una factura

        # --- Texto descriptivo de las facturas
        textoFactura = "Seleccione el cliente que corresponde a la factura\npara devolver el producto"
        descripcionFactura = tk.Label(Facturas, text=textoFactura, font=("Georgia", 12, "bold"), border=1, relief="sunken")
        descripcionFactura.grid(row=0, padx=10, pady=10, sticky="nsew")

        # --- Desplegable para seleccionar factura
        seleccionarFactura = tk.StringVar(value='Seleccionar Factura')
        Devoluciones.listaFacturas = []
        for factura in Factura.getListaFacturas():
            cliente = factura.getCliente()
            if cliente not in Devoluciones.listaFacturas:
                Devoluciones.listaFacturas.append(cliente)
        desplegableFactura = ttk.Combobox(Facturas, values=Devoluciones.listaFacturas, textvariable=seleccionarFactura, state='readonly', width=30)
        desplegableFactura.grid(row=1, padx=10, pady=10, sticky="nsew")
        desplegableFactura.bind("<<ComboboxSelected>>", self.opcionFactura)

        # --- Texto descriptivo de los productos
        descripcionProducto = tk.Label(Productos, text="Seleccione el producto a devolver", font=("Georgia", 12, "bold"), border=1, relief="sunken")
        descripcionProducto.grid(row=0, padx=10, pady=10, sticky="nsew")

        # --- Desplegable para seleccionar producto
        seleccionarProducto = tk.StringVar(value='Seleccionar producto')
        desplegableProducto = ttk.Combobox(Productos, values=Devoluciones.listaProductos, textvariable=seleccionarProducto, state='readonly', width=30)
        desplegableProducto.grid(row=1, padx=10, pady=10, sticky="nsew")
        desplegableProducto.bind("<<ComboboxSelected>>", self.opcionProducto)

        # ---- Botón para devolver producto ----
        boton = tk.Button(self, text="Realizar\nDevolución", width=20, height=4, bg="#e895b0", font=("Georgia", 14, "bold"), fg="#ffffff", border=3, relief="raised", command=self.devolverProducto)
        boton.grid(row=3, column=1)
        boton.grid_remove()  # Oculto hasta que se seleccione un producto

    def opcionFactura(self, event):
        """
        Lógica para mostrar los productos disponibles para devolución, según el cliente seleccionado.
        """
        Devoluciones.clienteElegido = desplegableFactura.get()

        for factura in Factura.getListaFacturas():
            if f"{factura.getCliente()}" == Devoluciones.clienteElegido:
                Devoluciones.clienteElegido = factura.getCliente()

        listaParaRecorrer = Devoluciones.clienteElegido.getProductos()

        for producto in listaParaRecorrer:
            if not producto.isDevuelto():
                Devoluciones.listaProductos.append(producto.getNombre())

        Productos.grid()  # Mostrar contenedor de productos
        desplegableProducto['value'] = Devoluciones.listaProductos
        Devoluciones.listaProductos = []  # Resetear la lista para futuras selecciones

    def opcionProducto(self, event):
        """
        Habilita el botón de devolución una vez que se ha seleccionado un producto.
        """
        boton.grid()

    def devolverProducto(self):
        """
        Realiza el proceso de devolución del producto seleccionado, devolviendo el dinero y actualizando los estados.
        """
        Devoluciones.productoElegido = desplegableProducto.get()

        for producto in Devoluciones.clienteElegido.getProductos():
            if f"{producto.getNombre()}" == Devoluciones.productoElegido:
                Devoluciones.productoElegido = producto
                break

        # Procesar devolución de dinero y actualizar estados
        CuentaBancaria.devolverDinero(Devoluciones.clienteElegido.getCuentaBancaria(), Devoluciones.productoElegido.getValor(), Devoluciones.clienteElegido)
        CuentaBancaria.disminuirSaldo(Fabrica.getListaFabricas()[0].getCuentaBancaria(), Devoluciones.productoElegido.getValor())

        # Cambiar estado del producto
        Devoluciones.productoElegido.setDevuelto(True)
        Devoluciones.clienteElegido.getProductos().remove(Devoluciones.productoElegido)

        # Mensaje de éxito
        messagebox.showinfo("¡Devolución Exitosa!", f"El producto devuelto fue:\n{Devoluciones.productoElegido.getNombre()}")

        # Reiniciar valores
        desplegableFactura.set('')
        desplegableProducto.set('')
        Productos.grid_remove()
        boton.grid_remove()