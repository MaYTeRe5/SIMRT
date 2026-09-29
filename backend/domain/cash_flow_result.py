from dataclasses import dataclass


@dataclass
class CashFlowResult:

    company_id: str

    operating_cash_flow: float

    investing_cash_flow: float

    financing_cash_flow: float

    ending_cash: float
