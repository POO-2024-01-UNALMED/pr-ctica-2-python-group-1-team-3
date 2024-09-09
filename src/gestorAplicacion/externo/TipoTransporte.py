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

    # NOMBRE = (precioEnvio_COP, capacidad_KG, "Nombre")
    CAMINANDO = (1000, 5, "Caminando")
    BICICLETA = (2000, 8, "Bicicleta")
    MOTO = (5000, 10, "Moto")
    CARRO = (10000, 30, "Carro")
    CAMION = (50000, 100, "Camion")
    AVION = (500000, 1000, "Avion")


    # CONSTRUCTOR ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self, precioEnvio_COP, capacidad_KG, nombre):
        self.precioEnvio_COP = precioEnvio_COP
        self.capacidad_KG = capacidad_KG
        self.nombre = nombre


    # MÉTODOS ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    @classmethod
    def transporteSegunCarga(cls, PesoTotalProductos):
        """
        Verifica qué tipos de transporte son aptos según el peso de los productos a enviar.
        
        @param PesoTotalProductos: Peso total de los productos a enviar
        @return: Una lista de tipos de transporte que pueden manejar el peso total de los productos
        
        Funcionalidades en las que se usa: Envio pedidos
        """
        transportesPosibles = []
        try:
            for tipoTransporte in TipoTransporte:
                CargaTipoTrans = 0
                CargaTipoTrans = tipoTransporte.value[2]
                if CargaTipoTrans >= PesoTotalProductos:
                    transportesPosibles.append(tipoTransporte)
        except TypeError:
            pass
        return transportesPosibles
    

    @staticmethod
    def mostrarTransporteSegunCarga():
        """
        Muestra los tipos de transporte disponibles según la carga.
        
        @param transportesPosibles: Lista de tipos de transporte posibles
        @return: Una cadena de texto con información sobre los tipos de transporte disponibles
        
        Funcionalidades en las que se usa: Envio pedidos
        """

        cadenaTexto = ""
        
        for tipoTransporte in TipoTransporte:
            cadenaTexto+=(tipoTransporte.value[0])
            cadenaTexto+=("\n")
        return cadenaTexto
    

    @staticmethod
    def mostrarTransportes():
        cadenaTexto = ""
        
        for tipoTransporte in TipoTransporte:
            cadenaTexto+=(tipoTransporte.value[0])
            cadenaTexto+=("\n")
        return cadenaTexto
    
    def getPrecioOriginalTransporte(self):
        return self.precioEnvio_COP

    @staticmethod
    def enviarGratis(transporteSeleccionado):
        """
        Cambia el valor del envío a 0.
        
        @param transporteSeleccionado: Transporte al que se le cambiará el precio del envío
        @return: El objeto transporte con el precio del envío cambiado a 0
        
        Funcionalidades en las que se usa: Envio pedidos
        """
        transporteSeleccionado.tipo.precioEnvio_COP = 0
        return transporteSeleccionado


    def recordarPrecioTransporte(self):
        """
        Guarda el valor del precio de envío en la variable precioTransporte.
        
        Funcionalidades en las que se usa: Envio pedidos
        """
        self.precioOriginalTransporte = self.precioEnvio_COP

    def reestablecerPrecioTransporte(self):
        """
        Guarda en precioEnvio el valor que está en precioTransporte.
        
        Funcionalidades en las que se usa: Envio pedidos
        """
        self.precioEnvio_COP = 0

    def __str__(self):
        """
        Genera una representación en cadena del tipo de transporte.
        
        @return: Una cadena de texto con el nombre del tipo de transporte
        """
        return self.nombre