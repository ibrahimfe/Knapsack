# Knapsack Problem Solver

This repository contains Python implementations of three algorithms for solving the knapsack problem:

    - Greedy algorithm
    - Dynamic programming algorithm
    - Recursive memoization algorithm

It also includes test cases to validate the output of each algorithm using the unittest library.

## Contributor

- Ibrahim
- Reza Hatta Pratama
- Ryan Rafael

## Problem Description

The knapsack problem is a classic combinatorial optimization problem. It involves choosing a subset of items, each with a weight and a value, to maximize the total value while ensuring that the total weight does not exceed a given capacity.

## Algorithms

### Greedy Algorithm

The greedy algorithm takes items in decreasing order of value-to-weight ratio until the knapsack is full. It's a simple and fast approach, but it doesn't always produce the optimal solution.

### Dynamic Programming Algorithm

The dynamic programming algorithm builds a table of solutions for subproblems and uses it to find the optimal solution for the full problem. It guarantees an optimal solution but has higher computational complexity.

### Recursive Memoization Algorithm

The recursive memoization algorithm uses recursion to explore possible solutions while storing intermediate results to avoid redundant calculations. It's similar to dynamic programming but uses a top-down approach.

## Usage

1. Clone this repository:

```bash
git clone https://github.com/your-username/knapsack-solver.git
```

2. Install the required dependency:

```bash
pip install unittest
```

3. Run the test cases:

```bash
python -m unittest tests.py
```

## Contributing

Feel free to contribute to this repository by:

- Reporting issues
- Suggesting improvements
- Submitting pull requests

## License

This project is licensed under the MIT License. See the LICENSE file for details.
