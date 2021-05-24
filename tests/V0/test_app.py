import pytest
from flask.testing import FlaskClient


def test_app_works(test_client: FlaskClient):
    rv = test_client.get('/')
    assert b"Hello World" in rv.data


def test_hi():
    assert "1" in "1203"
