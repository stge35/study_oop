import re

from app.share.validation.business_exception import ValidationException
from app.share.validation.error_code import ErrorCode


class DataValidator:

    @staticmethod
    def validate_korean_name(name: str) -> str:
        if not re.match(r'^[가-힣]+$', name):
            raise ValidationException(ErrorCode.INVALID_NAME_FORMAT)
        return name

    @staticmethod
    def validate_numeric_string(value: str, field_name: str, context: str = "데이터"):
        value = value.strip().replace("-", "")

        if not re.match(r'^[0-9]+$', value):
            raise ValidationException(ErrorCode.INVALID_NUMBER_FORMAT)
        return value

    @staticmethod
    def validate_clean_phone(value: str) -> str:
        value = value.strip().replace("-", "")
        if value == "":
            return "031-903-7360"

        if not re.match(r'^([0-9]*)$', value):
            raise ValidationException(ErrorCode.INVALID_NUMBER_FORMAT)
        return value

    @staticmethod
    def validate_clean_address(value: str) -> str:
        value = value.strip()
        if value == "":
            return "경기도 고양시 일산동구 장백로 194, 601호"

        return value

