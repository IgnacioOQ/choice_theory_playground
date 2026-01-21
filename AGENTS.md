# AGENTS.md

## SHORT ADVICE
- The whole trick is providing the AI Assistants with context, and this is done using the *.md files (AGENTS.md, AGENTS_LOG.md, and the AI_AGENTS folder)
- Learn how to work the Github, explained below.
- Keep logs of changes in AGENTS_LOG.md
- Make sure to execute the HOUSEKEEPING.md protocol often.
- Always ask several forms of verification, so because the self-loop of the chain of thought improves performance.
- Impose restrictions and constraints explicitly in the context.

## HUMAN-ASSISTANT WORKFLOW
1. Open the assistant and load the ai-agents-branch into their local repositories. Do this by commanding them to first of all read the AGENTS.md file.
2. Work on the ASSISTANT, making requests, modifying code, etc.
3. IMPORTANT: GIT MECHANISM
    3.1. This is basically solved in Antigravity, but Jules (and maybe Claude) push the changes into a newly generated branch. In my case, this is `jules-sync-main-v1-15491954756027628005`. **This is different from the `ai-agents-branch`!!**
    3.2. So what you need to do is merge the newly generated branch and the `ai-agents-branch` often. Usually in the direction from `jules-sync-main-v1-15491954756027628005` to `ai-agents-branch`. I do this by:
        3.2.1. Going to pull requests.
        3.2.2. New Pull request
        3.2.3. Base: `ai-agents-branch`, Compare: `jules-sync-main-v1-15491954756027628005` (arrow in the right direction).
        3.2.4. Follow through. It should allow to merge and there should not be incompatibilities. If there are incompatibilities, you can delete the `ai-agents-branch` and create a new one cloning the `jules-sync-main-v1-15491954756027628005` one. After deleting `ai-agents-branch`, go to the `jules-sync-main-v1-15491954756027628005` branch, look at the dropdown bar with the branches (not the link), and create a new copy.
4. It is very useful to use specialized agents for different sectors of the code. 
5. Enjoy!

## WORKFLOW & TOOLING

*   **Documentation Logs (`AGENTS_LOG.md`):**
    *   **Rule:** Every agent that performs a significant intervention or modifies the codebase **MUST** update the `AGENTS_LOG.md` file.
    *   **Action:** Append a new entry under the "Intervention History" section summarizing the task, the changes made, and the date.

## DEVELOPMENT RULES & CONSTRAINTS
1.  **Immutable Core Files:** Do not modify 
    *   If you need to change the logic of an agent or the model, you must create a **new version** (e.g., a subclass or a new file) rather than modifying the existing classes in place.
2.  **Consistency:** Ensure any modifications or new additions remain as consistent as possible with the logic and structure of the `main` branch.
3.  **Coding Conventions:** Always keep the coding conventions pristine.

## CONTEXT FINE-TUNING
You cannot "fine-tune" an AI agent (change its underlying neural network weights) with files in this repository. **However**, you **CAN** achieve a similar result using **Context**.

**How it works (The "Context" Approach):**
If you add textbooks or guides to the repository (preferably as Markdown `.md` or text files), agents can read them. You should then update the relevant agent instructions (e.g., `AI_AGENTS/LINEARIZE_AGENT.md`) to include a directive like:

> "Before implementing changes, read `docs/linearization_textbook.md` and `docs/jax_guide.md`. Use the specific techniques described in Chapter 4 for sparse matrix operations."

**Why this is effective:**
1.  **Specific Knowledge:** Adding a specific textbook helps if you want a *specific style* of implementation (e.g., using `jax.lax.scan` vs `vmap` in a particular way).
2.  **Domain Techniques:** If the textbook contains specific math shortcuts for your network types, providing the text allows the agent to apply those exact formulas instead of generic ones.

