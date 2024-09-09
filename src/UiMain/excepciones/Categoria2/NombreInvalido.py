from UiMain.excepciones.Categoria2.ExceptionC2 import ExceptionC2

class NombreInvalido(ExceptionC2):
    def __init__(self):
        super().__init__("El nombre debe contener nombre y apellido (2 palabras)")