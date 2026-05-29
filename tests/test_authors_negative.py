import allure
import pytest



pytestmark = [allure.feature('Authors API')]


@allure.story('Negative cases')
@allure.severity(allure.severity_level.MINOR)
@allure.title('Testing negative author get')
@pytest.mark.parametrize('author_id, status_code' , [
    (-1,404),
    ('abc',400)
])
def test_negative_authors_get(author_api, author_id, status_code):
    response = author_api.get_author_by_id(author_id)
    assert response.status_code == status_code

    
@allure.story('Negative cases - post')
@allure.severity(allure.severity_level.MINOR)
@allure.title('Testing negative post author')
def test_negative_post_author(author_api):
    data = {
  "id": -1,
  "idBook": 555,
  "firstName": [],
  "lastName": []
}
    response = author_api.post_author(data)
    assert response.status_code == 400
    
    
@allure.story('Negative cases - put')
@allure.severity(allure.severity_level.MINOR)
@allure.title('Testing negative put author')
def test_negative_put_author(author_api):
    author_id = 9999
    data = {
  "id": 99999999,
  "idBook": 9999999999,
  "firstName": [],
  "lastName": []
}
    response = author_api.put_author(author_id,data)
    assert response.status_code == 400