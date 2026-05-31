from models.book import Book
import allure
from tests.constants import BOOK_ID_GET, BOOK_ID_POST, BOOK_ID_PUT
import pytest
from faker import Faker


pytestmark = [allure.feature('Books API')]
fake = Faker()


@pytest.mark.smoke
@pytest.mark.regression
@allure.story('Get books')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Testing get books')
def test_get_books(books_api):
    response = books_api.get_books()
    books_api.attach_response(response)
    assert response.status_code == 200
    assert len(response.json()) > 0
    book = Book(**response.json()[0])
    assert book.id is not None
    assert book.title is not None
    assert response.elapsed.total_seconds() < 2


@pytest.mark.regression
@allure.story('Get book by id')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Testing get book by id')
@pytest.mark.parametrize('book_id', [BOOK_ID_GET, 15])
def test_get_book_by_id(books_api, book_id):
    response = books_api.get_book_by_id(book_id)
    books_api.attach_response(response)
    assert response.status_code == 200
    book = Book(**response.json())
    assert book.id == book_id


@pytest.mark.regression
@allure.story('Delete books')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Testing delete books')
def test_delete_books(books_api, created_book):
    response = books_api.delete_book(created_book)
    assert response.status_code == 200


@pytest.mark.regression
@allure.story('Put books')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Testing put books')
def test_put_books(books_api):
    book_id = BOOK_ID_PUT
    title = fake.word()
    page_count = fake.random_int(min=1, max=500)
    data = {
        "id": book_id,
        "title": title,
        "description": fake.sentence(),
        "pageCount": page_count,
        "excerpt": fake.text(max_nb_chars=50),
        "publishDate": fake.iso8601()

    }
    response = books_api.put_book(book_id, data)
    books_api.attach_response(response)
    assert response.status_code == 200
    book = Book(**response.json())
    assert book.title == title
    assert book.id == book_id
    assert book.pageCount == page_count


@pytest.mark.regression
@allure.story('Post books')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Testing post books')
def test_post_books(books_api):
    title = fake.word()
    page_count = fake.random_int(min=1, max=500)
    excerpt_fake = fake.text(max_nb_chars=50)
    data = {
        "id": BOOK_ID_POST,
        "title": title,
        "description": fake.sentence(),
        "pageCount": page_count,
        "excerpt": excerpt_fake,
        "publishDate": fake.iso8601()
    }

    response = books_api.post_book(data)
    books_api.attach_response(response)
    assert response.status_code == 200
    book = Book(**response.json())
    assert book.title == title
    assert book.pageCount == page_count
    assert book.excerpt == excerpt_fake
