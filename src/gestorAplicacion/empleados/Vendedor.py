# Este módulo pertenece al paquete 'gestorAplicacion.empleados' y contiene  la clase 'Vendedor', que hereda 
# de la clase 'Persona' y define las características y comportamientos del vendedor que es el trabajador 
# encargado de realizar las ventas en alguna de las tiendas disponibles.
# 
# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero

from .Meta import Meta
from gestorAplicacion.externo.Persona import Persona
from gestorAplicacion.empresa.Tienda import Tienda

class Vendedor(Persona):
    # La clase 'Vendedor' representa a un empleado vendedor en la empresa, que tiene metas de rendimiento 
    # y pertenece a una tienda.
    # Funcionalidades en las que se usa:
    #       - Pago de nomina


    # ATRIBUTOS ---------------------------------------------------------------

    metasVendedor = [
        Meta("Facil", 6, 12000),
        Meta("Dificil", 12, 25000)
    ]
    listaVendedores = []


    # CONSTRUCTORES ---------------------------------------------------------------
    
    # @param nombre Nombre del vendedor
    #
    # @param edad Edad del vendedor
    #
    # @param identificacion Identificación del vendedor
    #
    # @param cuentaBancaria Cuenta bancaria del vendedor
    #
    # @param tienda Tienda a la que pertenece el vendedor
    
    def __init__(self, nombre, edad, identificacion, cuentaBancaria, tienda):
        super().__init__(nombre, edad, identificacion, cuentaBancaria)
        self.tienda: Tienda = tienda
        self.listaVendedores.append(self)


    # MÉTODOS -------------------------------------------------------------------

    # Funcionalidades en las que se usa: Pago de nomina
    #
    # Realiza el pago de salario a un objeto de tipo vendedor.
    #
    # Este método está sobreescrito de la clase Persona.
    #
    # Se disminuye el saldo de la cuenta bancaria de la tienda en el monto especificado
    # y se incrementa el saldo de la cuenta bancaria del vendedor en el mismo monto.
    #
    # @param pago Monto del salario a pagar
    
    def recibirPagos(self, total):
        self.tienda.getCuentaBancaria().disminuirSaldo(total)
        self.getCuentaBancaria().incrementarSaldo(total)


    # Devuelve una representación en cadena del objeto Vendedor.
    #
    # @return Una cadena de texto con información sobre el vendedor, incluyendo su nombre, edad,
    #         identificación y el nombre de la tienda a la que pertenece.
    
    def __str__(self):
        return "Nombre: " + self.getNombre() + "\n" \
               + "Edad: " + str(self.getEdad()) + "\n" \
               + "Cedula: " + str(self.getCedula())


    # GETTERS Y SETTERS ---------------------------------------------------------

    def getTienda(self):
        return self.tienda

    def setTienda(self, tienda):
        self.tienda = tienda

    @classmethod
    def getMetasVendedor(cls):
        return cls.metasVendedor

    @classmethod
    def setMetasVendedor(cls, metasVendedor):
        cls.metasVendedor = metasVendedor

    @classmethod
    def getListaVendedores(cls):
        return cls.listaVendedores

    @classmethod
    def setListaVendedores(cls, listaVendedores):
        cls.listaVendedores = listaVendedores
