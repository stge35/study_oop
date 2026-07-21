from app.share.validation.error_code import ErrorCode


class BusinessException(Exception):

    def __init__(self, error_code: ErrorCode, custom_message: str = None):
        self.error_code = error_code
        self.message = custom_message if custom_message else error_code.message
        super().__init__(self.message)


class ValidationException(BusinessException):

    def __init__(self, error_code: ErrorCode = ErrorCode.INVALID_INPUT_VALUE, custom_message:str = None):
        super().__init__(error_code, custom_message)

class NotFoundException(BusinessException):

    def __init__(self, error_code: ErrorCode = ErrorCode.MEMBER_NOT_FOUND, custom_message: str = None):
        super().__init__(error_code,custom_message)



