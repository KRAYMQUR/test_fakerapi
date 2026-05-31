import allure
import pytest
from faker import Faker


pytestmark = [allure.feature('Books API'), pytest.mark.regression]
fake = Faker()


@allure.story('Negative cases')
@allure.severity(allure.severity_level.MINOR)
@allure.title('Testing negative book get')
@pytest.mark.parametrize('book_id, status_code', 
                         [
                             (-1,404),
                             ('abc',400)
                         ] )
def test_negative_book_get(books_api, book_id, status_code):
    response = books_api.get_book_by_id(book_id)
    books_api.attach_response(response)
    assert response.status_code == status_code
    
 
@allure.story('Negative cases - post')
@allure.severity(allure.severity_level.MINOR)  
@allure.title('Testing negative post book') 
def test_negative_post_book(books_api):
    data = {
  "id": -1,
  "title": {},
  "description": 'abc',
  "pageCount": 'abc',
  "excerpt": "string",
  "publishDate": fake.iso8601()
}
    response = books_api.post_book(data)
    books_api.attach_response(response)
    assert response.status_code == 400
    
 
@allure.story('Negative cases - put')
@allure.severity(allure.severity_level.MINOR)
@allure.title('Testing negative put book') 
def test_negative_put_book(books_api):
    book_id = 9999
    data = {
  "id": 0,
  "title": "string",
  "description": "string",
  "pageCount": 0,
  "excerpt": "string",
  "publishDate": fake.iso8601()
}
    response = books_api.put_book(book_id,data)
    books_api.attach_response(response)
    assert response.status_code == 200 # fakerestapi возвращает 200
    assert response.json()['id'] == 0 # но возвращает дефолтный объект