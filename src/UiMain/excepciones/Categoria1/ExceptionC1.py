from UiMain.excepciones.ErrorAplicacion import ErrorAplicacion

class ExceptionC1(ErrorAplicacion):
    def __init__(self, mensaje):
        self._excepcion = "Categoría 1: " + mensaje
        super().__init__(self._excepcion)