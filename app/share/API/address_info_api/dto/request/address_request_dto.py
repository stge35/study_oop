from dataclasses import dataclass

@dataclass
class RequestAddressDto:
    keyword: str

    def __post_init__(self):

        if not self.keyword or len(self.keyword.strip()) < 2:
            from app.share.validation.business_exception import ValidationException
            from app.share.validation.error_code import ErrorCode
            raise ValidationException(ErrorCode.INVALID_INPUT_VALUE, "검색어는 최소 2글자")

        self.keyword = self.keyword.strip()
