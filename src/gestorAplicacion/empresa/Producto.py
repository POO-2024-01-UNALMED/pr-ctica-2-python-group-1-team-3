# Este módulo pertenece al paquete 'gestorAplicacion.empresa' y contiene clases relacionadas con los productos
# y su gestión dentro de la empresa. Incluye la clase 'Producto' que representa un producto con sus atributos
# y métodos para su manipulación.
# 
# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero

import pickle

class Producto:
    # La clase 'Producto' representa un producto dentro de la empresa.
    #
    # Contiene información sobre el nombre, descripción, valor, peso, tamaño, costo de producción, categoría
    # y estado de devolución del producto.
    #
    #  Proporciona métodos para gestionar estos atributos y para generar una representación en cadena del producto.


    # ATRIBUTOS ---------------------------------------------------------------
    
    _numProductos = 0
    _listaProductos = []


    # CONSTRUCTORES ---------------------------------------------------------------
    
    # @param nombre Nombre del producto
    #
    # @param descripcion Descripción del producto
    # 
    # @param valor Valor del producto
    # 
    # @param peso Peso del producto
    # 
    # @param tamano Tamaño del producto
    # 
    # @param costoProduccion Costo de producción del producto
    # 
    # @param categoria Categoría del producto
    
    def __init__(self, nombre, descripcion, valor, peso, tamano, costoProduccion, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.valor = valor
        self.peso = peso
        self.tamano = tamano
        self.costoProduccion = costoProduccion
        self.categoria = categoria.lower()
        Producto._numProductos += 1
        Producto._listaProductos.append(self)
        self.devuelto = False

    
    # MÉTODOS -------------------------------------------------------------------

    # Funcionalidades en las que se usa: Gestión de productos
    #
    # Genera una representación en cadena del objeto Producto.
    #
    # @return Una cadena de texto con la información del producto, incluyendo nombre, descripción,
    #         valor, peso, tamaño y costo de producción.
    
    def __str__(self):
        return "\nNombre: " + self.nombre + "\n" \
               + "Descripción: " + self.descripcion + "\n" \
               + "Valor: " + str(self.valor) + "\n" \
               + "Peso: " + str(self.peso) + "\n" \
               + "Tamaño: " + str(self.tamano) + "\n" \
               + "Costo de producción: " + str(self.costoProduccion) + "\n" \
               + "Categoría: " + str(self.categoria)

    
    # GETTERS Y SETTERS ---------------------------------------------------------

    @classmethod
    def getNumProductos(cls):
        return cls._numProductos

    @classmethod
    def setNumProductos(cls, numProductos):
        cls._numProductos = numProductos

    @classmethod
    def getListaProductos(cls):
        return cls._listaProductos

    @classmethod
    def setListaProductos(cls, listaProductos):
        cls._listaProductos = listaProductos

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getPeso(self):
        return self.peso

    def setPeso(self, peso):
        self.peso = peso

    def getTamano(self):
        return self.tamano

    def setTamano(self, tamano):
        self.tamano = tamano

    def getCostoProduccion(self):
        return self.costoProduccion

    def setCostoProduccion(self, costoProduccion):
        self.costoProduccion = costoProduccion

    def getCategoria(self):
        return self.categoria

    def setCategoria(self, categoria):
        self.categoria = categoria

    def isDevuelto(self):
        return self.devuelto

    def setDevuelto(self, devuelto):
        self.devuelto = devuelto
