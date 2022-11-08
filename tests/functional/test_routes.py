from iebank_api import app
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/wrong_path')
    assert response.status_code == 404
    assert response.data == b'{"message": "Not Found"}'

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'Test Account', 'currency': '€'})
    assert response.status_code == 200
    assert response.json['name'] == 'Test Account'
    assert response.json['currency'] == '€'

def test_delete_account(testing_client):

    response = testing_client.delete('/accounts/1')
    assert response.status_code == 200
    assert response.data == b'{"id": 1, "name": "Test Account", "message": "Account deleted"}'

def test_update_account(testing_client):
    response = testing_client.put('/accounts/1', json={'name': 'Test Account', 'currency': '€'})
    assert response.status_code == 200
    assert response.json['name'] == 'Test Account'
    assert response.json['currency'] == '€'

def test_get_account(testing_client):
    response = testing_client.get('/accounts/1')
    assert response.status_code == 200


