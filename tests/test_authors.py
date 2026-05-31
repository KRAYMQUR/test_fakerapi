from models.authors import Author 
import allure
from tests.constants import AUTHOR_ID_DELETE, AUTHOR_ID_GET , AUTHOR_ID_POST , AUTHOR_ID_PUT




pytestmark = [allure.feature('Authors API')]


@allure.story('Get authors')
@allure.severity(allure.severity_level.NORMAL)
@allure.title('Testing get authors')
def test_get_author(author_api):
    response = author_api.get_authors()
    allure.attach(response.text, name="Response body",
                  attachment_type=allure.attachment_type.JSON)
    assert response.status_code == 200
    assert len(response.json()) > 0
    authors = Author(**response.json()[0])
    
@allure.story('Get author by id')
@allure.severity(allure.severity_level.NORMAL)   
@allure.title('Testing get_id authors')
def test_get_author_by_id(author_api):
    author_id = AUTHOR_ID_GET
    response = author_api.get_author_by_id(author_id)
    allure.attach(response.text, name="Response body",
                  attachment_type=allure.attachment_type.JSON)
    assert response.status_code == 200
    authors = Author(**response.json())
    assert authors.id == author_id 
    
    
@allure.story('Delete authors')
@allure.severity(allure.severity_level.NORMAL)  
@allure.title('Testing delete authors')
def test_delete_author(author_api):
    author_id = AUTHOR_ID_DELETE
    response = author_api.delete_author(author_id)
    assert response.status_code == 200
  
@allure.story('Post authors')  
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Testing post authors')   
def test_post_author(author_api):
    data = {
  "id": AUTHOR_ID_POST,
  "idBook": 4,
  "firstName": "Ivanov",
  "lastName": "test"
}
    response = author_api.post_author(data)
    allure.attach(response.text, name="Response body",
              attachment_type=allure.attachment_type.JSON)
    assert response.status_code == 200 
    authors = Author(**response.json())
    assert authors.id == AUTHOR_ID_POST
    assert authors.idBook == 4
    assert authors.firstName == 'Ivanov'
    
    
@allure.story('Put authors')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Testing put authors')
def test_put_author(author_api):
    author_id = AUTHOR_ID_PUT
    data = {
  "id": AUTHOR_ID_PUT,
  "idBook": 4,
  "firstName": "Ivanchenkop",
  "lastName": "Maria"
}
    response = author_api.put_author(author_id,data)
    allure.attach(response.text, name="Response body",
              attachment_type=allure.attachment_type.JSON)
    assert response.status_code == 200 
    authors = Author(**response.json())
    assert authors.id == AUTHOR_ID_PUT
    assert authors.firstName == 'Ivanchenkop'
    
    