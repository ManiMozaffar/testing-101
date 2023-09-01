from unittest.mock import AsyncMock

import pytest
from fastapi.testclient import TestClient

from .app import Mailer, app, get_mailer


class MockMailer:
    def __init__(self, _from):
        ...

    async def send_mail(self, message: str, to: str) -> None:
        ...


# WAY 1:
def mock_mailer() -> AsyncMock:
    return AsyncMock(spec=Mailer)


# WAY 2:
def mock_mailer_with_impl() -> MockMailer:
    return MockMailer("admin@gmail.com")


app.dependency_overrides[get_mailer] = mock_mailer_with_impl
client = TestClient(app)


@pytest.mark.asyncio
async def test_forget_password():
    response = client.post("/forget-password/", json={"email": "user@example.com"})
    assert response.status_code == 200
    assert response.json() == {
        "message": "If the email exists, a reset link has been sent."
    }
