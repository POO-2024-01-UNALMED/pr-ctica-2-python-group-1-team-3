from UiMain.excepciones.ErrorAplicacion import ErrorAplicacion

class ExceptionC2(ErrorAplicacion):
    def __init__(self, mensaje): 
        self._excepcion = "Categoría 2: " +  mensaje
        super().__init__(self._excepcion)