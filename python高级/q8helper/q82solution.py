import cProfile
from graph_goody import random_graph, spanning_tree
import pstats

# Put script below to generate data for Problem #2
# In case you fail, the data appears in sample8.pdf in the helper folder
graph_1 = random_graph(5000,lambda n:10*n)
graph_2 = random_graph(10000, lambda n:10*n)
cProfile.run('spanning_tree(graph_1)','profile5K')
cProfile.run('spanning_tree(graph_2)','profile10K')
p1 = pstats.Stats('profile5K')
p1.strip_dirs().sort_stats(0).print_stats()
p2 = pstats.Stats('profile10K')
p2.strip_dirs().sort_stats(1).print_stats()