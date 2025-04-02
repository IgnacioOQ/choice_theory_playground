from imports import *

def find_all_subsets(input_set):
    """
    Finds all subsets of the given set.

    Args:
    input_set (set): The input set.

    Returns:
    list: A list of subsets, where each subset is represented as a set.
    """
    input_list = list(input_set)
    subsets = list(chain.from_iterable(combinations(input_list, r) for r in range(len(input_list) + 1)))
    return [set(subset) for subset in subsets]


def find_all_subsets_without_empty(input_set):
    """
    Finds all subsets of the given set, excluding the empty set.

    Args:
    input_set (set): The input set.

    Returns:
    list: A list of subsets, where each subset is represented as a set.
    """
    input_list = list(input_set)
    subsets = list(chain.from_iterable(combinations(input_list, r) for r in range(len(input_list) + 1)))
    # Convert to sets and exclude the empty set
    return [set(subset) for subset in subsets if subset]  # if subset Exclude the empty set

def generate_random_choice_function(input_set):
  all_subsets = find_all_subsets_without_empty(input_set)
  for subset in all_subsets:
    all_subsubsets = find_all_subsets_without_empty(subset)
    choice_function[frozenset(subset)] = random.choice(all_subsubsets)
  return choice_function


