import tkinter as tk
from tkinter import messagebox

from app.domain.gui.login.main_gui import MainGui
from app.domain.member.controller.member_controller import MemberController


class LogIn:

    def __init__(self, window: tk.Tk, controller: MemberController):

        self.window = window
        self.controller = controller

        # 창 기본 설정
        self.window.title("로그인")
        self.window.geometry("350x220")
        self.window.resizable(False, False)

        self.main_frame = tk.Frame(self.window, padx = 30, pady = 20)
        self.main_frame.pack(expand = True, fill = 'both')

        self._create_widgets()

    def _create_widgets(self):

        title_label = tk.Label(self.main_frame, text = "시스템 로그인", font = ("맑은 고딕", 16, "bold"))
        title_label.grid(row = 0, column = 0, columnspan = 2, pady = (0,20))

        name_label = tk.Label(self.main_frame, text = "사용자 이름 : ", font = ("맑은 고딕", 10))
        name_label.grid(row = 1, column = 0, sticky = "e", pady = 5)

        self.name_entry = tk.Entry(self.main_frame, width = 20, font = ("맑은 고딕", 10))
        self.name_entry.grid(row = 1, column = 1, padx = 10, pady = 5)
        self.name_entry.focus()

        # password input

        password_label = tk.Label(self.main_frame, text = "비밀번호 : ", font = ("맑은 고딕", 10))
        password_label.grid(row = 2, column = 0, sticky = "e", pady = 5)

        self.password_entry = tk.Entry(self.main_frame, width=20, font=("맑은 고딕", 10), show = "*")
        self.password_entry.grid(row = 2, column = 1, padx = 10, pady = 5)

        self.password_entry.bind("<Return>", lambda event: self._on_login_click())

        login_btn = tk.Button(
            self.window,
            text = "로그인",
            command = self._on_login_click,
            width = 22,
            font = ("맑은 고딕", 10, "bold")
        )
        login_btn.pack(pady = 20, side = "left", expand = True)

        cancel_btn = tk.Button(
            self.window,
            text="닫기",
            command = lambda : self.window.destroy(),
            width = 22,
            font=("맑은 고딕", 10, "bold")
        )
        cancel_btn.pack(pady = 20, side = "right", expand = True)

    def _on_login_click(self):

        name = self.name_entry.get().strip()
        password = self.password_entry.get().strip()

        if not name or not password:
            messagebox.showwarning("경고", "이름과 비밀번호를 모두 입력해 주세요.")
            return

        try:
            success = self.controller.login_member(name, password)

            if success:
                messagebox.showinfo("로그인 성공", f"{name}님")
                self._open_main_dashboard(name)
            else:
                messagebox.showerror("로그인 실패", "비밀번호가 일치하지 않습니다.")

        except ValueError as e:
            messagebox.showerror("로그인 실패", str(e))

    def _open_main_dashboard(self, name: str):
        self.window.destroy()

        main_window = tk.Tk()

        from app.domain.gui.login.main_gui import MainGui
        MainGui(window = main_window, member_controller = self.controller, login_member_name = name)

        main_window.mainloop()