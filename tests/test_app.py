import pytest
from flask import Flask
from app import app, get_ip_info

# Test if the Flask app is set up correctly
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test the IP information retrieval function
def test_get_ip_info_success(monkeypatch):
    class MockResponse:
        @staticmethod
        def json():
            return {
                'ip': '192.168.1.1',
                'city': 'City',
                'region': 'Region',
                'country_name': 'Country',
                'ipv6': 'Not available',
                'org': 'ISP',
                'asn': 'ASN',
                'latitude': 10.0,
                'longitude': 20.0
            }

    # Mock requests.get to return the mock response
    monkeypatch.setattr('requests.get', lambda url: MockResponse())
    
    ip_info = get_ip_info()
    assert ip_info['ip'] == '192.168.1.1'
    assert ip_info['city'] == 'City'
    assert ip_info['region'] == 'Region'

# Test the home route
def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'IP Address Information' in response.data

