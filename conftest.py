import pytest 
from api.books_api import BooksApi
from api.authors_api import AuthorsApi




@pytest.fixture(scope='session')
def books_api():
    return BooksApi()


@pytest.fixture(scope='session')
def authors_api():
    return AuthorsApi()

