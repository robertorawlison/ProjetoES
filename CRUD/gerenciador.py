import pyodbc
from CRUD.usuarios import Usuarios

class GerenciadorBancoDados:
    def __init__(self):
        self.conn = pyodbc.connect(
            'DRIVER={MySQL ODBC 8.0 ANSI Driver};'
            'SERVER=localhost;'
            'DATABASE=appES;'
            'UID=seu_usuario;'
            'PWD=sua_senha;'
        )
        self.cursor = self.conn.cursor()

        # Instâncias das classes
        self.usuarios = Usuarios(self.conn, self.cursor)

        