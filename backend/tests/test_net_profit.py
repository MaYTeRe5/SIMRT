from engines.algorithm_engine import (
    AlgorithmEngine
)


engine = AlgorithmEngine()

profit_before_tax = (
    engine.calculate_profit_before_tax(
        ebit=4960000,
        interest_income=100000,
        interest_expense=250000
    )
)

tax_expense = (
    engine.calculate_tax_expense(
        profit_before_tax,
        tax_rate=0
    )
)

net_profit = (
    engine.calculate_net_profit(
        profit_before_tax,
        tax_expense
    )
)

print("Profit Before Tax")
print(profit_before_tax)

print()

print("Tax Expense")
print(tax_expense)

print()

print("Net Profit")
print(net_profit)
