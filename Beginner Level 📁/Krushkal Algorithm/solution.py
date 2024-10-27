class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}  # Each vertex is its own parent (makes a set for each vertex)
        self.rank = {v: 0 for v in vertices}  # To keep track of the "depth" of trees for efficient union operations
    
    def find_set(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find_set(self.parent[v])  # Path compression
        return self.parent[v]

    def union_set(self, u, v):
        root1 = self.find_set(u)
        root2 = self.find_set(v)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal(graph):
    vertices = list(graph.keys())  # Get a list of all vertices from the graph
    # If we remove "if u < v" condition then edges will be bidirectional means (a,b,6) & (b,a,6) both will appear
    edges = [(u, v, w) for u in graph for v, w in graph[u].items() if u < v]
    # Sort edges based on the given weights
    edges.sort(key = lambda x: x[2])  # x = (u,v,w)

    # Initialize the disjoint set with all vertices
    ds = DisjointSet(vertices)

    # Print the initial sets (only once)
    print("Make sets:", end = " ")
    for v in vertices:
        print(f"{{ {v} }}", end = ", ")
    print()

    # For storing edges of minimum spanning tree
    mst = []
    for u, v, w in edges:
        if ds.find_set(u) != ds.find_set(v):  # Check if u and v belong to different sets
            print(f"Selected edge: ({u}, {v}, {w})")

            # Union operation and print the sets after union
            ds.union_set(u, v)

            # Find and print sets after edge selection
            print("Make sets after selection:", end=" ")
            sets = {}
            for vertex in vertices:
                root = ds.find_set(vertex)   # Find the root of each vertex to know the current set
                if root not in sets:
                    sets[root] = []
                sets[root].append(vertex)  # Group vertices by their root (which set they belong to)
            for root, group in sets.items():
                print(f"{{ {' '.join(sorted(group))} }}", end = ", ")  # Print the current sets after the union operation
            print()

            mst.append((u, v, w))  # Add the selected edge to the MST

    # Return list of selected edges
    return mst

# Function to take user input for the graph
def input_graph():
    # is_directed = input("Is the graph directed? (yes/no): ").lower() == "yes"
    n = int(input("Enter the number of vertices: "))
    m = int(input("Enter the number of edges: "))
    
    graph = {}
    
    print("Enter the edges in the format (u v w), where u and v are vertices, and w is the weight:")
    for _ in range(m):
        u, v, w = input().split()
        w = int(w)  # Convert the weight to an integer
        
        if u not in graph:
            graph[u] = {}   # Initialize an empty dictionary for vertex u if it's not already in the graph
        if v not in graph:
            graph[v] = {}  # Same for vertex v.
        
        # Since it's an undirected graph, we add both u -> v and v -> u
        # For Undirected graph
        graph[u][v] = w
        graph[v][u] = w

        # Add only the directed edge u -> v
        # For Directed graph
        # graph[u][v] = w
    
    return graph

# Take graph input from the user
graph = input_graph()

# Find the MST using Kruskal's algorithm
mst = kruskal(graph)

# Print the final MST
total_cost = 0
print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"({u}, {v}, {w})")
    total_cost += w  # Add the weight of each edge to the total cost

print(f"Total cost of MST: {total_cost}")
"""
graph = {
    'a': {'b': 6, 'c': 4},
    'b': {'a': 6, 'h': 10, 'c': 5, 'e': 14},
    'c': {'a': 4, 'b': 5, 'f': 2, 'd': 9},
    'd': {'c': 9},
    'e': {'b': 14, 'h': 3},
    'f': {'c': 2, 'g': 15, 'h': 8},
    'g': {'f': 15},
    'h': {'b': 10, 'e': 3, 'f': 8}
}

Points to Remember:-

● Time Complexity = O(nlogn) + O(n) = O(nlogn)
    For sorting it takes O(nlogn) where n is the no of items
    For 'for' loop it takes O(n) 

● Space Complexity = O(V) + O(E) = O(V+E)
    For storing edges of mst which would be 'V-1' it takes O(V)
    For sorting edges it requires O(E)

● Both Krushkal's and Prim's algorithm is used only for undirected graph and for non-negative & zero weights.
● Edmonds' algorithm is used to find a minimum spanning tree (MST) in a directed graph.
"""