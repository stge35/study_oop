import re
from typing import Optional
from app.domain.member.entity.member import Member


class CreateMemberDto:

    def __init__(self,
                name : str,
                password : str,
                personal_number: str,
                phone_number : str,
                member_id : Optional[int] = None):
        if not re.match(r'^[가-힣]+$', name):
            raise ValueError("DTO 에러: 이름은 한글만 입력 가능합니다.")

        if not re.match(r'^[0-9]+$', personal_number):
            raise ValueError("DTO 에러: 주민번호는 숫자만 입력 가능합니다.")

        phone_number = phone_number.strip()
        phone_number = phone_number.replace("-","")

        if not re.match(r'^([0-9]*)$', phone_number):
            raise ValueError("DTO 에러: 전화번호는 숫자만 입력가능합니다.")

        phone_number = phone_number.strip()
        phone_number = phone_number.replace("-", "")

        if phone_number == "":
            phone_number = "031-903-7360"


        self.name = name
        self.password = password
        self.personal_number = personal_number
        self.phone_number = phone_number
        self.member_id = member_id



    def to_member(self) -> Member:

        return Member.to_member(
            name = self.name,
            password = self.password,
            personal_number = self.personal_number,
            phone_number = self.phone_number,
            member_id = self.member_id
        )

