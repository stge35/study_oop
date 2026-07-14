from typing import Optional

class Member:

    def __init__(self,
                 name : str,
                 password : str,
                 personal_number : str,
                 phone_number : str,
                 member_id: Optional[int] = None):
        self.name = name
        self.password = password
        self.personal_number = personal_number
        self.phone_number = phone_number
        self.member_id = member_id
        self.role = 2

    def __repr__(self) -> str:
        return f"Member(name = '{self.name}', member_id = '{self.member_id}"

    @classmethod
    def to_member(cls,
            name : str,
            password : str,
            personal_number : str,
            phone_number : str,
            member_id: int = None
            ) -> "Member":

        # 하이픈이 있으면 제거를 하고 저장
        cleaned_personal_number = personal_number.replace("-","")

        return cls(
            name = name,
            password= password,
            personal_number=cleaned_personal_number,
            phone_number=phone_number,
            member_id = member_id,
        )