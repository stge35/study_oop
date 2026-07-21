from app.domain.member.dto.request.create_member_dto import CreateMemberDto
from app.domain.member.dto.request.update_member_dto import UpdateMemberDto
from app.domain.member.dto.response.response_member_dto import ResponseMemberDto
from app.domain.member.entity.member import Member
from app.domain.member.repository.member_interface import MemberInterface


class MemberService:

    def __init__(self, repository: MemberInterface):

        self.repository =repository

    def save(self, dto: CreateMemberDto)-> ResponseMemberDto:

        member = dto.to_member()

        if self.repository.exists_by_name(member.name):
            raise ValueError("이미 가입된 멤버입니다.")

        saved_member = self.repository.save_member(member)

        return ResponseMemberDto.from_member(saved_member)

    def login(self, name: str) -> Member | None:

        members = self.repository.find_by_name(name)

        if not members:
            return None

        return members[0]

    def patch(self, dto:UpdateMemberDto) -> Member:
        existing_member = self.repository.find_by_id(dto.member_id)
        if not existing_member:
            raise ValueError(f"수정 실패: ID {dto.member_id} 회원을 찾을 수 없습니다.")

        patch_member = dto.phone_number if dto.phone_number is not None else existing_member.phone_number
        address = dto.address if dto.address is not None else existing_member.address

        update_member = Member(
            name=existing_member.name,
            password=existing_member.password,
            personal_number=existing_member.personal_number,
            phone_number=patch_member,
            address = address,
            member_id = existing_member.member_id
        )

        self.repository.update_member(update_member)

        return update_member

    def has_any_member(self) -> bool:

        all_members = self.repository.find_all_member()

        return len(all_members) > 0