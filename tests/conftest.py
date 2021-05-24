import pytest
from app.app import app


@pytest.fixture()
def test_client():
    with app.test_client() as client:
        yield client
