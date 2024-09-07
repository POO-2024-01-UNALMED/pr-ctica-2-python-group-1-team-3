import pickle
from gestorAplicacion.empleados.Operario import Operario
from gestorAplicacion.empleados.Vendedor import Vendedor
from gestorAplicacion.empresa.Fabrica import Fabrica
from gestorAplicacion.empresa.Producto import Producto
from gestorAplicacion.empresa.Tienda import Tienda
from gestorAplicacion.empresa.Factura import Factura
from gestorAplicacion.externo.Cliente import Cliente
from gestorAplicacion.empleados.Transportador import Transportador
from gestorAplicacion.externo.Transporte import Transporte

import os
import pathlib
path = os.path.join(pathlib.Path(__file__).parent.absolute())
path = os.path.dirname(path)

class Serializador:

    @classmethod
    def serializar(cls):

        #Fábrica
        pickleFileFabrica = open(path+"/baseDatos/temp/pickleFileFabrica.pkl","wb")
        pickle.dump(Fabrica.getListaFabricas(),pickleFileFabrica)
        pickleFileFabrica.close()

        #Tiendas
        pickleFileTienda = open(path+"/baseDatos/temp/pickleFileTienda.pkl","wb")
        pickle.dump(Tienda.getListaTiendas(),pickleFileTienda)
        pickleFileTienda.close()

        #Productos
        pickleFileProducto = open(path+"/baseDatos/temp/pickleFileProducto.pkl","wb")
        pickle.dump(Producto.getListaProductos(),pickleFileProducto)
        pickleFileProducto.close()

        #Facturas
        pickleFileFactura = open(path+"/baseDatos/temp/pickleFileFactura.pkl","wb")
        pickle.dump(Factura.getListaFacturas(),pickleFileFactura)
        pickleFileFactura.close()

        #Clientes
        pickleFileCliente = open(path+"/baseDatos/temp/pickleFileCliente.pkl","wb")
        pickle.dump(Cliente.getListaClientes(),pickleFileCliente)
        pickleFileCliente.close()

        #Vendedores
        pickleFileVendedor = open(path+"/baseDatos/temp/pickleFileVendedor.pkl","wb")
        pickle.dump(Vendedor.getListaVendedores(),pickleFileVendedor)
        pickleFileVendedor.close()

        #Transportadores
        pickleFileTransportador = open(path+"/baseDatos/temp/pickleFileConductor.pkl","wb")
        pickle.dump(Transportador.getListaTransportadores(),pickleFileTransportador)
        pickleFileTransportador.close()

        #Operarios
        pickleFileOperario = open(path+"/baseDatos/temp/pickleFileOperario.pkl","wb")
        pickle.dump(Operario.getListaOperarios(),pickleFileOperario)
        pickleFileOperario.close()

        #Transportes
        pickleFileTransporte = open(path+"/baseDatos/temp/pickleFileTransporte.pkl","wb")
        pickle.dump(Transporte.getListaTransportes(),pickleFileTransporte)
        pickleFileTransporte.close()