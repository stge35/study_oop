from app.domain.client.dto.request.create_client_dto import CreateClientDto
from app.domain.client.dto.response.response_client_dto import ResponseClientDto
from app.domain.client.service.client_service import ClientService


class ClientController:

    def __init__(self, service: ClientService):

        self.client_service = service

    def register_client(self, dto: CreateClientDto) -> ResponseClientDto:

        try:
            response: ResponseClientDto = self.client_service.save(dto)
            return response

        except ValueError as e:
            raise ValueError(f"fail : {e}")

    def search_client_by_name(self, name: str) -> list[ResponseClientDto]:

        clients = self.client_service.search_client_by_name(name)

        return clients

    def search_client_by_id(self, client_id: int) -> ResponseClientDto:

        client = self.client_service.search_client_by_id(client_id)

        return client

    def del_client_by_id(self, client_id: int) -> None:

        return self.client_service.del_client(client_id)