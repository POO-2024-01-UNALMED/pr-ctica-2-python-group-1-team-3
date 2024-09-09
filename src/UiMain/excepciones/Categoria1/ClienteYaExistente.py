from UiMain.excepciones.Categoria1.ExceptionC1 import ExceptionC1

class ClienteYaExistente(ExceptionC1):
    def __init__(self):
        super().__init__("Ya existe un cliente con ese nombre en la lista de clientes")