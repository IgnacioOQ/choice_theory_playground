from imports import *
from basic_functions import *

def is_reflexive(relation):
    """
    Check if a binary relation is reflexive.

    Parameters:
    - relation (set of tuples): Binary relation as a set of ordered pairs.

    Returns:
    - bool: True if the relation is reflexive, False otherwise.
    """
    universe = {x for pair in relation for x in pair}
    return all((x, x) in relation for x in universe)


def is_transitive(relation):
    """
    Check if a binary relation is transitive.

    Parameters:
    - relation (set of tuples): The binary relation as a set of ordered pairs.

    Returns:
    - bool: True if the relation is transitive, False otherwise.
    """
    for (a, b) in relation:
        for (c, d) in relation:
            if b == c and (a, d) not in relation:
                return False
    return True

def is_symmetric(relation):
    """
    Check if a binary relation is symmetric.

    Parameters:
    - relation (set of tuples): The binary relation as a set of ordered pairs.

    Returns:
    - bool: True if the relation is symmetric, False otherwise.
    """
    return all((b, a) in relation for (a, b) in relation)

def is_antisymmetric(relation):
    """
    Check if a binary relation is antisymmetric.

    Parameters:
    - relation (set of tuples): The binary relation as a set of ordered pairs.

    Returns:
    - bool: True if the relation is antisymmetric, False otherwise.
    """
    return all(a == b or (b, a) not in relation for (a, b) in relation)


def is_acyclic(relation):
    """
    Check if a binary relation is acyclic.

    Parameters:
    - relation (set of tuples): The binary relation as a set of ordered pairs.

    Returns:
    - bool: True if the relation is acyclic, False otherwise.
    """
    from collections import defaultdict

    # Build adjacency list
    graph = defaultdict(list)
    for a, b in relation:
        graph[a].append(b)

    visited = set()
    stack = set()

    def dfs(node):
        visited.add(node)
        stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in stack:
                return True

        stack.remove(node)
        return False

    # Run DFS from all unvisited nodes
    for node in graph:
        if node not in visited:
            if dfs(node):
                return False  # Cycle found

    return True
