from dataclasses import dataclass


@dataclass
class RankingTopsisRow:

    company_id: str

    market_share: float

    ebitda: float

    roe: float

    debt_asset_ratio: float

    inventory_turn: float
