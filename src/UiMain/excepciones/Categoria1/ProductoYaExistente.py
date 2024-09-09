from UiMain.excepciones.Categoria1.ExceptionC1 import ExceptionC1

class ProductoYaExistente(ExceptionC1):
    def __init__(self):
        super().__init__("Ya existe un producto con ese nombre")