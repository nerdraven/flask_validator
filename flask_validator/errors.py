
class BaseError(BaseException):
    pass


class ValidationError(BaseError):

    def __init__(self, expression, message=None):
        self.message = message
        self.expression = expression
