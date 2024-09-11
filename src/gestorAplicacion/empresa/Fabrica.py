# Este módulo pertenece al paquete 'gestorAplicacion.empresa' y contiene la clase 'Fabrica'. Esta clase es 
# la encargada de gestionar la producción y el inventario de la fábrica, aquí es donde se da la fabricación 
# de los productos y su posterior distribución en las diferentes tiendas. 
# 
# Esta clase resulta fundamental para el funcionamiento del sistema, ya que es usada por todas las funcionalidades,
# excepto la de evaluación de operación.
# 
# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero

#from excepciones import ProductoYaExistente
#from gestorAplicacion.empleados.Operario import Operario
#from gestorAplicacion.externo.Persona import Persona
#from gestorAplicacion.empresa.Factura import Factura
#from gestorAplicacion.externo.CuentaBancaria import CuentaBancaria
#from gestorAplicacion.empresa.Producto import Producto
#from gestorAplicacion.empresa.Tienda import Tienda
from UiMain.excepciones.Categoria1.ProductoYaExistente import ProductoYaExistente

import copy
import pickle

class Fabrica:
    # La clase 'Fabrica' representa una fábrica dentro de la empresa. 
    # Contiene una lista de productos, una lista de tiendas, una cuenta bancaria y un operario.
    #
    # Proporciona métodos para gestionar estos elementos, como mostrar productos, tiendas y empleados,
    # así como realizar operaciones financieras y seleccionar elementos específicos.
    # Funcionalidades en las que se usa: 
    #        - Proveer tiendas
    #        - Envio pedidos
    #        - Devolución de productos
    #        - Pago de nomina


    # ATRIBUTOS ---------------------------------------------------------------

    _listaFabricas = []


    # CONSTRUCTORES ---------------------------------------------------------------
    
    # @param listaProductos La lista de productos que maneja la fábrica.
    #
    # @param listaTienda La lista de tiendas asociadas a la fábrica.
    #
    # @param cuentaBancaria La cuenta bancaria asociada a la fábrica.
    #
    # @param operario El operario asignado a la fábrica.
    
    def __init__(self, listaProductos, listaTiendas, cuentaBancaria, operario=None):
        self.listaProductos = listaProductos
        self.listaTiendas = listaTiendas
        self.cuentaBancaria = cuentaBancaria
        self.operario = operario
        Fabrica._listaFabricas.append(self)

   
    # MÉTODOS -------------------------------------------------------------------

    # Funcionalidades en las que se usa: Proveer tiendas
    #
    # Muestra los productos disponibles en la fábrica.
    #
    # @return Una cadena de texto con información sobre los productos disponibles en la fábrica, 
    #         incluyendo número, nombre, peso, precio y categoría de cada producto.
    
    def mostrarProductos(self):
        mensaje = "\nNÚMERO-PRODUCTO-PESO-PRECIO-CATEGORIA\n"
        numero = 1
        for producto in self.listaProductos:
            mensaje += f"{numero}. {producto.getNombre()} - {producto.getPeso()} - {producto.getCostoDeProduccion()} - {producto.getCategoria()}\n"
            numero += 1
        return mensaje


    # Funcionalidades en las que se usa: Proveer tiendas, Envio pedidos
    #
    # Muestra las tiendas disponibles.
    #
    # @return Una cadena de texto con información sobre las tiendas disponibles, incluyendo número, 
    #         nombre y cantidad de productos de cada tienda.
    
    def mostrarTiendas(self):
        mensaje = ""
        numero = 1
        for tienda in self.listaTiendas:
            mensaje += f"{numero}. {tienda.getNombre()}-Productos: {tienda.cantidadProductos()}\n"
            numero += 1
            if numero == len(self.listaTiendas):
                mensaje += "\n"
        return mensaje

    
    # Funcionalidades en las que se usa: Envio pedidos
    #
    # Permite seleccionar una de las tiendas disponibles.
    #
    # @param indice Índice de la tienda a seleccionar (indice - 1).
    #
    # @return La tienda seleccionada correspondiente al índice proporcionado.
    
    def seleccionarTienda(self, indice):
        return self.listaTiendas[indice - 1]


    # Funcionalidades en las que se usa: Devolución de productos
    #
    # Descuenta el valor del producto devuelto de la cuenta de la fábrica.
    #
    # @param productoDevuelto Producto que fue devuelto.
    #
    # @return El monto descontado de la cuenta de la fábrica por el producto devuelto.
    
    def descontarDinero(self, productoDevuelto):
        total = productoDevuelto.getValor()
        self.cuentaBancaria.descontarFondos(total)
        return total


    # Funcionalidades en las que se usa: Proveer tiendas
    #
    # Crea una lista con cierta cantidad de un mismo producto.
    #
    # @param cantidad Cantidad de productos a crear.
    #
    # @param producto Producto a replicar en la lista.
    #
    # @return Una lista de productos con la cantidad especificada.
   
    def cantidadProductos(self, cantidad, producto):
        productos = []
        for _ in range(cantidad):
            productos.append(copy.deepcopy(producto))
        return productos

    
    # Funcionalidades en las que se usa: Pago de nomina
    #
    # Busca en las facturas los trabajadores involucrados en los envíos.
    # Verifica que no se les haya pagado antes (Trabajo mayor a 0).
    #
    # @param listaFacturas Lista de facturas a revisar.
    #
    # @param tipo Tipo de trabajador (1: Operario, 2: Transportador, 3: Vendedor).
    #
    # @return Una lista de personas que son trabajadores involucrados en los envíos.
    
    @classmethod
    def TrabajadoresInvolucrados(cls, listaFacturas, tipo):
        listaPersonas = []
        for factura in listaFacturas:
            if tipo == 1 and factura.operario not in listaPersonas and factura.operario.getTrabajo() > 0:
                listaPersonas.append(factura.operario)
            elif tipo == 2 and factura.getTransporte().getTransportador() not in listaPersonas and factura.getTransporte().getTransportador().getTrabajo() > 0:
                listaPersonas.append(factura.getTransporte().getTransportador())
            elif tipo == 3 and factura.getTienda().getVendedor() not in listaPersonas and factura.getTienda().getVendedor().getTrabajo() > 0:
                listaPersonas.append(factura.getTienda().getVendedor())
        return listaPersonas

    
    # Funcionalidades en las que se usa: Pago de nomina
    #
    # Muestra información de los empleados en una lista de trabajadores.
    #
    # @param trabajadores Lista de trabajadores a mostrar.
    #
    # @return Una cadena de texto con información sobre cada trabajador en la lista.
    
    @classmethod
    def mostrarEmpleados(cls, trabajadores):
        mensaje = ""
        numero = 1
        for trabajador in trabajadores:
            mensaje += f"\nTrabajador {numero} {trabajador._str_()}"
            numero += 1
        return mensaje


    # toString para saber qué imprimir cuando se llame al objeto Fabrica
    # @Override  
    
    def _str_(self):
        return "Fábrica Delicia Fresca"


    # Método para añadir un producto a la lista de productos de la fábrica
    #
    # @param producto Producto a añadir.
    #
    # @throws ProductoYaExistente si el producto ya está en la lista.
    def anadirProducto(self, producto):
        if producto.getNombre() in [p.getNombre() for p in self.listaProductos]:
            raise ProductoYaExistente()
        else:
            self.listaProductos.append(producto)

    # GETTERS Y SETTERS ---------------------------------------------------------

    def getOperario(self):
        return self.operario
    
    def setOperario(self, operario):
        self.operario = operario
    
    def getListaProductos(self):
        return self.listaProductos
    
    def setListaProductos(self, listaProductos):
        self.listaProductos = listaProductos
    
    def getListaTiendas(self):
        return self.listaTiendas
    
    def setListaTiendas(self, listaTiendas):
        self.listaTiendas = listaTiendas
    
    def getCuentaBancaria(self):
        return self.cuentaBancaria
    
    def setCuentaBancaria(self, cuentaBancaria):
        self.cuentaBancaria = cuentaBancaria

    @classmethod
    def setListaFabricas(cls, listaFabricas):
        cls._listaFabricas = listaFabricas

    @classmethod
    def getListaFabricas(cls):
        return cls._listaFabricas