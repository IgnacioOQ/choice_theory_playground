import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.relation_properties import (
    is_reflexive,
    is_transitive,
    is_symmetric,
    is_antisymmetric,
    is_acyclic
)

def test_is_reflexive():
    # {1, 2}
    # Needs (1,1) and (2,2)
    R_pass = {(1, 1), (2, 2), (1, 2)}
    assert is_reflexive(R_pass) == True
    
    R_fail = {(1, 1), (1, 2)} # Missing (2,2) - 2 is in universe because appears in (1,2)
    assert is_reflexive(R_fail) == False

def test_is_transitive():
    # (1,2), (2,3) -> implies (1,3)
    R_pass = {(1, 2), (2, 3), (1, 3)}
    assert is_transitive(R_pass) == True
    
    R_fail = {(1, 2), (2, 3)} # Missing (1,3)
    assert is_transitive(R_fail) == False

def test_is_symmetric():
    # If (x,y) then (y,x)
    R_pass = {(1, 2), (2, 1), (3, 3)}
    assert is_symmetric(R_pass) == True
    
    R_fail = {(1, 2)}
    assert is_symmetric(R_fail) == False

def test_is_antisymmetric():
    # if (x,y) and (y,x) then x=y
    R_pass = {(1, 2), (2, 3), (3, 3)}
    assert is_antisymmetric(R_pass) == True
    
    R_fail = {(1, 2), (2, 1)} # 1!=2 but both directions exist
    assert is_antisymmetric(R_fail) == False

def test_is_acyclic():
    # No cycles
    R_pass = {(1, 2), (2, 3), (1, 3)}
    assert is_acyclic(R_pass) == True
    
    R_fail = {(1, 2), (2, 3), (3, 1)}
    assert is_acyclic(R_fail) == False
    
    R_fail_self = {(1, 1)} # Self loop is a cycle? 
    # Usually acyclic allows self-loops in weak preference? No, strict part.
    # The function builds a graph from relation pairs and checks DFS.
    # If graph has (1,1), DFS will find 1 already in recursion stack?
    # Let's assume strict acyclicity (no self loops allowed).
    assert is_acyclic(R_fail_self) == False
