from dataclasses import dataclass

from domain.ranking_topsis_row import (
    RankingTopsisRow
)


@dataclass
class RankingTopsisMatrix:

    rows: list[RankingTopsisRow]
