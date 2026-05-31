from api.base_api import BaseApi
import allure


class AuthorsApi(BaseApi):

    def get_authors(self):
        with allure.step("Get /Authors"):
            return self.get('Authors')

    def get_author_by_id(self, author_id):
        with allure.step(f"Get /Authors/{author_id}"):
            return self.get(f"Authors/{author_id}")

    def post_author(self, data):
        with allure.step("Post /Authors"):
            return self.post('Authors', data)

    def put_author(self, author_id, data):
        with allure.step(f"Put /Authors/{author_id}"):
            return self.put(f"Authors/{author_id}", data)

    def delete_author(self, author_id):
        with allure.step(f"Delete /Authors/{author_id}"):
            return self.delete(f"Authors/{author_id}")
