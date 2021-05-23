from typing import Dict

from flask_validator.errors import ValidationError
from flask_validator.fields import BaseField, StringField


class BaseMeta(type):
    def __new__(mcs, name, bases, attrs: dict):
        """
        Get all the values that are of the type Field
        """

        cls = super().__new__(mcs, name, bases, attrs)
        fields_list: Dict[str] = {}
        for name, value in attrs.items():
            print(name)
            if isinstance(value, (BaseField,)):
                fields_list[name] = value

        class Meta:
            fields_list: Dict = {}

            def __init__(self, field_list):
                self.name = cls.__name__
                self.fields_list = field_list

            def get_item(self, field: str):
                return self.fields_list.get(field, None)

        meta = Meta(fields_list)
        cls._Meta = meta
        return cls


class APIValidator(metaclass=BaseMeta):
    """

    Example:
    class RequestValidator(APIValidator):
        name = StringField(required=True)

    validator = RequestValidator()

    @route('/')
    @validator.validate()
    def index():
        return "Hello"
    """
    
    def __init__(self):
        self.data = {}

    def validate(self):
        res = []
        for name, value in list(self.fields_list.keys()):
            res.append(getattr(self, name).validate())
        if res:
            raise ValidationError(res)

    def __getattr__(self, attr):
        if attr.startswith("b"):
            name = 10
            return f"[fallback resolved] {name}"
        raise AttributeError(
            f"{self.__class__.__name__} has no attribute {attr}"
        )

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in self._Meta.fields_list.keys():
            self.data[key] = value


class FormValidator(metaclass=BaseMeta):
    pass


class GetValidator(metaclass=BaseMeta):
    pass


if __name__ == "__main__":
    class A(APIValidator):
        a = StringField(max_length=10)

    a = A()
