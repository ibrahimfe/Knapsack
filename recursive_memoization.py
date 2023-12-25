def knapsack_recursive_memoization(weights, values, capacity):
    n = len(weights)
    memo = {}

    def recursive_helper(index, capacity_left):
        if index < 0 or capacity_left <= 0:
            return 0

        if (index, capacity_left) in memo:
            return memo[(index, capacity_left)]

        if weights[index] > capacity_left:
            memo[(index, capacity_left)] = recursive_helper(index - 1, capacity_left)
            return memo[(index, capacity_left)]

        included = values[index] + recursive_helper(index - 1, capacity_left - weights[index])
        excluded = recursive_helper(index - 1, capacity_left)
        memo[(index, capacity_left)] = max(included, excluded)
        return memo[(index, capacity_left)]

    max_value = recursive_helper(n - 1, capacity)
    return max_value