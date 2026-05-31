from models.authors import Author 
import allure
from tests.constants import AUTHOR_ID_GET , AUTHOR_ID_POST , AUTHOR_ID_PUT
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
    authors = Author(**response.json()[0])
    assert authors.id is not None
    assert authors.firstName is not None
    assert authors.lastName is not None
    assert response.elapsed.total_seconds() < 2

    
    
@pytest.mark.regression
@allure.story('Get author by id')
@allure.severity(allure.severity_level.NORMAL)   
@allure.title('Testing get_id authors')
def test_get_author_by_id(authors_api):
    author_id = AUTHOR_ID_GET
    response = authors_api.get_author_by_id(author_id)
    authors_api.attach_response(response)
    assert response.status_code == 200
    authors = Author(**response.json())
    assert authors.id == author_id 
    
@pytest.mark.regression  
@allure.story('Delete authors')
@allure.severity(allure.severity_level.NORMAL)  
@allure.title('Testing delete authors')
def test_delete_author(authors_api,created_author):
    response = authors_api.delete_author(created_author)
    assert response.status_code == 200    
  
  
@pytest.mark.regression
@allure.story('Post authors')  
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Testing post authors')   
def test_post_author(authors_api):
    firstName = fake.first_name()
    lastName = fake.last_name()
    data = {
  "id": AUTHOR_ID_POST,
  "idBook": 4,
  "firstName": firstName,
  "lastName": lastName
}
    response = authors_api.post_author(data)
    authors_api.attach_response(response)
    assert response.status_code == 200 
    authors = Author(**response.json())
    assert authors.id == AUTHOR_ID_POST
    assert authors.idBook == 4
    assert authors.firstName == firstName
    assert authors.lastName == lastName
    


@pytest.mark.regression
@allure.story('Put authors')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Testing put authors')
def test_put_author(authors_api):
    firstName = fake.first_name()
    lastName = fake.last_name()
    author_id = AUTHOR_ID_PUT
    data = {
  "id": AUTHOR_ID_PUT,
  "idBook": 4,
  "firstName": firstName,
  "lastName": lastName
}
    response = authors_api.put_author(author_id,data)
    authors_api.attach_response(response)
    assert response.status_code == 200 
    authors = Author(**response.json())
    assert authors.id == AUTHOR_ID_PUT
    assert authors.firstName == firstName
    assert authors.lastName == lastName
    
    