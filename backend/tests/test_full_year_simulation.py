from domain.company_total_demand import CompanyTotalDemand
from domain.company_available_supply import CompanyAvailableSupply
from domain.company_redistribution_score import CompanyRedistributionScore
from domain.kpi_result import KPIResult

from engines.demand_redistribution_engine import DemandRedistributionEngine
from engines.algorithm_engine import AlgorithmEngine
from engines.kpi_engine import KPIEngine
from engines.ranking_engine import RankingEngine


# Phase 1 full-year integration test.
# This test connects the currently verified redistribution, algorithm,
# financial calculation, KPI, and ranking layers.
# State Update and Market Engine inputs are represented here by their
# already calculated yearly outputs and will be connected to the
# SimulationYearRunner in the next integration step.


def build_company_financials(
    algorithm_engine,
    company_id,
    sales_units,
    price,
    beginning_inventory_units,
    beginning_inventory_value,
    production_units,
    production_cost,
    marketing_fixed_cost,
    marketing_variable_cost,
    product_rd_fixed_cost,
    product_rd_variable_cost,
    general_management_fixed_cost,
    general_management_variable_cost,
    depreciation,
    interest_income,
    interest_expense,
    tax_rate
):
    weighted_average_cost = (
        algorithm_engine.calculate_weighted_average_cost(
            beginning_inventory_units=beginning_inventory_units,
            beginning_inventory_value=beginning_inventory_value,
            production_units=production_units,
            production_cost=production_cost
        )
    )

    available_product = (
        beginning_inventory_units
        + production_units
    )

    ending_inventory_units = max(
        available_product - sales_units,
        0
    )

    revenue = sales_units * price

    cogs = algorithm_engine.calculate_cogs(
        sales_units=sales_units,
        weighted_average_cost=weighted_average_cost
    )

    ending_inventory_value = (
        algorithm_engine.calculate_inventory_value(
            ending_inventory_units=ending_inventory_units,
            weighted_average_cost=weighted_average_cost
        )
    )

    gross_profit = revenue - cogs

    operating_expense = (
        algorithm_engine.calculate_operating_expense(
            marketing_fixed_cost=marketing_fixed_cost,
            marketing_variable_cost=marketing_variable_cost,
            product_rd_fixed_cost=product_rd_fixed_cost,
            product_rd_variable_cost=product_rd_variable_cost,
            general_management_fixed_cost=(
                general_management_fixed_cost
            ),
            general_management_variable_cost=(
                general_management_variable_cost
            )
        )
    )

    total_operating_expense = operating_expense[
        "total_operating_expense"
    ]

    ebitda = algorithm_engine.calculate_ebitda(
        gross_profit=gross_profit,
        operating_expense=total_operating_expense
    )

    financial_result = (
        algorithm_engine.build_financial_result(
            company_id=company_id,
            revenue=revenue,
            cogs=cogs,
            gross_profit=gross_profit,
            operating_expense=total_operating_expense,
            ebitda=ebitda,
            depreciation=depreciation,
            interest_income=interest_income,
            interest_expense=interest_expense,
            tax_rate=tax_rate
        )
    )

    return {
        "weighted_average_cost": weighted_average_cost,
        "ending_inventory_units": ending_inventory_units,
        "ending_inventory_value": ending_inventory_value,
        "financial_result": financial_result
    }


