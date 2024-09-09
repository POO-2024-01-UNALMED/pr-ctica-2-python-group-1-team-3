from UiMain.excepciones.Categoria2.ExceptionC2 import ExceptionC2

class CategoriaNoValida(ExceptionC2):
    def __init__(self):
        super().__init__("Se debe ingresar una categoría válida (panaderia - frutas y verduras - salsas y mermeladas - bebidas)")