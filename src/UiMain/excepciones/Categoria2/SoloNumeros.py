from UiMain.excepciones.Categoria2.ExceptionC2 import ExceptionC2

class SoloNumeros(ExceptionC2):
    def __init__(self):
        super().__init__("En los campos de valor, peso, tamaño y costo de producción solo se pueden ingresar números.")