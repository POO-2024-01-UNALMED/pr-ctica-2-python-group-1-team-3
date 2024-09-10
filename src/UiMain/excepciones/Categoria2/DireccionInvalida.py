from UiMain.excepciones.Categoria2.ExceptionC2 import ExceptionC2

class DireccionInvalida(ExceptionC2):
    def __init__(self):
        super().__init__("La dirección debe contener tanto letras como números")