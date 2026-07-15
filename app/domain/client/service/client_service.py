from app.domain.client.dto.request.create_client_dto import CreateClientDto
from app.domain.client.dto.response.response_client_dto import ResponseClientDto
from app.domain.client.repository.file_client_repository import FileClientRepository


class ClientService:

    def __init__(self, repository: FileClientRepository):

        self.repository = repository

    def save(self, dto:CreateClientDto) -> ResponseClientDto:

        client = dto.to_client()

        if self.repository.exists_by_personal_number(client.personal_number):
            raise ValueError("이미 등록되어 있는 고객입니다.")

        saved_client = self.repository.save_client(client)

