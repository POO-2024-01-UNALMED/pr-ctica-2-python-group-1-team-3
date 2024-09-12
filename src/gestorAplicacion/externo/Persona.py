"""
Este módulo contiene la clase abstracta 'Persona' que representa una persona con sus atributos y métodos para su manipulación.
    
Esta clase representa la clase base para 'Operario', 'Transportador' y 'Vendedor'.
    
AUTORES: - Sebastian Estrada Villa
         - Valentina Luján Robledo
         - Santiago Ochoa Quintero
"""
from abc import ABC, abstractmethod

class Persona(ABC):
    """
    La clase abstracta `Persona` representa una persona dentro de la empresa. 
  
    Esta proporciona atributos y métodos para la creación de los diferentes empleados de la empresa.
  
    Contiene información sobre el nombre, edad, identificación, cuenta bancaria, trabajado, y cumplimiento de metas.
   
    Funcionalidades en las que se usa:
         - Pago de nomina
    """
    
    # ATRIBUTOS DE CLASE ----------------------------------------------------------------------------------------------------------------------

    personasTotales = 0
    listaPersonas = []
    SALARIO = 50000


    # CONSTRUCTORES ----------------------------------------------------------------------------------------------------------------------
    def __init__(self, nombre, edad, cedula, cuentaBancaria):
        """
        Constructor que recibe todos los parámetros.
        
        :param nombre: Nombre de la persona
        :param edad: Edad de la persona
        :param cedula: Identificación de la persona
        :param cuentaBancaria: Cuenta bancaria de la persona
        """
        self._nombre = nombre
        self._edad = edad
        self._cedula = cedula
        self._cuentaBancaria = cuentaBancaria
        self._trabajo = 0
        self._indiceMeta = 0
        self._verificadorMetasCumplidas = [False, False]
        Persona.listaPersonas.append(self)
        Persona.personasTotales += 1


    # MÉTODOS 
    
    @abstractmethod
    def recibirPagos(self, total):
        """
        Método para realizar pagos.
        
        :param total: Monto del pago a realizar
        """
        self._cuentaBancaria.disminuirSaldo(total)
        self.getCuentaBancaria().incrementarSaldo(total)


    def __str__(self):
        return (
            "\nNombre: " + self.getNombre() + "\n"
            + "Edad: " + str(self.getEdad()) + "\n"
            + "Cedula: " + str(self.getCedula()) + "\n"
        )
    

    # GETTERS Y SETTERS ---------------------------------------------------------------------------------------------------------------------------------------
    
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getCedula(self):
        return self._cedula

    def setCedula(self, cedula):
        self._cedula = cedula

    def getCuentaBancaria(self):
        return self._cuentaBancaria

    def setCuentaBancaria(self, cuentaBancaria):
        self._cuentaBancaria = cuentaBancaria

    #Solo getter ya que se trata de una constante 
    @classmethod
    def getSalario(cls):
        return cls.SALARIO

    def getTrabajo(self):
        return self._trabajo

    def setTrabajo(self, trabajo):
        self._trabajo = trabajo

    def getIndiceMeta(self):
        return self._indiceMeta

    def setIndiceMeta(self, indiceMeta):
        self._indiceMeta = indiceMeta

    def getVerificadorMetasCumplidas(self):
        return self._verificadorMetasCumplidas

    def setVerificadorMetasCumplidas(self, verificadorMetasCumplidas):
        self._verificadorMetasCumplidas = verificadorMetasCumplidas

    @classmethod
    def getPersonasTotales(cls):
        return cls.personasTotales

    @classmethod
    def getListaPersonas(cls):
        return cls.listaPersonas
