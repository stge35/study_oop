import tkinter as tk

from app.domain.gui.login.sign_in_app import SignInApp
from app.domain.member.controller.member_controller import MemberController
from app.domain.member.repository.file_member_repository import FileMemberRepository
from app.domain.member.service.member_service import MemberService

if __name__ == "__main__":

    repository = FileMemberRepository("member.json")
    service = MemberService(repository = repository)
    controller = MemberController(service = service)

    root = tk.Tk()
    app = SignInApp(window = root, controller = controller)
    root.mainloop()