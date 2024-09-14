# Archivo: src/principal.py

import sys
import os

from gestorAplicacion.externo import Cliente
from gestorAplicacion.empresa import Producto

# Asegura que el sistema pueda encontrar los módulos del proyecto
sys.path.append(os.path.dirname(__file__))

# Importamos el archivo main de UiMain.Ventanas
from UiMain.Ventanas.VentanaPrincipal import VentanaPrincipal
#from UiMain.Ventanas.main import ventanaMain
from baseDatos.Deserializador import Deserializador
from gestorAplicacion.empresa.Fabrica import Fabrica
#from UiMain.Ventanas import main

if __name__ == "__main__":
    # Ejecutamos la lógica de main.py

    # Deserialización de los datos necesarios
    #Deserializador.deserializar()
    #print(Producto.getListaProductos())  # Assuming the method is defined in the Producto class
    ventana = VentanaPrincipal()
    ventana.mainloop()
    #ventanaMain.mainloop()
    
