import pytest 
from api.books_api import BooksApi
from api.authors_api import AuthorsApi



@pytest.fixture 
def books_api():
    return BooksApi()


@pytest.fixture
def author_api():
    return AuthorsApi()

