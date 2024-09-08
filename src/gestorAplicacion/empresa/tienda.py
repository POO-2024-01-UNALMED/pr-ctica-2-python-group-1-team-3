# Este módulo pertenece al paquete 'gestorAplicacion.empresa' y contiene clases relacionadas con las tiendas
# y su gestión dentro de la empresa. Incluye la clase 'Tienda' que representa una tienda con sus atributos
# y métodos para su manipulación. 
#  
# Esta clase representa la tienda donde se gestiona el inventario y se  realizan las ventas de los productos. 
#  
# Esta clase implementa la interfaz 'Moda'.
#  
# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero

#from gestorAplicacion.externo.Cliente import Cliente
#from gestorAplicacion.empleados.Vendedor import Vendedor
from gestorAplicacion.empresa.Factura import Factura  
from gestorAplicacion.empresa.Moda import Moda
#from gestorAplicacion.empleados.Operario import Operario
#from gestorAplicacion.empresa.Producto import Producto
import pickle
import random
import copy

from gestorAplicacion.empresa import Producto

class Tienda(Moda):
    # La clase 'Tienda' representa una tienda dentro de la empresa.
    #  
    # Contiene información sobre el nombre, el vendedor, la cuenta bancaria, las listas de productos y sus cantidades.
    #  
    # Proporciona métodos para gestionar estos atributos y realizar operaciones como mostrar productos, vender productos,
    # enviar pedidos y manejar devoluciones.
    #  
    # Funcionalidades en las que se usa:
    #      - Envio pedidos
    #      - Proveer tiendas
    #      - Devolucion de productos


    # ATRIBUTOS--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
    _listaTiendas = []
    _numTiendas = 0


    # CONSTRUCTOR -------------------------------------------------------------------------------------------------------------------------------------------------
    
    def __init__(self, nombre, vendedor, cuentaBancaria):
        """
        Constructor que recibe todos los parámetros.

        :param nombre: Nombre de la tienda
        :param vendedor: Vendedor asociado a la tienda
        :param cuentaBancaria: Cuenta bancaria de la tienda
        """
        self._nombre = nombre
        self._vendedor = vendedor
        self._cuentaBancaria = cuentaBancaria
        self._listaProductos = []
        self._listaCantidadProductos = [{}]
        self._productosPorCategoria = {}
        self._productosDevueltos = []
        Tienda._numTiendas += 1
        Tienda._listaTiendas.append(self)
        self._cantidadPorCategoria = {
            "frutas y verduras": random.randint(50, 100),
            "panaderia": random.randint(50, 100),
            "salsas y mermeladas": random.randint(50, 100),
            "bebidas": random.randint(50, 100)
        }


    # MÉTODOS----------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def mostrarProductos(self):
        """
        Muestra los productos disponibles en la tienda.

        :return: Una cadena de texto con la información de los productos disponibles en la tienda.
        """
        result = ""
        for i, producto in enumerate(self._listaProductos):
            result += f"\n{i + 1}" + str(producto) + "\n"
        return result
    

    def cantidadProductos(self):
        """
        Permite ver los productos que hay en la tienda y su cantidad.

        :return: Una cadena de texto con la cantidad de cada producto disponible en la tienda.
        """
        self._listaCantidadProductos = {}
        cadena = "\n"
        
        for producto in self._listaProductos: #Agregar valores y hacer conteo
            if producto.getNombre() in self._listaCantidadProductos:
                self._listaCantidadProductos[producto.getNombre()] += 1
            else:
                self._listaCantidadProductos[producto.getNombre()] = 1

        for producto, cantidad in self._listaCantidadProductos.items():
            cadena += f"{producto}: {cantidad} \n"

        return cadena


    def productosPorCategoria(self):
        """
        Permite ver la cantidad de productos por categoría que tiene cada tienda, y la cantidad máxima que puede tener.

        :return: Una cadena de texto con la cantidad de productos por categoría en la tienda.
        """
        cadena = ""
        self._productosPorCategoria = {
            "frutas y verduras": 0,
            "panaderia": 0,
            "salsas y mermeladas": 0,
            "bebidas": 0
        }
        for producto in self._listaProductos:
            categoria = producto.getCategoria()
            if categoria in self._productosPorCategoria:
                self._productosPorCategoria[categoria] += 1

        for categoria, cantidad in self._productosPorCategoria.items():
            cadena += f"{categoria} {cantidad}/{self._cantidadPorCategoria[categoria]}  "
        return cadena


    def cantidadProductosVentas(self):
        """
        Muestra un texto con la cantidad de productos vendidos.

        :return: Una cadena de texto con la cantidad de cada producto vendido.
        """
        self._listaCantidadProductos = {}
        cadena = "    "
        indice = 1
        
        for producto in self._listaProductos:
            if producto in self._listaCantidadProductos:
                self._listaCantidadProductos[producto] += 1
            else:
                self._listaCantidadProductos[producto] = 1

        for producto in self._listaProductos:
            if producto.getNombre() not in cadena:
                cadena += f"\n{indice}. {producto.getNombre()}: {self._listaCantidadProductos[producto]} "
                indice += 1
        
        return cadena


    def venderProducto(self, producto):
        """
        Método que permite hacer la venta de un producto, eliminándolo de la lista de productos
        y reduciendo la cantidad en 1 en cantidadProductos.

        :param producto: Producto a vender.
        """
        for productos in self._listaProductos:
            if producto.getNombre() == productos.getNombre():
                self._listaProductos.remove(productos)
                break
            

    def enviarPedido(self, listaProductosPedidos, transporte, cliente, dia, operario):
        """
        Permite descontar una unidad a las cantidades de los productos, añadir trabajo a los trabajadores
        involucrados con la venta, y crear la factura de la venta.

        :param listaProductosPedidos: Lista de productos pedidos.
        :param transporte: Transporte utilizado para el envío.
        :param cliente: Cliente que realiza el pedido.
        :param dia: Día del envío.
        :param operario: Operario responsable del pedido.
        :return: La factura generada para el pedido.
        """
        self._vendedor.setTrabajo(self._vendedor.getTrabajo()+1)
        self._vendedor.setIndiceMeta(self._vendedor.getIndiceMeta() + len(listaProductosPedidos))

        transporte.getTransportador().setTrabajo(transporte.getTransportador().getTrabajo() + 1)
        for producto in listaProductosPedidos:
            transporte.getTransportador().setIndiceMeta(transporte.getTransportador().getIndiceMeta() + producto.getPeso())

        operario.setTrabajo(operario.getTrabajo()+1)
        operario.setIndiceMeta(operario.getIndiceMeta() + len(listaProductosPedidos))

        if cliente.getProductos() is None:
            cliente.setProductos([])

        listaProvicional = cliente.getProductos()
        for producto in listaProductosPedidos:
            listaProvicional.append(copy.deepcopy(producto))

        cliente.setProductos(listaProvicional)

        factura = Factura(self, cliente, transporte, listaProductosPedidos, int(dia), operario)
        return factura


    def devolverProducto(self, factura, producto):
        """
        Devuelve el producto seleccionado, agregándolo a la lista donde se almacenan las devoluciones de la tienda
        y retorna al cliente al que se le hizo la devolución.

        :param factura: Factura asociada a la devolución.
        :param producto: Producto a devolver.
        :return: El cliente al que se le hizo la devolución.
        """
        self._productosDevueltos.append(producto)
        return factura.getCliente()


    def descargarProducto(self, transporte):
        """
        Permite que la tienda reciba los productos enviados en el transporte.

        :param transporte: Transporte utilizado para el envío.
        """
        while len(transporte.getListaDeProductos()) > 0:
            self._listaProductos.append(transporte.getListaDeProductos().pop(0))
        transporte.getTransportador().setTrabajo(transporte.getTransportador().getTrabajo() + 1)


    # GETTERS Y SETTERS----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getVendedor(self):
        return self._vendedor

    def setVendedor(self, vendedor):
        self._vendedor = vendedor

    def getCuentaBancaria(self):
        return self._cuentaBancaria

    def setCuentaBancaria(self, cuentaBancaria):
        self._cuentaBancaria = cuentaBancaria

    def getListaProductos(self):
        return self._listaProductos

    def setListaProductos(self, listaProductos):
        self._listaProductos = listaProductos

    def getProductosPorCategoria(self):
        return self._productosPorCategoria

    def getCantidadPorCategoria(self):
        return self._cantidadPorCategoria

    def getListaCantidadProductos(self):
        return self._listaCantidadProductos

    def setListaCantidadProductos(self, listaCantidadProductos):
        self._listaCantidadProductos = listaCantidadProductos

    def getProductosDevueltos(self):
        return self._productosDevueltos

    def setProductosDevueltos(self, productosDevueltos):
        self._productosDevueltos = productosDevueltos

    @classmethod
    def get_num_tiendas(cls):
        return cls._numTiendas
    
    @classmethod
    def setListaTiendas(cls, listaTiendas):
        cls._listaTiendas = listaTiendas

    @classmethod
    def getListaTiendas(cls):
        return cls._listaTiendas

    def _str_(self) -> str:
        return self._nombre