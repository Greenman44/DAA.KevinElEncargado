from BuildGraph import buildGraph


def WeightedVertex(items, k):
    G = buildGraph(items)
    for node in G.nodes():
        G.nodes[node]['weight'] = 2 ** (-G.degree(nodes))
    mis = set()
    while G:
        node = max(G.nodes(), key=lambda x: G.nodes[x]['weight'])
        cover.add(node)
        for neighbor in G.neighbors(node):
            G.nodes[neighbor]['weight'] = 0
        G.remove_node(node)

    if len(mis) >= k:
        return mis[:k]
    else:
        return mis
