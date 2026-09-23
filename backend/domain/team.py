from dataclasses import dataclass


@dataclass
class Team:
    id: str
    name: str

    assigned_company_id: str

    advisor_id: str | None
