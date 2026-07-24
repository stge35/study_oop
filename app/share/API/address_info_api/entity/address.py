from dataclasses import dataclass


@dataclass
class Address:

    zip_code: str
    road_address: str
    detail_address: str
    building_name: str
