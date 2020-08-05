%matplotlib inline
import matplotlib.pyplot as plt
nx.draw(P, with_labels = True)

# Initiating an empty Graph object 
P = nx.Graph() # create an empty object
# You can add nodes using add_nodes_from()
P.add_nodes_from(['A','B','C','D', 'E'])
# Use add_edges_from to add pairwise relationships
P.add_edges_from ([('B','C'), ('A','C'), ('B','D'), ('D','A'), ('D','E'), ('B','E')])

print(P.nodes())
print(P.edges())

