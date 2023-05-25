import sys
from flask import Flask
from routes import app as routes_app


app = Flask(__name__)


app.register_blueprint(routes_app)

if __name__== '__main__':
    app.run(host='0.0.0.0', port=int(sys.argv[1]))
