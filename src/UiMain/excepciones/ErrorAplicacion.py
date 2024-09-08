class ErrorAplicacion(Exception):
    def __init__(self, mensaje):
        self._excepcion = "Manejo de errores de la Aplicacion: " + mensaje
        super().__init__(self._excepcion)