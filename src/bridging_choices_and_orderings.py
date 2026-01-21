from .imports import *

def extract_revealed_preference(choice_function: Dict[FrozenSet[int], Set[int]]) -> Set[Tuple[int, int]]:
    """
    Extracts the revealed preference relation (>=) from a choice function.
    Returns a set of pairs (a, b) meaning a >= b.
    """
    revealed_preference = set()
    
    for A, chosen in choice_function.items():
        A = set(A)
        for a in chosen:
            for b in A:
                revealed_preference.add((a, b))  # a >= b if a ∈ C(A) and b ∈ A
    
    return revealed_preference


def build_preference_graph(relation: Set[Tuple[int, int]]) -> Dict[int, Set[int]]:
    """
    Builds a graph from the revealed preference relation: b -> a if a >= b.
    Useful for topological sort (reverse relation).
    """
    graph = defaultdict(set)
    for a, b in relation:
        if a != b:
            graph[b].add(a)  # Edge from b to a means a >= b
    return graph


def topological_sort(graph: Dict[int, Set[int]]) -> List[int]:
    """
    Returns a topological sort of the preference graph if it's acyclic.
    Raises an error if there's a cycle.
    """
    in_degree = defaultdict(int)
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    all_nodes = set(graph.keys()) | {n for neighbors in graph.values() for n in neighbors}
    queue = deque([n for n in all_nodes if in_degree[n] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(all_nodes):
        raise ValueError("Cycle detected in the preference graph")

    return result[::-1]  # reverse to get most preferred first


def build_choice_function_from_relation(
    relation: Set[Tuple[int, int]]
) -> Dict[FrozenSet[int], Set[int]]:
    """
    Given a binary relation (a >= b), builds a choice function C(A)
    such that C(A) = { a in A | a >= b for all b in A }.
    Automatically infers the universe from the relation.
    """
    # Extract universe from the relation
    universe = set()
    for a, b in relation:
        universe.add(a)
        universe.add(b)

    # Build lookup: for each a, the set of b such that a >= b
    geq = {a: set() for a in universe}
    for a, b in relation:
        geq[a].add(b)

    # Compute choice function over all nonempty subsets
    choice_function = {}
    for r in range(1, len(universe) + 1):
        for subset in itertools.combinations(universe, r):
            A = set(subset)
            maximal = {a for a in A if all(b in geq.get(a, set()) for b in A)}
            choice_function[frozenset(A)] = maximal

    return choice_function
