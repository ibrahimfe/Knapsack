def knapsack_greedy(weights, values, capacity):
    # Initialize a variable to keep track of the total value in the knapsack
    total_value = 0

    # Loop through the items in the input lists
    for i in range(len(weights)):
        # Check if the weight of the current item fits within the remaining capacity
        if weights[i] <= capacity:
            # Add the current item to the knapsack
            total_value += values[i]
            capacity -= weights[i]
        else:
            # If the weight of the current item exceeds the remaining capacity,
            # select the item that maximizes the value-to-weight ratio
            max_ratio = float('inf')
            for j in range(i+1, len(weights)):
                if weights[j] > capacity:
                    break
                ratio = values[j] / weights[j]
                if ratio > max_ratio:
                    max_ratio = ratio
                    total_value += values[j]
                    capacity -= weights[j]

    # Return the total value in the knapsack
    return total_value