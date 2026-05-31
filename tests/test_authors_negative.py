import allure
import pytest
from tests.constants import AUTHOR_ID_PUT


pytestmark = [allure.feature('Authors API'), pytest.mark.regression]


@allure.story('Negative cases')
@allure.severity(allure.severity_level.MINOR)
@allure.title('Testing negative author get')
@pytest.mark.parametrize('author_id, status_code', [
    (-1, 404),
    ('abc', 400)
])
def test_negative_authors_get(authors_api, author_id, status_code):
    response = authors_api.get_author_by_id(author_id)
    authors_api.attach_response(response)
    assert response.status_code == status_code


@allure.story('Negative cases - post')
@allure.severity(allure.severity_level.MINOR)
@allure.title('Testing negative post author')
def test_negative_post_author(authors_api):

    data = {
        "id": -1,
        "idBook": 555,
        "firstName": [],
        "lastName": []
    }
    response = authors_api.post_author(data)
    authors_api.attach_response(response)
    assert response.status_code == 400


@allure.story('Negative cases - put')
@allure.severity(allure.severity_level.MINOR)
@allure.title('Testing negative put author')
def test_negative_put_author(authors_api):
    author_id = AUTHOR_ID_PUT
    data = {
        "id": AUTHOR_ID_PUT,
        "idBook": 4,
        "firstName": [],
        "lastName": []
    }
    response = authors_api.put_author(author_id, data)
    authors_api.attach_response(response)
    assert response.status_code == 400
