# 0/1 Knapsack Problem

## Problem Statement
The 0/1 Knapsack problem is a classic optimization problem. Given a set of items, each with a weight and a value, determine the maximum value that can be obtained by selecting a subset of the items such that the total weight does not exceed a given limit. Each item can either be included in the knapsack or excluded (hence, 0/1).

### Definitions
- **Knapsack Capacity (W)**: The maximum weight that the knapsack can hold.
- **Items**: Each item has a weight (`w[i]`) and a value (`v[i]`).
- **Objective**: Maximize the total value of items in the knapsack without exceeding its capacity.

## Input
- **n**: Number of items.
- **W**: Maximum capacity of the knapsack.
- Two lists:
  - **weights**: An array of integers representing weights of the items.
  - **values**: An array of integers representing values of the items.

## Output
- The maximum value achievable within the weight limit.

## Example
Given:
- `W = 50`
- `weights = [10, 20, 30]`
- `values = [60, 100, 120]`

The maximum value that can be obtained is **220** by selecting items 2 and 3.

## Approach
1. **Dynamic Programming Table (dp)**: Create a 2D table `dp[i][w]` where `i` is the index of items and `w` is the weight limit. `dp[i][w]` stores the maximum value achievable with the first `i` items and weight limit `w`.
2. **Recursive Choice**: For each item `i` and weight `w`:
   - **Exclude the item**: `dp[i][w] = dp[i-1][w]`
   - **Include the item**: `dp[i][w] = dp[i-1][w - weights[i-1]] + values[i-1]`
   - Choose the option with the maximum value that does not exceed the weight `W`.

## Complexity
- **Time Complexity**: O(n * W), where `n` is the number of items and `W` is the knapsack capacity.
- **Space Complexity**: O(n * W) for the DP table.