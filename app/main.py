import tkinter as tk

from app.domain.gui.login.log_in import LogIn
from app.domain.gui.login.sign_in_app import SignInApp
from app.domain.member.controller.member_controller import MemberController
from app.domain.member.repository.file_member_repository import FileMemberRepository
from app.domain.member.service.member_service import MemberService
from app.share.utils.initialize_keyring import InitializeKeyring

if __name__ == "__main__":

    repository = FileMemberRepository("member.json")
    service = MemberService(repository = repository)
    controller = MemberController(service = service)

    InitializeKeyring.register_key()

    window = tk.Tk()

    if service.has_any_member():
        LogIn(window, controller)
    else:
        SignInApp(window, controller)
    window.mainloop()
