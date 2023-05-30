import sys
from flask import Flask
from routes.routes import app as routes_app
from routes.AlunoRoutes import app as aluno_routes
from routes.ProfessorRoutes import app as professor_routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(routes_app)
app.register_blueprint(aluno_routes)
app.register_blueprint(professor_routes)

if __name__== '__main__':
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
