from flask import Flask
from api.incident.view_incident import incident_v1
#from flask_jwt_extended import JWTManager
from config import  config

def create_app(config_name):
    '''creating the app instance '''
    app = Flask(__name__, )
   

    #blueprints for url
    app.register_blueprint(incident_v1, url_prefix='/api/v1') 
    return app

