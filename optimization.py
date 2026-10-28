def knapsack_01(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for current_capacity in range(capacity + 1):
            dp[i][current_capacity] = dp[i - 1][current_capacity]

            if weight <= current_capacity:
                dp[i][current_capacity] = max(
                    dp[i][current_capacity],
                    value + dp[i - 1][current_capacity - weight]
                )

    return dp[n][capacity]

def fractional_knapsack(weights, values, capacity):
    items = sorted(
        zip(weights, values),
        key=lambda item: item[1] / item[0],
        reverse=True
    )

    total_value = 0.0

    for weight, value in items:
        if capacity <= 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value * capacity / weight
            capacity = 0

    return total_value