from PySide6.QtWidgets import (
    QMainWindow, QPushButton,
    QVBoxLayout, QHBoxLayout,
    QLabel, QWidget, QMessageBox,
    QLineEdit, QGridLayout
)
from PySide6.QtCore import Qt

from app.domain.member.controller.member_controller import MemberController


class SignInWindow(QMainWindow):

    def __init__(self, controller: MemberController):
        self.controller = controller
        super().__init__()

        self.setWindowTitle("회원 가입")
        self.setFixedSize(580, 420)

        self._create_widgets()


    def _create_widgets(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(35, 25, 35, 25)


        # 1. 위젯 생성
        title_label = QLabel("회원 가입", self)
        title_label.setObjectName("titleLabel")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)
        main_layout.addSpacing(15)

        # 2. 입력 폼 레이아웃
        form_layout = QGridLayout()
        form_layout.setSpacing(12)

        # 2-1. 이름

        name_label = QLabel("이름", self)
        name_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.name_entry = QLineEdit(self)
        self.name_entry.setPlaceholderText("홍길동")
        form_layout.addWidget(name_label, 0, 0)
        form_layout.addWidget(self.name_entry, 0, 1, 1, 3)
        ### 제목 글자 크기 및 정렬 설정
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = self.title_label.font()
        font.setPointSize(16)
        font.setBold(True)
        self.title_label.setFont(font)

        # id 입력 영역
        self.name_label = QLabel("이름 : ", self)
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("이름을 입력하세요.")

        # pw 입력 영역
        self.pw_label = QLabel("비밀번호 : ", self)
        self.pw_input = QLineEdit(self)
        self.pw_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.pw_input.setPlaceholderText("비밀번호를 입력하세요.")

        # personal_number 입력 영역
        self.personal_number

