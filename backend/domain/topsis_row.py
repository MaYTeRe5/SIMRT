from dataclasses import dataclass


@dataclass
class TopsisRow:
    company_id: str

    price: float

    brand_score: float

    innovation_score: float

    credit_terms: int
