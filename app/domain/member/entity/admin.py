from typing import Optional

from app.domain.member.entity.member import Member


class Admin(Member):

    name = "최명진 법무사 사무소"
    fixed_personal_number = "286-30-00784"
    fixed_phone_number = "031-903-7360"

    def __init__(self,
                 password: str,
                 member_id : Optional[int] = None):
        super().__init__(
            name = Admin.name,
            password = password,
            personal_number= Admin.fixed_personal_number,
            phone_number = Admin.fixed_phone_number,
            member_id = member_id
        )
        self.role = 1

    @classmethod
    def to_admin(cls, password: str, member_id : Optional[int] = None) -> "Admin":



        return cls.to_member(
            name = cls.name,
            password = password,
            personal_number = cls.fixed_personal_number,
            phone_number = cls.fixed_phone_number,
            member_id = member_id
        )


    def __repr__(self) -> str:
        return f"Admin(name = '{self.name}', role = {self.role})"