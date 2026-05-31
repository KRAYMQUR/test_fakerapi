from api.base_api import BaseApi
import allure

class BooksApi(BaseApi):
    
    
    def get_books(self):
        with allure.step("Get /Books"):
            return self.get('Books')
    
    def get_book_by_id(self,book_id):
        with allure.step(f"Get /Books/{book_id}"):
            return self.get(f'Books/{book_id}')
    
    def post_books(self,data):
        with allure.step("Post /Books"):
            return self.post('Books',data)
    
    def put_books(self,book_id,data):
        with allure.step(f"Put /Books/{book_id}"):
            return self.put(f'Books/{book_id}',data) 
    
    def delete_books(self,book_id):
        with allure.step(f"Delete /Books/{book_id}"):
            return self.delete(f'Books/{book_id}')