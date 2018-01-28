from api_commons.common import ApiResponse
from api_commons.common import exception_handler
from api_commons.error import ErrorCode
from rest_framework.exceptions import MethodNotAllowed

UNEXPECTED_CODE = ErrorCode(2, 'Unexpected Error')
NOT_FOUND_CODE = ErrorCode(3, 'Not Found')
NOT_UNIQUE_CODE = ErrorCode(4, 'Not Unique')


class ControlledError(Exception):
    def __init__(self, error_code, *args):
        self.error_code = error_code
        super(ControlledError, self).__init__(*args)


class UnexpectedError(ControlledError):
    def __init__(self, error_text="Something went wrong"):
        super(UnexpectedError, self).__init__(UNEXPECTED_CODE, error_text)


class NotFoundError(ControlledError):
    def __init__(self, model, pk=None, filter=None):
        pk_text = "[pk={}]".format(pk) if pk else ""
        filter_text = "[filter={}]".format(filter) if filter else ""
        super(NotFoundError, self).__init__(NOT_FOUND_CODE,
                                            "Not Found: {}{}{}".format(model.__name__, pk_text, filter_text))


class NotUniqueError(ControlledError):
    def __init__(self, model, fields=None):
        fields_text = "[fields={}]".format(
            ",".join(["{}:{}".format(k, v) for k, v in fields.items()])) if filter else ""
        super(NotUniqueError, self).__init__(NOT_UNIQUE_CODE, "Not Unique: {}{}".format(model.__name__, fields_text))


def error_handler(exc, context):
    if isinstance(exc, MethodNotAllowed):
        return ApiResponse.bad_request('Request method error')
    if isinstance(exc, ControlledError):
        if isinstance(exc, NotFoundError):
            return ApiResponse.not_found(exc.error_code)
        if isinstance(exc, NotUniqueError):
            return ApiResponse.bad_request(exc.error_code)
    return exception_handler(exc, context)
