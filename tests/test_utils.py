import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import (
    find_all_subsets,
    find_all_subsets_without_empty,
    generate_random_choice_function,
    find_maximal_elements
)

def test_find_all_subsets():
    S = {1, 2}
    subsets = find_all_subsets(S)
    expected = [set(), {1}, {2}, {1, 2}]
    # Compare as frozensets for order independence
    subsets_fs = sorted([frozenset(s) for s in subsets], key=lambda x: (len(x), sorted(list(x))))
    expected_fs = sorted([frozenset(s) for s in expected], key=lambda x: (len(x), sorted(list(x))))
    
    assert subsets_fs == expected_fs
    assert len(subsets) == 2**len(S)

def test_find_all_subsets_without_empty():
    S = {1, 2}
    subsets = find_all_subsets_without_empty(S)
    assert set() not in subsets
    assert len(subsets) == 2**len(S) - 1

def test_generate_random_choice_function():
    S = {1, 2, 3}
    C = generate_random_choice_function(S)
    all_subsets = find_all_subsets_without_empty(S)
    assert len(C) == len(all_subsets)
    for fs_A, chosen in C.items():
        A = set(fs_A)
        assert chosen.issubset(A)
        assert len(chosen) > 0

def test_find_maximal_elements():
    # As analyzed, the function returns elements x where (x, y) is NOT in relation for any y != x.
    # If relation is interpreted as 'x dominates y', it returns non-dominating elements.
    # If relation is interpreted as 'x < y' (strict less), it returns elements that are explicitly smaller than nothing (minimal?)
    # or rather elements that are NOT smaller than anything?
    # No, all((x, y) NOT in relation). If (x,y) means x < y.
    # Then x < y is false for all y. So x is not smaller than any y. So x is MAXIMAL.
    # So the function works for 'strictly less than' relations.
    
    # x < y
    # 1 < 2, 2 < 3.
    # Relation: {(1, 2), (2, 3), (1, 3)}
    strict_less = {(1, 2), (2, 3), (1, 3)}
    
    # 1: (1,2) in R. Fails.
    # 2: (2,3) in R. Fails.
    # 3: (3, y). No pair starts with 3. Passes.
    
    max_elements = find_maximal_elements(strict_less)
    assert max_elements == {3}
