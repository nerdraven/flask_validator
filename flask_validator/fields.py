
from abc import ABC, abstractmethod


class BaseField(ABC):

    def __init__(self, required=False):
        self.required = required

    @abstractmethod
    def validate(self):
        pass


class FieldMeta(type):

    def __new__(mcs, name, bases, attrs: dict):
        print(mcs)
        print(name)
        cls = super().__new__()
        return cls


class StringField(BaseField):

    def __init__(self, /, max_length, **kwargs):
        super().__init__(**kwargs)
        self.max_length = max_length

    def validate(self):
        pass
