import json
import os
from typing import List
from app.domain.client.entity.client import Client
from app.domain.client.repository.clinet_interface import ClientInterface
from app.share.utils.data_encryptor import DataEncryptor


class FileClientRepository(ClientInterface):

    def __init__(self, file_path : str = "clients.json"):
        self.file_path = file_path

        if not os.path.exists(self.file_path):
            self._save_data([])

    def save_client(self, client: Client) -> Client:

        all_client = self._read_data()

        if client.client_id is None:
            client.client_id = len(all_client) + 1

        client_dict = client.__dict__

        all_client.append(client_dict)

        self._save_data(all_client)

        print("저장 성공")

        return client

    def find_all_client(self) -> list[Client]:

        raw_data_list = self._read_data()
        clients = []

        for data in raw_data_list:
            decrypt_p_number = DataEncryptor.decrypt(data['personal_number'])

            client = Client(
                name = data['name'],
                personal_number=decrypt_p_number,
                address = data['address'],
                phone_number = data['phone_number'],
                client_id = data['client_id']
            )
            clients.append(client)

        return clients

    def find_by_name(self, name: str) -> list[Client]:

        all_clients = self._read_data()
        results = []

        for data in all_clients:
            if data['name'] == name:
                decrypted_p_num = DataEncryptor.decrypt(data['personal_number'])

                client_entity = Client.to_client(
                    name = data['name'],
                    personal_number = decrypted_p_num,
                    address = data['address'],
                    phone_number = data['phone_number'],
                    client_id = data['client_id']
                )
                results.append(client_entity)

        return results

    def find_by_id(self, client_id: str) -> Client | None:

        all_clients = self._read_data()
        for data in all_clients:
            if data['client_id'] == client_id:

                decrypted_p_num = DataEncryptor.decrypt(data['personal_number'])

                return Client.to_client(
                    client_id=data['client_id'],
                    name = data['name'],
                    personal_number = decrypted_p_num,
                    address = data['address'],
                    phone_number = data['phone_number']
                )
        return None

    def exists_by_personal_number(self, personal_number: str) -> bool:

        all_clients = self._read_data()

        for data in all_clients:
            if data.get("personal_number") == personal_number:
                return True

        return False


    def _save_data(self, data: List[dict]):

        with open(self.file_path, "w", encoding = 'utf-8') as f:
            return json.dump(data, f, ensure_ascii = False, indent = 4)

    def _read_data(self) ->List[dict]:

        with open(self.file_path, "r", encoding = 'utf-8') as f:
            return json.load(f)