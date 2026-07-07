import tkinter as tk
from tkinter import messagebox

from app.domain.member.controller.member_controller import MemberController
from app.domain.member.dto.request.create_member_dto import CreateMemberDto


class SignInApp:

    def __init__(self, window: tk.Tk, controller: MemberController):

        self.window = window
        self.controller = controller

        # 윈도우창 레이아웃
        self.window.title("최명진 법무사 사무소 - 멤버가입 시스템")
        self.window.geometry("400x350")
        self.window.resizable(False, False)

        self. _create_widgets()

    def _create_widgets(self):

        # 프레임 구분
        title_label = tk.Label(self.window, text = "신규사원가입", font=("Arial", 10, "bold"))
        title_label.pack(pady = 15)

        # 입력 폼 프레임 (가운데 정렬을 위해)
        form_frame = tk.Frame(self.window)
        form_frame.pack(pady = 10)

        # 1. 이름 입력
        tk.Label(form_frame, text = "이름: ", font = ("Arial", 10)).grid(row = 0, column = 0, sticky = "e", pady = 5)
        self.name_entry = tk.Entry(form_frame, width = 25)
        self.name_entry.grid(row = 0, column = 1, pady = 5, padx = 10)

        # 2. 비밀번호 입력
        tk.Label(form_frame, text = "비밀번호: ", font = ("Arial", 10)).grid(row = 1, column = 0, sticky = "e", pady = 5)
        self.password_entry = tk.Entry(form_frame, width = 25, show = "*") # 비밀번호 마스킹
        self.password_entry.grid(row = 1, column = 1, pady = 5, padx = 10)

        # 3. 주민번호 입력
        tk.Label(form_frame, text="주민번호: ", font = ("Arial", 10)).grid(row = 2, column = 0, sticky = "e", pady = 5)
        self.personal_number_front_entry = tk.Entry(form_frame, width = 25)
        self.personal_number_front_entry.grid(row = 2, column = 1, pady = 5, padx = 10)
        tk.Label(form_frame, text = "-", font = ("Arial", 10)).grid(row = 2, column = 2, sticky = "e", pady = 5)
        self.personal_number_back_entry = tk.Entry(form_frame, width=25)
        self.personal_number_back_entry.grid(row=2, column=3, pady=5, padx=10)

        # 4. 전화번호 입력
        tk.Label(form_frame, text = "전화번호: ", font = ("Arial", 10)).grid(row = 3, column = 0, sticky = "e", pady = 5)
        self.phone_number_entry = tk.Entry(form_frame, width = 25)
        self.phone_number_entry.grid(row = 3, column = 1, pady = 5, padx = 10)
        # 5. 신청버튼

        submit_btn =tk.Button(
            self.window,
            text = "확인",
            font = ("Arial", 11, "bold"),
            command = self._on_click_register,
            width = 10,
            height = 2
        )

        submit_btn.pack(pady = 20, side = "left", expand = True)

        # 6. 취소버튼(클릭시 이전 화면으로 이동)

        cancel_btn = tk.Button(
            self.window,
            text = " 취소",
            font = ("Arial", 11, "bold"),
            command = self._on_click_cancel,
            width = 10,
            height = 2
        )

        cancel_btn.pack(pady = 20, side = "right", expand = True)
    def _on_click_register(self):

        # 버튼 클릭 하면 controller로 데이터를 던지는 함수
        name = self.name_entry.get().strip()
        password = self.password_entry.get().strip()
        personal_number = self.personal_number_front_entry.get().strip()+ self.personal_number_back_entry.get().strip()
        phone_number = self.phone_number_entry.get().strip()

        if not (name and password and personal_number):
            messagebox.showwarning("필수 항목을 입려해 주세요.")
            return

        try:
            create_dto = CreateMemberDto(
                name = name,
                password = password,
                personal_number = personal_number,
                phone_number = phone_number
            )
            response_dto = self.controller.register_member(create_dto)

            success_msg = (
                f"가입이 성공적으로 완료되었습니다."
                f"가입자: {response_dto.name}"
            )
            messagebox.showinfo("성공", success_msg)

            self._clear_entries()

        except ValueError as e:
            messagebox.showerror("가입실패", str(e))

    def _clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.personal_number_front_entry.delete(0, tk.END)
        self.personal_number_back_entry.delete(0, tk.END)
        self.phone_number_entry.delete(0, tk.END)

    def _on_click_cancel(self):
        pass