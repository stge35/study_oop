from abc import ABCMeta, abstractmethod

from app.domain.member.dto.request.create_member_dto import CreateMemberDto
from app.domain.member.entity.member import Member


class MemberInterface:

    @abstractmethod
    def save_member(self, dto : CreateMemberDto) -> Member:
        pass