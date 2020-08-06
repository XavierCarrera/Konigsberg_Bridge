%matplotlib inline
import matplotlib.pyplot as plt
nx.draw(P, with_labels = True)


P = nx.Graph() 

P.add_nodes_from(['A','B','C','D', 'E'])

P.add_edges_from ([('B','C'), ('A','C'), ('B','D'), ('D','A'), ('D','E'), ('B','E')])

print(P.nodes())
print(P.edges())

