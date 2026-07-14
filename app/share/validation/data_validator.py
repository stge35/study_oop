import re

class DataValidator:

    @staticmethod
    def validate_korean_name(name: str, context : str = "데이터"):
        if not re.match(r'^[가-힣]+$', name):
            raise ValueError(f"{context} 에러: 이름은 한글만 입력 가능합니다.")
        return name

    @staticmethod
    def validate_numeric_string(value: str, field_name: str, context: str = "데이터"):
        value = value.strip().replace("-", "")

        if not re.match(r'^[0-9]+$', value):
            raise ValueError(f"{context} 에러: {field_name}은(는) 숫자만 입력 가능합니다.")
        return value

    @staticmethod
    def validate_clean_phone(value: str, context: str = "데이터") -> str:
        value = value.strip().replace("-", "")

        if value == "":
            return "031-903-7360"

        if not re.match(r'^([0-9]*)$', value):
            raise ValueError(f"{context} 에러: 전화번호는 숫자만 입력가능합니다.")
        return value