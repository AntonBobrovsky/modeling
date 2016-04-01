from random import randint
from graphviz import Graph


def graph_draw(nodes, edges, name):
    g = Graph(name, format="png")
    for node in nodes:
        g.node(str(node))
    for edge in edges:
        x = edge.split(' ')[0]
        y = edge.split(' ')[1]
        g.edge(x, y)
    g.view()


def tree_deep(N, max_deep):

    use_nodes = []
    edges = []
    deeps = {}
    nodes = range(N)

    root = randint(0, N - 1)
    use_nodes.append(root)
    nodes.remove(root)
    deeps[root] = 0

    while len(nodes) > 0:
        a = use_nodes[randint(0, len(use_nodes) - 1)]
        b = nodes[randint(0, len(nodes) - 1)]

        if deeps[a] + 1 > max_deep:
            continue

        use_nodes.append(b)
        nodes.remove(b)
        deeps[b] = deeps[a] + 1
        edges.append(str(a) + ' ' + str(b))
        print edges
    return edges


def tree_max_degree(N, max_degree):

    nodes = range(N)
    use_nodes = []
    edges = []
    degrees = {}

    root = randint(0, N - 1)
    use_nodes.append(root)
    nodes.remove(root)
    degrees[root] = 0
    while len(nodes) > 0:

        a = use_nodes[randint(0, len(use_nodes) - 1)]
        b = nodes[randint(0, len(nodes) - 1)]

        if degrees[a] + 1 > max_degree:
            continue

        use_nodes.append(b)
        nodes.remove(b)
        degrees[b] = 1
        degrees[a] += 1
        edges.append(str(a) + ' ' + str(b))
        print edges
    return edges


if __name__ == "__main__":

    nodes = 100
    i = 20

    edges = tree_deep(nodes, i)
    graph_draw(range(nodes), edges, "deep")

    edges = tree_max_degree(nodes, i)
    graph_draw(range(nodes), edges, "max_root")
