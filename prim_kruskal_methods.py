import numpy as np

class Weighted_Graph:
    # Constructor initializes number of nodes and adj_matrix elements.
    def __init__(self, number_of_nodes: (int)):
        self.num_of_nodes = number_of_nodes
        self.adjMatrix = []

        for i in range(number_of_nodes):
            self.adjMatrix.append([0 for i in range(number_of_nodes)])

    # Add edges
    def add_edge(self, v1, v2, weight = 1):
        if(v1 == v2):
            # Same pair of nodes may not have an edge.
            pass

        # back and forth edges.
        self.adjMatrix[v1][v2] = weight
        self.adjMatrix[v2][v1] = weight

    # Remove edges
    def remove_edge(self, v1, v2):
        if(self.adjMatrix[v1][v2] == 0):
            print("No edge present between the two nodes.")
            return

        # remove back and forth edges.
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.num_of_nodes

    # Print the matrix
    def print_matrix(self):
        print("Adjacency Matrix : ")
        print(np.array(self.adjMatrix))


'''
A minimum spanning tree is a subset of the edges of a connected, 
edge-weighted undirected graph that connects all nodes together, 
without any cycles and with the minimum possible total edge weight.
'''
# Prim's method for MST.
def prim_mst(adjMatrix: list):
    # Initialize the MST
    MST = []
    # Initialize the visited list
    visited = [False for i in range(len(adjMatrix))]
    # Initialize the distance list
    distance = [float("inf") for i in range(len(adjMatrix))]
    # Initialize the parent list
    parent = [None for i in range(len(adjMatrix))]

    # Initialize the starting node
    visited[0] = True
    distance[0] = 0

    # Initialize the priority queue
    pq = []
    for i in range(len(adjMatrix)):
        pq.append((distance[i], i))

    # Sort the priority queue
    pq.sort()

    # Initialize the MST
    MST.append(pq[0][1])

    # While the MST is not complete
    while len(MST) != len(adjMatrix):
        # Get the minimum distance node
        min_node = pq[0][1]
        # Remove the node from the priority queue
        pq.pop(0)

        # Add the node to the MST
        MST.append(min_node)

        # Update the visited list
        visited[min_node] = True

        # Update the distance list
        for i in range(len(adjMatrix)):
            if adjMatrix[min_node][i] != 0 and visited[i] == False:
                if adjMatrix[min_node][i] < distance[i]:
                    distance[i] = adjMatrix[min_node][i]
                    parent[i] = min_node
                    pq.append((distance[i], i))
                    pq.sort()

    return MST, distance


# Kruskal's method for MST.
def kruskal_mst(adjMatrix: list):
    # Initialize the MST
    MST = []
    # Initialize the visited list
    visited = [False for i in range(len(adjMatrix))]
    # Initialize lower inf value
    distance = [float("inf") for i in range(len(adjMatrix))]
    # Initialize the parent list
    parent = [None for i in range(len(adjMatrix))]

    # Initialize the priority queue
    pq = []
    for i in range(len(adjMatrix)):
        pq.append((distance[i], i))

    # Sort the priority queue
    pq.sort()

    # Initialize the MST
    MST.append(pq[0][1])

    # While the MST is not complete
    while len(MST) != len(adjMatrix):
        # Get the minimum distance node
        min_node = pq[0][1]
        # Remove the node from the priority queue
        pq.pop(0)

        # Add the node to the MST
        MST.append(min_node)

        # Update the visited list
        visited[min_node] = True

        # Update the distance list
        for i in range(len(adjMatrix)):
            if adjMatrix[min_node][i] != 0 and visited[i] == False:
                if adjMatrix[min_node][i] < distance[i]:
                    distance[i] = adjMatrix[min_node][i]
                    parent[i] = min_node
                    pq.append((distance[i], i))
                    pq.sort()

    return MST, distance