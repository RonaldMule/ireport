from flask import Flask
from api.incident.view_incident import incident_v1
#from flask_jwt_extended import JWTManager
from config import  config

def create_app(config_name):
    '''creating the app instance '''
    app = Flask(__name__, )
    app.config['JWT_SECRET_KEY'] = 'wh)0**yp@ass+wh3nnot^passis~@!!provided'
    app.secret_key = 'Z4X*N)_P%***~md9ag01a'
    #jwt = JWTManager(app)

    #blueprints for url
    app.register_blueprint(incident_v1, url_prefix='/api/v1') 
    return app

