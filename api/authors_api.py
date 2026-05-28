from api.base_api import BaseApi 
import allure

class AuthorsApi(BaseApi):
    
    
    def get_authors(self):
        with allure.step("Get /Authors"):
            return self.get('Authors')
    
    def get_author_by_id(self,id):
        with allure.step(f"Get /Authors/{id}"):
            return self.get(f"Authors/{id}")
    
    def post_author(self,data):
        with allure.step("Post /Authors"):
            return self.post('Authors',data)
    
    def put_author(self,id,data):
        with allure.step(f"Put /Authors/{id}"):
            return self.put(f"Authors/{id}", data)
    
    def delete_author(self,id):
        with allure.step(f"Delete /Authors/{id}"):
            return self.delete(f"Authors/{id}")
    
    