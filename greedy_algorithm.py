def knapsack_greedy(weights, values, capacity):
    n = len(weights)
    ratios = [(values[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    current_weight = 0

    for ratio, index in ratios:
        if current_weight + weights[index] <= capacity:
            total_value += values[index]
            current_weight += weights[index]

    return total_value