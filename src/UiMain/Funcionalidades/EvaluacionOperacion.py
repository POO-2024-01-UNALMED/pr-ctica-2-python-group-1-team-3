import tkinter as tk
from tkinter import Frame, messagebox
import sys

# Agrega el directorio superior al sistema de rutas para importar módulos desde allí
sys.path.append('../')

from gestorAplicacion.empresa.Factura import Factura
from UiMain.excepciones.Categoria1.FechasFueraDeRango import FechasFueraDeRango
from UiMain.excepciones.Categoria1.InicioMayorQueFin import InicioMayorQueFin
from UiMain.excepciones.Categoria2.NumerosEnteros import NumerosEnteros
from UiMain.excepciones.Categoria1.NoHayFechas import NoHayFechas

# Clase principal que hereda de Frame y que maneja la evaluación de operaciones
class EvaluacionOperacion(Frame):
    def __init__(self, window):
        # Inicializa la clase base (Frame) y configura el fondo
        super().__init__(window)
        self.config(bg="#f8d5e1")
        
        # Configura las filas y columnas del layout de la ventana principal
        for i in range(6):
            self.rowconfigure(i, weight=1)

        self.columnconfigure(0, weight=8)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=8)

        # Crea un marco para la cabecera de la interfaz
        frameCabecera = tk.Frame(self, bg="#f8d5e1")
        frameCabecera.grid(row=0, column=1, padx=5, pady=5)

        # Título de la sección de estadísticas
        titulo = tk.Label(frameCabecera, text="Evaluación operación", font=("Georgia", 15, "bold"), bg ="#f2a6c2", relief="raised", borderwidth=3)
        titulo.pack(padx=3, pady=3, fill="x")

        # Descripción explicativa de la funcionalidad
        textoDescripcion = """En esta sección podrá realizar evaluaciones de las operaciones de la empresa.\nPara esto, ingrese dos fechas para obtener la información obtenida en ese periodo de tiempo."""
        descripcion = tk.Label(frameCabecera, text=textoDescripcion, font=("Georgia", 12), bg ="#fbcfe0", relief="sunken", borderwidth=2)
        descripcion.pack(padx=3, pady=3)

        # Obtiene las fechas mínima y máxima desde la clase Factura
        fechaMin = Factura.getFechaMin()
        fechaMax = Factura.getFechaMax()

        # Muestra el rango de fechas disponibles
        textoRangoFechas = "La fecha mínima es " + str(fechaMin) + " y la fecha máxima es " + str(fechaMax) + "\nSeleccione fechas que se encuentren dentro de este rango"
        lblRangoFechas = tk.Label(frameCabecera, text=textoRangoFechas, font=('Georgia', 10), bg ="#ffb0cb", fg="#000000", relief="sunken", borderwidth=2)
        lblRangoFechas.pack(pady=6)

        # Crea un marco para ingresar las fechas
        frameFechas = tk.Frame(self, bg="#ff8fc5", relief="raised", borderwidth=2)
        frameFechas.grid(row=1, column=1, padx=30, pady=5, sticky="nsew")

        # Configura el layout del marco de fechas
        for a in range(3):
            frameFechas.rowconfigure(a, weight=1)
        frameFechas.columnconfigure(0, weight=2)
        frameFechas.columnconfigure(1, weight=1)
        frameFechas.columnconfigure(2, weight=2)
        
        # Etiquetas y campos de entrada para las fechas
        lblFecha1 = tk.Label(frameFechas, text='Fecha 1', font=("Georgia", 12, "bold"), relief="raised", borderwidth=2, width=10)
        lblFecha1.grid(row=0, column=0, padx=1, pady=1)

        lblFecha2 = tk.Label(frameFechas, text='Fecha 2', font=("Georgia", 12, "bold"), relief="raised", borderwidth=2, width=10)
        lblFecha2.grid(row=1, column=0, padx=1, pady=1)
        
        self.fieldFecha1 = tk.Entry(frameFechas, font=("Georgia", 12), width=10)
        self.fieldFecha1.grid(row=0, column=2, pady=1)
        self.fieldFecha2 = tk.Entry(frameFechas, font=("Georgia", 12), width=10)
        self.fieldFecha2.grid(row=1, column=2, pady=1)

        # Botón para procesar las fechas ingresadas
        buttonIngresar = tk.Button(frameFechas, text="Ingresar", command=self.ingresar, font=("Georgia", 12, "bold"), relief="raised", borderwidth=2, width=10)
        buttonIngresar.grid(row=2, column=1, pady=10)

        # Crea un marco para mostrar las estadísticas
        self.frameEstadisticas = tk.Frame(self, bg="#ff8fc5", relief="raised", borderwidth=2)

        # Etiquetas y campos de texto para mostrar las estadísticas
        lblGananciasTotales = tk.Label(self.frameEstadisticas, text="Ganancias totales", font=("Georgia", 12, "bold"))
        lblGananciasTotales.grid(row=0, column=0, padx=5, pady=5)
        self.entryGananciasTotales = tk.Entry(self.frameEstadisticas, font=("Georgia", 12), state="readonly")
        self.entryGananciasTotales.grid(row=0, column=1, padx=5, pady=5)

        lblPromedioPorDia = tk.Label(self.frameEstadisticas, text="Promedio por día", font=("Georgia", 12, "bold"))
        lblPromedioPorDia.grid(row=1, column=0, padx=5, pady=5)
        self.entryPromedioPorDia = tk.Entry(self.frameEstadisticas, font=("Georgia", 12), state="readonly")
        self.entryPromedioPorDia.grid(row=1, column=1, padx=5, pady=5)

        # Botones para mostrar estadísticas adicionales
        buttonGananciasPorDia = tk.Button(self.frameEstadisticas, text="Ganancias por día", command=self.mostrarGananciasPorDia, font=("Georgia", 12, "bold"), relief="raised", borderwidth=2, width=20, bg= "#fbcfe0")
        buttonGananciasPorDia.grid(row=2, column=0, padx=5, pady=5)

        buttonMostrarPorcentajeAumento = tk.Button(self.frameEstadisticas, text="Porcentaje de aumento", command=self.mostrarPorcentajeAumento, font=("Georgia", 12, "bold"), relief="raised", borderwidth=2, width=20, bg= "#fbcfe0")
        buttonMostrarPorcentajeAumento.grid(row=2, column=1, padx=5, pady=5)

        # Marco para mostrar modas (información más repetida) después de calcular estadísticas
        self.frameModas = tk.Frame(self, bg="#ff8fc5", relief="raised", borderwidth=2)

    def ingresar(self):
        # Validación de que los campos de fecha no estén vacíos
        if self.fieldFecha1.get() == "" or self.fieldFecha2.get() == "":
            messagebox.showerror('Error', 'Debe llenar ambos campos de fecha')
            return
        else: 
            try:
                # Verifica si hay fechas disponibles para el análisis
                if not self.verificarFechasDisponibles():
                    messagebox.showerror('Error', 'No hay fechas para realizar la evaluación, realice algún envío para poder hacer uso de esta funcionalidad')
                    return

                campos_incorrectos = []
                # Captura las fechas ingresadas por el usuario
                fecha1 = self.fieldFecha1.get()
                fecha2 = self.fieldFecha2.get()

                # Verifica si las fechas contienen solo números enteros
                try:
                    fecha1 = int(fecha1)
                except ValueError:
                    campos_incorrectos.append('Fecha 1')

                try:
                    fecha2 = int(fecha2)
                except ValueError:
                    campos_incorrectos.append('Fecha 2')

                # Lanza una excepción si hay errores en los campos
                if campos_incorrectos:
                    raise NumerosEnteros(campos_incorrectos)

                # Obtiene el rango de fechas permitidas
                fecha1 = int(self.fieldFecha1.get())
                fecha2 = int(self.fieldFecha2.get())

                # Calcula las ganancias discretas entre las fechas ingresadas
                self.dict = Factura.gananciasPorDia(fecha1, fecha2)

                # Muestra las estadísticas en la interfaz
                self.frameEstadisticas.grid(row=2, column=0, columnspan=8)

                self.entryGananciasTotales.configure(state="normal")
                self.entryGananciasTotales.delete(0, tk.END)
                self.entryGananciasTotales.insert(0, str(Factura.ganancias(self.dict)))
                self.entryGananciasTotales.configure(state="readonly")

                self.entryPromedioPorDia.configure(state="normal")
                self.entryPromedioPorDia.delete(0, tk.END)
                self.entryPromedioPorDia.insert(0, str(Factura.promedioPorDia(self.dict)))
                self.entryPromedioPorDia.configure(state="readonly")

                # Muestra la moda (valores más repetidos) de las ganancias
                self.frameModas.grid(row=3, column=0, columnspan=8, padx=5, pady=5)

                fecha1 = int(self.fieldFecha1.get())
                fecha2 = int(self.fieldFecha2.get())

                tiendaModa = Factura.moda(fecha1, fecha2, "tienda")
                clienteModa = Factura.moda(fecha1, fecha2, "cliente")
                transporteModa = Factura.moda(fecha1, fecha2, "transporte")

                lblModaTienda = tk.Label(self.frameModas, text='Tienda más frecuente: ' + str(tiendaModa), font=("Georgia", 12))
                lblModaTienda.grid(row=0, column=0, padx=5, pady=5)

                lblModaTransporte = tk.Label(self.frameModas, text='Transporte más frecuente: ' + str(transporteModa), font=("Georgia", 12))
                lblModaTransporte.grid(row=1, column=0, padx=5, pady=5)

                lblModaCliente = tk.Label(self.frameModas, text='Cliente al que más se le vendió: ' + str(clienteModa), font=("Georgia", 12))
                lblModaCliente.grid(row=2, column=0, padx=5, pady=5)

            except FechasFueraDeRango:
                messagebox.showerror('Error', str(FechasFueraDeRango()) + f'. La fecha mínima es {Factura.getFechaMin()} y la máxima es {Factura.getFechaMax()}')

            except InicioMayorQueFin:
                messagebox.showerror('Error', str(InicioMayorQueFin()))

            except NumerosEnteros as e:
                messagebox.showerror('Error', str(e))

    def mostrarGananciasPorDia(self):
        # Crear la ventana principal
        ventana = tk.Tk()
        ventana.title("Ganancias por día")

        datos = [(k, v) for k, v in self.dict.items()]
        datos.sort()

        # Crear etiquetas para la cabecera
        lbl_dia_header = tk.Label(ventana, text="Día", font=("Georgia", 12, "bold"))
        lbl_dia_header.grid(row=0, column=0, padx=5, pady=5)

        lbl_ganancias_header = tk.Label(ventana, text="Ganancias", font=("Georgia", 12, "bold"))
        lbl_ganancias_header.grid(row=0, column=1, padx=5, pady=5)

        # Crear la tabla utilizando etiquetas
        for i, (dia, ganancias) in enumerate(datos):
            # Crear etiqueta para el día
            lbl_dia = tk.Label(ventana, text=dia, font=("Georgia", 12))
            lbl_dia.grid(row=i + 1, column=0, padx=5, pady=5)

            # Crear etiqueta para las ganancias
            lbl_ganancias = tk.Label(ventana, text=ganancias, font=("Georgia", 12))
            lbl_ganancias.grid(row=i + 1, column=1, padx=5, pady=5)

    def mostrarPorcentajeAumento(self):
        # Crear la ventana principal
        ventana = tk.Tk()
        ventana.title("Porcentaje de aumento")

        # Crear una lista de datos de ejemplo
        datos = [(k, str(v) + "%") for k, v in Factura.porcentajeDeAumento(self.dict).items()]
        datos.sort()

        # Crear etiquetas para la cabecera
        lbl_dia_header = tk.Label(ventana, text="Día", font=("Georgia", 12, "bold"))
        lbl_dia_header.grid(row=0, column=0, padx=5, pady=5)

        lbl_aumento_header = tk.Label(ventana, text="Porcentaje de aumento", font=("Georgia", 12, "bold"))
        lbl_aumento_header.grid(row=0, column=1, padx=5, pady=5)

        # Crear la tabla utilizando etiquetas
        for i, (dia, aumento) in enumerate(datos):
            # Crear etiqueta para el día
            lbl_dia = tk.Label(ventana, text=dia, font=("Georgia", 12))
            lbl_dia.grid(row=i + 1, column=0, padx=5, pady=5)

            # Crear etiqueta para el porcentaje de aumento
            lbl_aumento = tk.Label(ventana, text=aumento, font=("Georgia", 12))
            lbl_aumento.grid(row=i + 1, column=1, padx=5, pady=5)
    
    def verificarFechasDisponibles(self):
        # Verifica si existen fechas mínimas y máximas para los análisis
        try:
            Factura.getFechaMin()
            Factura.getFechaMax()
            return True
        except NoHayFechas:
            return False
