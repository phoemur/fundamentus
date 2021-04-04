from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()


def test_get_ticker():
    response = client.get("/ticker/abev3")
    assert response.status_code == 200
    assert response.json()


def test_get_tickers():
    response = client.get("/tickers")
    assert response.status_code == 200
    assert response.json()


def test_get_ticker_not_found():
    response = client.get("/ticker/abev")
    assert response.status_code == 404
    assert response.json()
