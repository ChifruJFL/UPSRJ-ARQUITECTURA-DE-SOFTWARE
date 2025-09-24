# entity_server.py
# Archivo mínimo con la interfaz que los tests esperan

class UserRepository:
    def get_all(self):
        # Retorna una lista de ejemplo
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bod"}]

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def list_users(self):
        # Devuelve todos los usuarios desde el repositorio
        return self.repository.get_all()
