from .common import *
from .utils import *

def test_alpha(choice, verbose=False):
    # Optimized implementation: O(3^N)
    # Iterate B (Superset), then A (Subset of B)
    # Alpha: If x in C(B) and x in A (subset of B), then x in C(A).
    
    # 1. Map all choice entries for fast lookup
    # choice is Dict[FrozenSet, Set]
    
    # In order to iterate B and then A < B efficiently without generating all subsets every time:
    # We can iterate through the keys of 'choice' as B.
    # Then generate subsets A of B.
    # But checking if A is in choice keys? Yes.
    
    # Sort keys by size to potentially fail fast? No necessarily.
    
    for B_fs, choice_B in choice.items():
        B = set(B_fs)
        
        # Iterate all x in C(B). 
        # For Alpha to fail, we need A subset B such that x in A, but x not in C(A).
        
        # To avoid generating 2^|B| subsets, we can try to find a counter-example smarter?
        # But for full verification we essentially need to check all A.
        # Generating all non-empty subsets of B:
        
        subsets_B = find_all_subsets_without_empty(B)
        
        for A_set in subsets_B:
            A_fs = frozenset(A_set)
            
            # Skip B itself (trivial, x in C(B) <-> x in C(B))
            if A_fs == B_fs:
                continue
            
            # If A is not in the choice function domain, skip (or assume valid/undefined)
            # Usually choice function is defined on all non-empty subsets. 
            if A_fs not in choice:
                continue
                
            choice_A = choice[A_fs]
            
            # Condition: x in C(B) AND x in A => x in C(A)
            for x in choice_B:
                if x in A_set:
                    if x not in choice_A:
                        if verbose:
                            print(f"Alpha failed: x={x}, A={A_set}, B={B}, C(B)={choice_B}, C(A)={choice_A}")
                        return False
    return True

def test_beta(choice, verbose=False):
    # Optimized implementation: O(3^N)
    # Beta: If x, y in C(A), A subset B, y in C(B) => x in C(B)
    
    # Iterate B (Superset)
    for B_fs, choice_B in choice.items():
        B = set(B_fs)
        subsets_B = find_all_subsets_without_empty(B)

        for A_set in subsets_B:
            A_fs = frozenset(A_set)
            if A_fs == B_fs or A_fs not in choice:
                continue
            
            choice_A = choice[A_fs]
            
            # Check Beta condition
            # We need x, y in C(A).
            # If C(A) is singleton, Beta is vacuously true for distinct x,y 
            # (unless x=y, definition usually implies distinct? No, x,y can be same. If x=y, trivial).
            
            if len(choice_A) < 2:
                continue
                
            # For each y in C(A) that is also in C(B)
            # Check if all other x in C(A) are in C(B)
            
            # Let Y_intersect = C(A) intersect C(B)
            # If Y_intersect is not empty, then ALL C(A) must be in C(B) (acting as 'x')?
            # Beta says: if y in C(B) (and y in C(A)), then x in C(B) (for x in C(A)).
            # So: If C(A) intersects C(B), then C(A) must be subset of C(B).
            
            # Optimization using sets:
            # intersection = choice_A & choice_B
            # if intersection:
            #    assert choice_A.issubset(choice_B)
            
            intersection = choice_A.intersection(choice_B)
            if intersection:
                if not choice_A.issubset(choice_B):
                    if verbose:
                        # Find specific x that failed
                        diff = choice_A - choice_B
                        # Any y in intersection works as witness
                        y = next(iter(intersection))
                        x = next(iter(diff))
                        print(f"Beta failed: x={x}, y={y}, A={A_set}, B={B}, C(A)={choice_A}, C(B)={choice_B}")
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

