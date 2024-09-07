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

class Deserializador:

    @classmethod
    def deserializar(cls):

        #Fábrica
        pickleFileFabrica = open(path+"/baseDatos/temp/pickleFileFabrica.pkl","rb")
        pcsFabrica = pickle.load(pickleFileFabrica)
        Fabrica.setListaFabricas(pcsFabrica)
        pickleFileFabrica.close()

        #Tiendas
        pickleFileTienda = open(path+"/baseDatos/temp/pickleFileTienda.pkl","rb")
        pcsTienda = pickle.load(pickleFileTienda)
        Tienda.setListaTiendas(pcsTienda)
        pickleFileTienda.close()

        #Productos
        pickleFileProducto = open(path+"/baseDatos/temp/pickleFileProducto.pkl","rb")
        pcsProducto = pickle.load(pickleFileProducto)
        Producto.setListaProductos(pcsProducto)
        pickleFileProducto.close()

        #Facturas
        pickleFileFactura = open(path+"/baseDatos/temp/pickleFileFactura.pkl","rb")
        pcsFactura = pickle.load(pickleFileFactura)
        Factura.setListaFacturas(pcsFactura)
        pickleFileFactura.close()

        #Clientes
        pickleFileCliente = open(path+"/baseDatos/temp/pickleFileCliente.pkl","rb")
        pcsCliente = pickle.load(pickleFileCliente)
        Cliente.setListaClientes(pcsCliente)
        pickleFileCliente.close()

        #Vendedores
        pickleFileVendedor = open(path+"/baseDatos/temp/pickleFileVendedor.pkl","rb")
        pcsVendedor = pickle.load(pickleFileVendedor)
        Vendedor.setListaVendedores(pcsVendedor)
        pickleFileVendedor.close()

        #Transportadores
        pickleFileTransportador = open(path+"/baseDatos/temp/pickleFileConductor.pkl","rb")
        pcsTransportador = pickle.load(pickleFileTransportador)
        Transportador.setListaTransportadores(pcsTransportador)
        pickleFileTransportador.close()

        #Operarios
        pickleFileOperario = open(path+"/baseDatos/temp/pickleFileOperario.pkl","rb")
        pcsOperario = pickle.load(pickleFileOperario)
        Operario.setListaOperarios(pcsOperario)
        pickleFileOperario.close()

        #Transportes
        pickleFileTransporte = open(path+"/baseDatos/temp/pickleFileTransporte.pkl","rb")
        pcsTransporte = pickle.load(pickleFileTransporte)
        Transporte.setListaTransportes(pcsTransporte)
        pickleFileTransporte.close()    