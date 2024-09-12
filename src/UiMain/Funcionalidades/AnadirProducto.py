import tkinter as tk
from tkinter import Frame, messagebox

from UiMain.excepciones.Categoria1.CamposVacios import CamposVacios
from UiMain.excepciones.Categoria2.SoloNumeros import SoloNumeros
from UiMain.excepciones.Categoria2.CategoriaNoValida import CategoriaNoValida
from UiMain.excepciones.Categoria1.ProductoYaExistente import ProductoYaExistente

from UiMain.Ventanas.FieldFrame import FieldFrame

from gestorAplicacion.empresa.Fabrica import Fabrica
from gestorAplicacion.empresa.Producto import Producto

class AnadirProducto(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        
        # Configuración del fondo con tonos rosados
        self.configure(bg="#f8d5e1")
        
        # Distribución de filas y columnas
        for fila in range(6):
            self.rowconfigure(fila, weight=1)
        
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)

        # Frame para el título
        cabecera = tk.Frame(self, bg="#f8d5e1")
        cabecera.grid(row=0, column=1, padx=10, pady=10)

        # Título principal
        titulo = tk.Label(cabecera, text='Registrar nuevo producto', font=("Georgia", 18, "bold"), bg="#f2a6c2", relief="raised", border=4)
        titulo.pack(pady=10, fill="x")

        # Texto descriptivo
        descripcion = """Complete los campos del formulario para agregar un nuevo producto."""
        labelDescripcion = tk.Label(cabecera, text=descripcion, font=("Georgia", 12), bg="#fbcfe0", border=2, relief="sunken")
        labelDescripcion.pack(pady=10)

        # Contenedor de campos
        contenedorCampos = tk.Frame(self, width=100, height=200, bg="#fbcfe0")
        contenedorCampos.grid(row=1, column=1, pady=10, sticky="nsew")
        contenedorCampos.rowconfigure(0, weight=1)
        contenedorCampos.columnconfigure(0, weight=1)
        contenedorCampos.columnconfigure(1, weight=1)
        contenedorCampos.columnconfigure(2, weight=1)

        # Criterios para los campos (self, nombre, descripcion, valor, peso, tamano, costoProduccion, categoria)
        self.criterios = ["Nombre", "Descripción", "Precio", "Peso", "Tamaño", "Costo de fabricación", "Categoría"]
        
        # Todos los campos habilitados
        habilitados = [True] * len(self.criterios)
        
        self.fp = FieldFrame(contenedorCampos, "Criterio", self.criterios, "Valor", None, habilitados)
        self.fp.configure(bg="#f2a6c2", relief="raised", border=2, padx=20, pady=20)
        self.fp.grid(row=0, column=1, padx=30, pady=30, sticky="nsew")

        # Botones de acción
        botonFrame = Frame(self, bg="#f8d5e1")
        botonFrame.grid(row=2, column=1, padx=10)

        # Botón para agregar producto
        botonAgregar = tk.Button(botonFrame, text="Agregar Producto", command=self.agregarProducto, width=15, height=2, bg="#e895b0", font=("Georgia", 13, "bold"), fg="#ffffff", border=3, relief="raised")
        botonAgregar.grid(row=0, column=0, padx=10)

        # Botón para limpiar campos
        botonLimpiar = tk.Button(botonFrame, text="Limpiar", command=self.limpiarCampos, width=10, height=2, bg="#e895b0", font=("Georgia", 13, "bold"), fg="#ffffff", border=3, relief="raised")
        botonLimpiar.grid(row=0, column=1, padx=10)

        # Instrucción sobre las categorías (Frutas y verduras, Panaderia, Salsas y mermeladas, Bebidas)
        labelCategorias = tk.Label(contenedorCampos, text="Las categorias validas son:\n- frutas y verduras\n- panaderia\n- salsas y mermeladas\n- bebidas", font=("Georgia", 12), bg="#fbcfe0", border=2, relief="sunken")
        labelCategorias.grid(row=1, column=1, padx=6)

    def agregarProducto(self):
        """
        Maneja la lógica para agregar un producto, validando los campos y mostrando mensajes de error si es necesario.
        """
        nombre = self.fp.getValue("Nombre")
        descripcion = self.fp.getValue("Descripción")
        precio = self.fp.getValue("Precio")
        peso = self.fp.getValue("Peso")
        dimensiones = self.fp.getValue("Tamaño")
        costo_fabricacion = self.fp.getValue("Costo de fabricación")
        categoria = self.fp.getValue("Categoría")

        try:
            # Validar campos vacíos
            if len(self.fp.getEntrysVacios()) > 0:
                raise CamposVacios()

            # Validar categoría
            if categoria not in ["frutas y verduras", "panaderia", "salsas y mermeladas", "bebidas"]:
                raise CategoriaNoValida()

            # Validar campos numéricos
            campos_numericos = {
                "Precio": precio,
                "Peso": peso,
                "Dimensiones": dimensiones,
                "Costo de fabricación": costo_fabricacion
            }

            campos_invalidos = [campo for campo, valor in campos_numericos.items() if not valor.isdigit()]
            if campos_invalidos:
                raise SoloNumeros(campos_invalidos)

            # Crear producto y añadirlo a la fábrica
            producto = Producto(nombre, descripcion, int(precio), int(peso), int(dimensiones), int(costo_fabricacion), categoria)
            fabrica = Fabrica.getListaFabricas()[0]

            try:
                fabrica.anadirProducto(producto)
            except ProductoYaExistente:
                messagebox.showerror('Error', str(ProductoYaExistente()))
            else:
                messagebox.showinfo('Éxito', 'Producto agregado correctamente.')
                self.limpiarCampos()

        except CamposVacios as e:
            campos = "\n".join(self.fp.getEntrysVacios())
            messagebox.showerror("Campos vacíos", f"Los siguientes campos están vacíos:\n{campos}")

        except SoloNumeros as e:
            messagebox.showerror("Error", str(e))

        except CategoriaNoValida as e:
            messagebox.showerror("Error", str(e))

    def limpiarCampos(self):
        """ Limpia todos los campos del formulario. """
        for criterio in self.criterios:
            self.fp.getEntry(criterio).delete(0, tk.END)
