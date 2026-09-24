from domain.company_state import CompanyState
from domain.decision import Decision
from domain.topsis_row import TopsisRow


class TopsisRowBuilder:

    def build(
        self,
        company_state: CompanyState,
        decision: Decision
    ) -> TopsisRow:

        return TopsisRow(
            company_id=company_state.company_id,

            price=decision.price,

            brand_score=company_state.brand_score,

            innovation_score=company_state.innovation_score,

            credit_terms=decision.ar_days
        )
