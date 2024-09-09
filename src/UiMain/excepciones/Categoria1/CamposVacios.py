from UiMain.excepciones.Categoria1.ExceptionC1 import ExceptionC1

class CamposVacios(ExceptionC1):
    def __init__(self, campos = ""):
        super().__init__("Faltan los siguientes campos por llenar: " + campos)