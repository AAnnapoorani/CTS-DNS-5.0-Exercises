def future_value(amount, rate, years):

    if years == 0:
        return amount

    return future_value(amount * (1 + rate), rate, years - 1)


principal = 10000
growth_rate = 0.10
years = 5

result = future_value(principal, growth_rate, years)

print("Future Value =", round(result, 2))