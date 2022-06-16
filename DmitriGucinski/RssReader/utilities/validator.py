from exceptions.limit_error_exception import LimitIsNotIntegerError


class Validator:

    @classmethod
    def validate_limit(cls, limit):
        if not isinstance(limit, int):
            raise LimitIsNotIntegerError


