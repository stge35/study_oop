from enum import Enum

class ErrorCode(Enum):

    # (error code, error message)
    # common
    INVALID_INPUT_VALUE = ("C001", "잘못된 입력 값 입니다.")

    # Validation - Member
    INVALID_NAME_FORMAT = ("M001", "한글만 입력해 주세요.")
    INVALID_NUMBER_FORMAT = ("M002", "숫자만 입력해 주세요.")

    MEMBER_NOT_FOUND = ("M100", "회원이 존재 하지 않습니다.")
    DUPLICATE_MEMBER = ("M101", "이미 존재 하는 회원 입니다.")

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message