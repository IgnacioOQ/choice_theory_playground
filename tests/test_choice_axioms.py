import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.choice_axioms import (
    test_alpha as check_alpha,
    test_beta as check_beta,
    test_gamma as check_gamma
)

def test_alpha_axiom():
    # Alpha: If x chosen in AUB and x in A, then x chosen in A.
    # Failing example:
    # A = {1, 2}, B = {2, 3}
    # C({1, 2, 3}) = {1}
    # C({1, 2}) = {2}  <-- 1 should be chosen if it was chosen in larger set
    # Wait, 1 is in A={1,2}. 1 is chosen in AUB={1,2,3}. So 1 MUST be in C(A).
    # Here 1 is not in C(A)={2}. So Alpha fails.
    
    universe = {1, 2, 3}
    C = {
        frozenset({1}): {1},
        frozenset({2}): {2},
        frozenset({3}): {3},
        frozenset({1, 2}): {2},       # 1 available, not chosen
        frozenset({1, 3}): {1},
        frozenset({2, 3}): {2},
        frozenset({1, 2, 3}): {1}     # 1 chosen here in superset of {1,2}
    }
    # x=1. AUB={1,2,3}. x in C(AUB). A={1,2}. x in A.
    # Alpha requires x in C(A).
    # {1} is NOT subset of {2}. (Wait, C(A) is {2})
    # So 1 is NOT in {2}. Alpha fails.
    assert check_alpha(C) == False

    # Passing example (Rational)
    # Order 3 > 2 > 1
    C_pass = {
        frozenset({1}): {1},
        frozenset({2}): {2},
        frozenset({3}): {3},
        frozenset({1, 2}): {2},
        frozenset({1, 3}): {3},
        frozenset({2, 3}): {3},
        frozenset({1, 2, 3}): {3}
    }
    assert check_alpha(C_pass) == True

def test_beta_axiom():
    # Beta: If x, y chosen in A, and A subset B, and y chosen in B, then x chosen in B.
    # Rational functions usually satisfy this.
    
    # Failing example
    # A = {1, 2}. C(A) = {1, 2}.
    # B = {1, 2, 3}. C(B) = {2}.
    # x=1, y=2. Both in C(A). y=2 in C(B).
    # Beta requires x=1 in C(B). It is not.
    
    C_fail = {
        frozenset({1}): {1},
        frozenset({2}): {2},
        frozenset({3}): {3},
        frozenset({1, 2}): {1, 2},
        frozenset({1, 3}): {1},
        frozenset({2, 3}): {2},
        frozenset({1, 2, 3}): {2}
    }
    assert check_beta(C_fail) == False
    
    # Rational passes
    C_pass = {
        frozenset({1}): {1},
        frozenset({2}): {2},
        frozenset({3}): {3},
        frozenset({1, 2}): {2},
        frozenset({1, 3}): {3},
        frozenset({2, 3}): {3},
        frozenset({1, 2, 3}): {3}
    }
    assert check_beta(C_pass) == True

def test_gamma_axiom():
    # Gamma (Weak): If C(A)={x} and x in C(B), then x in C(AUB).
    # Useful for combining sets.
    
    # Failing example
    # C({1}) = {1}
    # C({2}) = {2}
    # x=1. A={1}. C(A)={1}.
    # y=2. B={1, 2}. Suppose C(B)={2}. 
    # Wait, condition: x in C(B).
    # Test case:
    # A = {1, 2}, C(A) = {1}
    # B = {1, 3}, C(B) = {1, 3} (so 1 is in C(B))
    # AUB = {1, 2, 3}
    # Gamma implies 1 in C(AUB).
    # Let C(AUB) = {2}. Then fails.
    
    C_fail = {
        frozenset({1}): {1},
        frozenset({2}): {2},
        frozenset({3}): {3},
        frozenset({1, 2}): {1},
        frozenset({1, 3}): {1, 3},
        frozenset({2, 3}): {2},
        frozenset({1, 2, 3}): {2}
    }
    assert check_gamma(C_fail) == False
    
    # Rational passes
    C_pass = {
        frozenset({1}): {1},
        frozenset({2}): {2},
        frozenset({3}): {3},
        frozenset({1, 2}): {2},
        frozenset({1, 3}): {3},
        frozenset({2, 3}): {3},
        frozenset({1, 2, 3}): {3}
    }
    assert check_gamma(C_pass) == True
