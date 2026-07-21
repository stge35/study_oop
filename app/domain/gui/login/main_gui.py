import tkinter as tk
from tkinter import messagebox

class MainGui:

    def __init__(self, window, member_controller, login_member_name):
        self.window= window
        self.member_controller = member_controller
        self.login_member_name = login_member_name

        self.window.title("최명진 법무사 사무소")
        self.window.geometry("800x1200")
        self.window.resizable(False, False)

        self._create_header_frame()
        self._create_document_nav_frame()


    # header frame
    def _create_header_frame(self):
        header_frame = tk.Frame(self.window, bg = "#1E293B", height = 80)
        header_frame.pack(fill = "x", side = "top")
        header_frame.pack_propagate(False)

        # 타이틀 라벨
        title_label = tk.Label(
            header_frame,
            text = "최명진 법무사 사무소",
            font = ("맑은 고딕", 18, "bold"),
            fg = "white",
            bg = "#1E293B"
        )
        title_label.pack(side = "left", padx = 20)

        member_info_label = tk.Label(
            header_frame,
            text = f"접속자: {self.login_member_name}님",
            font = ("맑은 고딕", 11),
            fg = "#94A3B8",
            bg = "#1E293B"
        )
        member_info_label.pack(side = "right", padx = 20)

    # 1. 기본서류 frame
    def _create_document_nav_frame(self):
        doc_frame = tk.LabelFrame(
            self.window, text = "1. 기본서류 / 메뉴 선택", font = ("맑은 고딕", 11, "bold"), padx = 10, pady = 10
        )
        doc_frame.pack(fill="x", padx = 15, pady = 10)
        # 체크박스 목록 정의
        doc_list = ["등기신청서", "인감증명서", "초본/등본", "위임장"]

        for idx, doc_name in enumerate(doc_list):
            # 각 체크박스의 선택 상태(True/False)를 저장하는 BooleanVar 생성
            var = tk.BooleanVar(value=False)
            # self.doc_vars[doc_name] = var

            # Checkbutton 생성
            chk = tk.Checkbutton(
                doc_frame,
                text=doc_name,
                variable=var,
                font=("맑은 고딕", 11),
                # command=self._on_check_changed,  # 체크 상태 변경 시 호출
            )
            chk.grid(row=0, column=idx, padx=15, pady=5)






    # body frame

    # body frame
