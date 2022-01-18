import sys
import numpy 
numpy.set_printoptions(threshold = sys.maxsize)                                                       # disable array truncation in console.
from itertools import chain
import random
import time
import networkx as nx
import matplotlib.pyplot as plt
from prim_kruskal_methods import Weighted_Graph
from prim_kruskal_methods import prim_mst
from prim_kruskal_methods import kruskal_mst

print("\t\t\t\t\t Simulation Of Algorithms By Prim And Kruskal To Create MSTs \t\t\t\t\t", "\n\n\n")
print("Create An Adjacency Matrix Representation Of A Custom Made Weighted Graph !")
__num_of_nodes = int(input("Enter the number of nodes you wish to have in the weighted graph = "))

# Set available nodes for the weighted graph[nodes range from 1 to __num_of_nodes specified].
src_s_nodes = random.sample(range(1, __num_of_nodes + 1), __num_of_nodes)                                   # each value is random and unique.
dest_s_nodes = random.sample(src_s_nodes, len(src_s_nodes))                                                 # shuffled src_nodes.
for idx in range(__num_of_nodes):
    if(src_s_nodes[idx] == dest_s_nodes[idx]):
        # Avoid same pairs of node by replacing both with another different pair of values.
        src_s_nodes[idx] = random.choice(src_s_nodes)
        dest_s_nodes[idx] = random.choice(dest_s_nodes)

# Let user distribute the weight of each edge in the graph.
__weight_lower_range = int(input("Enter lower bound for the weight of all edges = "))
__weight_higher_range = int(input("Enter upper bound for the weight of all edges = "))
weights =  random.sample(list(range(__weight_lower_range, __weight_higher_range + 1)), __num_of_nodes)      # randomized weights.

# Instantiate object of weighted graph class and add all edges.
my_graph = Weighted_Graph(__num_of_nodes + 1)
for i in range(__num_of_nodes):
    my_graph.add_edge(src_s_nodes[i], dest_s_nodes[i], weights[i])

# Preview adjacency matrix of weighted graph.
print('\n\n')
my_graph.print_matrix()

# Function to draw the weighted graph.
def draw_graph():
    # Add edges and their weights.
    g = nx.Graph()
    for i in range(__num_of_nodes):
        g.add_edge(src_s_nodes[i], dest_s_nodes[i], weight = weights[i])
    
    # Dictionary containing weight label for graph edges.
    weight_labels = {}
    for i in range(__num_of_nodes):
        weight_labels[(src_s_nodes[i], dest_s_nodes[i])] = weights[i]

    # Use standard graph layout.
    pos = nx.random_layout(g)

    # Create figure.
    plt.figure(figsize = (10, 10), dpi = 100) 
    nx.draw_random(g, edge_color = 'black', width = 1, linewidths = 1, node_size = 250, node_color = 'green', 
                      alpha = 0.9, labels = {node: node for node in g.nodes()})
    nx.draw_networkx_edge_labels(g, pos, edge_labels = weight_labels, font_color = 'blue')
    plt.get_current_fig_manager().canvas.set_window_title('Initial Graph With Weighted Edges')
    plt.axis('off')
    plt.show()

# Draw the weighted graph.
draw_graph()

# isolate found AdjMatrix and cast into array from list.
ValidAdjMatrix = numpy.array(my_graph.adjMatrix)

# Apply both algorithms from Prim and Kruskal to calculate the MST.
print("\n\nPrim's Algorithm")
start = time.time()
prim_res = prim_mst(ValidAdjMatrix)
end = time.time()
prim_mst_res = prim_res[0]
prim_mst_dest = prim_res[1]
print("MST : ", prim_mst_res)
print("Distance : ", prim_mst_dest)
temp = [el if(isinstance(el, int) == True) else 0 for el in prim_mst_dest]
print("Obtained Minimum Sum Of Weights : ", sum(temp))
print("Time taken : ", end - start, "seconds.")

print("\n\nKruskal's Algorithm")
start_2 = time.time()
kruskal_res = kruskal_mst(ValidAdjMatrix)
end_2 = time.time()
kruskal_mst_res = kruskal_res[0]
kruskal_mst_dest = kruskal_res[1]
print("MST : ", kruskal_mst_res)
print("Distance : ", kruskal_mst_dest)
temp_2 = [el if(isinstance(el, int) == True) else 0 for el in kruskal_mst_dest]
print("Obtained Minimum Sum Of Weights : ", sum(temp_2))
print("Time taken : ", end_2 - start_2, "seconds.")

'''
Draw Prim's MST.
In the MST, the vertex zero(0) or edges pointing from a node to itself is not valid and could be omitted.
'''
# Add edges and their weights.
prim_g = nx.Graph()
for i in range(__num_of_nodes - 1):
    prim_g.add_edge(prim_mst_res[i], prim_mst_res[i + 1], weight = prim_mst_dest[i])
    
# Dictionary containing weight label for graph edges.
prim_weight_labels = {}
for i in range(__num_of_nodes - 1):
    prim_weight_labels[(prim_mst_res[i], prim_mst_res[i + 1])] = prim_mst_dest[i]

# Use standard graph layout.
pos = nx.random_layout(prim_g)

# Create figure.
plt.figure(figsize = (10, 10), dpi = 100) 
nx.draw_random(prim_g, edge_color = 'black', width = 1, linewidths = 1, node_size = 250, node_color = 'green', 
                       alpha = 0.9, labels = {node: node for node in prim_g.nodes()})
nx.draw_networkx_edge_labels(prim_g, pos, edge_labels = prim_weight_labels, font_color = 'blue')
plt.get_current_fig_manager().canvas.set_window_title("Prim's MST")
plt.axis('off')
plt.show()

'''
Draw Kruskal's MST.
In the MST, the vertex zero(0) or edges pointing from a node to itself is not valid and could be omitted.
'''
# Add edges and their weights.
kruskal_g = nx.Graph()
for i in range(__num_of_nodes - 1):
    kruskal_g.add_edge(kruskal_mst_res[i], kruskal_mst_res[i + 1], weight = kruskal_mst_dest[i])
    
# Dictionary containing weight label for graph edges.
kruskal_weight_labels = {}
for i in range(__num_of_nodes - 1):
    kruskal_weight_labels[(kruskal_mst_res[i], kruskal_mst_res[i + 1])] = kruskal_mst_dest[i]

# Use standard graph layout.
pos = nx.random_layout(kruskal_g)

# Create figure.
plt.figure(figsize = (10, 10), dpi = 100) 
nx.draw_random(kruskal_g, edge_color = 'black', width = 1, linewidths = 1, node_size = 250, node_color = 'green', 
                          alpha = 0.9, labels = {node: node for node in kruskal_g.nodes()})
nx.draw_networkx_edge_labels(kruskal_g, pos, edge_labels = kruskal_weight_labels, font_color = 'blue')
plt.get_current_fig_manager().canvas.set_window_title("Kruskal's MST")
plt.axis('off')
plt.show()