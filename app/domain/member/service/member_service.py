from app.domain.member.dto.request.create_member_dto import CreateMemberDto
from app.domain.member.dto.response.response_member_dto import ResponseMember
from app.domain.member.repository.member_interface import MemberInterface


class MemberService:

    def __init__(self, repository: MemberInterface):

        self.repository =repository

    def save(self, dto: CreateMemberDto)-> ResponseMember:

        member = dto.to_member()

        saved_member = self.repository.save_member(member)

        return ResponseMember.from_member(saved_member)
        