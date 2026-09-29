from domain.algorithm_result import (
    AlgorithmResult
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
