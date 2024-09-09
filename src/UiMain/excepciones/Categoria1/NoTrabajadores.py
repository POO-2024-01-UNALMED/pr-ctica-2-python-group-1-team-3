from UiMain.excepciones.Categoria1.ExceptionC1 import ExceptionC1

class NoTrabajadores(ExceptionC1):
    def __init__(self):
        super().__init__("No hay pagos pendientes para este tipo de trabajadores")