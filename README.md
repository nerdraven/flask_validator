# Flask request validator

This is a middleware that could be added to a flask route to validate the type of request sent
It is when created, it will be used to decorate a flask route immediately after the flask route

```python

from flask import Flask
from flask_validator import JSONValidator, Fields

app = Flask(__name__)

class Validator(JSONValidator):
    name = Fields.StringFields()

@app.route("/")
def index():
    name = request.json.get("name")
    return f"Hello, {name}", 200

```