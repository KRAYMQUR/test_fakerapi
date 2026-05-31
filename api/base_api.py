import requests
import os 
from dotenv import load_dotenv


load_dotenv()
class BaseApi:
    BASE_URL = os.getenv('BASE_URL', 'https://fakerestapi.azurewebsites.net/api/v1')


    def __init__(self,):
        self.session = requests.Session()
        self.session.headers = {'Content-Type': 'application/json'}


    def get(self,endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        return self.session.get(url,timeout=10,)
    
    def post(self,endpoint,data):
        url = f"{self.BASE_URL}/{endpoint}"
        return self.session.post(url,timeout=10,json=data)

    def put(self,endpoint,data):
        url = f"{self.BASE_URL}/{endpoint}"
        return self.session.put(url,timeout=10,json=data)
    
    def delete(self,endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        return self.session.delete(url,timeout=10)
    