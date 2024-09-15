# Este módulo pertenece al paquete 'gestorAplicacion.externo' y contiene la clase 'Cliente' que representa a los clientes que compran productos 
# en las diferentes tiendas. 
#  
# Esta clase implementa la interfaz 'Moda'.
#  
# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero

import pickle
from gestorAplicacion.empresa.Moda import Moda

class Cliente(Moda):
    #La clase 'Cliente' representa un cliente de la empresa.
    #  
    # Contiene información sobre el nombre, dirección, cuenta bancaria y los productos adquiridos por el cliente.
    #  
    # Proporciona métodos para gestionar estos atributos y para mostrar y seleccionar clientes.
    #  
    # Funcionalidades en las que se usa:
    #       - Envio pedidos


    # ATRIBUTOS ----------------------------------------------------------------------------------------------------------------------------------------------------
    
    _listaClientes = []  # Lista de clientes
    
    
    # CONSTRUCTORES ------------------------------------------------------------------------------------------------------------------------------------------------
    
    def __init__(self, nombre, direccion, cuentaBancaria):
        """
        Constructor que recibe todos los parámetros.

        :param nombre: Nombre del cliente
        :param direccion: Dirección del cliente
        :param cuentaBancaria: Cuenta bancaria del cliente
        """
        self._nombre = nombre
        self._direccion = direccion
        self._cuentaBancaria = cuentaBancaria
        self._productos = []
        Cliente._listaClientes.append(self)


    # MÉTODOS ------------------------------------------------------------------------------------------------------------------------------------------------------
    
    @staticmethod
    def mostrarClientes():
        """
        Muestra todos los objetos de tipo Cliente que han sido creados.

        :return: Una cadena de texto con información sobre todos los clientes creados.
        
        Funcionalidades en las que se usa: Envío pedidos
        """
        mensaje = ""
        numero = 1
        for cliente in Cliente._listaClientes:
            if cliente.getNombre() not in mensaje:
                mensaje += f"{numero}. {cliente}\n"  # Se hace uso del método __str__() para obtener la representación del objeto
                numero += 1
        return mensaje


    @staticmethod
    def seleccionarCliente(indice):
        """
        Permite que se elija alguno de los objetos tipo Cliente que han sido creados para interactuar con él.

        :param indice: Índice del cliente a seleccionar (indice - 1).
        :return: El cliente seleccionado correspondiente al índice proporcionado, o None si el índice no es válido.
        """
        clienteSeleccionado = None
        # El ciclo while en caso de que retorne None debe estar en el main
        if indice - 1 >= 0 and indice <= len(Cliente._listaClientes):
            indice = indice - 1
            clienteSeleccionado = Cliente._listaClientes.pop(indice)
        else:
            return clienteSeleccionado
        return clienteSeleccionado


    def __str__(self):
        """
        Genera una representación en cadena del objeto Cliente.

        :return: Una cadena de texto con la información del cliente, incluyendo nombre y dirección.
        """
        return f"{self.getNombre()} - Dirección: {self.getDireccion()}"


    # GETTERS Y SETTERS --------------------------------------------------------------------------------------------------------------------------------------------
    
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getDireccion(self):
        return self._direccion

    def setDireccion(self, direccion):
        self._direccion = direccion

    def getCuentaBancaria(self):
        return self._cuentaBancaria

    def setCuentaBancaria(self, cuentaBancaria):
        self._cuentaBancaria = cuentaBancaria

    def getProductos(self):
        if self._productos is None:
            self._productos = []
        return self._productos

    def setProductos(self, productos):
        self._productos = productos

    @classmethod
    def getListaClientes(cls):
        return cls._listaClientes

    @classmethod
    def setListaClientes(cls, listaClientes):
        cls._listaClientes = listaClientes

    @staticmethod
    def getNextID():
        return len(Cliente._listaClientes) + 1