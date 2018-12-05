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
