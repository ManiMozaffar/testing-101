import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from learn_pytest.main import Base, app, get_db


@pytest.fixture(scope="session")
def test_db():
    MOCK_DB_URL = "sqlite:///./test_test.db"
    engine = create_engine(MOCK_DB_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    yield SessionLocal()
    Base.metadata.drop_all(bind=engine)
    if os.path.exists("test_test.db"):
        os.remove("test_test.db")


@pytest.fixture(scope="session")
def client(test_db):
    app.dependency_overrides[get_db] = lambda: test_db
    with TestClient(app) as client:
        yield client


def test_animal_behavior(client: TestClient):
    response = client.get("/animals/")
    before_create = len(response.json())

    response = client.post(
        "/add_animal/", json={"name": "Tiger", "species": "..", "age": 4}
    )
    response = client.get("/animals/")
    print(response.text)
    assert response.status_code == 200
    assert len(response.json()) == before_create + 1
