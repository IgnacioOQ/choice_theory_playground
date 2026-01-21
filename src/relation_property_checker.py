from .imports import *
from .basic_functions import *

def is_reflexive(relation):
    """
    Check if a binary relation is reflexive.

    Parameters:
    - relation (set of tuples): Binary relation as a set of ordered pairs.

    Returns:
    - True if the relation is reflexive.
    - Otherwise, returns a tuple ('Not reflexive', missing_pair).
    """
    universe = {x for pair in relation for x in pair}
    for x in universe:
        if (x, x) not in relation:
            print('Not reflexive, missing pair:', (x, x))
            return False
    return True


def is_transitive(relation):
    """
    Check if a binary relation is transitive.

    Parameters:
    - relation (set of tuples): The binary relation as a set of ordered pairs.

    Returns:
    - True if the relation is transitive.
    - Otherwise, returns a tuple ('Not transitive', ((a, b), (b, c), (a, c))).
    """
    for (a, b) in relation:
        for (c, d) in relation:
            if b == c and (a, d) not in relation:
                print('Not transitive:', ((a, b), (b, d)),'are there, but the following is not:', ((a, d)))
                return False
    return True

def is_symmetric(relation):
    """
    Check if a binary relation is symmetric.

    Returns:
    - True if the relation is symmetric.
    - Otherwise, returns ('Not symmetric', (a, b), expected (b, a)).
    """
    for (a, b) in relation:
        if (b, a) not in relation:
            print('Not symmetric', (a, b), f'Missing {(b, a)}')
            return False
    return True

def is_antisymmetric(relation):
    """
    Check if a binary relation is antisymmetric.

    Returns:
    - True if the relation is antisymmetric.
    - Otherwise, returns ('Not antisymmetric', ((a, b), (b, a))).
    """
    for (a, b) in relation:
        if (b, a) in relation and a != b:
            print('Not antisymmetric', ((a, b), (b, a)))
            return False
    return True

def is_acyclic(relation):
    """
    Check if a binary relation is acyclic.

    Returns:
    - True if the relation is acyclic.
    - Otherwise, prints the cycle and returns False.
    """
    from collections import defaultdict

    # Build full graph with all nodes initialized
    graph = defaultdict(list)
    nodes = set()
    for a, b in relation:
        graph[a].append(b)
        nodes.update([a, b])  # ensure all nodes (including leaves) are known

    for node in nodes:
        graph[node]  # ensure all nodes appear in the graph

    visited = set()
    stack = []

    def dfs(node, path):
        visited.add(node)
        path.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                result = dfs(neighbor, path)
                if result:
                    return result
            elif neighbor in path:
                cycle_start = path.index(neighbor)
                return path[cycle_start:] + [neighbor]

        path.pop()
        return None

    for node in list(graph):  # safe to iterate now
        if node not in visited:
            cycle = dfs(node, [])
            if cycle:
                print('Not acyclic, cycle is:', cycle)
                return False

    return True

