from dataclasses import dataclass


@dataclass()
class Land:

    pnu: str
    address: str
    land_type: str
    area: float
    official_price: int

    owner_name: str
    owner_type: str
    share_numerator: int        # 분자
    share_denominator: int      # 분모

    @property
    def share_ratio(self) -> float:
        if self.share_denominator == 0:
            return 1.0

        return self.share_numerator / self.share_denominator

    @property
    def owned_area(self) -> float:
        return round(self.area * self.share_ratio, 4)
