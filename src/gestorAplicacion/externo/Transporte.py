"""
Este módulo pertenece al paquete 'gestorAplicacion.externo' y contiene la clase 'Transporte' que representa un transporte 
con sus atributos y métodos para su manipulación.
 
Esta clase gestiona el transporte de productos, representando los diferentes medios de transporte que se pueden utilizar 
para realizar el transporte de los productos. 

Esta clase implementa la interfaz 'Moda'.

AUTORES: - Sebastian Estrada Villa
         - Valentina Luján Robledo
         - Santiago Ochoa Quintero
"""

from enum import Enum

from gestorAplicacion.externo.TipoTransporte import TipoTransporte

class Transporte:
    """
    La clase 'Transporte' representa un medio de transporte dentro de la empresa.
    
    Contiene información sobre el tipo de transporte, su capacidad, costo, transportador asignado, y los productos transportados.
    
    Proporciona métodos para gestionar estos atributos y para realizar operaciones como suministrar productos,
    mostrar tipos de transporte y enviar productos gratis.
    
    Funcionalidades en las que se usa:
        - Envio pedidos
        - Proveer tiendas
    """
    
    # ATRIBUTOS ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    listaTransportes = []


    # CONSTRUCTOR ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def __init__(self, tipo: TipoTransporte, capacidad, costo, transportador):
        """
        Constructor que recibe todos los parámetros.
        
        @param tipo: Tipo de transporte
        @param capacidad: Capacidad de carga del transporte
        @param costo: Costo del transporte
        @param transportador: Transportador asignado al transporte
        """
        #self.tipoTransporte = tipo
        self.capacidad = capacidad 
        self.costo = costo
        self.transportador = transportador
        self.listaTransportes = []
        self.tienda = None
        self.listaDeProductos = []
        self.tipo: TipoTransporte = tipo
        self.listaTransportes.append(self)


    # MÉETODOS -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def suministrarProducto(self, tienda, listaDeProductos):
        """
        Lleva los productos al transporte seleccionado y asigna la tienda a la que se enviarán.
        
        @param tienda: Tienda a la que se enviarán los productos
        @param listaDeProductos: Lista de productos a transportar
        
        Funcionalidades en las que se usa: Proveer tiendas
        """
        self.tienda = tienda
        self.listaDeProductos = listaDeProductos


    def tipoTransporte(self, tipoTransporte):
        """
        Genera una cadena de texto con el nombre, precio y capacidad de un tipo de transporte.
        
        @param tipoTransporte: Tipo de transporte a mostrar
        @return: Una cadena de texto con la información del tipo de transporte
        """
        textoTipoTransporte = f"Tipo de transporte: {tipoTransporte.value}, Precio: {tipoTransporte.precioEnvio_COP()}, Capacidad máxima: {tipoTransporte.capacidad_KG()}"
        return textoTipoTransporte

    def __str__(self):
        return self.tipo.name


    # GETTERS Y SETTERS -----------------------------------------------------------------------------------------------------------------------------------------------------------

    @classmethod
    def getListaTransportes(cls):
        return cls.listaTransportes

    @classmethod
    def setListaTransportes(cls, listaTransportes):
        cls.listaTransportes = listaTransportes

    def getCapacidad(self):
        return self.capacidad

    def setCapacidad(self, capacidad):
        self.capacidad = capacidad

    def getCosto(self):
        return self.costo

    def setCosto(self, costo):
        self.costo = costo

    def getTransportador(self):
        return self.transportador

    def setTransportador(self, transportador):
        self.transportador = transportador

    def getTienda(self):
        return self.tienda

    def setTienda(self, tienda):
        self.tienda = tienda

    def getListaDeProductos(self):
        return self.listaDeProductos

    def setListaDeProductos(self, listaDeProductos):
        self.listaDeProductos = listaDeProductos
    
    def getNombre(self):
        return self.tipo.name

    def getTipoTransporte(self):
        return self.tipo

    def setTipoTransporte(self, tipo):
        self.tipo = tipo
