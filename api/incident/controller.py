from flask import request, jsonify, json
from api.incident.incident_model import Incident, IncidentDb, Base_Incident
from api.incident.utilities import IncidentValidator

class IncidentController():
    ''' A class for connecting the views with the models '''
    def __init__(self):
        self.conn_db = IncidentDb()
        self.validate = IncidentValidator()
  
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
    
        if not  self.validate.validate_status(status):
            return jsonify ({'status': 400,
            'error': 'The status provided is not defined. Please note that it should either be [\'Draft\',\'Under investigation\',\'rejected\', or \'resolved\']'}), 400
        
        if not self.validate.validate_flag_type(flag_type):
            return jsonify ({'status': 400,
            'error': 'The flag_type is not defined. Please note that, it should either be "red-flag" or "intervention"'}),400
      
        if self.validate.check_field_type(data['comment'], data['createdBy'], data['images'],data['videos']):
            return jsonify({'status': 400,
                            'error': 'field should be a string'
            }),400    
        
        
        if not self.validate.validate_location(location):
            return jsonify({'status': 400,
                            'error': 'Please verify the location'}),400                                           
       

        incident = Incident(Base_Incident(createdBy, status, 
         flag_type, location), images, videos, comment)
        
        self.conn_db.add_incident(incident)
     
        return jsonify({
            "status": 201,
            'data':[{
                'incident_id':incident.incident_id,
                "message": "created {flag_type}".format(flag_type=flag_type)}]
                   
            }), 201
    def get_mall_incidents(self):
        '''geting all incidents '''
        response = self.conn_db.get_incident_json()
        if response:
            return jsonify ({'status':200, 
                        'data':response }),200
        return jsonify({'status': 200,
                    'error': 'There are no incidents currently to fetch.'}),200                 

        
    
    def get_a_specific_incident(self,incident_id ):
        ''' A method to get an incidnt by id'''
        response = self.conn_db.get_incident_by_id(incident_id)
        if response:
            return jsonify({'data':response})
        return jsonify({'status': 200,
                    'error': 'The id provided couldn\'t be found.'}),200

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
            location=data['location']
            if not self.validate.validate_location(location):
                return jsonify({'status': 400,
                                'error': 'Please verify the location, it should be a list of floating numbers representing the latitudes and long tudes'}),400
                      
            if response['status'] == 'Draft':
                self.conn_db.get_incident_by_id(incident_id).update(location = data['location'])           
                return jsonify({'status':200,
                                'data':response,
                                'message': 'location was successfully made'}),200

            return jsonify({'status':400,
                            'message': 'Sorry you can not update this record please'}), 400  

        return jsonify({'status': 200,
                        'message':"No incident records currently "})  

    def update_comment(self, incident_id):
        ''' Amethod to update the comment of an incident if the status is Draft '''
        response = self.conn_db.get_incident_by_id(incident_id)
        if response:
            data = request.get_json()
            comment = data['comment']
            if not isinstance(comment, str):
                return jsonify({'status': 400,
                            'error': 'The comment should be a string'}),400
            if response['status'] == 'Draft':                
                self.conn_db.get_incident_by_id(incident_id).update(comment = data['comment'])
                return jsonify({'status':200,
                                'data':response,
                                'message': 'location was successfully made'}),200
            return jsonify({'status':400,
                            'message': 'Sorry you can not update this record please'}), 400  
  
        return jsonify({'status': 200,
                        'message':"No incident records currently "}),200 
    
    

