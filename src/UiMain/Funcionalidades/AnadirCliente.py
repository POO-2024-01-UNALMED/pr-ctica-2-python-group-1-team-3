import tkinter as tk
from tkinter import Frame, messagebox

# Importación de excepciones personalizadas
from UiMain.excepciones.Categoria1.CamposVacios import CamposVacios
from UiMain.excepciones.Categoria2.SoloNumeros import SoloNumeros
from UiMain.excepciones.Categoria2.DireccionInvalida import DireccionInvalida
from UiMain.excepciones.Categoria1.ClienteYaExistente import ClienteYaExistente
from UiMain.excepciones.Categoria2.NombreInvalido import NombreInvalido

# Importación de clases para la gestión de clientes y cuentas bancarias
from gestorAplicacion.externo.Cliente import Cliente
from gestorAplicacion.externo.CuentaBancaria import CuentaBancaria
from UiMain.Ventanas.FieldFrame import FieldFrame

class AnadirCliente(Frame):
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
        titulo = tk.Label(cabecera, text="Añadir cliente", font=("Georgia", 18, "bold"), bg="#f2a6c2", relief="raised", border=4)
        titulo.pack(pady=10, fill="x")

        # Texto descriptivo
        descripcion = """Complete los campos del formulario para añadir un nuevo cliente."""
        labelDescripcion = tk.Label(cabecera, text=descripcion, font=("Georgia", 12), bg="#fbcfe0", border=2, relief="sunken")
        labelDescripcion.pack(pady=10)

        # Contenedor de campos
        contenedorCampos = tk.Frame(self, width=100, height=200, bg="#fbcfe0")
        contenedorCampos.grid(row=1, column=1, pady=10, sticky="nsew")
        contenedorCampos.rowconfigure(0, weight=1)
        contenedorCampos.columnconfigure(0, weight=1)
        contenedorCampos.columnconfigure(1, weight=1)
        contenedorCampos.columnconfigure(2, weight=1)

        # Criterios del formulario
        self.criterios = ["ID", "Nombre", "Direccion", "Cuenta Bancaria"]

        # Calcular el ID inicial del cliente basado en la longitud de la lista de clientes
        cliente_id = Cliente.getNextID()

        # Valores iniciales para los campos, con el ID como no editable
        valores_iniciales = [cliente_id, "", "", ""]
        habilitados = [False, True, True, True]  # Solo el ID está deshabilitado

        # Crear FieldFrame para ingresar los datos del cliente
        self.fp = FieldFrame(contenedorCampos, "Criterio", self.criterios, "Valor", valores_iniciales, habilitados)
        self.fp.configure(bg="#f2a6c2", relief="raised", border=2, padx=20, pady=20)
        self.fp.grid(row=0, column=1, padx=30, pady=30, sticky="nsew")

        # Frame para los botones de acción
        botonFrame = Frame(self, bg="#f8d5e1")
        botonFrame.grid(row=2, column=1, padx=10)

        # Botón para agregar cliente
        botonAgregar = tk.Button(botonFrame, text="Agregar Cliente", command=self.ingresarCliente, width=15, height=2, bg="#e895b0", font=("Georgia", 13, "bold"), fg="#ffffff", border=3, relief="raised")
        botonAgregar.grid(row=0, column=0, padx=10)

        # Botón para limpiar campos
        botonLimpiar = tk.Button(botonFrame, text="Borrar", command=self.borrar, width=10, height=2, bg="#e895b0", font=("Georgia", 13, "bold"), fg="#ffffff", border=3, relief="raised")
        botonLimpiar.grid(row=0, column=1, padx=10)


    def ingresarCliente(self):
        """
        Maneja la lógica para agregar un cliente, validando los campos y mostrando mensajes de error si es necesario.
        """
        nombre = self.fp.getValue("Nombre")
        direccion = self.fp.getValue("Direccion")
        cuenta_bancaria = self.fp.getValue("Cuenta Bancaria")

        try:
            # Validar campos vacíos
            if len(self.fp.getEntrysVacios()) > 0:
                raise CamposVacios()

            # Validar nombre (Debe ser "Nombre Apellido")
            if len(nombre.split()) != 2:
                raise NombreInvalido()

            # Validar si el cliente ya existe
            for cliente in Cliente.getListaClientes():
                if cliente.getNombre() == nombre:
                    raise ClienteYaExistente()

            # Validar dirección (Debe contener números y letras)
            if not any(char.isdigit() for char in direccion) or not any(char.isalpha() for char in direccion):
                raise DireccionInvalida()

            # Validar cuenta bancaria (debe contener solo números)
            if not cuenta_bancaria.isdigit():
                raise SoloNumeros("cuenta bancaria")
            nueva_cuenta = CuentaBancaria(cuenta_bancaria, 100000)  # Saldo inicial = 100.000

            # Crear el nuevo cliente
            nuevo_cliente = Cliente(nombre, direccion, nueva_cuenta)

            messagebox.showinfo('Éxito', 'El cliente fue agregado con éxito.')
            self.borrar()

        except CamposVacios as e:
            campos = "\n".join(self.fp.getEntrysVacios())
            messagebox.showerror("Campos Vacíos", f"Los siguientes campos están vacíos:\n{campos}")

        except ClienteYaExistente as e:
            messagebox.showerror("Error", str(e))

        except SoloNumeros as e:
            messagebox.showerror("Error", str(e))

        except DireccionInvalida as e:
            messagebox.showerror("Error", str(e))

        except NombreInvalido as e:
            messagebox.showerror("Error", str(e))


    def borrar(self):
        """
        Limpia todos los campos del formulario excepto el ID.
        """
        for criterio in self.criterios:
            if criterio != "ID":  # El ID no se borra
                self.fp.getEntry(criterio).delete(0, tk.END)
