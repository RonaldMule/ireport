from flask import request, jsonify, json
from api.incident_model import Incident, IncidentDb, Base_Incident
from api.utilities import IncidentValidator
incident_list = IncidentDb()
class IncidentController():
    def __init__(self):
        pass
  
    def create_incident(self):
        data = request.get_json()
        createdBy = data.get("createdBy")
        createdOn = data.get("created_on")
        flag_type = data.get("flag_type")
        location = data.get("location")
        status = data.get("status")
        images = data.get("images")
        videos = data.get("videos")
        comment = data.get("comment")
      
        #validation of user input
    
       
        if not  IncidentValidator.validate_status(status):
            return jsonify ({'status': 400,
                            'error': 'The status provided is not defined'
        })
        if not IncidentValidator.validate_flag_type(flag_type):
            return jsonify ({'status': 400,
                            'error': 'The flag_type is not defined'
            })
       

        incident = Incident(Base_Incident(createdOn, createdBy, 
         flag_type, location), status, images, videos, comment)
        
        incident_list.add_incident(incident)
     
        return jsonify({
            "status": 201,
            'data':[{
                'incident_id':incident.incident_id,
             "message": f"created {flag_type} "}]
                
            }), 201
    def get_mall_incidents(self):
        '''geting all incidents '''
        return jsonify ({'status':200, 
                        'data':incident_list.get_incident_json()
        }),200
    
    def get_a_specific_incident(self,incident_id ):
        response = incident_list.get_incident_by_id(incident_id)
        if response:
            return jsonify({'data':response})
        return jsonify({'message': 'No incident found  please'}) 

    def delete_a_specific_incident(self, incident_id):
        incident = incident_list.get_incident_by_id(incident_id)
        if incident:
            delete_incident = incident_list.delete_incident(incident_id)
 
            return jsonify ({'status': 200, 
                          'data': delete_incident,  
                         'message':'Incident successfuly deleted.\
                         however we advice you to report any incidences'
             }),200
        return jsonify({'status': 200,
                        'message': 'incident record not found'                      
            }), 200

    def update_location(self, incident_id, status='Draft'):
        response = incident_list.get_incident_by_id(incident_id)
        if response:
            data = request.get_json(force=True)
            if response['status'] == 'Draft':
                response.update(location = data['location'])
                return jsonify({'message': 'update location was successfully made'})
            return jsonify({'message': 'you can not update that please'})  
        return jsonify({'message':" no incidents currently"})
    
    

