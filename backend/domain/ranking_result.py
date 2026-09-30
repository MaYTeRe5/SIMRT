from dataclasses import dataclass


@dataclass
class RankingResult:

    company_id: str

    ranking_score: float

    rank: int
