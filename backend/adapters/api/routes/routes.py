from flask import Blueprint, request, jsonify
import sys
sys.path.append('../../../')

from backend.adapters.controllers.controller import AlunoController, ProfessorController

app = Blueprint('routes', __name__)

@app.route('/')
def index():
    return "Teste flask API"