def main():
    redistribution_engine = DemandRedistributionEngine()
    algorithm_engine = AlgorithmEngine()
    kpi_engine = KPIEngine()
    ranking_engine = RankingEngine()

    demands = [
        CompanyTotalDemand(
            company_id="A",
            value_demand=120000,
            balanced_demand=100000,
            premium_demand=80000,
            total_demand=300000
        ),
        CompanyTotalDemand(
            company_id="B",
            value_demand=70000,
            balanced_demand=60000,
            premium_demand=30000,
            total_demand=160000
        ),
        CompanyTotalDemand(
            company_id="C",
            value_demand=40000,
            balanced_demand=30000,
            premium_demand=20000,
            total_demand=90000
        )
    ]

    supplies = [
        CompanyAvailableSupply(
            company_id="A",
            available_units=180000
        ),
        CompanyAvailableSupply(
            company_id="B",
            available_units=180000
        ),
        CompanyAvailableSupply(
            company_id="C",
            available_units=190000
        )
    ]

    redistribution_scores = [
        CompanyRedistributionScore(
            company_id="A",
            redistribution_score=2.20
        ),
        CompanyRedistributionScore(
            company_id="B",
            redistribution_score=1.90
        ),
        CompanyRedistributionScore(
            company_id="C",
            redistribution_score=1.60
        )
    ]

    redistribution_result = (
        redistribution_engine.run_redistribution(
            demands=demands,
            supplies=supplies,
            redistribution_scores=redistribution_scores,
            maximum_rounds=2
        )
    )

    final_sales_by_company = {
        result.company_id: result.sales_units
        for result in redistribution_result[
            "final_company_results"
        ]
    }

    assert final_sales_by_company == {
        "A": 180000,
        "B": 180000,
        "C": 190000
    }

    assert redistribution_result["lost_demand"] == 0

    company_inputs = {
        "A": {
            "price": 100,
            "beginning_inventory_units": 20000,
            "beginning_inventory_value": 1000000,
            "production_units": 160000,
            "production_cost": 9600000,
            "marketing_variable_cost": 1000000,
            "product_rd_variable_cost": 500000,
            "depreciation": 300000,
            "interest_income": 0,
            "interest_expense": 250000,
            "equity": 20100000,
            "debt": 3000000,
            "total_assets": 24300000,
            "market_share": 180000 / 550000
        },
        "B": {
            "price": 110,
            "beginning_inventory_units": 20000,
            "beginning_inventory_value": 1000000,
            "production_units": 160000,
            "production_cost": 9200000,
            "marketing_variable_cost": 800000,
            "product_rd_variable_cost": 400000,
            "depreciation": 300000,
            "interest_income": 0,
            "interest_expense": 200000,
            "equity": 19000000,
            "debt": 3500000,
            "total_assets": 23500000,
            "market_share": 180000 / 550000
        },
        "C": {
            "price": 120,
            "beginning_inventory_units": 30000,
            "beginning_inventory_value": 1500000,
            "production_units": 160000,
            "production_cost": 8800000,
            "marketing_variable_cost": 1200000,
            "product_rd_variable_cost": 600000,
            "depreciation": 300000,
            "interest_income": 100000,
            "interest_expense": 100000,
            "equity": 22000000,
            "debt": 2000000,
            "total_assets": 25000000,
            "market_share": 190000 / 550000
        }
    }

    financials_by_company = {}
    kpi_results = []

    for company_id, company_input in company_inputs.items():
        financials = build_company_financials(
            algorithm_engine=algorithm_engine,
            company_id=company_id,
            sales_units=final_sales_by_company[company_id],
            price=company_input["price"],
            beginning_inventory_units=(
                company_input["beginning_inventory_units"]
            ),
            beginning_inventory_value=(
                company_input["beginning_inventory_value"]
            ),
            production_units=company_input["production_units"],
            production_cost=company_input["production_cost"],
            marketing_fixed_cost=150000,
            marketing_variable_cost=(
                company_input["marketing_variable_cost"]
            ),
            product_rd_fixed_cost=90000,
            product_rd_variable_cost=(
                company_input["product_rd_variable_cost"]
            ),
            general_management_fixed_cost=200000,
            general_management_variable_cost=0,
            depreciation=company_input["depreciation"],
            interest_income=company_input["interest_income"],
            interest_expense=company_input["interest_expense"],
            tax_rate=0
        )

        financials_by_company[company_id] = financials

        beginning_inventory_value = (
            company_input["beginning_inventory_value"]
        )
        ending_inventory_value = financials[
            "ending_inventory_value"
        ]
        average_inventory = (
            beginning_inventory_value
            + ending_inventory_value
        ) / 2

        if average_inventory == 0:
            average_inventory = 1

        financial_result = financials[
            "financial_result"
        ]

        kpi_results.append(
            kpi_engine.build_kpi_result(
                company_id=company_id,
                market_share=company_input["market_share"],
                ebitda=financial_result.ebitda,
                net_profit=financial_result.net_profit,
                equity=company_input["equity"],
                debt=company_input["debt"],
                total_assets=company_input["total_assets"],
                average_inventory=average_inventory,
                cogs=financial_result.cogs
            )
        )

    ranking_weights = {
        "market_share": 20,
        "ebitda": 20,
        "roe": 20,
        "debt_asset_ratio": 20,
        "inventory_turn": 20
    }

    ranking_results = ranking_engine.rank(
        kpi_results=kpi_results,
        weights=ranking_weights
    )

    assert len(ranking_results) == 3
    assert sorted(result.rank for result in ranking_results) == [1, 2, 3]
    assert ranking_results[0].ranking_score >= (
        ranking_results[1].ranking_score
    )
    assert ranking_results[1].ranking_score >= (
        ranking_results[2].ranking_score
    )

    print("Final Sales")
    for company_id, sales_units in final_sales_by_company.items():
        print(company_id, sales_units)

    print()
    print("Financial Results")
    for company_id, financials in financials_by_company.items():
        print(company_id, financials["financial_result"])

    print()
    print("KPI Results")
    for kpi_result in kpi_results:
        print(kpi_result)

    print()
    print("Ranking Results")
    for ranking_result in ranking_results:
        print(ranking_result)

    print()
    print("Full year integration test passed.")


if __name__ == "__main__":
    main()
