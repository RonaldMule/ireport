import itertools
from datetime import datetime
class Base_Incident(object):
    def __init__(self, createdOn, createdBy, flag_type, location): 
        self.createdOn = str(datetime.utcnow())
        self.createdBy = createdBy
        self.flag_type = flag_type
        self.location = location

    
    

class Incident(object):
    class_counter = 1
    def __init__(self, base_incident, status, images, videos, comment):
        self.base_incident = base_incident
        self.status = status
        self.images = images
        self.videos = videos
        self.comment = comment
        self.incident_id = Incident.class_counter
        Incident.class_counter += 1

    def to_json(self):
        return {
            "incident_id": self.incident_id,
            "createdOn": self.base_incident.createdOn,
            "createdBy": self.base_incident.createdBy,
            "flag_type": self.base_incident.flag_type,
            "location": self.base_incident.location,
            "status": self.status,
            "images": self.images,
            "videos": self.videos,
            "comment":self.comment 
    
    }    
#creating an incidentdb (list)
class IncidentDb():
    def __init__(self):
        self.incident_list = []

    def add_incident(self,incident):
        self.incident_list.append(incident.to_json())
          
    def get_incident_json(self):
        ''' A method for getting all incidents '''
        return self.incident_list 
 

    def get_incident_by_id(self, incident_id):
        for incident in self.incident_list:
            if incident['incident_id'] == incident_id:
                return incident
        return None   
   