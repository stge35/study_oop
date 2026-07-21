import re
from typing import Optional

from app.domain.client.entity.client import Client
from app.share.utils.data_encryptor import DataEncryptor
from app.share.validation.data_validator import DataValidator


class CreateClientDto:

    def __init__(self,
                 name : str,
                 personal_number: str,
                 address: str,
                 phone_number: str,
                 client_id : Optional[int] = None
                 ):

        self.name = DataValidator.validate_korean_name(name)
        self.personal_number = DataValidator.validate_numeric_string(personal_number, field_name = "주민번호", context = "DTO")
        self.personal_number = DataValidator.validate_clean_phone(phone_number)
        self.address = address
        self.client_id = client_id

    def to_client(self) -> Client:

        encrypted_p_num = DataEncryptor.encrypt(self.personal_number)
        encrypted_address = DataEncryptor.encrypt(self.address)

        return Client.to_client(
            name = self.name,
            personal_number = encrypted_p_num,
            address = encrypted_address,
            phone_number = self.personal_number,
            client_id = self.client_id
        )