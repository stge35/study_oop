from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QLabel
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QKeyEvent

class SsnInputWidget(QWidget):
    """
    주민번호 입력 및 포커스 제어를 담당하는 컴포넌트
    """

    def __init__(self, parent = None):

        super().__init__(parent)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.front_entry = QLineEdit(self)
        self.front_entry.setMaxLength(6)

        dash_label = QLabel("-", self)
        dash_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        dash_label.setFixedWidth(12)

        self.back_entry = QLineEdit(self)
        self.back_entry.setMaxLength(7)

        layout.addWidget(self.front_entry)
        layout.addWidget(dash_label)
        layout.addWidget(self.back_entry)

        # connect event
        self.front_entry.textChanged.connect(self._check_front_length)
        self.back_entry.installEventFilter(self)


    def _check_front_length(self, text: str):
        if len(text) == 6:
            self.back_entry.setFocus()

    def eventFilter(self, obj, event):
        if obj == self.back_entry and event.type() == QEvent.Type.KeyPress:
            key_event = QKeyEvent(event)
            if key_event.key() == Qt.Key.Key_Backspace and len(self.back_entry.text()) == 0:
                self.front_entry.setFocus()
                return True
        return super().eventFilter(obj, event)

    def get_ssn(self) -> str:
        return self.front_entry.text().strip() + self.back_entry.text().strip()

