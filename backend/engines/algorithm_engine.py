from domain.algorithm_result import (
    AlgorithmResult
)

from domain.financial_result import (
    FinancialResult
)

from domain.balance_sheet_result import (
    BalanceSheetResult
)


class AlgorithmEngine:

    def calculate_weighted_average_cost(
        self,
        beginning_inventory_units: int,
        beginning_inventory_value: float,
        production_units: int,
        production_cost: float
    ) -> float:

        total_units = (
            beginning_inventory_units
            + production_units
        )

        if total_units == 0:
            return 0.0

        total_cost = (
            beginning_inventory_value
            + production_cost
        )

        return (
            total_cost
            / total_units
        )

    def calculate_operating_result(
        self,
        company_id: str,
        final_demand: int,
        available_product: int,
        price: float,
        unit_cost: float,
        ending_capacity: int
    ) -> AlgorithmResult:

        sales_units = min(
            final_demand,
            available_product
        )

        ending_inventory = (
            available_product
            - sales_units
        )

        revenue = (
            sales_units
            * price
        )

        cogs = (
            sales_units
            * unit_cost
        )

        gross_profit = (
            revenue
            - cogs
        )

        return AlgorithmResult(
            company_id=company_id,
            sales_units=sales_units,
            ending_inventory=ending_inventory,
            ending_capacity=ending_capacity,
            unit_cost=unit_cost,
            revenue=revenue,
            cogs=cogs,
            gross_profit=gross_profit
        )

    def calculate_cogs(
           self,
           sales_units: int,
            weighted_average_cost: float
       ) -> float:

           return (
               sales_units
               * weighted_average_cost
           )

    def calculate_inventory_value(
           self,
           ending_inventory_units: int,
           weighted_average_cost: float
       ) -> float:
            return (
               ending_inventory_units
               * weighted_average_cost
           )
    def calculate_depreciation(
        self,
        asset_value: float,
        useful_life: int
    ) -> float:

        if useful_life == 0:
            return 0.0

        return (
            asset_value
            / useful_life
        )

    def calculate_operating_expense(
        self,
        marketing_fixed_cost: float,
        marketing_variable_cost: float,

        product_rd_fixed_cost: float,
        product_rd_variable_cost: float,

        general_management_fixed_cost: float,
        general_management_variable_cost: float
    ):

        marketing_total_cost = (
            marketing_fixed_cost
            + marketing_variable_cost
        )

        product_rd_total_cost = (
            product_rd_fixed_cost
            + product_rd_variable_cost
        )

        general_management_total_cost = (
            general_management_fixed_cost
            + general_management_variable_cost
        )

        total_operating_expense = (
            marketing_total_cost
            + product_rd_total_cost
            + general_management_total_cost
        )

        return {
            "marketing_total_cost":
                marketing_total_cost,

            "product_rd_total_cost":
                product_rd_total_cost,

            "general_management_total_cost":
                general_management_total_cost,

            "total_operating_expense":
                total_operating_expense
        }

    def calculate_ebitda(
        self,
        gross_profit: float,
        operating_expense: float
    ) -> float:

        return (
            gross_profit
            - operating_expense
        )

    def calculate_ebit(
        self,
        ebitda: float,
        depreciation: float
    ) -> float:

        return (
            ebitda
            - depreciation
        )

    def calculate_profit_before_tax(
        self,
        ebit: float,
        interest_income: float,
        interest_expense: float
    ) -> float:

        return (
            ebit
            + interest_income
            - interest_expense
        )

    def calculate_tax_expense(
        self,
        profit_before_tax: float,
        tax_rate: float
    ) -> float:

        if profit_before_tax <= 0:
            return 0.0

        return (
            profit_before_tax
            * tax_rate
        )

    def calculate_net_profit(
        self,
        profit_before_tax: float,
        tax_expense: float
    ) -> float:

        return (
            profit_before_tax
            - tax_expense
        )

    def calculate_required_borrowing(
        self,
        ending_cash: float,
        minimum_cash: float
    ) -> float:

        if ending_cash >= minimum_cash:
            return 0.0

        return (
            minimum_cash
            - ending_cash
        )

    def build_financial_result(
        self,

        company_id: str,

        revenue: float,

        cogs: float,

        gross_profit: float,

        operating_expense: float,

        ebitda: float,

        depreciation: float,

        interest_income: float,

        interest_expense: float,

        tax_rate: float
    ) -> FinancialResult:

        ebit = self.calculate_ebit(
            ebitda,
            depreciation
        )

        profit_before_tax = (
            self.calculate_profit_before_tax(
                ebit,
                interest_income,
                interest_expense
            )
        )

        tax_expense = (
            self.calculate_tax_expense(
                profit_before_tax,
                tax_rate
            )
        )

        net_profit = (
            self.calculate_net_profit(
                profit_before_tax,
                tax_expense
            )
        )

        return FinancialResult(
            company_id=company_id,

            revenue=revenue,

            cogs=cogs,

            gross_profit=gross_profit,

            operating_expense=operating_expense,

            ebitda=ebitda,

            depreciation=depreciation,

            ebit=ebit,

            interest_income=interest_income,

            interest_expense=interest_expense,

            profit_before_tax=profit_before_tax,

            tax_expense=tax_expense,

            net_profit=net_profit
        )

    def calculate_ending_equity(
        self,
        previous_equity: float,
        net_profit: float,
        dividend: float = 0
    ) -> float:

        return (
            previous_equity
            + net_profit
            - dividend
        )

    def build_balance_sheet_result(
        self,
        company_id: str,

        cash: float,
        receivables: float,
        inventory_value: float,
        fixed_assets: float,

        payables: float,
        debt: float,
        equity: float
    ) -> BalanceSheetResult:

        total_assets = (
            cash
            + receivables
            + inventory_value
            + fixed_assets
        )

        total_liabilities = (
            payables
            + debt
        )

        return BalanceSheetResult(
            company_id=company_id,

            cash=cash,
            receivables=receivables,
            inventory_value=inventory_value,
            fixed_assets=fixed_assets,

            total_assets=total_assets,

            payables=payables,
            debt=debt,

            total_liabilities=total_liabilities,

            equity=equity
        )

    def calculate_operating_cash_flow(
        self,
        net_profit: float,
        depreciation: float
    ) -> float:

        return (
            net_profit
            + depreciation
        )
