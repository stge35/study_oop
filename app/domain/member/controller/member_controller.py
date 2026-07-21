from app.domain.member.dto.request.create_member_dto import CreateMemberDto
from app.domain.member.dto.request.update_member_dto import UpdateMemberDto
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

    def patch_member(self, client_id: int, phone_number: str, address: str):

        try:
            update_dto = UpdateMemberDto(
                member_id = client_id,
                phone_number = phone_number,
                address = address
            )

            return self.member_service.patch(update_dto)

        except ValueError as e:
            raise ValueError(f"[수정 실패] {str(e)}")

        except Exception as e:
            raise RuntimeError(f"회원정보 수정중 오류 발생 {str(e)}")


