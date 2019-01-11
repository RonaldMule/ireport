from flask import  jsonify

from api.incident.controller import  IncidentController
from api.user.user_controller import UserController
from api.incident import incident_v1


call_incident = IncidentController()
call_user = UserController()



@incident_v1.route('/')
def index():
    return jsonify({"message": "hello browser do yo see me"},201)

@incident_v1.route('/incidents', methods= ['POST'])
def create_new_incident():
    return call_incident.create_incident()

@incident_v1.route('/incidents', methods = ['GET'])
def get_all_new_incidents():
    return call_incident.get_mall_incidents()
    

@incident_v1.route('/incidents/<int:incident_id>', methods = ['GET'])
def get_single_incidents(incident_id):
    return call_incident.get_a_specific_incident(incident_id)

@incident_v1.route('/incidents/<int:incident_id>', methods = ['DELETE'])
def delete_single_incidents(incident_id):
    return call_incident.delete_a_specific_incident(incident_id)


@incident_v1.route('/incidents/<int:incident_id>/location', methods = ['PATCH'])
def update_incident_location(incident_id):
    return call_incident.update_location(incident_id)

@incident_v1.route('/incidents/<int:incident_id>/comment', methods = ['PATCH'])
def update_incident_comment(incident_id):
    return call_incident.update_comment(incident_id)   

@incident_v1.route('/users', methods= ['POST'])
def create_api_users():
    return call_user.create_user()

@incident_v1.route('/login', methods=['POST'])
def create_login():
    return call_user.login_user()
