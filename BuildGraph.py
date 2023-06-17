import networkx as nx
from BruteForce import Fit


def buildGraph(items):
    g = nx.Graph()
    for i in range(len(items)):
        g.add_node(i)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if not Fit(items[i], [items[j]]):
                g.add_edge(i, j)
    return g
