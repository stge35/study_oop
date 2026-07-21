from typing import Optional

from app.share.validation.data_validator import DataValidator


class UpdateMemberDto:

    def __init__(self,
                 member_id: int,
                 phone_number: Optional[str] = None,
                 address: Optional[str] = None
                 ):
        self.member_id = member_id
        if phone_number is not None:
            self.phone_number = DataValidator.validate_clean_phone(phone_number)
        else:
            self.phone_number = None

        if address is not None:
            self.address = DataValidator.validate_clean_address(address, context = "DTO")
        else:
            self.address = None



    @classmethod
    def from_member(cls, member) -> "UpdateMemberDto":

        return cls(
            member_id = member.member_id,
            phone_number = member.phone_number,
            address = member.address
        )

    pass