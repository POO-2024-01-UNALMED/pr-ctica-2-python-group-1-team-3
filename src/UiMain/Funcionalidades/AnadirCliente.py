import tkinter as tk
from tkinter import Frame, messagebox

from UiMain.excepciones.Categoria1.CamposVacios import CamposVacios
from UiMain.excepciones.Categoria2.SoloNumeros import SoloNumeros
from UiMain.excepciones.Categoria2.DireccionInvalida import DireccionInvalida
from UiMain.excepciones.Categoria1.ClienteYaExistente import ClienteYaExistente
from UiMain.excepciones.Categoria2.NombreInvalido import NombreInvalido

from gestorAplicacion.externo.Cliente import Cliente
from gestorAplicacion.externo.CuentaBancaria import CuentaBancaria
from UiMain.Ventanas.FieldFrame import FieldFrame
from baseDatos.Deserializador import Deserializador  # Asegúrate de importar el Deserializador

class AnadirCliente(Frame):

    def __init__(self, window):
        super().__init__(window)
        self.configure(bg="#f391e8")
        for i in range(6):
            self.rowconfigure(i, weight=1)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)

        frameCabecera = tk.Frame(self, bg="#f391e8")
        frameCabecera.grid(row=0, column=1, padx=5, pady=5)

        titulo = tk.Label(frameCabecera, text='Añadir cliente', font=("Georgia", 15, "bold"), bg="#f2b2eb", relief="raised", border=3)
        titulo.pack(pady=5, fill="x")

        textoDescripcion = """Aquí podrá añadir un cliente rellenando el siguiente formulario."""
        descripcion = tk.Label(frameCabecera, text=textoDescripcion, font=("Georgia", 12), bg="#f2b2eb", border=2, relief="sunken")
        descripcion.pack(pady=5)

        contenedorField = tk.Frame(self, width=100, height=200, bg="#f2b2eb")
        contenedorField.grid(row=1, column=1, pady=3, sticky="nsew")
        contenedorField.rowconfigure(0, weight=1)
        contenedorField.columnconfigure(0, weight=1)
        contenedorField.columnconfigure(1, weight=1)
        contenedorField.columnconfigure(2, weight=1)

        self.criterios = ["ID", "Nombre", "Direccion", "Cuenta Bancaria"]

        # Deserializar datos
        Deserializador.deserializar()

        # Calcular el ID inicial basado en la longitud de la lista de clientes
        cliente_id = Cliente.getNextID()

        valores_iniciales = [cliente_id, "", "", ""]  # Lista de valores iniciales, con ID incluido
        habilitado = [False, True, True, True]  # El campo ID no es editable

        # Creación del FieldFrame con los valores actualizados
        self.fp = FieldFrame(contenedorField, "Criterio", self.criterios, "Valor", valores_iniciales, habilitado)
        self.fp.configure(bg="#f1b6ea", relief="raised", border=2, padx=20, pady=20)
        self.fp.grid(row=0, column=1, padx=50, pady=50, sticky="nsew")

        frameBotones = Frame(self, bg="#f391e8")
        frameBotones.grid(row=2, column=1, padx=5)

        botonIngresar = tk.Button(frameBotones, text="Ingresar Cliente", command=self.ingresarCliente, width=15, height=3, bg="#9d088c",
                                  font=("Georgia", 14, "bold"), fg="#ffffff", border=2, relief="raised")
        botonIngresar.grid(row=0, column=0, padx=6)

        botonBorrar = tk.Button(frameBotones, text="Borrar", command=self.borrar, width=10, height=3, bg="#9d088c",
                                font=("Georgia", 14, "bold"), fg="#ffffff", border=2, relief="raised")
        botonBorrar.grid(row=0, column=1, padx=6)

    def ingresarCliente(self):
        nombre = self.fp.getValue("Nombre")
        direccion = self.fp.getValue("Direccion")
        cuenta_bancaria = self.fp.getValue("Cuenta Bancaria")

        try:
            # Validar si hay campos vacíos
            if len(self.fp.getEntrysVacios()) > 0:
                raise CamposVacios()

            # Validar nombre (Debe ser "Nombre Apellido")
            if len(nombre.split()) != 2:
                raise NombreInvalido()

            # Validar que el cliente no exista ya
            for cliente in Cliente.getListaClientes():
                if cliente.getNombre() == nombre:
                    raise ClienteYaExistente()

            # Validar dirección (Debe contener números y letras)
            if not any(char.isdigit() for char in direccion) or not any(char.isalpha() for char in direccion):
                raise DireccionInvalida()

            # Crear la cuenta bancaria
            if not cuenta_bancaria.isdigit():
                raise SoloNumeros("cuenta bancaria")
            nueva_cuenta = CuentaBancaria(cuenta_bancaria, 100000)  # Saldo inicial = 100.000

            # Crear el nuevo cliente
            nuevo_cliente = Cliente(nombre, direccion, nueva_cuenta)

            messagebox.showinfo('Cliente agregado', 'El cliente fue agregado con éxito.')
            self.borrar()

        except CamposVacios as e:
            campos = self.fp.getEntrysVacios()
            c = "\n\n" + "\n".join([campo for campo in campos])
            messagebox.showerror("Error", str(CamposVacios(c)))

        except ClienteYaExistente as e:
            messagebox.showerror("Error", str(e))

        except SoloNumeros as e:
            messagebox.showerror("Error", str(e))

        except DireccionInvalida as e:
            messagebox.showerror("Error", str(e))

        except NombreInvalido as e:
            messagebox.showerror("Error", str(e))

    def borrar(self):
        for criterio in self.criterios:
            if criterio != "ID":  # El ID no se borra.
                self.fp.getEntry(criterio).delete(0, tk.END)
