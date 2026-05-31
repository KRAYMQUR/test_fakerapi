from models.authors import Author
import allure
from tests.constants import AUTHOR_ID_GET, AUTHOR_ID_POST, AUTHOR_ID_PUT
import pytest
from faker import Faker


pytestmark = [allure.feature('Authors API')]
fake = Faker()


@pytest.mark.smoke
@pytest.mark.regression
@allure.story('Get authors')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Testing get authors')
def test_get_author(authors_api):
    response = authors_api.get_authors()
    authors_api.attach_response(response)
    assert response.status_code == 200
    assert len(response.json()) > 0
    Author(**response.json()[0])
    assert response.elapsed.total_seconds() < 2


@pytest.mark.regression
@allure.story('Get author by id')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Testing get_id authors')
@pytest.mark.parametrize('author_id', [AUTHOR_ID_GET, 56])
def test_get_author_by_id(authors_api, author_id):
    response = authors_api.get_author_by_id(author_id)
    authors_api.attach_response(response)
    assert response.status_code == 200
    authors = Author(**response.json())
    assert authors.id == author_id


@pytest.mark.regression
@allure.story('Delete authors')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Testing delete authors')
def test_delete_author(authors_api, created_author):
    response = authors_api.delete_author(created_author)
    assert response.status_code == 200


@pytest.mark.regression
@allure.story('Post authors')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Testing post authors')
def test_post_author(authors_api):
    firstName = fake.first_name()
    lastName = fake.last_name()
    id_book = fake.random_int(min=1, max=10)
    data = {
        "id": AUTHOR_ID_POST,
        "idBook": id_book,
        "firstName": firstName,
        "lastName": lastName
    }
    response = authors_api.post_author(data)
    authors_api.attach_response(response)
    assert response.status_code == 200
    authors = Author(**response.json())
    assert authors.id == AUTHOR_ID_POST
    assert authors.idBook == id_book
    assert authors.firstName == firstName
    assert authors.lastName == lastName


@pytest.mark.regression
@allure.story('Put authors')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Testing put authors')
def test_put_author(authors_api):
    firstName = fake.first_name()
    lastName = fake.last_name()
    id_book = fake.random_int(min=1, max=10)
    author_id = AUTHOR_ID_PUT
    data = {
        "id": AUTHOR_ID_PUT,
        "idBook": id_book,
        "firstName": firstName,
        "lastName": lastName
    }
    response = authors_api.put_author(author_id, data)
    authors_api.attach_response(response)
    assert response.status_code == 200
    authors = Author(**response.json())
    assert authors.id == AUTHOR_ID_PUT
    assert authors.firstName == firstName
    assert authors.lastName == lastName
