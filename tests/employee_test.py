from fastapi.testclient import TestClient
from index import app

"""
What to test?:
- emplyees/add:
    [ ] send get request to employees/add
    [ ] send post request with incomplete data
"""

PREFIX_URL = 'api/v1/employees'
client = TestClient(app)

def test_get_add() -> None:
    """
    Simple test send get request to employees/add
    this should return 405 Method Not Allowed
    """
    response = client.get(PREFIX_URL + '/add')
    assert response.status_code == 405
    assert response.json() == { "detail": "Method Not Allowed" }

def test_post_incomplete_data_to_add() -> None:
    """
    Send incomplete post data to employees/add
    this should return 422 status code
    with some explain in return body
    """
    body = { 'email': 'usertest@mail.com' }
    response = client.post(PREFIX_URL + '/add', json=body)
    assert response.status_code == 422
    response_body = response.json()['detail']
    assert response_body[0]['loc'] == ['body', 'username']
    assert response_body[1]['loc'] == ['body', 'password']
