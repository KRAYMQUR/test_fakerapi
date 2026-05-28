import allure



pytestmark = [allure.feature('Books API')]


@allure.story('Negative cases')
@allure.severity(allure.severity_level.MINOR)
@allure.title('Testing negative book id')
def test_negative_book_id(books_api):
    book_id = -1 
    response = books_api.get_book_by_id(book_id)
    assert response.status_code == 404 
    
   
@allure.story('Negative cases - invalid id')
@allure.severity(allure.severity_level.MINOR) 
@allure.title('Testing negative book invalid id')   
def test_negative_book_invalid_id(books_api):
    book_id = 'abc'
    response = books_api.get_book_by_id(book_id)
    assert response.status_code == 400
    
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
  "publishDate": "2026-05-28T06:50:37.660Z"
}
    response = books_api.post_books(data)
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
  "publishDate": "2026-05-28T06:52:16.268Z"
}
    response = books_api.put_books(book_id,data)
    assert response.status_code == 200 # fakerestapi возвращает 200
    assert response.json()['id'] == 0 # но возвращает дефолтный объект