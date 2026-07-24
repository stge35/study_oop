import sys
from PySide6.QtWidgets import QApplication

# 1. UI Window
from app.domain.gui.sign_in.member_register_window import MemberRegisterWindow

# 2. Address API 의존성
from app.share.API.address_info_api.controller.address_controller import AddressController
from app.share.API.address_info_api.repository.file_address_repository import FileAddressRepository
from app.share.API.address_info_api.service.address_service import AddressService

# 3. Member Domain 의존성
from app.domain.member.controller.member_controller import MemberController
from app.domain.member.repository.file_member_repository import FileMemberRepository  # 예시 레포지토리
from app.domain.member.service.member_service import MemberService                # 예시 서비스


def main():
    app = QApplication(sys.argv)

    # ----------------------------------------------------
    # 💡 1. Address API 의존성 주입
    # ----------------------------------------------------
    address_repository = FileAddressRepository()
    address_service = AddressService(repository=address_repository)
    address_controller = AddressController(service=address_service)

    # ----------------------------------------------------
    # 💡 2. Member Domain 의존성 주입
    # ----------------------------------------------------
    member_repository = FileMemberRepository()
    member_service = MemberService(repository=member_repository)
    member_controller = MemberController(service=member_service)

    # ----------------------------------------------------
    # 💡 3. MemberRegisterWindow 생성 및 출력
    # ----------------------------------------------------
    register_window = MemberRegisterWindow(
        controller = member_controller,
        address_controller = address_controller
    )
    register_window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()