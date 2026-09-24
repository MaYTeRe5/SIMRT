from dataclasses import dataclass

from domain.topsis_row import TopsisRow


@dataclass
class TopsisMatrix:
    rows: list[TopsisRow]
