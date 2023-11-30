from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_translator_hi():
    response = client.post("/translate/",
        json={"text": "привет"}
    )
    text = response.json() 

    assert response.status_code == 200
    assert text == 'hi'

def test_read_translator_new():
    response = client.post("/translate/",
        json={"text": "что нового"}
    )
    text = response.json() 

    assert response.status_code == 200
    assert text == 'what\'s new'
