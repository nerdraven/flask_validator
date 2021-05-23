import pytest
from flask.testing import FlaskClient
from app.app import app


@pytest.fixture()
def test_client():
    with app.test_client() as client:
        yield client


def test_app_works(test_client: FlaskClient):
    rv = test_client.get('/')
    assert b"Hello World" in rv.data


def test_hi():
    assert "1" in "1203"
