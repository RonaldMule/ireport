
class BaseUser(object):
    def __init__(self,firstname, lastname, othernames,username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.othernames = othernames
        self.username = username
        self.password = password

class User(object):
    class_counter = 0
    def __init__(self, base_user, phoneNumber, email, registered, isAdmin):
        self.base_user = base_user
        self.phoneNumber = phoneNumber
        self.email = email
        self.registered = False
        self.isAdmin = None
        self.user_id = User.class_counter
        User.class_counter += 1


    def to_json(self):
        return {
              "firstname": self.base_user.firstname,
              "lastname": self.base_user.lastname,
              "othernames": self.base_user.othernames,
              "username": self.base_user.username,
              "password": self.base_user.password,
              "phoneNumber": self.phoneNumber,
              "email": self.email,
              "registered": True,
              "isAdmin" :False,
              "user_id" : self.user_id


        }

class UserDb:
    def __init__(self):
        self.user_list = []

    def add_user(self, user):
        self.user_list.append(user.to_json()) 

    def get_all_users(self):
        return self.user_list

    def get_single_user(self, user_id):
        for user in self.user_list:
            if user['user_id'] == user_id:
                return user
        return None
    def get_registered_user(self,email):
        for user in self.user_list:
            if user['email'] == email:
                return True
            return False    
