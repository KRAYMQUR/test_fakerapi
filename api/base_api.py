import requests



class BaseApi:
    BASE_URL = 'https://fakerestapi.azurewebsites.net/api/v1'

    def __init__(self,):
        self.headers = {'Content-Type': 'application/json'}


    def get(self,endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers)
        return response
    
    def post(self,endpoint,data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.post(url, json=data, headers=self.headers)
        return response
        
    def put(self,endpoint,data):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.put(url, json=data, headers=self.headers)
        return response
    
    def delete(self,endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.delete(url, headers=self.headers)
        return response
    