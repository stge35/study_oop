from dataclasses import dataclass


@dataclass(frozen=True)
class LandRequestDto:
    pnu: str
