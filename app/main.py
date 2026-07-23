import sys
from PySide6.QtWidgets import QApplication

from app.domain.gui.login.login_window import LoginWindow
from app.domain.gui.login.member_register_window import MemberRegisterWindow
from app.domain.member.controller.member_controller import MemberController
from app.domain.member.repository.file_member_repository import FileMemberRepository
from app.domain.member.service.member_service import MemberService
from app.share.utils.initialize_keyring import InitializeKeyring

if __name__ == "__main__":

    app = QApplication(sys.argv)

    repository = FileMemberRepository("member.json")
    service = MemberService(repository = repository)
    controller = MemberController(service = service)

    InitializeKeyring.register_key()

    if service.has_any_member():
        window = LoginWindow(controller)
        window.show()

    else:
        window = MemberRegisterWindow(controller)
        window.show()

    sys.exit(app.exec())