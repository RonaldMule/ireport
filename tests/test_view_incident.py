import pytest
from api import create_app
import json



@pytest.fixture()
def client():
    app = create_app('Testing')
    test_client = app.test_client()
    return test_client

class TestEndPoints:
    '''
    Test the endpoints
    '''
    def test_create_new_incident(self, client):
        response = client.post("/api/v1/incidents",content_type="application/json",  data=json.dumps({
        "comment": " mulyowa is not corrupt but his boss is corrupt ",
        "createdBy": "mule",
        "createdOn": "2018-12-20 02:47:37.869494",
        "flag_type": "redflag",
        "images": "http/www.com",
        "incident_id": 1,
        "location": [10.00, 100.012],
        "status": "Draft",
        "videos": "http/url"
        }))
        assert response.status_code ==201
    def test_get_all_new_incidents(self, client):
        response = client.get("/api/v1/incidents")
        assert response.status_code == 200

    def test_get_single_incidents(self, client):
        response =client.get("/api/v1/incidents/1")  
        assert response.status_code == 200   
    def test_delete_single_incidents(self, client):
        response =client.delete("/api/v1/incidents/1")  
        assert response.status_code == 200       
    def test_update_incident_location(self, client):
        response =client.patch("/api/v1/incidents/1/location")  
        assert response.status_code == 200

    def test_update_incident_comment(self, client):
        response =client.patch("/api/v1/incidents/1/comment")  
        assert response.status_code == 200     
    def test_create_api_users(self, client):
        response = client.post("/api/v1/users",content_type="application/json",  data=json.dumps({
            "email": "mule@yahoo.com",
            "firstname": "muleto",
            "lastname": "mbamabzi",
            "othernames": "legosh",
            "password": "12345678",
            "phoneNumber": "0704970950",  
            "username": "kasawuli"
        }))
        assert response.status_code ==201
    def test_create_login (self, client):
        response = client.post("/api/v1/users",content_type="application/json",  data=json.dumps({
            "email": "mule@yahoo.com",
	        "password": "12345678"	
        }))
        assert response.status_code ==200



