rom flask import Blueprint, request, jsonify

app = Blueprint('routes', __name__)

@app.route('/')
def index():
    return "Teste flask API"

###Pode ser substituito por um único end point mas com diferentes requisições HTML

@app.route("/create/aluno", methods=['POST'])
def create_aluno() -> tuple:
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid data'}), 400
    name = data.get('name')
    born_date = data.get('born_date')
    address = data.get("address")
    tutor_name = data.get("tutor_name")
    tutor_phone = data.get("tutor_phone")
    class_shift = data.get("class_shift")
    
    ### chamar função pra criar aluno
    return data, 200

@app.route("/update/aluno", methods=['POST'])
def update_aluno() -> tuple:
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid data'}), 400
    
    id = data.get('id')
    name = data.get('name')
    born_date = data.get('born_date')
    address = data.get("address")
    tutor_name = data.get("tutor_name")
    tutor_phone = data.get("tutor_phone")
    class_shift = data.get("class_shift")

    return data, 200

@app.route("/delete/aluno", methods=['POST'])
def delete_aluno() -> tuple:
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid data'}), 400
    
    id = data.get('id')
    name = data.get('name')
    born_date = data.get('born_date')
    address = data.get("address")
    tutor_name = data.get("tutor_name")
    tutor_phone = data.get("tutor_phone")
    class_shift = data.get("class_shift")

    ### chamar função pra criar aluno
    return data, 200

@app.route("aluno", methods=['GET'])
def get_aluno() -> tuple:
    data = request.get_json()
    if not data.get('id'):
        return jsonify({"error": 'Invalid body'}), 400
    
    id = data.get('id')
    
    ###chamar função para retornar um aluno
    return None, 200

@app.route("alunos", methods=['GET'])
def get_alunos() -> tuple:
    data = request.get_json()
    if not data:
        return jsonify({'error', 'Ivalid data'}), 400
    
    #pegar dados do data
    
    ### chamar função para retornar alunos

    return data, 200