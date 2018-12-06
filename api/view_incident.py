from flask import Flask, request, jsonify
from api.controller import  IncidentController

call_incident = IncidentController()

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "hello browser do yo see me"})

@app.route('/api/v1/incidents', methods= ['POST'])
def create_new_incident():
    return call_incident.create_incident()

@app.route('/api/v1/incidents', methods = ['GET'])
def get_all_new_incidents():
    return call_incident.get_mall_incidents()

@app.route('/api/v1/incidents/<int:incident_id>', methods = ['GET'])
def get_single_incidents(incident_id):
    return call_incident.get_a_specific_incident(incident_id)

@app.route('/api/v1/incidents/<int:incident_id>', methods = ['DELETE'])
def delete_single_incidents(incident_id):
    return call_incident.delete_a_specific_incident(incident_id)

@app.route('/api/v1/incidents/<int:incident_id>/location', methods = ['PATCH'])
def update_incident_location(incident_id):
    return call_incident.update_location(incident_id)







