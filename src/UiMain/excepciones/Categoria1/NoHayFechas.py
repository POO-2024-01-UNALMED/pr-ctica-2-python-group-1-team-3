from UiMain.excepciones.Categoria1.ExceptionC1 import ExceptionC1

class NoHayFechas(ExceptionC1):
    def __init__(self):
        super().__init__("No hay fechas para realizar la evaluación, realice algún envio para poder hacer uso de esta funcionalidad")