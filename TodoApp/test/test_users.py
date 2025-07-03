from .utils import *
from ..routers.users import get_db, get_current_user
from fastapi import status


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    assert test_user.username == 'testuser'
    assert test_user.email == 'testuser@gmail.com'
    assert test_user.firstname == 'test'
    assert test_user.lastname == 'user'
    assert test_user.role == 'admin'
    assert test_user.phone_number == '0111 111 11 11'


def test_change_password_success(test_user):
    response = client.put('/user/password', json={'password': 'testuser_password', 'new_password': 'testuser_newpassword'})
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_invalid_current_password_success(test_user):
    response = client.put('/user/password', json={'password': 'wrong_password', 'new_password': 'testuser_newpassword'})
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {'detail': 'Error on password change!'}


def test_change_phone_number_success(test_user):
    response = client.put('/user/phone_number', json={'new_phone_number': '0222 222 22 22'})
    assert response.status_code == status.HTTP_204_NO_CONTENT