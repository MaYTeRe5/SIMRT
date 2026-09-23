from dataclasses import dataclass


@dataclass
class Player:
    id: str
    first_name: str
    last_name: str
    email: str
