from flask import request, jsonify, json
from api.incident_model import Incident, IncidentDb, Base_Incident
from api.utilities import IncidentValidator

class IncidentController():
    ''' A class for connecting the views with the models '''
    def __init__(self):
        self.conn_db = IncidentDb()
  
    def create_incident(self):
        '''  A method to create an incidence '''
        data = request.get_json()
        createdBy = data.get("createdBy")
        createdOn = data.get("created_on")
        flag_type = data.get("flag_type")
        location = data.get("location")
        status = data.get("status")
        images = data.get("images")
        videos = data.get("videos")
        comment = data.get("comment")
      
        '''validation of user input fields '''
    
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
        
        self.conn_db.add_incident(incident)
     
        return jsonify({
            "status": 201,
            'data':[{
                'incident_id':incident.incident_id,
             "message": f"created {flag_type} "}]
                
            }), 201
    def get_mall_incidents(self):
        '''geting all incidents '''
        return jsonify ({'status':200, 
                        'data':self.conn_db.get_incident_json()
        }),200
    
    def get_a_specific_incident(self,incident_id ):
        ''' A method to get an incidnt by id'''
        response = self.conn_db.get_incident_by_id(incident_id)
        if response:
            return jsonify({'data':response})
        return jsonify({'message': 'No incident found  please'}) 

    def delete_a_specific_incident(self, incident_id):
        ''' A method to delete a specific incidncence '''
        response = self.conn_db.get_incident_by_id(incident_id)
        if response:
            self.conn_db.incident_list.remove(response)
            return jsonify ({'status': 200, 

                          'data': [{'incident':incident_id,  
                         'message':'Incident successfuly deleted'
                          }]
             }),200
        return jsonify({'status': 200,
                        'message': 'incident record not found'                      
            }), 200

    def update_location(self, incident_id):
        ''' A method for updating the location of an incidence '''
        response = self.conn_db.get_incident_by_id(incident_id)
        if response:
            data = request.get_json()
            if response['status'] == 'Draft':
                self.conn_db.get_incident_by_id(incident_id).update(location = data['location'])
                return jsonify({ 'status': 201,
                    'data': [{ "incident_id": incident_id,
                                "message":  'Updated red-flag record\'s location'  
                    }]
                })
            return jsonify({"status": 400,
                    'error': 'you can not update that please'})  

        return jsonify({"status":400,
            'error':" no incidents currently"})

    def update_comment(self, incident_id):
        ''' Amethod to update the comment of an incident if the status is Draft '''
        response = self.conn_db.get_incident_by_id(incident_id)
        if response:
            data = request.get_json(force=True)
            if response['status'] == 'Draft':
                self.conn_db.get_incident_by_id(incident_id).update(comment = data['comment'])
                return jsonify({ "status": 400,
                        "data":[{"incident_id":incident_id,
                            'message': 'comment successfully updated'}]
                    })
            
            return jsonify({'status': 400,
                    'error': 'you can not update that please'})  
        return jsonify({'status':400,
            'error':' no incidents currently'}) 

#help(IncidentController)        

    
    
    

