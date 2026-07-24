from PySide6.QtWidgets import (
    QMainWindow, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QWidget, QMessageBox)
from PySide6.QtCore import Qt

from app.domain.gui.sign_in.person_info_form_widget import PersonInFoFormWidget
from app.domain.member.controller.member_controller import MemberController
from app.share.API.address_info_api.controller.address_controller import AddressController


class MemberRegisterWindow(QMainWindow):

    def __init__(self, controller: MemberController, address_controller: AddressController):
        super().__init__()

        self.member_controller = controller
        self.address_controller = address_controller
        self.setWindowTitle("최명진 법무사 사무소 - 직원 등록")
        self.setFixedSize(580, 420)

        self._init_ui()

    def _init_ui(self):

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(35, 25, 35, 25)

        # 1. member register title
        title_label = QLabel("신규 직원 등록", self)
        title_label.setObjectName("titleLabel")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)
        main_layout.addSpacing(15)

        # 2. component recycle

        self.form_widget = PersonInFoFormWidget(controller = self.address_controller, parent = self)
        # self.form_widget.pw_entry.hide()

        main_layout.addWidget(self.form_widget)
        main_layout.setSpacing(25)

        # 3. button
        button_layout = QHBoxLayout()
        self.submit_btn = QPushButton("저장", self)
        self.cancel_btn = QPushButton("취소", self)

        button_layout.addStretch()
        button_layout.addWidget(self.submit_btn)
        button_layout.addWidget(self.cancel_btn)
        main_layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # 4. connecting event
        self.submit_btn.clicked.connect(self._on_click_save_data)
        self.cancel_btn.clicked.connect(self.close)

    def _on_click_save_data(self):
        data = self.form_widget.get_form_data()
        if not data.name or data.personal_number:
            QMessageBox.warning(self, "경고", "이름과 주민번호는 필수 입력 항목입니다.")
            return

        self.member_controller.register_member(data)

