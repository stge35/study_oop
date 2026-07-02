from app.domain.member.dto.request.create_member_dto import CreateMemberDto
from app.domain.member.dto.response.response_member_dto import ResponseMember
from app.domain.member.service.member_service import MemberService


class MemberController:


    def __init__(self, service: MemberService):
        self.member_service = service

    def register_member(self, dto: CreateMemberDto) -> ResponseMember:

        try:
            response: ResponseMember = self.member_service.save(dto)
            return response

        except ValueError as e:
            raise ValueError(f"fail : {e}")

