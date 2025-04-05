from imports import *
from basic_functions import *

def test_alpha(choice,verbose = False):
    # Extract universe from the choice function
    universe = set()
    for A in choice:
        universe = universe.union(A)

    all_subsets = find_all_subsets_without_empty(universe)
    all_fsets = [frozenset(subset) for subset in all_subsets]

    choice_cache = {fs: choice[fs] for fs in all_fsets}
    union_cache = {}

    for i, subset1 in enumerate(all_subsets):
        fs1 = all_fsets[i]
        choice_A = choice_cache[fs1]

        for j, subset2 in enumerate(all_subsets):
            # Cache and reuse unions
            key = (i, j)
            if key not in union_cache:
                union_set = frozenset(set(subset1).union(subset2))
                union_cache[key] = union_set
            else:
                union_set = union_cache[key]

            choice_AUB = choice.get(union_set, set())

            for x in subset1:
                if x in choice_AUB:
                    if x not in choice_A:
                        if verbose:
                            print(f"Alpha failed: x={x}, A={subset1}, AUB={set(subset1).union(subset2)}, "
                                  f"C(AUB)={choice_AUB}, C(A)={choice_A}")
                        return False
    return True

def test_beta(choice,vebose=False):
    universe = set()
    for A in choice:
        universe = universe.union(A)
        
    all_subsets = find_all_subsets_without_empty(universe)
    all_fsets = [frozenset(subset) for subset in all_subsets]

    choice_cache = {fs: choice[fs] for fs in all_fsets}
    union_cache = {}

    for i, subset1 in enumerate(all_subsets):
        fs1 = all_fsets[i]
        choice_A = choice_cache[fs1]

        for j, subset2 in enumerate(all_subsets):
            # Cache union frozensets
            key = (i, j)
            if key not in union_cache:
                union_fs = frozenset(set(subset1).union(subset2))
                union_cache[key] = union_fs
            else:
                union_fs = union_cache[key]

            choice_AUB = choice.get(union_fs, set())

            # Test Beta condition
            for x in choice_A:
                if x in choice_AUB:
                    for y in choice_A:
                        if y not in choice_AUB:
                            if verbose:
                                print(f"Beta failed: x,y={x},{y} A={subset1}, B={subset2}, "
                                  f"C(A)={choice_A} C(AUB)={choice_AUB}")
                            return False

    return True
    
def test_gamma(choice, verbose=False):
    universe = set()
    for A in choice:
        universe = universe.union(A)
    
    all_subsets = find_all_subsets_without_empty(universe)
    all_fsets = [frozenset(subset) for subset in all_subsets]

    choice_cache = {fs: choice[fs] for fs in all_fsets}
    union_cache = {}

    for i, subset1 in enumerate(all_subsets):
        fs1 = all_fsets[i]
        choice_A = choice_cache[fs1]

        for j, subset2 in enumerate(all_subsets):
            fs2 = all_fsets[j]
            choice_B = choice_cache[fs2]

            intersection = set(subset1).intersection(subset2)
            if not intersection:
                continue

            # Cache union
            key = (i, j)
            if key not in union_cache:
                fs_union = frozenset(set(subset1).union(subset2))
                union_cache[key] = fs_union
            else:
                fs_union = union_cache[key]

            choice_AUB = choice.get(fs_union, set())

            for x in intersection:
                if choice_A == {x} and x in choice_B:
                    if x not in choice_AUB:
                        if verbose:
                            print(f"Weak Gamma failed: x={x}, A={subset1}, B={subset2}, "
                              f"C(A)={choice_A} C(B)={choice_B} C(AUB)={choice_AUB}")
                        return False
    return True

