"""
Este módulo pertenece al paquete 'gestorAplicacion.externo' y contiene una enumeración para representar
los diferentes tipos de transporte y sus atributos. Incluye la clase 'TipoTransporte' que define los diferentes
tipos de transporte, sus capacidades y costos.

AUTORES: - Sebastian Estrada Villa
         - Valentina Luján Robledo
         - Santiago Ochoa Quintero
"""

from enum import Enum
#from gestorAplicacion.empleados.Transportador import Transportador
#from gestorAplicacion.externo.Transporte import Transporte

class TipoTransporte(Enum):
    """
    La enumeración 'TipoTransporte' representa los diferentes tipos de transporte disponibles.
    
    Contiene información sobre el costo de envío, la capacidad de carga y el nombre del transporte.
    
    Proporciona métodos para gestionar estos atributos y seleccionar el transporte adecuado según la carga.
    
    Funcionalidades en las que se usa:
        - Envio pedidos
    """
    
    # CONSTANTES ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    CAMINANDO = ("Caminando", 1000, 5)
    BICICLETA = ("Bicicleta", 2000, 8)
    MOTO = ("Moto", 5000, 10)
    CARRO = ("Carro", 10000, 30)
    CAMION = ("Camión", 50000, 100)
    AVION = ("Avión", 500000, 1000)

    def __init__(self, nombre, precio_envio, capacidad):
        self.nombre = nombre
        self.precio_envio = precio_envio
        self.capacidad = capacidad

    @classmethod
    def transporteSegunCarga(cls, peso_total_productos):
        listaTransFiltrada = []
        try:
            for tipoTransporte in TipoTransporte:
                CargaTipoTrans = 0
                CargaTipoTrans = tipoTransporte.value[2]
                if CargaTipoTrans >= peso_total_productos:
                    listaTransFiltrada.append(tipoTransporte)
        except TypeError:
            pass
        return listaTransFiltrada

    def __str__(self):
        return f"Tipo: {self.nombre}, Precio: {self.precio_envio}, Capacidad: {self.capacidad}"

    @staticmethod
    def mostrarTransportes():
        cadenaTexto = ""
        
        for tipoTransporte in TipoTransporte:
            cadenaTexto+=(tipoTransporte.value[0])
            cadenaTexto+=("\n")
        return cadenaTexto

    @staticmethod
    def mostrarTransportesSegunCarga():
        cadenaTexto = ""
        
        for tipoTransporte in TipoTransporte:
            cadenaTexto+=(tipoTransporte.value[0])
            cadenaTexto+=("\n")
        return cadenaTexto
    
    @classmethod
    def enviarGratis(cls, transporteSeleccionado):
        transporteSeleccionado.tipo.precio_envio = 0
        return transporteSeleccionado

    @classmethod
    def recordarPrecioTransporte(cls):
        cls.precioOriginalTransporte = cls.tipo.precio_envio
   

    @classmethod
    def reestablecerPrecioTrans(cls):
        cls.tipo.precio_envio = cls.precioOriginalTransporte


    def getPrecioOriginalTransporte(self):
        return self.capacidad

    def getCapacidad(self):
        return self.capacidad
