from dataclasses import dataclass

from app.domain.member.entity.member import Member


@dataclass
class ResponseMemberDto:

    name: str
    personal_number: str
    phone_number: str

    @classmethod
    def from_member(cls, entity: Member) -> "ResponseMemberDto":

        return cls(
            name = entity.name,
            personal_number = entity.personal_number,
            phone_number = entity.phone_number
        )