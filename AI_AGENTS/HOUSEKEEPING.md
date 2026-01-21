# Housekeeping Protocol

1. Read the AGENTS.md file.
2. Look at the dependency network of the project.
3. Proceed doing different sanity checks and unit tests from root scripts to leaves.
4. Compile all errors and tests results into a report. And print that report in the Latest Report subsection below, overwriting previous reports.
5. Add that report to the AGENTS_LOG.md.

# Current Project Housekeeping

## Dependency Network

Based on project restructuring:
- **`src.common`**: Base module (imports).
- **`src.utils`**: Depends on `common`.
- **`src.choice_axioms`**: Depends on `utils`.
- **`src.relation_properties`**: Depends on `utils`.
- **`src.revealed_preferences`**: Depends on `utils`.
- **`src.experiments`**: Depends on `utils`, `choice_axioms`.

## Latest Report

**Execution Date:** 2026-01-21

**Test Results:**
1. `tests/test_utils.py`: **Passed** (4 tests).
2. `tests/test_choice_axioms.py`: **Passed** (3 tests).
3. `tests/test_relation_properties.py`: **Passed** (5 tests).
4. `tests/test_revealed_preferences.py`: **Passed** (2 tests).

**Total: 14 tests passed.**

**Summary:**
New test suite implemented and verified. All modules (`utils`, `choice_axioms`, `relation_properties`, `revealed_preferences`) are functioning correctly. Project structure is stable.
