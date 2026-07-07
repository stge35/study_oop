from abc import ABCMeta, abstractmethod
from typing import Optional

from app.domain.member.dto.request.create_member_dto import CreateMemberDto
from app.domain.member.entity.member import Member


class MemberInterface:

    @abstractmethod
    def save_member(self, member : Member) -> Member:
        pass

    @abstractmethod
    def exists_by_name(self, name: str) -> bool:
        pass