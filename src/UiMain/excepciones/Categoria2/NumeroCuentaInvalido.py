from UiMain.excepciones.Categoria2.ExceptionC2 import ExceptionC2

class NumeroCuentaInvalido(ExceptionC2):
    def __init__(self):
        super().__init__("El número de cuenta bancaria debe contener solo números")