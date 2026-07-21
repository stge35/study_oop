import re
from typing import Optional
from app.domain.member.entity.member import Member
from app.share.utils.data_encryptor import DataEncryptor
from app.share.utils.password_encoder import PasswordEncoder
from app.share.validation.data_validator import DataValidator


class CreateMemberDto:

    def __init__(self,
                name : str,
                password : str,
                personal_number: str,
                phone_number : str,
                address : str = None,
                member_id : Optional[int] = None):

        self.name = DataValidator.validate_korean_name(name)
        self.personal_number = DataValidator.validate_numeric_string(personal_number, field_name = "주민번호", context = "DTO")
        self.phone_number = DataValidator.validate_clean_phone(phone_number)
        self.password = password
        self.address = DataValidator.validate_clean_address(address, context = "DTO")
        self.member_id = member_id



    def to_member(self) -> Member:

        encrypted_password = PasswordEncoder.hash_password(self.password)
        encrypted_p_num = DataEncryptor.encrypt(self.personal_number)

        return Member.to_member(
            name = self.name,
            password = encrypted_password,
            personal_number = encrypted_p_num,
            phone_number = self.phone_number,
            address = self.address,
            member_id = self.member_id
        )

