import json
from fastapi.testclient import TestClient

from ..main import app


def test_read_items():
    with TestClient(app) as client:
        response = client.get("/api/v1/employees")
        assert response.status_code == 200
        assert response.json().get('total') == 600

        response = client.get("/api/v1/employees?name=jo")
        assert response.status_code == 200
        assert response.json().get('total') == 19

        response = client.get("/api/v1/employees?age__lt=50")
        assert response.status_code == 200
        assert response.json().get('total') == 350

        response = client.get("/api/v1/employees?gender=other")
        assert response.status_code == 200
        assert response.json().get('total') == 194