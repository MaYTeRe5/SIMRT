from domain.scenario import Scenario
from domain.segment import Segment
from domain.segment_preference import SegmentPreference
from domain.company_state import CompanyState
from domain.decision import Decision
from domain.market_result import MarketResult


class MarketEngine:

    def run(
        self,
        scenario: Scenario,
        segments: list[Segment],
        segment_preferences: list[SegmentPreference],
        company_states: list[CompanyState],
        decisions: list[Decision]
    ) -> list[MarketResult]:

        pass
