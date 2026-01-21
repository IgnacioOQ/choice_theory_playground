# Choice Theory Playground

A computational toolkit for studying and verifying properties of choice functions, preference relations, and the axioms of choice theory (Alpha, Beta, Gamma).

## 📌 Overview

This project provides a Python suite for:
- **Generating random choice functions** and sets.
- **Testing Choice Axioms**: Verify if a choice function satisfies Sen's $\alpha$, $\beta$, and $\gamma$ properties.
- **Checking Relation Properties**: Test binary relations for reflexivity, transitivity, symmetry, antisymmetry, and acyclicity.
- **Bridging Concepts**: Convert between choice functions and revealed preference relations.
- **AI Agent Skills**: Includes documentation and skills for AI agents to work with the codebase.

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd choice_theory_playground
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Quick Start

You can import the package `src` to access all core functions.

### 1. Working with Choice Functions & Axioms
```python
from src import generate_random_choice_function, test_alpha, test_beta, test_gamma

# Define a universe of elements
universe = {1, 2, 3, 4}

# Generate a random choice function
C = generate_random_choice_function(universe)

# Test axioms
print(f"Satisfies Alpha: {test_alpha(C)}")
print(f"Satisfies Beta:  {test_beta(C)}")
print(f"Satisfies Gamma: {test_gamma(C)}")
```

### 2. Working with Relations
```python
from src import is_transitive, is_acyclic

relation = {(1, 2), (2, 3), (1, 3)} # 1 >= 2, 2 >= 3, 1 >= 3

print(f"Transitive: {is_transitive(relation)}") # Should be True
print(f"Acyclic:    {is_acyclic(relation)}")    # Should be True
```

### 3. Revealed Preferences
Extract the "revealed preference" relation from a choice function.
```python
from src import extract_revealed_preference

# C is a dictionary mapping frozensets to sets
revealed_rel = extract_revealed_preference(C)
print("Revealed Relation:", revealed_rel)
```

## 📂 Project Structure

```
choice_theory_playground/
├── src/                          # Main Python Package
│   ├── utils.py                  # Core utility functions
│   ├── choice_axioms.py          # Axiom tests (Alpha, Beta, Gamma)
│   ├── relation_properties.py    # Relation property tests
│   ├── revealed_preferences.py   # Revealed preference conversions
│   ├── experiments.py            # Batch testing utilities
│   └── common.py                 # Shared dependencies
├── notebooks/                    # Demonstration Notebooks
│   ├── 01_choice_axioms_demo.ipynb
│   └── 02_relations_and_revealed_prefs_demo.ipynb
├── AI_AGENTS/                    # AI Agent Context & Skills
│   ├── HOUSEKEEPING.md           # Maintenance protocols
│   └── LINEARIZE_AGENT.md        # Vectorization instructions
├── AGENTS.md                     # Documentation for AI Assistants
├── requirements.txt              # Project dependencies
└── README.md                     # This file
```

## 🧠 Choice Theory Concepts

- **Property $\alpha$ (Alpha)**: If $x \in A \subseteq B$ and $x \in C(B)$, then $x \in C(A)$. (Contraction Consistency)
- **Property $\beta$ (Beta)**: If $x, y \in C(A)$ and $A \subseteq B$ and $y \in C(B)$, then $x \in C(B)$. (Expansion Consistency)
- **Revealed Preference**: $x \succeq y$ iff $\exists A$ such that $x \in C(A)$ and $y \in A$.
