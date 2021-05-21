
from abc import ABC, abstractmethod


class BaseField(ABC):

    def __init__(self, required=False):
        self.required = required

    @abstractmethod
    def validate():
        pass


class StringField(BaseField):

    def __init__(self, maxlength, **kwargs):
        super().__init__(**kwargs)
        self.maxlength = maxlength

    def validate(self):
        pass
