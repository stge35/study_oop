from abc import abstractmethod

from app.domain.client.entity.client import Client


class ClientInterface:

    @abstractmethod
    def save_client(self, client: Client) -> Client:
        pass

    @abstractmethod
    def find_all_client(self) -> list[Client]:
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> list[Client]:
        pass

    @abstractmethod
    def find_by_id(self, client_id: str) -> Client | None:
        pass

    @abstractmethod
    def exists_by_personal_number(self, personal_number: str) -> bool:
        pass

    @abstractmethod
    def remove_by_client_id(self, client_id: str) -> bool:
        pass