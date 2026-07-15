from dataclasses import dataclass

from app.domain.client.entity.client import Client


@dataclass
class ResponseClientDto:

    name: str
    personal_number: str
    address: str
    phone_number: str
    client_id: int

    @classmethod
    def from_client(cls, entity: Client) -> "ResponseClientDto":

        return cls(
            name = entity.name,
            personal_number = entity.personal_number,
            address = entity.address,
            phone_number = entity.phone_number,
            client_id = entity.client_id
        )