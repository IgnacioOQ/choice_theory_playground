# Choice Theory Playground - Source Package
# 
# Core modules for studying choice theory properties computationally.
#
# Modules:
# - common: Common imports and dependencies
# - utils: Core utility functions (subsets, orderings, choice functions)
# - relation_properties: Functions to check properties of binary relations
# - choice_axioms: Functions to check choice theory axioms (alpha, beta, gamma)
# - revealed_preferences: Functions bridging choice functions and preferences
# - experiments: Testing utilities for running property tests

from .common import *
from .utils import (
    find_all_subsets,
    find_all_subsets_without_empty,
    generate_random_choice_function,
    find_all_orderings,
    find_maximal_elements,
)
from .relation_properties import (
    is_reflexive,
    is_transitive,
    is_symmetric,
    is_antisymmetric,
    is_acyclic,
)
from .choice_axioms import (
    test_alpha,
    test_beta,
    test_gamma,
)
from .revealed_preferences import (
    extract_revealed_preference,
    build_preference_graph,
    topological_sort,
    build_choice_function_from_relation,
)
from .experiments import (
    generate_random_int_set,
    silent_test,
    run_property_tests,
    run_choice_function_tests,
)
