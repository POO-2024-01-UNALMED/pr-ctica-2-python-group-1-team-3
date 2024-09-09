from UiMain.excepciones.Categoria1.ExceptionC1 import ExceptionC1

class MayorA(ExceptionC1):
    def __init__(self):
        super().__init__("La cantidad de productos seleccionada es superior a la permitida en esa categoria")