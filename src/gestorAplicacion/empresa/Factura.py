#  Este módulo pertenece al paquete 'gestorAplicacion.empresa' y contiene la clase 'Factura' que representa las 
# transacciones de compra en la empresa. Esta clase es la encargada de registrar la información importante
# acerca de las ventas y gestionar las devoluciones de productos.
# 
# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero

import pickle

from UiMain.excepciones.Categoria1.InicioMayorQueFin import InicioMayorQueFin
from UiMain.excepciones.Categoria1.FechasFueraDeRango import FechasFueraDeRango
from UiMain.excepciones.Categoria1.NoHayFechas import NoHayFechas

class Factura:
    # La clase 'Factura' representa una factura de compra dentro del supermercado.
    #
    # Contiene información sobre la tienda, el cliente, el transporte, la fecha, la identificación de la compra,
    # el total de la factura, el operario responsable y la lista de productos comprados.
    #
    # Proporciona métodos para calcular el total de la factura, las ganancias por periodo, y obtener resúmenes de facturas y productos.
    #
    # Funcionalidades en las que se usa:
    #      - Evaluacion operacion
    #      - Devolucion de productos


    # ATRIBUTOS-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    serialVersionUID = 1  # Versión del serializado asociado a esta clase
    listaFacturas = []
    facturasCreadas = 0

    
    # CONSTRUCTORES--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self, tienda, cliente, transporte, listaProductos, fecha, operario):
        """
        Constructor que inicializa una nueva instancia de Factura con todos los parámetros especificados.
        
        :param tienda: La tienda asociada a la factura.
        :param cliente: El cliente que realizó la compra.
        :param transporte: El transporte utilizado para la entrega.
        :param listaProductos: La lista de productos comprados.
        :param fecha: La fecha de la compra (representada como un entero).
        :param operario: El operario que procesó la compra.
        """
        self.tienda = tienda
        self.cliente = cliente
        self.transporte = transporte
        self.listaProductos = listaProductos
        self.fecha = fecha
        self.operario = operario
        self.infoAtributos = {}

        self.infoAtributos["tienda"] = tienda
        self.infoAtributos["transporte"] = transporte
        self.infoAtributos["cliente"] = cliente

        self.total = self.calcularTotal()
        self.identificacionCompra = Factura.facturasCreadas + 1
        Factura.facturasCreadas += 1
        Factura.listaFacturas.append(self)


    # MÉTODOS -----------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def calcularTotal(self):
        """
        Calcula el precio total de la factura sumando los precios de los productos y el valor del envío.
        
        :return: El total de la factura incluyendo el costo de los productos y el envío.
        """
        totalCompra = sum([producto.getValor() for producto in self.listaProductos])
        return totalCompra + self.valorEnvio()

    
    def valorEnvio(self):
        """
        Calcula la tarifa de envío de una factura dependiendo del tipo de transporte seleccionado.
        
        :return: El costo del envío basado en el tipo de transporte.
        """
        return self.transporte.tipo[0].value[1]


    @staticmethod
    def facturasPorPeriodo(inicio, fin):
        """
        Obtiene una lista de facturas en un periodo específico.
        
        :param inicio: Fecha de inicio del periodo.
        :param fin: Fecha de fin del periodo.
        :return: Una lista de facturas dentro del periodo especificado.
        """
        return [factura for factura in Factura.listaFacturas if inicio <= factura.fecha <= fin]


    @staticmethod
    def gananciasPorDia(inicio, fin):
        """
        Obtiene las ganancias de cada fecha dentro del periodo ingresado como parámetro.
        
        :param inicio: Fecha de inicio del periodo.
        :param fin: Fecha de fin del periodo.
        :return: Un diccionario con las ganancias por día dentro del periodo especificado.
        """
        if(inicio < Factura.getFechaMin() or fin > Factura.getFechaMax()):
                raise FechasFueraDeRango

        if(inicio > fin):
            raise InicioMayorQueFin

        fechas = Factura.listaFechas(inicio, fin)
        facturas = Factura.facturasPorPeriodo(inicio, fin)
        dictGananciasDiscretas = {}

        for fecha in fechas:
            dictGananciasDiscretas[fecha] = 0.0

        for fecha in dictGananciasDiscretas.keys():
            for factura in facturas:
                if factura.fecha == fecha:
                    valorAnterior = dictGananciasDiscretas[fecha]
                    dictGananciasDiscretas[fecha] = valorAnterior + factura.getTotal()

        return dictGananciasDiscretas


    @staticmethod
    def ganancias(dictGananciasPorDia):
        """
        Obtiene las ganancias totales a partir de las ganancias por día.
        
        :param dictGananciasPorDia: Diccionario con las ganancias por día.
        :return: El total de las ganancias.
        """
        return sum(dictGananciasPorDia.values())


    @staticmethod
    def promedioPorDia(dictGananciasPorDia):
        """
        Obtiene el promedio de ganancias por día a partir de un diccionario de ganancias por día.
        
        :param dictGananciasPorDia: Diccionario con las ganancias por día.
        :return: El promedio de las ganancias por día.
        """
        return Factura.ganancias(dictGananciasPorDia) / len(dictGananciasPorDia)


    @staticmethod
    def porcentajeDeAumento(dictGananciasPorDia):
        """
        Obtiene el porcentaje de aumento de ganancias de cada fecha respecto a la fecha anterior.
        
        :param dictGananciasPorDia: Diccionario con las ganancias por día.
        :return: Un diccionario con el porcentaje de aumento de ganancias por día.
        """
        fechas = sorted(dictGananciasPorDia.keys())
        porcentajeDeAumento = {}

        for i in range(1, len(fechas)):
            valorActual = dictGananciasPorDia[fechas[i]]
            valorAnterior = dictGananciasPorDia[fechas[i - 1]]
            porcentajeDeAumento[fechas[i]] = ((valorActual - valorAnterior) / valorAnterior) * 100

        return porcentajeDeAumento


    @staticmethod
    def moda(inicio, fin, atributo):
        """
        Obtiene la moda de un atributo específico de las facturas en un periodo específico.
        
        :param inicio: Fecha de inicio del periodo.
        :param fin: Fecha de fin del periodo.
        :param atributo: Nombre del atributo a analizar.
        :return: La moda del atributo especificado en el periodo especificado.
        """
        facturas = Factura.facturasPorPeriodo(inicio, fin)
        objetos = [factura.getAtributos().get(atributo) for factura in facturas]
        return max(set(objetos), key=objetos.count)


    @staticmethod
    def listaFechas(inicio="", fin=""):
        """
        Devuelve una lista de fechas sin repetir de las facturas existentes en la listaFacturas.
        
        :param inicio: Fecha de inicio del periodo.
        :param fin: Fecha de fin del periodo.
        :return: Una lista de fechas sin repetir dentro del periodo especificado.
        """
        if inicio == "" and fin == "":

            listaFechas = []
            for factura in Factura.listaFacturas:
                if factura.fecha not in listaFechas:
                    listaFechas.append(factura.fecha)
            return listaFechas

        listaFechas = []
        for factura in Factura.listaFacturas:
            if factura.fecha >= inicio and factura.fecha <= fin and factura.fecha not in listaFechas:
                listaFechas.append(factura.fecha)
        return listaFechas


    @staticmethod
    def getFechaMin():
        """
        Obtiene la fecha más pequeña en la lista de fechas.
        
        :return: La fecha mínima en la lista de fechas.
        """
        fechas = Factura.listaFechas()
        if not fechas:
            raise NoHayFechas()
        return min(fechas)



    @staticmethod
    def getFechaMax():
        """
        Obtiene la fecha más grande en la lista de fechas.
        
        :return: La fecha máxima en la lista de fechas.
        """
        fechas = Factura.listaFechas()
        if not fechas:
            raise NoHayFechas()
        return max(fechas)


    def seleccionarProductoDevolver(self, opcion):
        """
        Obtiene el producto seleccionado por el cliente para devolver a la tienda.
        
        :param opcion: Número del producto a devolver (1-based).
        :return: El producto seleccionado correspondiente al número especificado, o None si el número no es válido.
        """
        if 0 < opcion <= len(self.listaProductos):  # Valida que la opción ingresada sea válida
            return self.listaProductos[opcion - 1]
        else:
            return None  # Para que no salga un error si el índice ingresado no es válido


    @staticmethod
    def mostrarFacturas():
        textoFactura = ""
        indice = 1
        for factura in Factura.listaFacturas:
            textoFactura += str(indice) + ". ID: " + str(factura.getId()) + " Cliente: " + factura.getCliente().getNombre() + "\n"
            indice += 1
        return textoFactura
    

    @staticmethod
    def seleccionarFactura(opcion):
        facturaSeleccionada = Factura.listaFacturas[opcion - 1]
        return facturaSeleccionada
    

    @staticmethod
    def mostrarProductosFacturas(productosFactura):
        textoSalida = ""
        indice = 1
        for producto in productosFactura:
            if producto.isDevuelto():
                textoSalida += str(indice) + ". Producto: " + producto.getNombre() + " (Devuelto)" + "\n"
                indice += 1
            else:
                textoSalida += str(indice) + ". Producto: " + producto.getNombre() + "\n"
                indice += 1
        return textoSalida


    # GETTERS Y SETTERS ----------------------------------------------------------------------------------------------------------------------------------------------------------------

    def getTienda(self):
        return self.tienda

    def setTienda(self, tienda):
        self.tienda = tienda

    def getCliente(self):
        return self.cliente

    def setCliente(self, cliente):
        self.cliente = cliente

    def getTransporte(self):
        return self.transporte

    def setTransporte(self, transporte):
        self.transporte = transporte

    def getFecha(self):
        return self.fecha

    def setFecha(self, fecha):
        self.fecha = fecha

    def getIdentificacionCompra(self):
        return self.identificacionCompra

    def setIdentificacionCompra(self, identificacionCompra):
        self.identificacionCompra = identificacionCompra

    def getTotal(self):
        return self.total

    def setTotal(self, total):
        self.total = total

    def getListaProductos(self):
        return self.listaProductos

    def setListaProductos(self, listaProductos):
        self.listaProductos = listaProductos

    @staticmethod
    def getListaFacturas():
        return Factura.listaFacturas

    @staticmethod
    def setListaFacturas(listaFacturas):
        Factura.listaFacturas = listaFacturas

    @staticmethod
    def getFacturasCreadas():
        return Factura.facturasCreadas

    @staticmethod
    def setFacturasCreadas(facturasCreadas):
        Factura.facturasCreadas = facturasCreadas

    def getOperario(self):
        return self.operario

    def setOperario(self, operario):
        self.operario = operario

    def getAtributos(self):
        return self.infoAtributos

    @staticmethod
    def getInfoAtributos():
        return Factura.infoAtributos

    @staticmethod
    def setInfoAtributos(infoAtributos):
        Factura.infoAtributos = infoAtributos
