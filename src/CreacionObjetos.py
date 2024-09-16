"""

from gestorAplicacion.externo.CuentaBancaria import CuentaBancaria
from gestorAplicacion.empleados.Operario import Operario
from gestorAplicacion.empleados.Vendedor import Vendedor
from gestorAplicacion.empresa.Fabrica import Fabrica
from gestorAplicacion.empresa.Producto import Producto
from gestorAplicacion.empresa.Tienda import Tienda
from gestorAplicacion.empresa.Factura import Factura
from gestorAplicacion.externo.Cliente import Cliente
from gestorAplicacion.empleados.Transportador import Transportador
from gestorAplicacion.externo.Transporte import Transporte
from gestorAplicacion.externo.TipoTransporte import TipoTransporte
from baseDatos.Serializador import Serializador

# Creación de objetos

# PRODUCTOS
# Frutas y verduras
producto1 = Producto("Manzana","Paquete de 10 manzanas", 8000, 2.5, 20,3000,"frutas y verduras")
producto2 = Producto("Zanahoria", "Paquete de 5 zanahorias", 7000, 2, 15, 2000, "frutas y verduras")
producto3 = Producto("Pepino","Pepino fresco", 1500, 0.5, 8,500,"frutas y verduras")
producto4 = Producto("Limon", "1 kilo de limones", 2000, 1, 15, 800, "frutas y verduras")
producto5 = Producto("Piña","Piña fresca", 10000, 3, 20,3500,"frutas y verduras")
producto6 = Producto("Pera","Paquete de 10 peras", 10000, 2.5, 20,4000,"frutas y verduras")
producto7 = Producto("Tomate", "Paquete de 5 tomates", 6000, 2, 10, 1500, "frutas y verduras")

# Panaderia
producto8 = Producto("Ponque","Ponque Ramo tradicional", 6000, 1.5, 15,1500,"panaderia")
producto9 = Producto("Pan", "Pan integral sin gluten", 5000, 1.5, 30, 1500, "panaderia")
producto10 = Producto("Sanduche","Sanduche de pollo, queso y verduras", 8000, 1.5, 20,2500,"panaderia")
producto11 = Producto("Pandebono","Pandebono fresco", 2000, 0.5, 10,500,"panaderia")
producto12 = Producto("Pan hojaldrado","Pan hojaldrado fresco", 2500, 0.5, 15,800,"panaderia")
producto13 = Producto("Galletas","Galletas de avena", 1500, 1.5, 15,400,"panaderia")
producto14 = Producto("Palito de queso", "Palito de queso fresco", 2500, 0.5, 10, 500, "panaderia")

# Salsas y mermeladas
producto15 = Producto("Mermelada de frambuesa","Mermelada de frambuesa fresca", 10000, 1.5, 15,3500,"salsas y mermeladas")
producto16 = Producto("Mermelada de piña","Mermelada de piña fresca", 9000, 1.2, 13,3000,"salsas y mermeladas")
producto17 = Producto("Mermelada de mora","Mermelada de mora fresca", 7000, 0.8, 8,2000,"salsas y mermeladas")
producto18 = Producto("Mayonesa","Mayonesa baja en grasa", 15000, 2.5, 20,6000,"salsas y mermeladas")
producto19 = Producto("Salsa de tomate","Salsa de tomate natural", 8000, 1.5, 10,2000,"salsas y mermeladas")
producto20 = Producto("Mermelada de fresa","Mermelada de fresa fresca", 12000, 2, 15,4500,"salsas y mermeladas")
producto21 = Producto("Mermelada de kiwi","Mermelada de kiwi fresca", 15000, 2, 15,5000,"salsas y mermeladas")

# Bebidas
producto22 = Producto("Te verde","Hojas de te verde", 3000, 0.5, 10,300,"bebidas")
producto23 = Producto("Jugo de naranja","Jugo de naranja natural", 3000, 2, 20,1000,"bebidas")
producto24 = Producto("Leche de almendras", "Leche de almendras endulzada", 10000, 1.5, 18, 4000, "bebidas")
producto25 = Producto("Leche de avena", "Leche de avena con sabor a vainilla", 15000, 2, 25, 6000, "bebidas")
producto26 = Producto("Yogur de soya", "Yogur hecho en base de leche de soya", 12000, 1.5, 18, 4500, "bebidas")
producto27 = Producto("Cafe instantaneo","Frasco de cafe instantaneo", 20000, 3, 15,7000,"bebidas")
producto28 = Producto("Bebida achocolatada","Bebida achocolatada en polvo", 30000, 2, 15,10000,"bebidas")

catalogoProductos = []

for i in range(1, 29):
    text = f'catalogoProductos.append(producto{i})'
    exec(text) # Ejecuta el código contenido en un string como si fuera código Python

cuentaEmpresa = CuentaBancaria(123456789, 100000000)

# Cuentas para los empleados - cada uno con 500.000 pesos
#Operario
cuentaOperario1 = CuentaBancaria(111111, 500000)

#Vendedores
cuentaVendedor1 = CuentaBancaria(22222, 500000) 
cuentaVendedor2 = CuentaBancaria(33333, 500000)
cuentaVendedor3 = CuentaBancaria(44444, 500000)

# Transportadores
#Vendedores
cuentaTransportador1 = CuentaBancaria(55555, 500000) 
cuentaTransportador2 = CuentaBancaria(666666, 500000)
cuentaTransportador3 = CuentaBancaria(77777, 500000)


#Creación de empleados
#Operario
operario1 = Operario("Mateo Lopez", 22 ,11111111,cuentaOperario1,None)

#Vendedores
vendedor1 = Vendedor("Isabella Restrepo", 19, 2222222, cuentaVendedor1, None)
vendedor2 = Vendedor("Karen Ardila",23, 3333333, cuentaVendedor2, None)
vendedor3 = Vendedor("Carlos Escobar", 21, 4444444, cuentaVendedor3, None)

#Transportadores
transportador1 = Transportador("Kevin Castaño", 35, 5555555, cuentaTransportador1, None)
transportador2 = Transportador("Cristian Toro", 42, 6666666, cuentaTransportador2, None)
transportador3 = Transportador("Andres Salcedo", 29, 7777777, cuentaTransportador3, None)


# Creación Tiendas
tienda1 = Tienda("Delicia Fresca Norte", vendedor1,cuentaEmpresa) 
tienda2 = Tienda("Delicia Fresca Sur", vendedor2,cuentaEmpresa)
tienda3 = Tienda("Delicia Fresca Centro", vendedor3,cuentaEmpresa)

#Agregar productos a las tiendas
productos = [producto1, producto2, producto3, producto4, producto5, producto6, producto7,
             producto8, producto9, producto10, producto11, producto12, producto13, producto14,
             producto15, producto16, producto17, producto18, producto19, producto20, producto21, 
             producto22, producto23, producto24, producto25, producto26, producto27, producto28]

tiendas = [tienda1, tienda2, tienda3]

productos_por_tienda = [
      [producto1,producto2,producto3,producto4,producto5,producto6,producto11,producto12,producto13,
      producto14,producto15,producto16,producto21,producto22,producto23],  # Productos para tienda1
      [producto6,producto7,producto8,producto9,producto10,producto11,producto16,
      producto17,producto18,producto19,producto20,producto21,producto26,producto27,producto28],  # Productos para tienda2
      [producto5, producto7, producto8, producto9, producto10, producto12, producto14, producto15, 
      producto17, producto19, producto20, producto23, producto24, producto25, producto27]  # Productos para tienda3
      ]

#Añadir los productos a cada tienda
for i in range(5):
    for tienda, productos_tienda in zip(tiendas, productos_por_tienda): # Para tomar un elemento y un elemento
        tienda.getListaProductos().extend(productos_tienda) #agrega todos los productos de productos_tienda a la lista de productos de esa tienda

#Creación de la fábrica
fabrica = Fabrica(catalogoProductos, tiendas, cuentaEmpresa,operario1)

# Creación Clientes
cuentaCliente1 = CuentaBancaria(842348, 1000000)
cliente1 = Cliente("Esteban Carrillo", "Calle 64 # 20", cuentaCliente1)

cuentaCliente2 = CuentaBancaria(8376483, 2000000)
cliente2 = Cliente("Tiffany Mendoza", "Carrera 89 # 17", cuentaCliente2)

cuentaCliente3 = CuentaBancaria(472539,500000)
cliente3 = Cliente("Santiago Perez", "Avenida 35 # 21", cuentaCliente3)

cuentaCliente4 = CuentaBancaria(28935, 2500000)
cliente4 = Cliente("Mariana Lopera", "Carrera 23 # 56", cuentaCliente4)

cuentaCliente5 = CuentaBancaria(3984394, 200000)
cliente5 = Cliente("Jose Manuel Vergara", "Calle 65 # 21", cuentaCliente5)

cuentaCliente6 = CuentaBancaria(387465, 3000000)
cliente6 = Cliente("Camila Zapata", "Avenida 12 # 56", cuentaCliente6)

cuentaCliente7 = CuentaBancaria(826393, 700000)
cliente7 = Cliente("Miguel Acosta", "Carrera 37 # 67", cuentaCliente7)

cuentaCliente8 = CuentaBancaria(88849433, 5000000)
cliente8 = Cliente("Martin Berrio", "Calle 45 # 45", cuentaCliente8)

ListaClientes = [cliente1, cliente2, cliente3, cliente4, cliente5, cliente6, cliente7, cliente8]

# Asignación trabajadores
transportador1.setFabrica(fabrica)
transportador2.setFabrica(fabrica)
transportador3.setFabrica(fabrica)

vendedor1.setTienda(tienda1)
vendedor2.setTienda(tienda2)
vendedor3.setTienda(tienda3)

operario1.setFabrica(fabrica)


# Creación de transportes
# Creación de transportes
transporte1 = Transporte(TipoTransporte.CARRO, TipoTransporte.CARRO.getPrecioOriginalTransporte(), TipoTransporte.CARRO.capacidad, transportador1)
transporteAbastecer = Transporte(TipoTransporte.CAMION, TipoTransporte.CAMION.getPrecioOriginalTransporte(), TipoTransporte.CAMION.capacidad, transportador1)

# Asignar lista de transportes
Transporte.setListaTransportes([transporte1, transporteAbastecer])

transportador1.setTransporte(transporteAbastecer)
transportador1.setTransporte(transporte1)


#Serializar 
Serializador.serializar()

"""