from flask import Flask, jsonify, request, render_template
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

from exercises.basic_concepts.repository.user_repository import UserRepository
from exercises.basic_concepts.service.user_service import UserService

app = Flask(__name__, template_folder="../templates")
user_repository = UserRepository()
user_service = UserService(user_repository)

@app.route("/users")
def get_users():
    """HTTP endpoint that returns a JSON list of users."""
    plog("Received request for /users endpoint", INFO)
    users = user_service.list_users()
    return jsonify(users)

@app.route('/', methods=['GET'])
def home():
    """Render the user search form."""
    return render_template("search.html")

@app.route('/search', methods=['POST'])
def search():
    requested_service_id = request.form.get("id")
    requested_service_keyword = request.form.get("keyword")
    
    if requested_service_id:
        user = user_service.get_by_id(requested_service_id)
    elif requested_service_keyword:
        user = user_service.get_by_keyword(requested_service_keyword)
    
    if not user:
        plog(f"User not found.", ERROR)
        return render_template("error.html")
    else:
        plog(f"User found: {user['name']}.", DEBUG)
        return render_template("result.html", user=user) 
