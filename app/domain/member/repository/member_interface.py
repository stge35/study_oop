from abc import ABCMeta, abstractmethod
from app.domain.member.entity.member import Member


class MemberInterface:

    @abstractmethod
    def save_member(self, member : Member) -> Member:
        pass

    @abstractmethod
    def find_all_member(self) -> list[Member]:
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> list[Member]:
        pass

    @abstractmethod
    def find_by_id(self, member_id: str) -> Member | None:
        pass

    @abstractmethod
    def exists_by_name(self, name: str) -> bool:
        pass