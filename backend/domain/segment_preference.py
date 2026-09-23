@dataclass
class SegmentPreference:
    segment_id: str

    weight_price: float
    weight_brand: float
    weight_innovation: float
    weight_credit_terms: float
