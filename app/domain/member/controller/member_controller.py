from app.domain.member.dto.request.create_member_dto import CreateMemberDto
from app.domain.member.dto.response.response_member_dto import ResponseMemberDto
from app.domain.member.service.member_service import MemberService


class MemberController:


    def __init__(self, service: MemberService):
        self.member_service = service

    def register_member(self, dto: CreateMemberDto) -> ResponseMemberDto:

        try:
            response: ResponseMemberDto = self.member_service.save(dto)
            return response

        except ValueError as e:
            raise ValueError(f"fail : {e}")

    def login_member(self, name: str, password: str) -> bool:

        member = self.member_service.login(name)

        if not member:
            raise ValueError("사용자가 존재하지 않습니다.")

        from app.share.utils.password_encoder import PasswordEncoder
        return PasswordEncoder.check_password(password, member.password)


