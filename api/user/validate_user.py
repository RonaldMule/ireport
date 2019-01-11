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

