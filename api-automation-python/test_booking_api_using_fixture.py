import requests
import pytest

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.fixture(scope="session")
def auth_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{BASE_URL}/auth", json=payload)
    return response.json().get("token") # return the token to be used in the test function

@pytest.fixture(scope="session")
def created_booking_id(auth_token):
    headers = {
        "Cookie": f"token={auth_token}"
    }
    payload = {
        "firstname": "Khalid",
        "lastname": "Al-Otaibi",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2026-01-10"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{BASE_URL}/booking", json=payload)
    return response.json().get("bookingid") # return the booking id to be used in the test function

@pytest.mark.run(order=1)
def test_get_booking(created_booking_id):
    response = requests.get(f"{BASE_URL}/booking/{created_booking_id}")
    assert response.status_code == 200
    assert response.json()["firstname"] == "Khalid"
    assert response.json()["lastname"] == "Al-Otaibi"

@pytest.mark.run(order=2)
def test_delete_booking(auth_token, created_booking_id):
    headers = {
        "Cookie": f"token={auth_token}"
    }
    response = requests.delete(f"{BASE_URL}/booking/{created_booking_id}", headers=headers)
    assert response.status_code == 201