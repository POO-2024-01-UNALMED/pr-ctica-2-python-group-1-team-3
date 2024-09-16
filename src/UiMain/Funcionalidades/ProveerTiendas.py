import tkinter as tk
from tkinter import ttk, Frame, DISABLED,Entry,scrolledtext,messagebox
import sys
sys.path.append('../')  # Retrocede un nivel al directorio padre

# Importaciones de clases necesarias para la funcionalidad de la aplicación
from gestorAplicacion.externo.TipoTransporte import TipoTransporte
from gestorAplicacion.externo.Transporte import Transporte
from gestorAplicacion.empresa.Fabrica import Fabrica as fabrica
from gestorAplicacion.empleados.Transportador import Transportador 

# Importación de excepciones personalizadas para manejar errores específicos
from UiMain.excepciones.Categoria1.FaltaUno import FaltaUno
from UiMain.excepciones.Categoria1.Proveer0Productos import Proveer0Productos
from UiMain.excepciones.Categoria1.CantidadMayorA import CantidadMayorA
from UiMain.excepciones.Categoria2.SoloNumeros import SoloNumeros


class ProveerTiendas(Frame):
    # Variables de clase que almacenarán la tienda, producto, cantidad y tipo de transporte seleccionados
    tienda = None
    producto = None
    cantidadProducto = None
    tipoTransporte = None
    listaFiltradaTransportes = None
    
    def __init__(self, window): 
        super().__init__(window)
        self.config(bg="#f8d5e1") # Configuración del color de fondo del marco principal


        # Manejo de eventos
        def deshabilitarTienda(event):
            # Deshabilita el desplegable de tiendas para evitar cambios mientras se procesa
            desplegableTiendas.config(state='readonly')


        def rellenarCuadroDeTextoTienda(event):                    
            # Rellena el cuadro de texto con la información de la tienda seleccionada
            texto_widget.config(state=tk.NORMAL)  # Permite la edición del cuadro de texto
            desplegableProductos.config(state=tk.NORMAL)  # Habilita la selección de productos
            texto_widget.delete("1.0", tk.END)  # Limpia el cuadro de texto
            desplegableTransporte.set("")  # Resetea el desplegable de transporte
            ProveerTiendas.tipoTransporte = None  # Resetea el tipo de transporte seleccionado
            ProveerTiendas.tienda = encontrarObjeto(desplegableTiendas, fabrica.getListaFabricas()[0].getListaTiendas())[0]
            
            # Inserta la información de la tienda en el cuadro de texto
            cadenaDeTexto = ProveerTiendas.tienda.productosPorCategoria() + "\n" + ProveerTiendas.tienda.cantidadProductos()
            texto_widget.insert(tk.END, cadenaDeTexto)
            texto_widget.config(state=DISABLED)  # Deshabilita el cuadro de texto nuevamente


        def deshabilitarProductos(event):
            # Deshabilita el desplegable de productos si hay una tienda seleccionada
            if ProveerTiendas.tienda != None:
                desplegableProductos.config(state='readonly')


        def rellenarCuadroDeTextoProducto(event):                    
            # Rellena el cuadro de texto con la información del producto seleccionado
            texto_widgetProductos.config(state=tk.NORMAL)  # Permite la edición del cuadro de texto
            entradaProductosQa.config(state=tk.NORMAL)  # Habilita la entrada para cantidad de productos
            texto_widgetProductos.delete("1.0", tk.END)  # Limpia el cuadro de texto
            ProveerTiendas.producto = encontrarObjeto(desplegableProductos, fabrica.getListaFabricas()[0].getListaProductos())[0]
            
            # Inserta la información del producto en el cuadro de texto
            cadenaDeTexto = ProveerTiendas.producto.__str__()
            texto_widgetProductos.insert(tk.END, cadenaDeTexto)
            texto_widgetProductos.config(state=DISABLED)  # Deshabilita el cuadro de texto nuevamente


        def eventoEntry(event):                    
            # Maneja la entrada de cantidad de productos y verifica si la entrada es válida
            if event.keysym == "Return": # Ignora la tecla "Enter"
                return
            
            try:
                # Verifica si la entrada contiene letras y lanza una excepción si es así
                if event.char.isalpha():
                    entradaProductosQa.delete(0, tk.END)
                    # Lanzar la excepción SoloNumeros con el campo que causó el error
                    raise SoloNumeros("Cantidad de productos")
                else:
                    # Actualiza la lista de transportes según la cantidad de producto y su peso
                    desplegableTransporte.config(state=tk.NORMAL)
                    ProveerTiendas.cantidadProducto = entradaProductosQa.get()
                    ProveerTiendas.listaFiltradaTransportes = TipoTransporte.transporteSegunCarga(
                        ProveerTiendas.producto.getPeso() * float(ProveerTiendas.cantidadProducto)
                    )
                    desplegableTransporte['values'] = [x.value[0] for x in ProveerTiendas.listaFiltradaTransportes]
            
            except SoloNumeros as e:
                # Manejo de excepción: muestra un mensaje de error si la entrada contiene letras
                desplegableTransporte.config(state=DISABLED)
                entradaProductosQa.delete(0, tk.END)
                ProveerTiendas.cantidadProducto = None
                messagebox.showerror("Error", e)
            except ValueError:
                # Maneja errores cuando el valor ingresado no es un número
                messagebox.showerror("Error", "Valor no numérico ingresado.")
                entradaProductosQa.delete(0, tk.END)
                ProveerTiendas.cantidadProducto = None


        def deshabilitarTransporte(event):
            # Deshabilita el desplegable de transporte si la cantidad de productos es válida
            if ProveerTiendas.cantidadProducto != None:
                desplegableTransporte.config(state='readonly')


        def rellenarCuadroDeTextoTransporte(event):                    
            # Rellena el cuadro de texto con la información del transporte seleccionado
            texto_widgetTransporte.config(state=tk.NORMAL)
            texto_widgetTransporte.delete("1.0", tk.END)  # Limpia el cuadro de texto
            ProveerTiendas.tipoTransporte = list(filter(lambda x: x.value[0] == desplegableTransporte.get(), TipoTransporte))[0]
            cadenaDeTexto = ProveerTiendas.tipoTransporte.__str__()  # Inserta la información del transporte
            texto_widgetTransporte.insert(tk.END, cadenaDeTexto)
            botonEnviar.config(state="normal")  # Habilita el botón de envío
            texto_widgetTransporte.config(state=DISABLED)  # Deshabilita el cuadro de texto nuevamente


        def encontrarObjeto(comboBox,listaObjetos):
            # Busca el objeto correspondiente en la lista a partir del nombre seleccionado en el ComboBox
            nombre = comboBox.get()
            objeto = list(filter(lambda x: x.getNombre()==nombre,listaObjetos))
            return objeto
        

        def envio():
            # Lógica para gestionar el envío de productos a las tiendas
            try:
                # Verifica que todos los campos requeridos estén completos
                if any(var is None for var in (ProveerTiendas.tienda, ProveerTiendas.producto, ProveerTiendas.cantidadProducto, ProveerTiendas.tipoTransporte)):
                    raise FaltaUno
                elif entradaProductosQa.get()=='0':
                    raise Proveer0Productos
                elif ProveerTiendas.tienda.getCantidadPorCategoria()[ProveerTiendas.producto.getCategoria()]\
                -(ProveerTiendas.tienda.getProductosPorCategoria()[ProveerTiendas.producto.getCategoria()]+int(ProveerTiendas.cantidadProducto))<=0:
                    raise CantidadMayorA
                else:
                    # Proceso de envío y suministro del producto
                    listaProductos = fabrica.getListaFabricas()[0].cantidadProductos(int(ProveerTiendas.cantidadProducto),ProveerTiendas.producto)
                    transporte = Transporte(ProveerTiendas.tipoTransporte.value[0],ProveerTiendas.tipoTransporte.value[1],ProveerTiendas.tipoTransporte.value[2],Transportador.getListaTransportadores()[0])
                    transporte.suministrarProducto(ProveerTiendas.tienda,listaProductos)
                    ProveerTiendas.tienda.descargarProducto(transporte)
                    messagebox.showinfo("Proveer tiendas",f"La tienda {ProveerTiendas.tienda.getNombre()} ha sido surtida con {ProveerTiendas.cantidadProducto} unidades de {ProveerTiendas.producto.getNombre()}")
                    entradaProductosQa.delete(0, tk.END)

                    # Limpieza de campos
                    ProveerTiendas.tienda = None
                    ProveerTiendas.producto = None
                    ProveerTiendas.cantidadProducto = None
                    ProveerTiendas.tipoTransporte = None
                    ProveerTiendas.listaFiltradaTransportes = None
                    
                    # Resetear los widgets
                    desplegableTiendas.set('Seleccionar tienda')
                    desplegableProductos.set('Seleccionar producto')
                    entradaProductosQa.delete(0, tk.END)
                    desplegableTransporte.set('Seleccionar transporte')
                    texto_widget.config(state=tk.NORMAL)
                    texto_widget.delete('1.0', tk.END)
                    texto_widget.config(state=DISABLED)
                    texto_widgetProductos.config(state=tk.NORMAL)
                    texto_widgetProductos.delete('1.0', tk.END)
                    texto_widgetProductos.config(state=DISABLED)
                    texto_widgetTransporte.config(state=tk.NORMAL)
                    texto_widgetTransporte.delete('1.0', tk.END)
                    texto_widgetTransporte.config(state=DISABLED)
                    
                    # Deshabilitar botones y entradas según sea necesario
                    desplegableTiendas.config(state=tk.NORMAL)
                    desplegableProductos.config(state=DISABLED)
                    entradaProductosQa.config(state=DISABLED)
                    desplegableTransporte.config(state=DISABLED)
                    botonEnviar.config(state=DISABLED)

            except FaltaUno:
                messagebox.showerror("Error", FaltaUno())
            except Proveer0Productos:
                messagebox.showerror("Error", Proveer0Productos())
            except CantidadMayorA:
                messagebox.showerror("Error", CantidadMayorA())


        # Configuración de la interfaz gráfica
        # Configura el diseño de las filas y columnas para una distribución uniforme
        for i in range(5):
            self.rowconfigure(i, weight=1)

        # Distribución uniforme de columnas
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Marco para la cabecera con título y descripción
        frameCabecera = tk.Frame(self, bg="#f8d5e1")
        frameCabecera.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Configurar el peso de la fila y columna para centrar el marco
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Configurar el título de la ventana
        titulo = tk.Label(frameCabecera, text='Proveer tiendas', font=("Georgia", 15, "bold"), bg ="#f2a6c2", relief="raised", border=3 )
        titulo.pack(pady=3, fill="x")

        # Descripcioón de la funcionalidad
        textoDescripcion = """En esta sección podrá proveer a las tiendas con productos de la fábrica.\nPara esto, seleccione la tienda, el producto, la cantidad y el tipo de transporte."""
        descripcion = tk.Label(frameCabecera, text=textoDescripcion, font=("Georgia", 12), bg ="#fbcfe0", border=2,relief="sunken")
        descripcion.pack(pady=3)


        #TIENDAS
        predeterminadoTiendas = tk.StringVar(value='Seleccionar tienda')
        casillaTiendas = tk.Frame(self, width=100, height=200 ,bg="#ff8fc5",relief="raised",  border=2)
        casillaTiendas.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        stack = tk.Frame(casillaTiendas) 
        stack.pack(pady=3)

        #Etiqueta de tiendas
        textoTiedas = tk.Label(stack, text='Lista de tiendas',font=("Georgia", 12, "bold"),border=1,relief="sunken")
        textoTiedas.pack(side='top', anchor='center')
        desplegableTiendas = ttk.Combobox(stack, values=[x.getNombre() for x in fabrica.getListaFabricas()[0].getListaTiendas()], 
                                          textvariable=predeterminadoTiendas,state=tk.NORMAL)
        desplegableTiendas.pack(pady=5)

        # Crear una casilla para contener el cuadro de texto
        casillaTextoTiendas = tk.Frame(self, width=113, height=200)
        casillaTextoTiendas.grid(row=1, column=1, columnspan=1)

        # Crear un cuadro de texto para mostrar información
        informacion = "Aquí se mostrará la información de la tienda seleccionada."
        texto_widget = scrolledtext.ScrolledText(casillaTextoTiendas, width=32, height=8, bg="#f5a6db")
        texto_widget.pack(pady=5)
        
        # Agregar contenido al widget de texto
        texto_widget.insert(tk.END, informacion)
        texto_widget.configure(state=tk.DISABLED)

        desplegableTiendas.bind("<<ComboboxSelected>>",rellenarCuadroDeTextoTienda)
        desplegableTiendas.bind("<Button-1>",deshabilitarTienda)


        # PRODUCTOS
        predeterminadoProductos = tk.StringVar(value='Seleccionar producto')
        casillaProductos = tk.Frame(self, width=100, height=200, bg="#ff8fc5",relief="raised",  border=2)
        casillaProductos.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        stack = tk.Frame(casillaProductos)
        stack.pack()

        textoProductos = tk.Label(stack, text='Lista de Productos', font=("Georgia", 12, "bold"),border=1,relief="sunken")
        textoProductos.pack(pady=5)

        desplegableProductos = ttk.Combobox(stack, values=[x.getNombre() for x in fabrica.getListaFabricas()[0].getListaProductos()], textvariable=predeterminadoProductos,
                                            state=DISABLED,width=20)
        desplegableProductos.pack(pady=5)

        # Crear una casilla para contener el cuadro de texto
        casillaTextoProductos = tk.Frame(self, width=113, height=200)
        casillaTextoProductos.grid(row=2, column=1, columnspan=1)
        
        # Crear un cuadro de texto para mostrar información
        informacion = "Aquí se mostrará la información del producto seleccionado."
        texto_widgetProductos = tk.Text(casillaTextoProductos, width=30,height=5,bg="#f5a6db")
        texto_widgetProductos.pack(pady=5)
        
        # Agregar contenido al widget de texto
        texto_widgetProductos.insert(tk.END, informacion)
        texto_widgetProductos.configure(state=tk.DISABLED)

        desplegableProductos.bind("<<ComboboxSelected>>",rellenarCuadroDeTextoProducto)
        desplegableProductos.bind("<Button-1>",deshabilitarProductos)

        
        # Cantidad de productos
        casillaQaProductos = tk.Frame(self, width=113, height=200, bg="#ff8fc5",relief="raised",  border=2)
        casillaQaProductos.grid(row=2, column=2, sticky="ew")

        stack = tk.Frame(casillaQaProductos)
        stack.pack()

        textoProductosQa = tk.Label(stack, text='Cantidad de productos',font=("Georgia", 12, "bold"),border=1,relief="sunken")
        textoProductosQa.pack(side='top', anchor='center')

        entradaProductosQa = tk.Entry(stack)
        entradaProductosQa.pack(side='top', anchor='center')
        entradaProductosQa.configure(state=DISABLED)
        entradaProductosQa.bind("<KeyRelease>", eventoEntry)

        
        # TRANSPORTE
        predeterminadoTransporte = tk.StringVar(value='Seleccionar transporte')
        casillaTransporte = tk.Frame(self, width=100, height=200,bg="#ff8fc5",relief="raised",  border=2)
        casillaTransporte.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        stack = tk.Frame(casillaTransporte)
        stack.pack()

        textoTransporte = tk.Label(stack, text='Lista de Transporte', font=("Georgia", 12, "bold"),border=1,relief="sunken")
        textoTransporte.pack(pady=5)
        desplegableTransporte = ttk.Combobox(stack, values=["a"], textvariable=predeterminadoTransporte,
                                             state='readonly')
        desplegableTransporte.pack(pady=5)
        desplegableTransporte.configure(state=DISABLED)

        # Crear una casilla para contener el cuadro de texto
        casillaTextoTransporte = tk.Frame(self, width=113, height=200)
        casillaTextoTransporte.grid(row=2 + 1, column=1, columnspan=1)
        
        # Crear un cuadro de texto para mostrar información
        informacion = "Aquí se mostrará la información del transporte seleccionado."
        texto_widgetTransporte = tk.Text(casillaTextoTransporte, width=32, height=8, bg="#f5a6db")
        texto_widgetTransporte.pack(pady=5)
        
        # Agregar contenido al widget de texto
        texto_widgetTransporte.insert(tk.END, informacion)
        texto_widgetTransporte.configure(state=DISABLED)
        desplegableTransporte.bind("<<ComboboxSelected>>",rellenarCuadroDeTextoTransporte)
        desplegableTransporte.bind("<Button-1>",deshabilitarTransporte)
        
        
        # Boton de envio
        botonEnviar = tk.Button(self, text="Enviar",width=10, height=2, bg="#f682c5", font=("Franklin Gothic", 14, "bold"), fg="#ffffff",border=2,relief="raised",command=envio)
        botonEnviar.grid(row=4, column=1, sticky="ew")
        botonEnviar.config(state=DISABLED)
