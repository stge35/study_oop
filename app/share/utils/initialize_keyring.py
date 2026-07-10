import keyring
import tkinter as tk
from tkinter import messagebox, simpledialog

class InitializeKeyring:

    _SERVICE_NAME = "MyLawFirmApp"
    _KEY_NAME = "SecretKey"

    @classmethod
    def register_key(cls) -> bool:

        """
        프로그램 진입점(main.py)에서 실행되어 키 등록 상태를 확인하고 팝업을 띄운다.
        """
        saved_key = keyring.get_password(cls._SERVICE_NAME, cls._KEY_NAME)

        if saved_key and len(saved_key.encode('utf-8')) == 32:
            return True

        temp_root = tk.Tk()
        temp_root.withdraw() # 임시 창은 뒤로 숨기기

        messagebox.showinfo("최초 인증", "시스템 최초 실행 인증이 필요합니다.")

        user_key = simpledialog.askstring(
            "인증 키 주입",
            "발급받은 암호화 키를 입력하세요",
            show = "*"
        )

        if user_key and len(user_key.encode('utf-8')) == 32:
            keyring.set_password(cls._SERVICE_NAME, cls._KEY_NAME, user_key)
            messagebox.showinfo("인증 성공", "등록이 완료되었습니다.")
            temp_root.destroy()
            return True

        else:
            messagebox.showerror("인증실패", "올바른 키가 아닙니다. 프로그램을 종료합니다.")
            temp_root.destroy()
            exit()

