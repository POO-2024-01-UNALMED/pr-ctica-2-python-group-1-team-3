# Este módulo pertenece al paquete 'gestorAplicacion.externo' y contiene la clase 'CuentaBancaria' que representa una cuenta bancaria 
# con sus atributos y métodos para su manipulación.
#  
# Esta clase representa una cuenta bancaria en la que se gestionan las transacciones financieras, incluyendo acciones como realizar 
# los pagos y devoluciones de dinero, tanto para las cuentas bancarias de los clientes como para las cuentas bancarias de los empleados
# y la empresa. 
#  
# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero

from gestorAplicacion.empleados.Transportador import Transportador
from gestorAplicacion.empleados.Vendedor import Vendedor
from gestorAplicacion.empleados.Operario import Operario
from gestorAplicacion.externo.Persona import Persona


class CuentaBancaria:
    #La clase 'CuentaBancaria' representa una cuenta bancaria dentro de la empresa.
    #  
    # Contiene información sobre el número de cuenta y el saldo.
    #  
    # Proporciona métodos para gestionar estos atributos y realizar operaciones como incrementar y disminuir el saldo,
    # calcular el pago de empleados y devolver dinero a los clientes.
    #  
    # Funcionalidades en las que se usa:
    #      - Pago de nomina
    #      - Devolucion de productos


    # CONSTRUCTOR -----------------------------------------------------------------------------------------------------------------------------------------------------------

    def __init__(self, numeroCuenta, saldo):
        """
        Constructor que recibe el número de cuenta y el saldo inicial.

        :param numeroCuenta: Número de la cuenta bancaria
        :param saldo: Saldo inicial de la cuenta bancaria
        """
        self._numeroCuenta = numeroCuenta
        self._saldo = saldo

    # MÉTODOS ------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    def incrementarSaldo(self, cantidad):
        """
        Incrementa el saldo de la cuenta bancaria.

        :param cantidad: Cantidad a incrementar en el saldo de la cuenta.
        """
        self._saldo += cantidad


    def disminuirSaldo(self, cantidad):
        """
        Disminuye el saldo de la cuenta bancaria.

        :param cantidad: Cantidad a disminuir del saldo de la cuenta.
        """
        self._saldo -= cantidad


    @staticmethod
    def calcularPago(persona):
        """
        Calcula el pago de los empleados basado en el trabajo realizado.

        :param persona: Persona (empleado) para la cual se va a calcular el pago.
        :return: El monto total a pagar al empleado basado en su tipo y trabajo realizado.

        Funcionalidades en las que se usa: Pago de nómina
        """
        trabajo = persona.getTrabajo()
        salario = Persona.getSalario()
        total = 0

        # Diferentes pagos según el salario para cada uno de los tipos
        if isinstance(persona, Operario):
            total = (salario + 15000) * trabajo
        elif isinstance(persona, Vendedor):
            total = (salario + 20000) * trabajo
        elif isinstance(persona, Transportador):
            total = (salario + 10000) * trabajo

        return total


    def devolverDinero(self, cantidad, cliente):
        """
        Devuelve dinero a un cliente incrementando el saldo de su cuenta bancaria.

        :param cantidad: Cantidad de dinero a devolver.
        :param cliente: Cliente al cual se le va a devolver el dinero.

        Funcionalidades en las que se usa: Devolución de productos
        """
        cliente.getCuentaBancaria().incrementarSaldo(cantidad)


    # GETTERS Y SETTERS --------------------------------------------------------------------------------------------------------------------------------------------------

    def getNumeroCuenta(self):
        return self._numeroCuenta

    def setNumeroCuenta(self, numeroCuenta):
        self._numeroCuenta = numeroCuenta

    def getSaldo(self):
        return self._saldo

    def setSaldo(self, saldo):
        self._saldo = saldo
