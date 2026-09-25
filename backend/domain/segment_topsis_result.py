from dataclasses import dataclass


@dataclass
class SegmentTopsisResult:
    company_id: str

    segment_name: str

    topsis_score: float
