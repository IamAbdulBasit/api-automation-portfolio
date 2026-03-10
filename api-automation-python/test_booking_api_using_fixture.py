import requests
import pytest

BASE_URL = "https://restful-booker.herokuapp.com"

@pytest.mark.order(0)
def test_health_check():
    response = requests.get(f"{BASE_URL}/ping")
    assert response.status_code in [201, 200], "API is not healthy / not responding as expected"

@pytest.mark.order(1)
@pytest.fixture(scope="session")
def auth_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{BASE_URL}/auth", json=payload)
    return response.json().get("token") # return the token to be used in the test function

@pytest.mark.order(2)
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

@pytest.mark.run(order=3)
def test_get_single_booking(created_booking_id):
    response = requests.get(f"{BASE_URL}/booking/{created_booking_id}")
    assert response.status_code == 200
    assert response.json()["firstname"] == "Khalid"
    assert response.json()["lastname"] == "Al-Otaibi"

@pytest.mark.run(order=4)
def test_get_all_bookings(created_booking_id, auth_token):
    response = requests.get(f"{BASE_URL}/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list) # Ensure the response is a list of bookings
    booking_ids = [booking["bookingid"] for booking in response.json()] # Extract booking IDs from the response
    assert created_booking_id in booking_ids # Ensure the created booking is in the list of all bookings

@pytest.mark.run(order=5)
def test_update_booking(auth_token, created_booking_id):
    headers = {
        "Cookie": f"token={auth_token}"
    }
    payload = {
        "firstname": "Khalid Updated",
        "lastname": "Al-Otaibi Updated",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2025-12-31"
        },
        "additionalneeds": "Lunch"
    }
    response = requests.put(f"{BASE_URL}/booking/{created_booking_id}", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Khalid Updated"
    assert response.json()["lastname"] == "Al-Otaibi Updated"
    assert response.json()["totalprice"] == 200
    assert response.json()["depositpaid"] == False
    assert response.json()["additionalneeds"] == "Lunch"

@pytest.mark.run(order=6)
def test_partial_update_booking(auth_token, created_booking_id):
    headers = {
        "Cookie": f"token={auth_token}"
    }
    payload = {
        "firstname": "Khalid Partially Updated",
        "lastname": "Al-Otaibi Partially Updated",
        "totalprice": 250,
        "additionalneeds": "Dinner"
    }
    response = requests.patch(f"{BASE_URL}/booking/{created_booking_id}", json=payload, headers=headers)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Khalid Partially Updated"
    assert response.json()["lastname"] == "Al-Otaibi Partially Updated"
    assert response.json()["totalprice"] == 250
    assert response.json()["additionalneeds"] == "Dinner"

@pytest.mark.run(order=7)
def test_delete_booking(auth_token, created_booking_id):
    headers = {
        "Cookie": f"token={auth_token}"
    }
    response = requests.delete(f"{BASE_URL}/booking/{created_booking_id}", headers=headers)
    assert response.status_code == 201