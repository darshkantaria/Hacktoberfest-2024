def knapsack_0_1(weights, values, n, capacity):
    # Create a DP table where dp[i][w] will store the maximum value that can be obtained
    # with the first i items and capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + values[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    # Maximum profit will be in dp[n][capacity]
    max_profit = dp[n][capacity]

    # Display the dynamic table in i/w format
    print(" ")
    print("Dynamic Programming Table:")
    print(" ")
    
    # Print column headers (w values)
    print("i/w", end="    ")  # Header for i/w
    for w in range(capacity + 1):
        print(f"{w:2}", end="   ")  # 2 spaces for each capacity column
    print()  # Newline after headers

    # Print row headers (i values) and DP table contents
    for i in range(n + 1):
        print(f"{i:2}", end="     ")  # Row header for item i with extra space for alignment
        for w in range(capacity + 1):
            print(f"{dp[i][w]:2}", end="   ")  # DP table value with 2 spaces
        print()  # Newline after each row
    
    # Find which items are included in the knapsack
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:  # Item i is included
            selected_items.append(i)
            w -= weights[i-1]

    # Print the optimal path in reverse (row, column)
    print("\nOptimal Path (Row, Column):")
    for i in selected_items:
        print(f"Item {i} selected at Row: {i}, Column: {capacity - w}")
        w += weights[i-1]

    # Print the maximum profit
    print(f"\nMaximum Profit: {max_profit}")
    
    # Print the selected items
    print("\nItems included in the Knapsack:")
    selected_items.reverse()  # Reversing to show the correct order of selected items
    for item in selected_items:
        print(f"Item {item} with weight {weights[item-1]} and value {values[item-1]}")

# Taking input from the user one by one
n = int(input("Enter the number of items: "))
if n <= 0:
    print("Error: The number of items must be greater than zero !")
else:
    weights = []
    values = []

    # Input for weights and values one by one
    print("Enter the weights of the items:")
    for i in range(n):
        weight = int(input(f"Weight of item {i + 1}: "))
        if weight <= 0:
            print("Error: Weight must be greater than zero !")
            break  # Exit if invalid input
        weights.append(weight)

    else:  # This else will run if the loop completes without a break
        print("Enter the values of the items:")
        for i in range(n):
            value = int(input(f"Value of item {i + 1}: "))
            # Allow zero value
            values.append(value)

        capacity = int(input("Enter the capacity of the knapsack: "))
        if capacity <= 0:
            print("Error: Capacity must be greater than zero !")
        else:
            # Call the function with user input
            knapsack_0_1(weights, values, n, capacity)

"""
Points to Remember:-

● Time Complexity = O(N X W) + O(N) = O(N X W)
    For nested loops, the outer loop iterates over the items from (1 to N) and the inner loop iterates over the capacities from (1 to W) = O(N X W)
    For backtracking loop runs from (N to 1) = O(N)
● Space Complexity = O(N X W) + O(N) = O(N X W)
    For DP table of dimensions (N + 1) X (W + 1) = O(N X W)
    For storing selected items in list = O(N)

● 0/1 Knapsack works better with dynamic approach and will always give optimal solution for it
● You can peak or leave the item but cannot break the items
"""