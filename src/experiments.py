from .common import *
from .utils import *
from .choice_axioms import test_alpha, test_beta, test_gamma

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

    return set(random.sample(range(max_value), n))

def silent_test(func, *args, **kwargs):
    """
    Run a function while suppressing its print output.
    Exceptions will still propagate unless caught externally.
    """
    with contextlib.redirect_stdout(io.StringIO()):
        return func(*args, **kwargs)

def run_property_tests(example_set, num_trials=100):
    results = defaultdict(int)

    # Use manual loop with tqdm.update() to minimize RAM (good for large num_trials)
    with tqdm(total=num_trials, desc="Running tests", unit="test") as pbar:
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

            pbar.update(1)  # update progress by 1

    # Summary
    print("\n=== Summary ===")
    for key in sorted(results.keys()):
        print(f"{key}: {results[key]}")

def run_choice_function_tests(example_set, num_trials=100):
    results = defaultdict(int)

    # Use tqdm with manual updates to minimize memory usage
    with tqdm(total=num_trials, desc="Testing choice functions", unit="test") as pbar:
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

            pbar.update(1)

    # Print summary
    print("\n=== Summary ===")
    for key in sorted(results.keys()):
        print(f"{key}: {results[key]}")
