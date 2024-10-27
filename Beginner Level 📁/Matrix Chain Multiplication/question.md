# Matrix Chain Multiplication

## Problem Statement
The Matrix Chain Multiplication problem involves finding the most efficient way to multiply a given sequence of matrices. The goal is to minimize the total number of scalar multiplications required.

### Definitions
- A **matrix** is defined by its dimensions. For example, a matrix with dimensions `10 x 20` has 10 rows and 20 columns.
- The **cost** of multiplying two matrices is determined by the product of their dimensions.

## Input
- An array `p` of size `n+1`, where `n` is the number of matrices. The dimensions of the matrices are given as pairs in the array:
  - Matrix A1 has dimensions `p[0] x p[1]`
  - Matrix A2 has dimensions `p[1] x p[2]`
  - ...
  - Matrix An has dimensions `p[n-1] x p[n]`

## Output
- The minimum number of scalar multiplications needed to multiply the matrices together and the optimal order of multiplication.

## Example
Given an array `p = [10, 20, 30, 40, 30]`:
- The matrices are:
  - A1: `10 x 20`
  - A2: `20 x 30`
  - A3: `30 x 40`
  - A4: `40 x 30`

The minimum number of multiplications required to multiply these matrices is **30000**.

## Optimal Order of Multiplication
The optimal order to multiply the matrices can be derived using a table of split points during the dynamic programming approach. For the given example, the optimal multiplication order is:
- `(A1 * (A2 * (A3 * A4)))` or equivalently `A1 * A2 * A3 * A4`.

## Approach
1. **Dynamic Programming**: The solution uses dynamic programming to solve the problem by breaking it down into simpler subproblems.
2. **Matrix Dimensions**: Calculate the cost of multiplying different chains of matrices.
3. **Optimal Parenthesization**: Determine the best way to parenthesize the matrices to achieve the minimum multiplication cost.

## Complexity
- **Time Complexity**: O(n³) due to three nested loops.
- **Space Complexity**: O(n²) for storing intermediate results.