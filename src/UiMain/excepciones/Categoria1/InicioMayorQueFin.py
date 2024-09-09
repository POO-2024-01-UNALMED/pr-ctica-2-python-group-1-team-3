from UiMain.excepciones.Categoria1.ExceptionC1 import ExceptionC1

class InicioMayorQueFin(ExceptionC1):
    def __init__(self):
        super().__init__("La fecha de inicio no puede ser mayor a la fecha de fin")