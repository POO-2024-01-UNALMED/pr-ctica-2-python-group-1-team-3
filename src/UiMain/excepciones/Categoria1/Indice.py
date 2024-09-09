from UiMain.excepciones.Categoria1.ExceptionC1 import ExceptionC1

class Indice(ExceptionC1):
    def __init__(self):
        super().__init__("Seleccione un producto en todas las casillas disponibles")