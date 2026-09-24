from domain.decision import Decision
from domain.state_update_result import StateUpdateResult


class StateUpdateEngine:

    def calculate_weighted_effect(
        self,
        investments: list[float]
    ) -> float:
        """
        investments sıralaması:
        [Y1, Y2, Y3, ... Yn]

        En son eleman güncel yıl yatırımıdır.
        """

        effect = 0.0

        reversed_investments = list(reversed(investments))

        for age, investment in enumerate(reversed_investments, start=1):
            effect += investment / age

        return effect

    def calculate_brand_score(
        self,
        marketing_history: list[float]
    ) -> float:

        return self.calculate_weighted_effect(
            marketing_history
        )

    def calculate_innovation_score(
        self,
        product_rd_history: list[float]
    ) -> float:

        return self.calculate_weighted_effect(
            product_rd_history
        )

    def calculate_efficiency_score(
        self,
        process_rd_history: list[float]
    ) -> float:

        return self.calculate_weighted_effect(
            process_rd_history
        )

    def run(
        self,
        company_id: str,
        year_no: int,
        marketing_history: list[float],
        product_rd_history: list[float],
        process_rd_history: list[float]
    ) -> StateUpdateResult:

        brand_score = self.calculate_brand_score(
            marketing_history
        )

        innovation_score = self.calculate_innovation_score(
            product_rd_history
        )

        efficiency_score = self.calculate_efficiency_score(
            process_rd_history
        )

        return StateUpdateResult(
            company_id=company_id,
            year_no=year_no,
            brand_score=brand_score,
            innovation_score=innovation_score,
            efficiency_score=efficiency_score
        )
