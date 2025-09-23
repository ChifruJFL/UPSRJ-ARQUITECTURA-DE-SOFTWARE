from flask import Flask, jsonify
import sys
import os

# Agrega la carpeta actual (01_basic_concepts) al path para poder importar py_utils
sys.path.append(os.path.dirname(__file__))

from py_utils.logger import set_logging, plog
from logging import DEBUG, INFO

# Configurar logging
set_logging(log_file='app.log')

# --- Repository ---
class UserRepository:
    """Acceso a datos de usuarios."""
    def get_users(self):
        plog("Fetching users from repository", DEBUG)
        return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

# --- Service ---
class UserService:
    """Lógica de negocio de usuarios."""
    def __init__(self, repository: UserRepository):
        plog("Initializing UserService with repository", DEBUG)
        self.repository = repository

    def list_users(self):
        plog("Listing users from service", INFO)
        return self.repository.get_users()

# --- Flask App ---
app = Flask(__name__)
user_service = UserService(UserRepository())

@app.route("/users")
def get_users():
    plog("Received request for /users endpoint", INFO)
    users = user_service.list_users()
    return jsonify(users)

# Entry point
if __name__ == "__main__":
    plog("Starting Flask app", INFO)
    app.run(debug=True)
