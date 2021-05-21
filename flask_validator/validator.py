from .errors import ValidationError
from .fields import BaseField


class BaseMeta(type):
    def __new__(mcs, name, bases, attrs):
        """
        Get all the values that are of the type Field
        """

        cls = super().__new__(mcs, name, bases, attrs)
        cls.fields_list = []

        for name, value in attrs:
            if isinstance(value, BaseField):
                cls.fields_list[name] = value
                setattr(cls, name, value)


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

    def validate(self):
        res = []
        for name in self.fields_list:
            res.append(getattr(self, name).validate())
        if res:
            raise ValidationError(res)


class FormValidator(metaclass=BaseMeta):
    pass


class GetValidator(metaclass=BaseMeta):
    pass
