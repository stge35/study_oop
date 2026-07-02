from typing import Optional
from app.domain.member.entity.member import Member


class CreateMemberDto:

    def __init__(self,
                name : str,
                password : str,
                personal_number : str,
                phone_number : str,
                member_id : Optional[int] = None):

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

