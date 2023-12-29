from dynamic_programming import dynamic_knapsack
from greedy_algorithm import knapsack_greedy
from recursive_memoization import knapsack_recursive_memoization

import unittest


class TestKnapsackGreedy(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(knapsack_greedy([], [], 10), 0, "Expected 0")
        self.assertEqual(dynamic_knapsack([], [], 10), 0, "Expected 0")
        self.assertEqual(knapsack_recursive_memoization([], [], 10), 0, "Expected 0")

    def test_single_item(self):
        self.assertEqual(knapsack_greedy([1], [1], 10), 1, "Expected 1")
        self.assertEqual(dynamic_knapsack([1], [1], 10), 1, "Expected 1")
        self.assertEqual(knapsack_recursive_memoization([1], [1], 10), 1, "Expected 1")

    def test_two_items(self):
        self.assertEqual(knapsack_greedy([1, 2], [1, 2], 10), 3, "Expected 3")
        self.assertEqual(dynamic_knapsack([1, 2], [1, 2], 10), 3, "Expected 3")
        self.assertEqual(
            knapsack_recursive_memoization([1, 2], [1, 2], 10), 3, "Expected 3"
        )

    def test_three_items(self):
        self.assertEqual(knapsack_greedy([1, 2, 3], [1, 2, 3], 10), 6, "Expected 6")
        self.assertEqual(dynamic_knapsack([1, 2, 3], [1, 2, 3], 10), 6, "Expected 6")
        self.assertEqual(
            knapsack_recursive_memoization([1, 2, 3], [1, 2, 3], 10), 6, "Expected 6"
        )

    def test_four_items(self):
        self.assertEqual(
            knapsack_greedy([1, 2, 3, 4], [1, 2, 3, 4], 10), 10, "Expected 10"
        )
        self.assertEqual(
            dynamic_knapsack([1, 2, 3, 4], [1, 2, 3, 4], 10), 10, "Expected 10"
        )
        self.assertEqual(
            knapsack_recursive_memoization([1, 2, 3, 4], [1, 2, 3, 4], 10),
            10,
            "Expected 10",
        )

    def test_capacity_exceeded(self):
        self.assertEqual(
            knapsack_greedy([1, 2, 3, 4], [1, 2, 3, 4], 5), 3, "Expected 3"
        )
        self.assertEqual(
            dynamic_knapsack([1, 2, 3, 4], [1, 2, 3, 4], 5), 5, "Expected 5"
        )
        self.assertEqual(
            knapsack_recursive_memoization([1, 2, 3, 4], [1, 2, 3, 4], 5),
            5,
            "Expected 5",
        )

    def test_random_inputs(self):
        weights = [3, 2, 1, 4]
        values = [10, 5, 2, 8]
        capacity = 6
        expected_result = 17
        actual_result_greedy = knapsack_greedy(weights, values, capacity)
        actual_result_dynamic = dynamic_knapsack(weights, values, capacity)
        actual_result_recurive = knapsack_recursive_memoization(
            weights, values, capacity
        )
        self.assertEqual(actual_result_greedy, expected_result, "Expected 17")
        self.assertEqual(actual_result_dynamic, expected_result, "Expected 17")
        self.assertEqual(actual_result_recurive, expected_result, "Expected 17")

    def test_challenging_case(self):
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        capacity = 10
        expected_result = 34

        self.assertEqual(
            knapsack_greedy(weights, values, capacity), expected_result, "Expected 34"
        )
        self.assertEqual(
            dynamic_knapsack(weights, values, capacity), expected_result, "Expected 34"
        )
        self.assertEqual(
            knapsack_recursive_memoization(weights, values, capacity),
            expected_result,
            "Expected 34",
        )


if __name__ == "__main__":
    unittest.main()
