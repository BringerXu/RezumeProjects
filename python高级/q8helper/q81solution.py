from performance import Performance
from goody import irange
from graph_goody import random_graph,spanning_tree

# Put script below to generate data for Problem #1
# In case you fail, the data appears in sample8.pdf in the helper folder
for i in irange(0,7):
    nodes = 1000*2**i
    rg = random_graph(nodes,lambda n: 10*n)
    p = Performance(lambda:spanning_tree(rg),title = 'Spanning Tree of size '+str(nodes))
    p.evaluate()
    p.analyze()