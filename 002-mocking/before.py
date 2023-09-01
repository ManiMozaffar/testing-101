import pytest
from fastapi.testclient import TestClient

from .app import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_forget_password():
    response = client.post("/forget-password/", json={"email": "user@example.com"})
    assert response.status_code == 200
    assert response.json() == {
        "message": "If the email exists, a reset link has been sent."
    }
