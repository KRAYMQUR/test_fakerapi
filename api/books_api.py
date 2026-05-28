from api.base_api import BaseApi
import allure

class BooksApi(BaseApi):
    
    
    def get_books(self):
        with allure.step("Get /Books"):
            return self.get('Books')
    
    def get_book_by_id(self,id):
        with allure.step(f"Get /Books/{id}"):
            return self.get(f'Books/{id}')
    
    def post_books(self,data):
        with allure.step("Post /Books"):
            return self.post('Books',data)
    
    def put_books(self,id,data):
        with allure.step(f"Put /Books/{id}"):
            return self.put(f'Books/{id}',data) 
    
    def delete_books(self,id):
        with allure.step(f"Delete /Books/{id}"):
            return self.delete(f'Books/{id}')