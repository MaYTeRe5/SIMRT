from domain.treasury_result import TreasuryResult


class TreasuryEngine:

    def solve_liquidity(
        self,
        company_id: str,
        cash_before_treasury: float,
        minimum_cash_requirement: float,
        loan_interest_rate: float,
        deposit_interest_rate: float,
        tolerance: float = 0.01,
        maximum_iterations: int = 100
    ) -> TreasuryResult:

        self._validate_inputs(
            minimum_cash_requirement,
            loan_interest_rate,
            deposit_interest_rate,
            tolerance,
            maximum_iterations
        )

        borrowing = 0.0
        deposit = 0.0

        interest_expense = 0.0
        interest_income = 0.0

        ending_cash = cash_before_treasury
        converged = False
        iteration_count = 0

        for iteration_count in range(
            1,
            maximum_iterations + 1
        ):
            interest_expense = (
                borrowing
                * loan_interest_rate
            )

            interest_income = (
                deposit
                * deposit_interest_rate
            )

            ending_cash = (
                cash_before_treasury
                + borrowing
                - deposit
                + interest_income
                - interest_expense
            )

            cash_difference = (
                ending_cash
                - minimum_cash_requirement
            )

            if abs(cash_difference) <= tolerance:
                converged = True
                break

            if cash_difference < 0:
                required_cash = abs(
                    cash_difference
                )

                borrowing += required_cash
                deposit = 0.0

            else:
                excess_cash = cash_difference

                deposit += excess_cash
                borrowing = 0.0

        interest_expense = (
            borrowing
            * loan_interest_rate
        )

        interest_income = (
            deposit
            * deposit_interest_rate
        )

        ending_cash = (
            cash_before_treasury
            + borrowing
            - deposit
            + interest_income
            - interest_expense
        )

        return TreasuryResult(
            company_id=company_id,

            cash_before_treasury=cash_before_treasury,
            minimum_cash_requirement=(
                minimum_cash_requirement
            ),

            borrowing=borrowing,
            deposit=deposit,

            interest_expense=interest_expense,
            interest_income=interest_income,

            ending_cash=ending_cash,

            iteration_count=iteration_count,
            converged=converged
        )

    def _validate_inputs(
        self,
        minimum_cash_requirement: float,
        loan_interest_rate: float,
        deposit_interest_rate: float,
        tolerance: float,
        maximum_iterations: int
    ) -> None:

        if minimum_cash_requirement < 0:
            raise ValueError(
                "Minimum cash requirement cannot be negative."
            )

        if not 0 <= loan_interest_rate < 1:
            raise ValueError(
                "Loan interest rate must be between "
                "0 and 1."
            )

        if not 0 <= deposit_interest_rate < 1:
            raise ValueError(
                "Deposit interest rate must be between "
                "0 and 1."
            )

        if tolerance <= 0:
            raise ValueError(
                "Tolerance must be greater than zero."
            )

        if maximum_iterations <= 0:
            raise ValueError(
                "Maximum iterations must be greater "
            )
                
