from models.book import Book
import allure 


pytestmark = [allure.feature('Books API')]


@allure.story('Get books')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Testing get books')
def test_get_books(books_api):
    response = books_api.get_books()
    allure.attach(response.text, name="Response body",
                  attachment_type=allure.attachment_type.JSON)
    assert response.status_code == 200
    assert len(response.json()) > 0
    book = Book(**response.json()[0])
    
    
    
    
    
   
@allure.story('Get book by id')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Testing get book by id')
def test_get_book_by_id(books_api):
    book_id = 9
    response = books_api.get_book_by_id(book_id)
    allure.attach(response.text, name="Response body",
                  attachment_type=allure.attachment_type.JSON)
    assert response.status_code == 200
    book = Book(**response.json())
    assert book.id == book_id

@allure.story('Delete books')  
@allure.severity(allure.severity_level.NORMAL)   
@allure.title('Testing delete books')
def test_delete_books(books_api):
    book_id = 5
    response = books_api.delete_books(book_id)
    assert response.status_code == 200


@allure.story('Put books')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Testing put books')
def test_put_books(books_api):
    book_id = 6
    data = {
  "id": book_id,
  "title": "test",
  "description": "test",
  "pageCount": 1,
  "excerpt": "test",
  "publishDate": "2026-05-26T06:54:49.557Z"

    }
    response = books_api.put_books(book_id,data)
    allure.attach(response.text, name="Response body",
              attachment_type=allure.attachment_type.JSON)
    assert response.status_code == 200
    book = Book(**response.json())
    assert book.title == 'test'
    assert book.id == book_id 
    assert book.pageCount == 1
    

@allure.story('Post books')   
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Testing post books')
def test_post_books(books_api):
    data = {
  "id": 666,
  "title": "Author123",
  "description": "Testim in id 66",
  "pageCount": 2,
  "excerpt": "ahaha",
  "publishDate": "2026-05-26T07:27:32.559Z"
}
    
    response = books_api.post_books(data)
    allure.attach(response.text, name="Response body",
              attachment_type=allure.attachment_type.JSON)
    assert response.status_code == 200
    book = Book(**response.json())
    assert book.title == 'Author123'
    assert book.pageCount == 2
    assert book.excerpt == 'ahaha'
    
    
    
