from flask import Blueprint, request, jsonify
import sys
sys.path.append('../../../')

from backend.adapters.controllers.ProfessorController import ProfessorController

app = Blueprint('routes', __name__)

####                                                   ####
#       Implementação das rotas para os professores       #
####                                                   ####

@app.route("/login", methods=['POST'])
def login() -> tuple:
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    print(f'recebido no flask: {email}, {password}') # TODO: remove this
    if not email or not password:
        return jsonify({"error":"Invalid data"}), 400

    response = ProfessorController().login(email, password)
    if not response:
        return jsonify({"error":"Invalid email or password"}), 401

    return jsonify(response), 200

app.route("/create/professor", methods=['POST'])
def create_professor() -> tuple:
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid data'}), 400
    
    name = data.get('name')
    email = data.get('email')
    password = data.get("password")
    
    response = ProfessorController().create(name, email, password)
    if not response:
        return jsonify({"error":"Invalid credentials"}), 200
    
    return data, 200

@app.route("/update/professor", methods=['POST'])
def update_professor() -> tuple:
    data = request.get_json()
    if not data.get('id'):
        return jsonify({'error': 'ID not given'}), 400
    
    id = data.get('id')
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    
    response = ProfessorController().update(id, name, email, password)
    if not response:
        return jsonify({"error": "Invalid ID"}), 200
    return data, 200

@app.route("/delete/professor", methods=['POST'])
def delete_professor() -> tuple:
    data = request.get_json()
    if not data.get('id'):
        return jsonify({'error': 'Invalid data'}), 400
    
    id = data.get('id')

    response = ProfessorController().remove(id)
    if not response:
        return jsonify({"error": "Invalid ID"}), 200
    return data, 200