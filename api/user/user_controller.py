from flask import jsonify, request
from api.user.user_model import User, UserDb, BaseUser
from api.user.validate_user import UserValidator
import re

class UserController():
    def __init__(self):
        self.conn_user = UserDb()
        self.validate = UserValidator()
        #self.conn_helper = AuthHelper()
    def create_user(self):
        data = request.get_json()
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        othernames = data.get('othernames')
        username  =data.get('username') 
        password = data.get('password')
        phoneNumber = data.get('phoneNumber')
        email  = data.get('email')
       

        ''' Validation of user input '''
        if not isinstance(firstname, str) or firstname.isspace():
            return jsonify({'error': 'first name cannot be empty and should be a string'})
        elif len(firstname) <=2:
            return jsonify({'error': 'Enter a firstname valid name'})

        if not isinstance(lastname, str) or lastname.isspace():
            return jsonify({'error': 'lastname cannot be empty and should be a string'})
        elif len(lastname) <=2:
            return jsonify({'error': 'Enter a last valid name'})

        if not isinstance(othernames, str):
            return jsonify({'error': 'Other name should be a string'})  

        if not self.validate.validate_phoneNumber(data['phoneNumber']):
            return jsonify({'error': 'expected the phonenumber to be an int with atleast 10 values '})
            

        if not self.validate.validate_password(data['password']):
            return jsonify({'error': 'password should atleast be 8 characters'}) 

        if not isinstance(username, str) or username.isspace():
            return jsonify({'error': 'username should be  a string and should not be empty'})
        elif len(username) <=2:
            return jsonify({'error': 'Enter a valid username'})

        if not isinstance(email, str) or email.isspace():
            return jsonify({'error': 'Email should not be empty'})
        elif not re.match(r"[^@.]+@[A-Za-z]+\.[a-z]+", email):
            return jsonify({'error':'Enter a valid email address'})

        for user in self.conn_user.user_list:
            if user['email'] == data['email']:
                return jsonify({'message': 'user already existis please login'})
                
        
          
        user = User(BaseUser(firstname, lastname, othernames,username), \
        phoneNumber, email, password)

        self.conn_user.add_user(user)
        
        return jsonify({'status': 201,
                            'data':[{         
                                    'user_id':user.user_id,
                                    'user': user.to_json(),
                                    'message': 'created  new user'}]
                
                        }), 201

   
    def login_user(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        for registered_user in self.conn_user.get_all_users():
            if registered_user['email'] == email and registered_user['password'] == password:
                return jsonify({'status': 201,                            
                                'message':'login successful'}),201
            return jsonify({'status':400,
                            'message': 'Email or password is wrong'}),400                    
        return jsonify({'status':200,
                        'error':'No user currently created'}),200                    