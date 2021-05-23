# Flask request validator

This is a middleware that could be added to a flask route to validate the type of request sent
It is when created, it will be used to decorate a flask route immediately after the flask route

```python

from flask import Flask, request
from flask_validator import APIValidator, fields

app = Flask(__name__)

class Validator(APIValidator):
    name = fields.StringFields()

@app.route("/")
def index():
    name = request.json.get("field")
    return f"Hello, {name}", 200

```