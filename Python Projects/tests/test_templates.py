def test_index_template(client):
    response = client.get('/')
    assert b'<title>IP Information</title>' in response.data
    assert b'Show IP Address' in response.data
