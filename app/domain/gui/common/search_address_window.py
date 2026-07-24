from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLineEdit,
    QPushButton, QListWidget, QListWidgetItem, QMessageBox, QLabel
)
from PySide6.QtCore import Qt

class SearchAddressWindow(QDialog):

    def __init__(self, address_list: list, parent = None):
        super().__init__(parent)
        self.selected_address = None
        self.init_ui()
        self.set_address_list(address_list)

    def init_ui(self):
        self.setWindowTitle("주소 검색")
        self.resize(500, 400)

        list_layout = QVBoxLayout(self)

        # 상단 안내 문구
        info_label = QLabel("주소를 클릭하면 자동으로 입력됩니다.", self)
        list_layout.addWidget(info_label)

        self.result_list = QListWidget(self)

        self.result_list.itemClicked.connect(self.on_select_address)
        list_layout.addWidget(self.result_list)

    def set_address_list(self, address_list: list):
        self.result_list.clear()

        for item in address_list:
            display_text = f"[{item.road_address}]"
            list_item = QListWidgetItem(display_text)

            list_item.setData(Qt.ItemDataRole.UserRole, item)
            self.result_list.addItem(list_item)

    def on_select_address(self, item:QListWidgetItem):
        self.selected_address = item.data(Qt.ItemDataRole.UserRole)
        self.accept()

