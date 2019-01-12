from flask import jsonify
class IncidentValidator:
   
    @staticmethod
    def validate_flag_type(flag_type):
        ''' Validate the flag type '''
        return isinstance(flag_type, str) and \
        flag_type == "redflag" or flag_type =='intervention'

    @staticmethod
    def validate_status(status):
        '''This method validates the status according to the given status records '''
        return isinstance(status, str) and status == 'Draft' or \
        status == 'under investigation' or status == 'rejected' or \
        status == 'resolved'
    @staticmethod  
    def validate_location(location):
        ''' This method validates location '''  
        return isinstance(location, list) and len(location)==2 \
        and isinstance(location[0], float) and isinstance(location[1], float)  
    @staticmethod
    def check_field_type(comment,createdBy,images,videos):
        ''' A method to check for  wrong data type submited by the user '''
        if not isinstance(comment, str)  and isinstance(createdBy, str)  \
        and isinstance(images, str)  and isinstance(videos,str):
            return True
   
    