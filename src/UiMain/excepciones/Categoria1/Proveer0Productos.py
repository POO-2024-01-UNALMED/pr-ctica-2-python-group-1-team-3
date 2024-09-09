from UiMain.excepciones.Categoria1.ExceptionC1 import ExceptionC1

class Proveer0Productos(ExceptionC1):
    def __init__(self):
        super().__init__("No es posible proveer a una tienda con 0 productos")