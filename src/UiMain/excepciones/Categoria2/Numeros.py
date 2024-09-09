from UiMain.excepciones.Categoria2.ExceptionC2 import ExceptionC2

class Numeros(ExceptionC2):
    def __init__(self):
        super().__init__("No se pueden poner caracteres que no son numeros en los campos de cantidad")