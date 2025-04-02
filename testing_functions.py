from imports import *

def generate_random_int_set(n, max_value=None):
    """
    Generate a random set of unique integers of size n.

    Parameters:
    - n (int): Size of the set.
    - max_value (int, optional): The upper limit (exclusive) for number generation.
                                 Defaults to 10 * n to ensure enough unique values.

    Returns:
    - set of int: A set containing n unique random integers.
    """
    if max_value is None:
        max_value = 10 * n

    if n > max_value:
        raise ValueError("Cannot generate more unique numbers than the range allows.")

def silent_test(func, *args, **kwargs):
    """
    Run a function while suppressing its print output.
    Exceptions will still propagate unless caught externally.
    """
    with contextlib.redirect_stdout(io.StringIO()):
        return func(*args, **kwargs)

def run_property_tests(example_set, num_trials=100):
    results = defaultdict(int)

    for _ in range(num_trials):
        choice = generate_random_choice_function(example_set)

        # Alpha test
        try:
            silent_test(test_alpha, choice, example_set)
            results['alpha_passed'] += 1
        except Exception as e:
            results['alpha_failed'] += 1

        # Beta test
        try:
            silent_test(test_beta, choice, example_set)
            results['beta_passed'] += 1
        except Exception as e:
            results['beta_failed'] += 1

        # Gamma test
        try:
            silent_test(test_gamma, choice, example_set)
            results['gamma_passed'] += 1
        except Exception as e:
            results['gamma_failed'] += 1

    # Summary
    print("=== Summary ===")
    for key in sorted(results.keys()):
        print(f"{key}: {results[key]}")

def run_choice_function_tests(example_set, num_trials=100):
    results = defaultdict(int)

    for _ in range(num_trials):
        choice = generate_random_choice_function(example_set)

        # Alpha test
        try:
            silent_test(test_alpha, choice, example_set)
            results['alpha_passed'] += 1
        except Exception:
            results['alpha_failed'] += 1

        # Beta test
        try:
            silent_test(test_beta, choice, example_set)
            results['beta_passed'] += 1
        except Exception:
            results['beta_failed'] += 1

        # Gamma test
        try:
            silent_test(test_gamma, choice, example_set)
            results['gamma_passed'] += 1
        except Exception:
            results['gamma_failed'] += 1

    # Print summary
    print("=== Summary ===")
    for key in sorted(results.keys()):
        print(f"{key}: {results[key]}")
