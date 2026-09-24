from dataclasses import dataclass


@dataclass
class CompanyOffer:
    company_id: str

    price: float
