# Este módulo pertenece al paquete 'gestorAplicacion.empresa' y contiene La interfaz 'Moda' que 
# representa un tipo de dato que define un nombre. Es utilizada para obtener el nombre de los 
# elementos que se desean analizar y encontrar la moda entre un conjunto de datos.
#
# AUTORES: - Sebastian Estrada Villa
#          - Valentina Luján Robledo
#          - Santiago Ochoa Quintero

from abc import ABC, abstractmethod

class Moda(ABC):
    # 'Moda' representa una interfaz que permite seleccionar objetos para poder encontrar la moda en 
    # la funcionalidad de evaluación operación. Esta interfaz tiene un único método llamado 'getNombre'.


    # MÉTODOS ---------------------------------------------------------------
    
    #Obtiene el nombre del elemento.
    #
    #return: El nombre del elemento como una cadena de texto.

    @abstractmethod
    def getNombre(self):
        pass
