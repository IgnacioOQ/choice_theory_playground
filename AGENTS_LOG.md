# Agents Log

## Intervention History

### Project Reorganization: Choice Theory Playground
**Date:** 2026-01-21
**AI Assistant:** Antigravity
**Summary:** Reorganized the project structure for the Choice Theory Playground.
- **Created Directories:**
  - `src/`: Main Python package for choice theory computations
  - `AI_AGENTS/`: Agent skill markdown files
- **Moved Files:**
  - Python scripts → `src/` (imports.py, basic_functions.py, choice_property_checker.py, relation_property_checker.py, bridging_choices_and_orderings.py, testing_functions.py)
  - Agent markdown files → `AI_AGENTS/` (LINEARIZE_AGENT.md, HOUSEKEEPING.md)
- **Updated Imports:** Changed all internal imports to use relative imports (e.g., `from .imports import *`)
- **Created `src/__init__.py`:** Package with all exports for easy importing
- **Updated `AGENTS.md`:** Reflects new directory structure and project purpose (choice theory computational tool)

### Codebase Refactoring: Renaming for Clarity
**Date:** 2026-01-21
**AI Assistant:** Antigravity
**Summary:** Renamed source files in `src/` for better logical clarity.
- `basic_functions.py` → `utils.py`
- `choice_property_checker.py` → `choice_axioms.py`
- `relation_property_checker.py` → `relation_properties.py`
- `bridging_choices_and_orderings.py` → `revealed_preferences.py`
- `testing_functions.py` → `experiments.py`
- `imports.py` → `common.py`
- Updated all imports and documentation (`AGENTS.md`, `README.md`, `src/__init__.py`) to match.

### Documentation: Added Demonstration Notebooks
**Date:** 2026-01-21
**AI Assistant:** Antigravity
**Summary:** Added a `notebooks/` folder with two demonstration notebooks.
- `01_choice_axioms_demo.ipynb`: Shows how to generate random choice functions and test for Alpha/Beta/Gamma properties.
- `02_relations_and_revealed_prefs_demo.ipynb`: Demonstrates relation properties and the bridge between choices and preferences.
- Updated `README.md` and `AGENTS.md` to document the new folder.

### Housekeeping Report (Reorganization Phase)
**Date:** 2026-01-21
**AI Assistant:** Antigravity
**Summary:** Executed full housekeeping protocol following project reorganization.
- **Actions:**
    - Moved `HOUSEKEEPING.md` to `AI_AGENTS/`.
    - Created comprehensive test suite in `tests/` covering all `src` modules.
    - Verified all tests passed (14/14).
    - Updated `AI_AGENTS/HOUSEKEEPING.md` with latest dependency graph and report.
- **Status:** Stable.

---

### Housekeeping Report (Initial)
**Date:** 
**Summary:** Executed initial housekeeping protocol.
**AI Assitant:**
- **Dependency Network:** 
- **Tests:** 

### Bug Fix: Advanced Analysis (Shape Mismatch)
**Date:** 2024-05-22
**Summary:** Fixed RuntimeError in `advanced_experiment_interface.ipynb`.
- **Issue:** `compute_policy_metrics` in `src/analysis.py` passed 1D inputs `(100, 1)` to agents expecting 2D inputs `(100, 2)`.
- **Fix:** Created `src/advanced_analysis.py` with `compute_advanced_policy_metrics`.
- **Details:** The new function constructs inputs as `[p, t]` with `t` fixed at 0 (default).
- **Files Modified:** `src/advanced_simulation.py` updated to use the new analysis function.

### Bug Fix: Notebook NameError
**Date:** 2024-05-22
**Summary:** Fixed NameError in `advanced_experiment_interface.ipynb`.
- **Issue:** The variable `ep_id` was used in a print statement but was undefined in the new JSON saving block.
- **Fix:** Removed the erroneous print statement and cleanup old comments. Validated that the correct logging uses `current_step_info['episode_count']`.

