from UiMain.excepciones.Categoria2.ExceptionC2 import ExceptionC2

class NumerosEnteros(ExceptionC2):
    def __init__(self, campo):
        super().__init__("Solo se pueden ingresar números enteros en el campo: " + campo)