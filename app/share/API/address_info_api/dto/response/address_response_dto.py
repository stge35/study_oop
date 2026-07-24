from dataclasses import dataclass

from app.share.API.address_info_api.entity.address import Address


@dataclass
class AddressResponseDto:
    zip_code: str
    full_address: str
    road_address: str
    detail_address: str

    @classmethod
    def from_entity(cls, address: Address) -> "AddressResponseDto":
        full_addr = f"{address.road_address} {address.detail_address}".strip()
        return cls(
            zip_code = address.zip_code,
            full_address = full_addr,
            road_address = address.road_address,
            detail_address = address.detail_address
        )
