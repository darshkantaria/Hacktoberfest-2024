# Kruskal's Algorithm for Minimum Spanning Tree (MST)

## Problem Statement
Kruskal's algorithm is a **greedy algorithm** used to find the **Minimum Spanning Tree (MST)** of a connected, undirected graph. The MST is a subset of edges that connects all vertices with the minimum possible total edge weight and no cycles.

### Definitions
- **Graph**: Consists of vertices and weighted edges.
- **Minimum Spanning Tree (MST)**: A subset of edges that connects all vertices with minimum total edge weight.
- **Objective**: Find the MST for the graph.

## Input
- **V**: Number of vertices in the graph.
- **E**: List of edges, where each edge includes two vertices and a weight `(u, v, w)`.

## Output
- A list of edges that form the MST and the total minimum weight.

## Example
Given:
- Vertices: `V = {A, B, C, D}`
- Edges: `[(A, B, 1), (B, C, 2), (C, D, 3), (A, D, 4)]`

The MST would include edges `(A, B)`, `(B, C)`, and `(C, D)` with a total weight of **6**.

## Approach
1. **Sort the Edges**: Sort all edges in ascending order of their weights.
2. **Union-Find Structure**: Use the Union-Find data structure to detect cycles and help connect components.
3. **Add Edges Greedily**: Add edges to the MST in sorted order, skipping any that form a cycle.
4. **Stop Condition**: Stop once there are `V-1` edges in the MST.

### Steps:
1. Sort edges by weight.
2. Initialize MST as an empty set.
3. For each edge in sorted edges:
   - If adding the edge doesn’t form a cycle, add it to the MST.
4. Output the MST and its total weight.

## Complexity
- **Time Complexity**: \(O(E \log E + E \log V)\), where \(E\) is the number of edges and \(V\) is the number of vertices.
- **Space Complexity**: \(O(V)\) for storing subsets in Union-Find.