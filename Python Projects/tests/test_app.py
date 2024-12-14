import pytest
from app import app, get_ip_info

# Unit Test: Test the get_ip_info function
def test_get_ip_info(mocker):
    # Mock API response
    mock_response = {
        'ip': '192.168.1.1',
        'city': 'Sample City',
        'region': 'Sample Region',
        'country_name': 'Sample Country',
        'org': 'Sample ISP',
        'asn': 'AS12345',
        'latitude': 12.34,
        'longitude': 56.78,
    }
    mocker.patch('requests.get', return_value=mocker.Mock(json=lambda: mock_response))

    result = get_ip_info()
    assert result['ip'] == '192.168.1.1'
    assert result['city'] == 'Sample City'

# Integration Test: Test the home route
def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'IP Address Information' in response.data

# Integration Test: Check if IP info is rendered
def test_ip_render(client, mocker):
    mock_response = {
        'ip': '192.168.1.1',
        'city': 'Sample City',
        'region': 'Sample Region',
        'country_name': 'Sample Country',
        'org': 'Sample ISP',
        'asn': 'AS12345',
        'latitude': 12.34,
        'longitude': 56.78,
    }
    mocker.patch('requests.get', return_value=mocker.Mock(json=lambda: mock_response))

    response = client.get('/')
    assert b'192.168.1.1' in response.data
    assert b'Sample City' in response.data
