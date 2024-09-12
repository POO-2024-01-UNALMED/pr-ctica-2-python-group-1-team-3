from UiMain.excepciones.Categoria2.ExceptionC2 import ExceptionC2

class NumerosEnteros(ExceptionC2):
    def __init__(self, campos):
        self.campos = campos
        super().__init__(f"Los siguientes campos deben contener solo números enteros: {', '.join(campos)}")