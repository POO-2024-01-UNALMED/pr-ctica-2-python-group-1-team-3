# Este módulo pertenece al paquete 'gestorAplicacion.empleados' y contiene  la clase 'Transportador', que hereda 
# de la clase 'Persona' y define las características y comportamientos del transportador que es el trabajador 
# encargado de transportar productos en determinados transportes.
# 
# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero

from gestorAplicacion.empleados.Meta import Meta
from gestorAplicacion.externo.Persona import Persona

class Transportador(Persona):
    # La clase 'Transportador' representa a un empleado transportador en la empresa, que tiene metas de rendimiento 
    # y puede pertenecer a una fábrica y tener un transporte asignado.
    # Funcionalidades en las que se usa: 
    #  		- Pago de nomina


    # ATRIBUTOS ---------------------------------------------------------------
 
    metasTransportador = [
        Meta("Facil", 5, 10000),
        Meta("Dificil", 10, 20000)
    ]
    listaTransportadores = []


    # CONSTRUCTORES ---------------------------------------------------------------
    
    # @param nombre Nombre del transportador
    #
    # @param edad Edad del transportador
    #
    # @param identificacion Identificación del transportador
    #
    # @param cuentaBancaria Cuenta bancaria del transportador
    #
    # @param transporte Transporte asignado al transportador
    
    def __init__(self, nombre, edad, identificacion, cuentaBancaria, transporte):
        super().__init__(nombre, edad, identificacion, cuentaBancaria)
        self.transporte = transporte
        self.listaTransportadores.append(self)


    # MÉTODOS -------------------------------------------------------------------

    # Funcionalidades en las que se usa: Pago de nomina
    #
    # Realiza el pago de salario a un objeto de tipo transportador.
    #
    # Este método está sobreescrito de la clase Persona.
    #
    # Se disminuye el saldo de la cuenta bancaria de la fábrica en el monto especificado
    # y se incrementa el saldo de la cuenta bancaria del transportador en el mismo monto.
    #
    # @param pago Monto del salario a pagar

    def recibirPagos(self, total):
        self.fabrica.getCuentaBancaria().disminuirSaldo(total)
        self.getCuentaBancaria().incrementarSaldo(total)


    # Devuelve una representación en cadena del objeto Transportador.
    #
    # @return Una cadena de texto con información sobre el transportador, incluyendo su nombre, edad,
    #         identificación y el tipo de transporte asignado.
    
    def __str__(self):
        return "Nombre: " + self.getNombre() + "\n" \
            + "Edad: " + str(self.getEdad()) + "\n" \
            + "Cedula: " + str(self.getCedula())


    
    # GETTERS Y SETTERS ---------------------------------------------------------

    def getTransporte(self):
        return self.transporte

    def setTransporte(self, transporte):
        self.transporte = transporte

    def getFabrica(self):
        return self.fabrica

    def setFabrica(self, fabrica):
        self.fabrica = fabrica

    @classmethod
    def getMetasTransportador(cls):
        return cls.metasTransportador

    @classmethod
    def setMetasTransportador(cls, metasTransportador):
        cls.metasTransportador = metasTransportador

    @classmethod
    def getListaTransportadores(cls):
        return cls.listaTransportadores

    @classmethod
    def setListaTransportadores(cls, listaTransportadores):
        cls.listaTransportadores = listaTransportadores
