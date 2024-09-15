# Este módulo pertenece al paquete 'gestorAplicacion.empleados' y contiene  la clase 'Operario', que hereda 
# de la clase 'Persona' y define las características y comportamientos del operario que es el trabajador 
# encargado de supervisar y controlar la producción de los diferentes productos en la fábrica.
# 
# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero

#from gestorAplicacion.empleados.Meta import Meta
#from gestorAplicacion.externo.Persona import Persona

from gestorAplicacion.empleados.Meta import Meta
from gestorAplicacion.externo.Persona import Persona
from gestorAplicacion.empresa.Fabrica import Fabrica

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class Operario(Persona):
   # La clase 'Operario' representa a un empleado operario en la empresa, que tiene metas de rendimiento y puede 
   # pertenecer a una fábrica.
   #
   # Funcionalidades en las que se usa: 
   #       - Pago de nomina


    # ATRIBUTOS ---------------------------------------------------------------
  
    metasOperario = [
        Meta("Facil", 4, 5000),
        Meta("Dificil", 9, 15000)
    ]
    listaOperarios = []


    # CONSTRUCTORES ---------------------------------------------------------------
    
    # @param nombre Nombre del operario
    #
    # @param edad Edad del operario
    #
    # @param identificacion Identificación del operario
    #
    # @param cuentaBancaria Cuenta bancaria del operario
    #
    # @param fabrica Fábrica a la que pertenece el operario
    
    def __init__(self, nombre, edad, identificacion, cuentaBancaria, fabrica):
        super().__init__(nombre, edad, identificacion, cuentaBancaria)
        self.fabrica: Fabrica = fabrica
        self.listaOperarios.append(self)


    # MÉTODOS

    # Funcionalidades en las que se usa: Pago de nomina
    #
    # Realiza el pago de salario a un objeto de tipo operario.
    #
    # Este método esta sobre escrito de la clase Persona.
    #
    # Se disminuye el saldo de la cuenta bancaria de la fábrica en el monto especificado
    # y se incrementa el saldo de la cuenta bancaria del operario en el mismo monto.
    #
    # @param pago Monto del salario a pagar
    
    def recibirPagos(self, total):
        self.fabrica.getCuentaBancaria().disminuirSaldo(total)
        self.getCuentaBancaria().incrementarSaldo(total)


    # Devuelve una representación en cadena del objeto Operario.
    #
    # @return Una cadena de texto con información sobre el operario, incluyendo su nombre, edad, 
    #         identificación y la fábrica a la que pertenece.
    
    def __str__(self):
        return (
            "Nombre: " + self.getNombre() + "\n"
            + "Edad: " + str(self.getEdad()) + "\n"
            + "Identificación: " + str(self.getCedula())
        )


    # GETTERS Y SETTERS ---------------------------------------------------------

    @classmethod
    def getMetasOperario(cls):
        return cls.metasOperario

    @classmethod
    def setMetasOperario(cls, metasOperario):
        cls.metasOperario = metasOperario

    def getFabrica(self):
        return self.fabrica

    def setFabrica(self, fabrica):
        self.fabrica = fabrica

    @classmethod
    def getListaOperarios(cls):
        return cls.listaOperarios

    @classmethod
    def setListaOperarios(cls, listaOperarios):
        cls.listaOperarios = listaOperarios