**Recommendation:**
If you want to teach an agent a new language (like JAX) or technique:
1.  Add the relevant chapters as **text/markdown** files.
2.  Update the agent's instruction file (e.g., `AI_AGENTS/LINEARIZE_AGENT.md`) to reference them.
3.  Ask the agent to "Refactor the code using the techniques in [File X]".

## LOCAL PROJECT DESCRIPTION

### Project Overview
This project is a **Choice Theory Playground** — a computational tool for studying properties of choice functions and binary relations. It implements tests for choice-theoretic axioms (α, β, γ) and properties of relations (reflexivity, transitivity, symmetry, antisymmetry, acyclicity).

### Setup & Testing
*   **Install Dependencies:** `pip install -r requirements.txt`
*   **Import the package:** `from src import *` or individual modules
*   **Run Tests:** `python -c "from src import *; print('All imports successful!')"`

### Key Architecture & Logic

#### 1. Architecture (Modular Package)
*   **`src/`**: Python package containing all core logic for choice theory computations.
*   **`AI_AGENTS/`**: Contains markdown files with agent skill definitions.
    *   `LINEARIZE_AGENT.md`: Agent for vectorization tasks.
    *   `HOUSEKEEPING.md`: Protocol for testing and maintenance.

#### 2. Core Modules (`src/`)
*   **`common.py`**: Common imports (itertools, random, tqdm, typing, etc.).
*   **`utils.py`**: Core utility functions for subsets, orderings, and choice functions.
*   **`relation_properties.py`**: Functions to check relation properties (reflexive, transitive, symmetric, antisymmetric, acyclic).
*   **`choice_axioms.py`**: Functions to test choice theory axioms (α, β, γ).
*   **`revealed_preferences.py`**: Functions to convert between choice functions and preference relations.
*   **`experiments.py`**: Testing utilities for running batch property tests.

### Key Files and Directories

#### Directory Structure
```
choice_theory_playground/
├── AGENTS.md               # This file - project documentation for AI agents
├── AGENTS_LOG.md           # Log of agent interventions
├── requirements.txt        # Project dependencies
├── notebooks/              # Demonstration Notebooks
├── AI_AGENTS/              # Agent skill definitions
│   ├── HOUSEKEEPING.md     # Housekeeping and testing protocol
│   └── LINEARIZE_AGENT.md  # Vectorization agent instructions
└── src/                    # Main Python package
    ├── __init__.py         # Package exports
    ├── common.py           # Common imports
    ├── utils.py            # Core utilities
    ├── relation_properties.py
    ├── choice_axioms.py
    ├── revealed_preferences.py
    └── experiments.py
```

#### File Dependencies & Logic
- `utils.py` depends on `common.py`
- `relation_properties.py` depends on `common.py`, `utils.py`
- `choice_axioms.py` depends on `common.py`, `utils.py`
- `revealed_preferences.py` depends on `common.py`
- `experiments.py` depends on `common.py`, `utils.py`, `choice_axioms.py`

### Choice Theory Concepts

#### Choice Functions
A **choice function** C maps each non-empty subset A of a universe to a non-empty subset C(A) ⊆ A of "chosen" elements.

#### Choice Axioms
- **α (Alpha):** If x is chosen from A∪B and x ∈ A, then x is also chosen from A alone.
- **β (Beta):** If x, y ∈ C(A) and x ∈ C(A∪B), then y ∈ C(A∪B).
- **γ (Gamma - Weak):** If C(A) = {x} and x ∈ C(B), then x ∈ C(A∪B).

#### Relation Properties
- **Reflexive:** ∀x: (x, x) ∈ R
- **Transitive:** ∀x,y,z: (x,y) ∈ R ∧ (y,z) ∈ R → (x,z) ∈ R
- **Symmetric:** ∀x,y: (x,y) ∈ R → (y,x) ∈ R
- **Antisymmetric:** ∀x,y: (x,y) ∈ R ∧ (y,x) ∈ R → x = y
- **Acyclic:** No cycles in the strict part of R

**Testing & Verification:**
*   Run the functions in `testing_functions.py` to test random choice functions against axiomatic properties.

