from dataclasses import dataclass


@dataclass
class CompanyAvailableSupply:
    company_id: str

    available_units: int
