from flask import Blueprint, request, jsonify
import sys
sys.path.append('../../../')

from backend.adapters.controllers.AlunoController import AlunoController

app = Blueprint('routes', __name__)

####                                              ####
#       Implementação das rotas para os alunos       #
####                                              ####

@app.route("/create/aluno", methods=['POST'])
def create_aluno() -> tuple:
    data = request.get_json()

    # Check if all required fields are present in the request data
    required_fields = ["name", "born_date", "address", "tutor_name", "tutor_phone", "class_shift"]
    if not data or not all(key in data for key in required_fields):
        # Return an error response if any required field is missing
        error_response = {'error':'Invalid data'}
        return jsonify(error_response), 400

    name = data["name"]
    born_date = data["born_date"]
    address = data["address"]
    tutor_name = data["tutor_name"]
    tutor_phone = data["tutor_phone"]
    class_shift = data["class_shift"]

    response = AlunoController().create(name, born_date, address, tutor_name, tutor_phone, class_shift)
    if not response:
        return jsonify({"error":"Invalid credentials"}), 400

    return jsonify(data), 200

@app.route("/update/aluno", methods=['POST'])
def update_aluno() -> tuple:
    """Update an existing aluno.\\
    Returns:
        A tuple containing the updated data and a status code.
    """
    data = request.get_json()
    if not data.get('id'):
        return jsonify({'error': 'ID not given'}), 400

    aluno_id = data.get('id')
    name = data.get('name')
    born_date = data.get('born_date')
    address = data.get("address")
    tutor_name = data.get("tutor_name")
    tutor_phone = data.get("tutor_phone")
    class_shift = data.get("class_shift")

    response = AlunoController().update(aluno_id, name, born_date, address,
                                        tutor_name, tutor_phone, class_shift)
    if not response:
        return jsonify({"error":"Invalid credentials"}), 400

    return data, 200

@app.route("/delete/aluno", methods=['POST'])
def delete_aluno() -> tuple:
    """Delete an existing aluno.\\
    Returns:
        A tuple containing the deleted data and a status code.
    """
    data = request.get_json()
    if not data.get('id'):
        return jsonify({'error': 'Invalid data'}), 400
    aluno_id = data.get('id')

    response = AlunoController().remove(aluno_id)
    if not response:
        return jsonify({"error":"Invalid credentials"}), 400
    return data, 200


@app.route("/alunos/<name>", methods=['GET'])
def get_alunos(name) -> tuple:
    data = AlunoController().get_alunos_by_name(name)
    if not data:
        return jsonify({"error": "Aluno does not exist"}), 400

    return jsonify(data), 200


@app.route("/all_alunos/", methods=['GET'])
def get_all_alunos() -> tuple:
    """Get all alunos from the database.\\
    Returns:
        A tuple containing the data and a status code.
    """
    data = AlunoController().get_all_alunos()
    if not data:
        return jsonify({"error": "There are no alunos in the database"}), 400

    return jsonify(data), 200


@app.route('/aluno', methods=['GET'])
def get_aluno_paginated() -> tuple:
    """Get alunos from the database paginated.\\
    Returns:
        A tuple containing the data and a status code.
    """
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('_limit', 10, type=int)
    name_like = request.args.get('name_like', '', type=str)
    offset = (page - 1) * limit

    alunos = AlunoController().get_alunos_paginated(offset, limit, name_like)

    if not alunos:
        return jsonify({"error": "There are no alunos in the database"}), 400

    return jsonify(alunos), 200