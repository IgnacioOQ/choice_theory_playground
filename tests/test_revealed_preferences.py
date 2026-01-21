import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.revealed_preferences import (
    extract_revealed_preference,
    build_choice_function_from_relation
)

def test_extract_revealed_preference():
    # C({1, 2}) = {1} -> 1 >= 2, 1 >= 1.
    C = {
        frozenset({1, 2}): {1}
    }
    rp = extract_revealed_preference(C)
    assert (1, 2) in rp
    assert (1, 1) in rp
    assert (2, 1) not in rp # Unless implicit? No.

def test_build_choice_function_from_relation():
    # Relation: 1 >= 2, 2 >= 3. (Assume 1,2,3 universe)
    # 1>=1, 2>=2, 3>=3
    relation = {(1, 2), (2, 3), (1, 3), (1, 1), (2, 2), (3, 3)}
    
    C = build_choice_function_from_relation(relation)
    
    # C({1, 2, 3}) should be {1} (maximal)
    # Check 1: 1>=1, 1>=2, 1>=3? No, relation must contain ALL pairs?
    # Function logic: 
    # maximal = {a for a in A if all(b in geq.get(a) for b in A)}
    # a dominates EVERY b in A.
    
    assert C[frozenset({1, 2, 3})] == {1}
    assert C[frozenset({2, 3})] == {2}
    assert C[frozenset({1, 3})] == {1}
