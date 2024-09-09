from UiMain.excepciones.Categoria1.ExceptionC1 import ExceptionC1

class FechasFueraDeRango(ExceptionC1):
    def __init__(self):
        super().__init__("Las fechas deben estar dentro del rango permitido")