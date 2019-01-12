import re
class UserValidator:
    @staticmethod
    def validate_phoneNumber(phoneNumber):
        if isinstance(phoneNumber, str):
            if len(phoneNumber)==10:
                return True
            return None     

    @staticmethod
    def validate_password(password):
        if isinstance(password, str):
            if len(password) >=8:
                return True
            return False   

    @staticmethod
    def check_field_type(firstname,lastname,othernames,username):
        '''A method to check for data type submitted by the user '''
        if not isinstance(firstname, str) and isinstance(lastname, str) \
        and isinstance(othernames, str) and isinstance(username, str):
            return True
    @staticmethod
    def validate_email(email):
        if not isinstance(email, str) or email.isspace():
            return  True
        elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
            return True       