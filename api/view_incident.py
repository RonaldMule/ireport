from flask import Flask, request, jsonify
from api.controller import  IncidentController

call_incident = IncidentController()

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "hello browser do yo see me"})

@app.route('/incidents', methods= ['POST'])
def create_new_incident():
    return call_incident.create_incident()



