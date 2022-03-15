from hello import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'My name is Shard Vicens, and this is my first Python script, using CircleCI for contant integration.'
    assert response.status_code == 200