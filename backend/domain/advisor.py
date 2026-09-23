from dataclasses import dataclass


@dataclass
class Advisor:
    id: str
    first_name: str
    last_name: str
    email: str
