import sys

# Function to compute the matrix chain multiplication and determine the optimal order
def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]  # Minimum scalar multiplications
    s = [[0 for _ in range(n)] for _ in range(n)]  # Split points

    # Fill the m and s tables
    for chain_len in range(2, n + 1):  # Chain length from 2 to n
        for i in range(n - chain_len + 1):
            j = i + chain_len - 1
            m[i][j] = sys.maxsize  # Set initial cost to a very large number
            for k in range(i, j):  # Try different split points
                cost = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < m[i][j]:  # Update if a lower cost is found
                    m[i][j] = cost
                    s[i][j] = k  # Store split point

    return m, s  # Return the m and s tables

# Function to print optimal parenthesization steps
def print_optimal_parens_steps(s, i, j, step=1):
    if i == j:
        return step  # Base case for recursion
    k = s[i][j]  # Get split point
    # First, we handle the left part of the multiplication
    step = print_optimal_parens_steps(s, i, k, step)
    # Now we handle the right part
    step = print_optimal_parens_steps(s, k + 1, j, step)
    # Now we print the current multiplication step
    print(f"Step {step}: Multiply matrices A{i + 1} to A{k + 1} and A{k + 2} to A{j + 1}")
    symbolic_rep = f"({print_optimal_parens(s, i, k)} x {print_optimal_parens(s, k + 1, j)})"
    print(f"Symbolic form: {symbolic_rep}")  # Print symbolic representation
    return step + 1  # Increment step for the next multiplication

# Function to build symbolic representation of the multiplication
def print_optimal_parens(s, i, j):
    if i == j:
        return f"A{i + 1}"  # Base case for recursion
    else:
        k = s[i][j]  # Get split point
        return f"({print_optimal_parens(s, i, k)} x {print_optimal_parens(s, k + 1, j)})"  # Build representation

# Main function to execute the matrix chain multiplication
def matrix_chain_multiplication():
    n = int(input("Enter the number of matrices: "))  # User input for the number of matrices
    
    # Check for valid input for the number of matrices
    if n < 2:
        print("Invalid input! The number of matrices must be at least 2 !")
        return  # Exit the function if input is invalid
    
    p = []  # List to store the dimensions of matrices
    
    for i in range(n):
        # User input for the number of rows for the current matrix
        row = int(input(f"Enter the number of rows for matrix {i + 1}: "))
        # User input for the number of columns for the current matrix
        col = int(input(f"Enter the number of columns for matrix {i + 1}: "))
        
        # Check for positive integers for rows and columns
        if row <= 0 or col <= 0:
            print("Invalid input! Rows and columns must be positive integers !")
            return  # Exit if input is invalid
        
        # Check compatibility for multiplication
        # If this is not the first matrix, check if previous matrix's columns match current matrix's rows
        if i > 0 and p[i - 1][1] != row:  # Corrected comparison to check previous matrix's columns
            print("Invalid input! Number of columns of the previous matrix must match the number of rows of the current matrix !")
            return  # Exit if input is invalid
        
        # Append the dimensions for the current matrix
        p.append((row, col))  # Store both dimensions for reference

    # Prepare the dimension array for chain multiplication
    dimension_array = [p[0][0]] + [col for row, col in p]  # First row dimension + all column dimensions

    # Call the matrix_chain_order function to calculate the minimum multiplications and splits
    m, s = matrix_chain_order(dimension_array)

    # Output the m table (minimum scalar multiplications)
    print("\nm Table (Minimum scalar multiplications):")
    for row in m:
        print(row)

    # Output the s table (split points)
    print("\ns Table (Split points):")
    for row in s:
        print(row)

    # Print optimal parenthesization steps
    print("\nOptimal steps for Matrix Chain Multiplication:")
    print_optimal_parens_steps(s, 0, n - 1)
    print(f"\nTotal number of Scalar Multiplications: {m[0][n - 1]}")  # Total cost of multiplications

# Call the main function to execute the program
matrix_chain_multiplication()

"""
Points to Remember:-

● Time Complexity = O(n) * O(n) * O(n) = O(n³)
    For filling 'm' and 's' table we have one outer for loop and two nested for loop
● Space Complexity = O(n) * O(n) = O(n²)
    Due to the two tables used to store the multiplication costs and split points

● Total number of matrices should be minimum 'two' then only we can perform multiplication
● Columns of first matrix should be equal to rows of second matrix then only multiplication is posssible
● Minimum scalar multiplication value is present in the first row of the last column in 'm' table
"""