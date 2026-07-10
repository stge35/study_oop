from dataclasses import dataclass

from app.share.API.land_api.entity.land import Land


@dataclass(frozen=True)
class LandResponseDto:

    address: str
    land_type: str
    total_area: float
    owner_name: str
    share_text: str
    owned_area_m2:float
    official_price: int
    total_land_value: int
    owned_land_value: int

    @classmethod
    def from_entity(cls, entity: Land) -> "LandResponseDto":

        total_val = int(entity.area * entity.official_price)
        owned_val = int(entity.owned_area * entity.official_price)

        return cls(
            address=entity.address,
            land_type=entity.land_type,
            total_area=entity.area,
            owner_name=entity.owner_name,
            share_text=f"{entity.share_numerator} / {entity.share_denominator}" if entity.share_denominator > 0 else "단독 소유",
            owned_area_m2=entity.owned_area,
            official_price=entity.official_price,
            total_land_value=total_val,
            owned_land_value=owned_val
        )