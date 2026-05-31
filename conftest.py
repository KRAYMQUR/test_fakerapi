import pytest 
from api.books_api import BooksApi
from api.authors_api import AuthorsApi
from faker import Faker



@pytest.fixture(scope='session')
def books_api():
    return BooksApi()


@pytest.fixture(scope='session')
def authors_api():
    return AuthorsApi()


@pytest.fixture()
def created_author(authors_api):
    fake = Faker()
    data = {
        "id": fake.random_int(min=100,max=999),
        "idBook": fake.random_int(min=1,max=10),
        'firstName': fake.first_name(),
        'lastName': fake.last_name()
    }
    response = authors_api.post_author(data)
    author_id = response.json()['id']
    yield author_id
    authors_api.delete_author(author_id)
    
    
@pytest.fixture()
def created_book(books_api):
    fake = Faker()
    data = { 
            "id": fake.random_int(min=100,max=999),
  "title": fake.word(),
  "description": fake.sentence(),
  "pageCount": fake.random_int(min=1,max=500),
  "excerpt": fake.text(max_nb_chars=50),
  "publishDate": fake.iso8601()
}
    response = books_api.post_book(data)
    book_id = response.json()['id']
    yield book_id
    books_api.delete_book(book_id)