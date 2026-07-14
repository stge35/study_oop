from typing import Optional


class Client:

    def __init__(self,
                name: str,
                personal_number: str,
                address: str,
                phone_number: str,
                client_id: Optional[int] = None):

        self.name = name
        self.personal_number = personal_number
        self.address = address
        self.client_id = client_id
        self.phone_number = phone_number

    def __repr__(self) -> str:
        return f'Client(name = {self.name}, client_id = {self.client_id}'


        # 신분증 암호화 알고리즘 추가 예정

    @classmethod
    def to_client(cls,
                  name : str,
                  personal_number : str,
                  address : str,
                  phone_number: str,
                  client_id : int = None
                  ) -> "Client":

        cleaned_personal_number = personal_number.replace("-", "")


        return cls(
            name = name,
            personal_number = cleaned_personal_number,
            address = address,
            client_id = client_id,
            phone_number = phone_number
        )

