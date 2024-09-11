from UiMain.excepciones.Categoria2.ExceptionC2 import ExceptionC2

class SoloNumeros(ExceptionC2):
    def __init__(self, campos):
        super().__init__("Solo se pueden ingresar números en los campos: " + campos)