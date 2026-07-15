from typing import List

from app.domain.client.dto.request.create_client_dto import CreateClientDto
from app.domain.client.dto.response.response_client_dto import ResponseClientDto
from app.domain.client.entity.client import Client
from app.domain.client.repository.file_client_repository import FileClientRepository


class ClientService:

    def __init__(self, repository: FileClientRepository):

        self.repository = repository

    def save(self, dto:CreateClientDto) -> ResponseClientDto:

        client = dto.to_client()

        if self.repository.exists_by_personal_number(client.personal_number):
            raise ValueError("이미 등록되어 있는 고객입니다.")

        saved_client = self.repository.save_client(client)

        return ResponseClientDto.from_client(saved_client)

    def search_all_clients(self) -> list[ResponseClientDto]:
        clients = self.repository.find_all_client()

        return clients if clients else []

    def search_client_by_name(self, name: str) -> list[ResponseClientDto] | None:
        clients = self.repository.find_by_name(name)

        return clients if clients else []

    def search_client_by_id(self, client_id: int) -> ResponseClientDto | None:

        client = self.repository.find_by_id(client_id)
        return client if client else None

    def del_client(self, client_id: int) -> None:
        self.del_client(client_id)



