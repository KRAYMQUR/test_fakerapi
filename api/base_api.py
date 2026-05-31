import requests
import os
from dotenv import load_dotenv
import allure
import logging


load_dotenv()
logger = logging.getLogger(__name__)

class BaseApi:
    BASE_URL = os.getenv('BASE_URL', 'https://fakerestapi.azurewebsites.net/api/v1')

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {'Content-Type': 'application/json'}

    
    def get(self, endpoint: str) -> requests.Response:
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.get(url, timeout=10)
        logger.info(f"GET {url} → {response.status_code} ({response.elapsed.total_seconds():.2f}s)")
        return response

    def post(self, endpoint: str, data: dict) -> requests.Response:
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.post(url, timeout=10, json=data)
        logger.info(f"POST {url} → {response.status_code} ({response.elapsed.total_seconds():.2f}s)")
        return response

    def put(self, endpoint: str, data: dict) -> requests.Response:
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.put(url, timeout=10, json=data)
        logger.info(f"PUT {url} → {response.status_code} ({response.elapsed.total_seconds():.2f}s)")
        return response

    def delete(self, endpoint: str) -> requests.Response:
        url = f"{self.BASE_URL}/{endpoint}"
        response = self.session.delete(url, timeout=10)
        logger.info(f"DELETE {url} → {response.status_code} ({response.elapsed.total_seconds():.2f}s)")
        return response

    def attach_response(self, response: requests.Response) -> None:
        allure.attach(response.text, name="Response body",
                      attachment_type=allure.attachment_type.JSON)
