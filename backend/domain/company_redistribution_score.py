from dataclasses import dataclass


@dataclass
class CompanyRedistributionScore:
    company_id: str

    redistribution_score: float
