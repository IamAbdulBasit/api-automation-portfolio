import requests

BASE_URL = "https://restful-booker.herokuapp.com"


def create_auth_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{BASE_URL}/auth", json=payload)
    return response # return the response object to be used in the test function

def test_create_and_get_token():
    response = create_auth_token() # Call the function to get the response object
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert response.elapsed.total_seconds() < 3  # Ensure the response time is less than 3 seconds

    response_jsonData = response.json() # Parse the response body as JSON
    assert "token" in response_jsonData
    assert response_jsonData.get("token") is not None
    assert isinstance(response_jsonData.get("token"), str)
    assert len(response_jsonData.get("token")) > 0

def test_create_booking_with_token():
    payload = {
        "firstname": "Ahmed",
        "lastname": "Al-Qahtani",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-01-01",
            "checkout": "2026-01-10"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{BASE_URL}/booking", json=payload)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert response.json()["booking"]["firstname"] == payload["firstname"]
    #OR
    assert response.json()["booking"]["firstname"] == payload.get("firstname")
    #OR
    assert response.json()["booking"]["firstname"] == "Ahmed"
    assert response.json()["booking"]["lastname"] == payload["lastname"]