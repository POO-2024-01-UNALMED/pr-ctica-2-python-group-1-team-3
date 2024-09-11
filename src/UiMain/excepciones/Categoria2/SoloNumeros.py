from UiMain.excepciones.Categoria2.ExceptionC2 import ExceptionC2

class SoloNumeros(ExceptionC2):
    def __init__(self, campos):
        # Convertir la lista de campos en una cadena de texto, separando con comas
        if type(campos) == str:
            campos = [campos]
        campos_str = ', '.join(campos)
        super().__init__("Solo se pueden ingresar números en los campos: " + campos_str)