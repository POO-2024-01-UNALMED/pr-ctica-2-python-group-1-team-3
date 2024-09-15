import tkinter as tk
from tkinter import ttk, Frame, messagebox
import sys
sys.path.append('../')  # Retrocede un nivel al directorio padre

# Importación de módulos relacionados con excepciones y clases específicas
from UiMain.excepciones.Categoria1.NoTrabajadores import NoTrabajadores
from gestorAplicacion.empresa.Factura import Factura
from gestorAplicacion.empresa.Fabrica import Fabrica
from gestorAplicacion.externo.CuentaBancaria import CuentaBancaria
from gestorAplicacion.empleados.Operario import Operario
from gestorAplicacion.empleados.Vendedor import Vendedor
from gestorAplicacion.empleados.Transportador import Transportador

class PagoDeNomina(Frame):
    def _init_(self, window):
        super()._init_(window)

        # Configuración de la ventana
        self.config(bg="#f8d5e1")

        # Lista de facturas obtenida de la clase Factura
        listaFacturas = Factura.getListaFacturas()


        # Manejo de eventos
        # Evento cuando se selecciona un tipo de trabajador en el desplegable
        def opcionTipoTrabajador(evento):
            global listaMostrar
            global num

            # Obtener la opción seleccionada del desplegable
            opc = desplegableTipos.get()

            # Asignar un valor numérico según el tipo de trabajador seleccionado
            if opc == "Transportadores":
                num = 2
            elif opc == "Operarios":
                num = 1
            elif opc == "Vendedores":
                num = 3
            else:
                frameTipos12.grid_remove()
                desplegableTrabajadores['values'] = ()

            # Obtener la lista de trabajadores involucrados en las facturas
            listaMostrar = Fabrica.TrabajadoresInvolucrados(listaFacturas, num)
            values = [trabajador.getNombre() for trabajador in listaMostrar]

            # Excepción si no hay trabajadores disponibles
            try:
                if not values:
                    raise NoTrabajadores()
                else:
                    # Actualizar el desplegable con los nombres de los trabajadores
                    desplegableTrabajadores['values'] = list(set(values))
                    frameTipos12.grid()
            except NoTrabajadores:
                messagebox.showerror("No es posible realizar el pago", NoTrabajadores())


        # Evento cuando se selecciona un trabajador del desplegable
        def opcionTrabajador(evento):
            global trabajadorEscogido
            global pagoTrabajo
            global pagoMeta
            pagoMeta = 0

            # Obtener el trabajador seleccionado
            opc = desplegableTrabajadores.get()

            # Encontrar al trabajador en la lista y asignarlo a la variable global
            for trabajador in listaMostrar:
                if trabajador.getNombre() == opc:
                    trabajadorEscogido = trabajador
            
            # Mostrar información del trabajador
            datosTrabajador.config(text=trabajadorEscogido._str_())

            # Calcular el pago por trabajo y mostrarlo
            pagoTrabajo = CuentaBancaria.calcularPago(trabajadorEscogido)
            textoInfoTrabajador = f"Al trabajador seleccionado se le pagará ${pagoTrabajo} por trabajar {trabajadorEscogido.getTrabajo()} veces"
            infoTrabajador.config(text=textoInfoTrabajador)

            frameInfo.grid()


        # Evento para analizar y bonificar metas
        def opcionMetaSi():
            
            global listaMetas

            # Obtener las metas según el tipo de trabajador
            if num == 1:
                listaMetas = Operario.getMetasOperario()
                textoIndice = "Indice: Cantidad de productos vendidos\n"
            elif num == 2:
                listaMetas = Transportador.getMetasTransportador()
                textoIndice = "Indice: Peso de los productos transportados\n"
            elif num == 3:
                listaMetas = Vendedor.getMetasVendedor()
                textoIndice = "Indice: Cantidad de productos vendidos\n"

            # Mostrar las metas
            textoMetasTrabajador = textoIndice
            for i in range(len(listaMetas)):
                textoMetasTrabajador += f"Meta {i+1}"
                textoMetasTrabajador += listaMetas[i]._str_() + "\n"

            textoMetas.config(text=textoMetasTrabajador)
            frameMetas.grid()

            # Deshabilitar los desplegables
            desplegableTipos.config(state='disabled')
            desplegableTrabajadores.config(state='disabled')


        # Evento cuando se selecciona una meta del desplegable
        def opcionMeta(evento):
            global posicionMeta
            global pagoMeta
            opc = desplegableMetas.get()
            cumple = ""

            # Identificar la meta seleccionada
            if opc == "Meta 1":
                posicionMeta = 0
                metaEscogida = listaMetas[0]
            
            elif opc == "Meta 2":
                posicionMeta = 1
                metaEscogida = listaMetas[1]

            # Verificar si el trabajador cumple la meta y calcular el porcentaje de cumplimiento
            indice = trabajadorEscogido.getIndiceMeta()
            verificadorMeta = metaEscogida.cumplioMeta(indice)
            estadisticasMeta = metaEscogida.porcentajeCumplimiento(indice)

            # Revisar si ya ha recibido la bonificación por esta meta
            listaVerificadores = trabajadorEscogido.getVerificadorMetasCumplidas()
            if not listaVerificadores[posicionMeta]:
                if verificadorMeta:
                    pagoMeta = metaEscogida.getComision()
                    cumple = "Meta cumplida\n"
                textoInfoMeta.config(text=cumple + estadisticasMeta)
            else:
                textoInfoMeta.config(text="""La bonificación por esta meta ya ha sido dada,\nseleccione otra opción de meta o realice el pago""")

            frameMetas2.grid()
            botonPago.grid()


        # Evento para proceder con el pago
        def opcionPago():
            trabajadorEscogido.recibirPagos(pagoTrabajo + pagoMeta)
            messagebox.showinfo(f"Pago exitoso", f"Comprobante de pago\nPago asociado a los envios realizados: {pagoTrabajo}\nPago asociado al cumplimiento de metas: {pagoMeta}\nTotal: {pagoTrabajo + pagoMeta}")

            # Restablecer valores y limpiar la interfaz para el siguiente trabajador
            trabajadorEscogido.setTrabajo(0)
            if pagoMeta != 0:
                trabajadorEscogido.getVerificadorMetasCumplidas()[posicionMeta] = True

            # Habilitar nuevamente los desplegables
            desplegableTipos.config(state='readonly')
            desplegableTrabajadores.config(state='readonly')

            # Limpiar los cuadros y remover frames de la interfaz
            desplegableTipos.set('')
            desplegableTrabajadores.set('')
            frameTipos12.grid_remove()
            frameInfo.grid_remove()
            desplegableMetas.set('')
            frameMetas.grid_remove()
            textoInfoMeta.config(text="")
            frameMetas2.grid_remove()
            botonPago.grid_remove()

        # Divisiones en filas y columnas de la ventana
        for i in range(12):
            self.rowconfigure(i, weight=1)
        for j in range(4):
            self.columnconfigure(j, weight=1)

        # Título
        frameCabecera = tk.Frame(self, bg="#f8d5e1")
        frameCabecera.grid(row=0, column=1, columnspan=2, padx=3, pady=3)
        titulo = tk.Label(frameCabecera, text='Pago de nomina', font=("Georgia", 15, "bold"), bg="#f2a6c2", relief="raised", border=3)
        titulo.pack(fill="x", pady=3, padx=4)

        #Descripción
        textoDescripcion = """En esta sección podrá pagar a los trabajadores por el trabajo que han realizado.\nPara esto, seleccione alguno de los trabajadores disponibles y realizarles el pago por las horas trabajadas. \nAdemás, podrá verificar si han cumplido alguna meta y darles bonificaciones por ello."""
        descripcion = tk.Label(frameCabecera, text=textoDescripcion, font=("Georgia", 12), bg="#fbcfe0", border=2, relief="sunken")
        descripcion.pack(pady=2, padx=4)

        # Trabajadores
        # Tipo de trabajador
        frameTipos1 = tk.Frame(self, bg="#f2a6c2", relief="raised", border=2)
        frameTipos1.grid(row=1, column=1, columnspan=2, padx=20, pady=20)

        frameTipos11 = tk.Frame(frameTipos1, relief="raised", border=2)
        frameTipos11.grid(row=1, column=1, padx=20, pady=20)

        textoTipos = tk.Label(frameTipos11, text='Tipos de trabajadores', font=("Georgia", 11, "bold"))
        textoTipos.pack(side='top', anchor='center', pady=3, padx=3)

        tipoPredeterminado = tk.StringVar(value='Seleccionar tipo')
        desplegableTipos = ttk.Combobox(frameTipos11, values=["Operarios", "Transportadores", "Vendedores"], textvariable=tipoPredeterminado, state='readonly')
        desplegableTipos.pack(side='top', anchor='center', pady=3, padx=3)
        desplegableTipos.bind("<<ComboboxSelected>>", opcionTipoTrabajador)

        # Selección del trabajador
        frameTipos12 = tk.Frame(frameTipos1, relief="raised", border=2)
        frameTipos12.grid(row=1, column=2, padx=20, pady=5)
        frameTipos12.grid_remove()

        textoTrabajadores = tk.Label(frameTipos12, text='Trabajadores', font=("Georgia", 11, "bold"))
        textoTrabajadores.pack(side='top', anchor='center', pady=3, padx=3)

        trabajadorPredeterminado = tk.StringVar(value='Seleccionar trabajador')
        desplegableTrabajadores = ttk.Combobox(frameTipos12, values=[], textvariable=trabajadorPredeterminado, state='readonly')
        desplegableTrabajadores.pack(side='top', anchor='center', pady=3, padx=3)
        desplegableTrabajadores.bind("<<ComboboxSelected>>", opcionTrabajador)


        # Realización del pago y bonificación por metas
        # Información del trabajador
        frameInfo = tk.Frame(self, bg="#f2a6c2", relief="raised", border=2)
        frameInfo.grid(row=2, column=1, columnspan=2, padx=5, pady=5)
        frameInfo.grid_remove()

        datosTrabajador = tk.Label(frameInfo, text='', font=("Georgia", 9, "bold"))
        datosTrabajador.pack(side='top', anchor='center', pady=3, padx=3)

        infoTrabajador = tk.Label(frameInfo, text='', font=("Georgia", 9))
        infoTrabajador.pack(side='top', anchor='center', pady=3, padx=3)


        # Analisis de metas cumplidas
        pregunta = "¿Desea analizar y bonificar al trabajador por sus metas cumplidas?"
        textoPregunta = tk.Label(frameInfo, text=pregunta, font=("Georgia", 9, "bold"), border=2,relief="sunken" )
        textoPregunta.pack(pady=3, padx=3)

        frameInfoBotones = tk.Frame(frameInfo, border=2,relief="sunken")
        frameInfoBotones.pack(pady=6, padx=3)

        #Botón Sí
        botonSi = tk.Button(frameInfoBotones, text="Sí, deseo analizar las metas", font=("Georgia", 9), bg="#f682c5", command=opcionMetaSi)
        botonSi.pack(side="left", padx=10)

        # Botón No
        textPago = """No, deseo proceder al pago"""
        botonNo = tk.Button(frameInfoBotones, text=textPago, font=("Georgia", 9), bg="#f682c5", command=opcionPago)
        botonNo.pack(side="right", padx=10)


        # Metas
        # Verificar si el trabajador cumplió alguna meta
        frameMetas = tk.Frame(self, bg="#f2a6c2", relief="raised", border=2)
        frameMetas.grid(row=3, column=1, columnspan=2, rowspan=3, padx=5, pady=5)
        frameMetas.grid_remove()

        # Metas dependiendo del tipo de trabajador
        textoMetas = tk.Label(frameMetas, text='', font=("Georgia", 9))
        textoMetas.grid(row=3, column=1, columnspan=3, pady=5, padx=5)

        #Elegir la meta a bonificar
        frameMetas1 = tk.Frame(frameMetas, bg="#f2a6c2", relief="raised", border=2)
        frameMetas1.grid(row=4, column=1, padx=5, pady=5)

        textoTituloMetas = tk.Label(frameMetas1, text='Metas', font=("Georgia", 9, "bold"))
        textoTituloMetas.pack(side='top', anchor='center', padx=2, pady=2)

        metasPredeterminada = tk.StringVar(value='Seleccionar meta')
        desplegableMetas = ttk.Combobox(frameMetas1, values=["Meta 1", "Meta 2"], textvariable=metasPredeterminada, state='readonly')
        desplegableMetas.pack(side='top', anchor='center', padx=2, pady=2)
        desplegableMetas.bind("<<ComboboxSelected>>", opcionMeta)

        #Información de la meta
        frameMetas2 = tk.Frame(frameMetas)
        frameMetas2.grid(row=4, column=4, padx=5, pady=5)
        frameMetas2.grid_remove()  # Oculta el frame hasta que se seleccione una meta

        textoInfoMeta= tk.Label(frameMetas2,font=("Georgia", 9), border=2,relief="sunken")
        textoInfoMeta.pack(anchor='center')

        # Botón para proceder al pago
        botonPago = tk.Button(frameMetas, text='Pagar', font=("Georgia", 11), command=opcionPago)
        botonPago.grid(row=5, column=1, columnspan=2, padx=5, pady=5)
        botonPago.grid_remove()