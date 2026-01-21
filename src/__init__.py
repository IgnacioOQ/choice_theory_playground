# Choice Theory Playground - Source Package
# 
# Core modules for studying choice theory properties computationally.
#
# Modules:
# - imports: Common imports and dependencies
# - basic_functions: Core utility functions (subsets, orderings, choice functions)
# - relation_property_checker: Functions to check properties of binary relations
# - choice_property_checker: Functions to check choice theory axioms (alpha, beta, gamma)
# - bridging_choices_and_orderings: Functions bridging choice functions and preferences
# - testing_functions: Testing utilities for running property tests

from .imports import *
from .basic_functions import (
    find_all_subsets,
    find_all_subsets_without_empty,
    generate_random_choice_function,
    find_all_orderings,
    find_maximal_elements,
)
from .relation_property_checker import (
    is_reflexive,
    is_transitive,
    is_symmetric,
    is_antisymmetric,
    is_acyclic,
)
from .choice_property_checker import (
    test_alpha,
    test_beta,
    test_gamma,
)
from .bridging_choices_and_orderings import (
    extract_revealed_preference,
    build_preference_graph,
    topological_sort,
    build_choice_function_from_relation,
)
from .testing_functions import (
    generate_random_int_set,
    silent_test,
    run_property_tests,
    run_choice_function_tests,
)
