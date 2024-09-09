from UiMain.excepciones.Categoria1.ExceptionC1 import ExceptionC1

class FaltaUno(ExceptionC1):
    def __init__(self):
        super().__init__("Falta seleccionar uno de los campos")