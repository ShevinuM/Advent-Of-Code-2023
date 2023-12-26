import networkx as n 

g = n.Graph()

with open('input.txt', 'r') as f:
    for l in f:
        parts = l.strip().split(':')
        parts[0] = parts[0].strip()
        parts[1] = parts[1].strip().split()
        for p in parts[1]:
            g.add_edge(parts[0], p.strip())
            g.add_edge(p.strip(), parts[0])

g.remove_edges_from(n.minimum_edge_cut(g))
a, b = n.connected_components(g)
print(len(a) * len(b))
