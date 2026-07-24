import sys
from PySide6.QtWidgets import QApplication

from app.domain.gui.login.login_window import LoginWindow
from app.domain.gui.sign_in.member_register_window import MemberRegisterWindow
from app.domain.member.controller.member_controller import MemberController
from app.domain.member.repository.file_member_repository import FileMemberRepository
from app.domain.member.service.member_service import MemberService
from app.share.API.address_info_api.controller.address_controller import AddressController
from app.share.API.address_info_api.service.address_service import AddressService
from app.share.utils.initialize_keyring import InitializeKeyring

if __name__ == "__main__":

    app = QApplication(sys.argv)

    member_repository = FileMemberRepository("member.json")
    member_service = MemberService(repository = member_repository)
    member_controller = MemberController(service = member_service)


    address_service = AddressService()
    address_controller = AddressController(service = address_service)


    InitializeKeyring.register_key()

    if member_service.has_any_member():
        window = LoginWindow(member_controller)
        window.show()

    else:
        window = MemberRegisterWindow(member_controller, address_controller)
        window.show()

    sys.exit(app.exec())