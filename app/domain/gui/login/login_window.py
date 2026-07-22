from PySide6.QtWidgets import  (
    QMainWindow, QPushButton,
    QVBoxLayout, QLabel, QWidget,
    QMessageBox, QLineEdit, QHBoxLayout
)
from PySide6.QtCore import Qt

from app.domain.member.controller.member_controller import MemberController

class LoginWindow(QMainWindow):

    def __init__(self, controller: MemberController):
        self.controller = controller
        super().__init__()

        self.setWindowTitle("로그인 시스템")
        self.setFixedSize(320, 220) # 창 크기 고정 (너비, 높이)

        # 1. 위젯 생성
        self.title_label = QLabel("시스템 로그인", self) # 타이틀 라벨

        ### 제목 글자 크기 및 정렬 설정
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = self.title_label.font()
        font.setPointSize(16)
        font.setBold(True)
        self.title_label.setFont(font)

        ### 아이디 입력 영역
        self.name_label = QLabel("이름  : ", self)
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("이름을 입력하세요.")

        ### 비밀 번호 입력 영역
        self.pw_label = QLabel("비밀번호 : ", self)
        self.pw_input = QLineEdit(self)
        self.pw_input.setEchoMode(QLineEdit.EchoMode.Password) # 입력 내용 별표(*)
        self.pw_input.setPlaceholderText("비밀번호를 입력하세요.")

        ### 로그인 버튼
        self.login_button = QPushButton("로그인", self)

        ### 취소 버튼
        self.cancel_button = QPushButton("취소", self)

        ### 안내 메시지 표시 라벨
        self.result_label = QLabel("", self)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # 2. 레이 아웃 배치
        main_layout = QVBoxLayout()

        ### 아이디 행 (가로로 묶기)
        id_layout = QHBoxLayout()
        id_layout.addWidget(self.name_label)
        id_layout.addWidget(self.name_input)

        ### 비밀 번호 행(가로로 묶기)
        pw_layout = QHBoxLayout()
        pw_layout.addWidget(self.pw_label)
        pw_layout.addWidget(self.pw_input)

        ### 버튼 행(가로 묶기 + 우측 정렬)
        button_layout = QHBoxLayout()
        button_layout.addStretch() # 왼쪽에 가변 공간을 넣어 버튼을 오른쪽으로 배치
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.cancel_button)

        ### 메인 레이 아웃 에 세로로 묶기
        main_layout.addWidget(self.title_label)
        main_layout.addSpacing(10) # 간격 추가
        main_layout.addLayout(id_layout)
        main_layout.addLayout(pw_layout)
        main_layout.addSpacing(10)
        main_layout.addLayout(button_layout) # 우측 하단 버튼 레이아웃 추가
        main_layout.addWidget(self.result_label)

        ### 메인 위젯에 레이아웃 설정
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # 3. 시그널-슬롯 연결
        self.login_button.clicked.connect(self.handle_login)
        self.cancel_button.clicked.connect(self.handle_cancel)
        self.pw_input.returnPressed.connect(self.handle_login)

    def handle_login(self):
        name = self.name_input.text().strip()
        password = self.pw_input.text().strip()

        if not name :
            self.result_label.setText("<font color='red'> 이름을 입력해 주세요.")
            return

        if not password :
            self.result_label.setText("<font color='red'> 비밀 번호를 입력해 주세요.")
            return

        try:
            success = self.controller.login_member(name, password)

            if success:
                self.result_label.setText("<font color = 'green'> 로그인 성공!</font>")
                QMessageBox.information(self, "성공", f"환영합니다. {name}님")
            else:
                self.result_label.setText("<font color = 'red'> 아이디 또는 비밀번호가 틀렸습니다.")

        except ValueError as e:
            QMessageBox.information(self,"<font color = 'red'> 로그인 실패", str(e))

    def handle_cancel(self):
        self.name_input.clear()
        self.pw_input.clear()
        self.result_label.setText("입력 취소")