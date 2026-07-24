from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Qt

from app.domain.gui.common.search_address_window import SearchAddressWindow
from app.domain.gui.sign_in.ssn_input_widget import SsnInputWidget
from app.domain.member.dto.request.create_member_dto import CreateMemberDto
from app.share.API.address_info_api.controller.address_controller import AddressController
from app.share.validation.business_exception import BusinessException


class PersonInFoFormWidget(QWidget):
    """
    회원 정보 입력 폼 컴포넌트
    """

    def __init__(self, controller: AddressController, parent = None):
        super().__init__(parent)
        self.controller = controller

        form_layout = QGridLayout(self)
        form_layout.setContentsMargins(0, 0, 0, 0)
        form_layout.setSpacing(12)

        # 1. name
        name_label = QLabel("이름", self)
        name_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.name_entry = QLineEdit(self)
        form_layout.addWidget(name_label, 0, 0)
        form_layout.addWidget(self.name_entry, 0, 1, 1, 3)



        # 3. personal_number
        ssn_label = QLabel("주민번호", self)
        ssn_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.ssn_widget = SsnInputWidget(self)
        form_layout.addWidget(ssn_label, 1, 0)
        form_layout.addWidget(self.ssn_widget, 1, 1, 1, 3)

        # 4. address
        address_label = QLabel("주소", self)
        address_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.address_entry = QLineEdit(self)
        form_layout.addWidget(address_label, 2, 0)
        form_layout.addWidget(self.address_entry, 2, 1, 1, 2)
        self.address_search_btn = QPushButton("검색", self)
        form_layout.addWidget(self.address_search_btn, 2, 3)
        self.address_search_btn.clicked.connect(self._open_address_search_dialog)

        self.address_entry_back = QLineEdit(self)
        form_layout.addWidget(self.address_entry_back, 3, 1, 1, 2)


        # 5. phone_number
        phone_label = QLabel("전화번호", self)
        phone_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.phone_number_entry = QLineEdit(self)
        form_layout.addWidget(phone_label, 4, 0)
        form_layout.addWidget(self.phone_number_entry, 4, 1, 1, 3)

        # 2. password
        pw_label = QLabel("비밀번호", self)
        pw_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.pw_entry = QLineEdit(self)
        self.pw_entry.setEchoMode(QLineEdit.EchoMode.Password)
        form_layout.addWidget(pw_label, 5, 0)
        form_layout.addWidget(self.pw_entry, 5, 1, 1, 3)

    def _open_address_search_dialog(self):
        keyword = self.address_entry.text().strip()

        if not keyword:
            QMessageBox.warning(self, "알림", "검색할 주소를 입력해 주세요.")
            return
        try:
            address_list = self.controller.search_address(keyword)

            if not address_list:
                QMessageBox.information(self, "알림", "검색 결과가 없습니다.")
                return

            dialog = SearchAddressWindow(address_list = address_list, parent = self)

            if dialog.exec():
                selected_dto = dialog.selected_address
                if selected_dto:
                    self.address_entry.setText(selected_dto.road_address)

        except BusinessException as e:
            QMessageBox.warning(self,"검색 오류", e.message)
        except Exception as e:
            QMessageBox.critical(self, "오류", f"주소 검색 처리 중 오류 : {str(e)}")

    def get_form_data(self) -> CreateMemberDto:

        return CreateMemberDto(
            name = self.name_entry.text().strip(),
            password = self.pw_entry.text().strip(),
            personal_number = self.ssn_widget.get_ssn(),
            address = self.address_entry.text().strip(),
            phone_number = self.phone_number_entry.text().strip()
        )