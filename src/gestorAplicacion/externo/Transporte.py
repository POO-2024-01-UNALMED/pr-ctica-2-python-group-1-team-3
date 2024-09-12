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

from gestorAplicacion.empleados import Transportador
from gestorAplicacion.externo.TipoTransporte import TipoTransporte

#from gestorAplicacion.externo.TipoTransporte import TipoTransporte

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

    lista_transportes = []

    def __init__(self, tipo: TipoTransporte, capacidad, costo, transportador):
        self.tipo = tipo
        self.capacidad = capacidad
        self.costo = costo
        self.transportador = transportador
        self.tienda = None
        self.lista_de_productos = []
        Transporte.lista_transportes.append(self)

    def suministrarProducto(self, tienda, lista_de_productos):
        self.tienda = tienda
        self.lista_de_productos = lista_de_productos
    
    def tipoTransporte(self, tipoTransporte):
        textoTipoTransporte = f"Tipo de transporte: {tipoTransporte.value}, Precio: {tipoTransporte.precio_envio}, Capacidad máxima: {tipoTransporte.capacidad_max}"
        return textoTipoTransporte

    def __str__(self):
        return f"Transporte: {self.tipo}, Conductor: {self.transportador}, Capacidad: {self.capacidad}, Costo: {self.costo}"

    @classmethod
    def mostrar_transportes(cls):
        return [str(transporte) for transporte in cls.lista_transportes]

    

    # Getters
    def getTipo(self):
        return self.tipo

    def getTransportador(self):
        return self.transportador

    def getCapacidad(self):
        return self.capacidad

    def getCosto(self):
        return self.costo

    def getListaDeProductos(self):
        return self.lista_de_productos

    # Setters
    def setTipo(self, tipo):
        self.tipo = tipo

    def setTransportador(self, transportador):
        self.transportador = transportador

    def setCapacidad(self, capacidad):
        self.capacidad = capacidad

    def setCosto(self, costo):
        self.costo = costo

    def setListaDeProductos(self, lista_de_productos):
        self.lista_de_productos = lista_de_productos
    
    @classmethod
    def setListaTransportes(cls, lista_transportes):
        cls.lista_transportes = lista_transportes

    @classmethod
    def getListaTransportes(cls):
        return cls.lista_transportes