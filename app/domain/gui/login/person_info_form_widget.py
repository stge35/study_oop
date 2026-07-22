from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit
from PySide6.QtCore import Qt

from app.domain.gui.login.ssn_input_widget import SsnInputWidget


class PersonInFoFormWidget(QWidget):
    """
    회원 정보 입력 폼 컴포넌트
    """

    def __init__(self, parent = None):
        super().__init__(parent)

        form_layout = QGridLayout(self)
        form_layout.setContentsMargins(0, 0, 0, 0)
        form_layout.setSpacing(12)

        # 1. name
        name_label = QLabel("이름", self)
        name_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.name_entry = QLineEdit(self)
        form_layout.addWidget(name_label, 0, 0)
        form_layout.addWidget(self.name_entry, 0,1,1,3)

        # 2. password
        pw_label = QLabel("비밀번호", self)
        pw_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.pw_entry = QLineEdit(self)
        form_layout.addWidget(pw_label, 1, 0)
        form_layout.addWidget(self.pw_entry, 1, 1, 1, 3)

        # 3. personal_number
        ssn_label = QLabel("주민번호", self)
        ssn_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.ssn_widget = SsnInputWidget(self)
        form_layout.addWidget(ssn_label, 2, 0)
        form_layout.addWidget(self.ssn_widget, 2, 1, 1, 3)

        # 4. address

        # 5. phone_number