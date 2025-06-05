# 📘 AGENTS.md — WanderTopo Development Protocol

> This file defines how all agents (AI or human) must behave when contributing to this project. It includes the project vision, file structure, coding principles, commit message format, and output rules.

---

## 🧭 PROJECT: WanderTopo

**WanderTopo** is a cross-platform, graph-based travel planning engine that abandons traditional timeline itineraries.

Instead of planning trips by fixed schedule, users interact with a topological map of places — choosing restaurants, attractions, or experiences dynamically based on:
- trustworthiness
- proximity
- user intent
- contextual filters

> “Don’t follow a schedule — follow curiosity.”

---

## 📁 FILE STRUCTURE (Monorepo)

```
wander_topo/
│
├── lib/                        # Flutter UI app (Dart)
│   └── main.dart              # Entry point
│   └── screens/               # Screen views (e.g. MapScreen)
│   └── widgets/               # Custom UI components
│
├── api/                        # FastAPI server (Python)
│   └── main.py                # App init and route include
│   └── routes/                # Individual API endpoints
│   └── schemas/               # Pydantic request/response models
│
├── core/                       # Travel graph engine (Python)
│   └── graph_engine.py        # Graph builder & manager
│   └── models.py              # PlaceNode, PlaceEdge classes
│   └── recommender.py         # Suggestion algorithm
│
├── data/                       # Static/mock POI data
│   └── sample_pois.json
│
├── tests/                      # Unit tests
│   └── test_graph_engine.py
│
├── docs/                       # Design, logic, and documentation
│   └── RULES.md
│   └── ARCHITECTURE.md
│
├── LICENSE                     # BSL 1.1 license (commercial use restricted)
├── README.md                   # Project intro and quickstart
├── AGENTS.md                   # This file
├── pubspec.yaml                # Flutter dependencies
├── requirements.txt            # Python dependencies
```

---

## ⚙️ GIT COMMIT CONVENTION

All Git commits must follow the [Conventional Commits](https://www.conventionalcommits.org) format:

```
<type>: <short description>

[optional longer explanation or bullet list]
```

### Valid types:
- `feat`:     New feature or capability
- `fix`:      Bug fix
- `refactor`: Internal restructuring, no functional change
- `test`:     Add or modify unit tests
- `doc`:      Documentation changes (README, docstrings, etc.)
- `chore`:    Misc cleanup (e.g. dependencies, scripts)

### ❌ Disallowed:
- "update", "edit", "change", "new file" — too vague

### ✅ Examples:
- `feat: add PlaceGraph class with topological edge support`
- `fix: correct node ranking bug in recommender`
- `refactor: split graph logic into modular engine`

---

## 🧠 CODING STANDARDS

### For Python (`core/`, `api/`):
- Use **Object-Oriented Design (OOP)** with single-responsibility classes
- Docstrings must follow **PEP 257** with parameter and return types
- Use **SOLID principles** where applicable
- Prefer **type hints**, clear function signatures, and testable methods
- No placeholder functions — write complete logic unless otherwise noted

#### Example Python Docstring:
```python
class PlaceNode:
    """
    Represents a travel point of interest in the topological graph.

    Attributes:
        name (str): Name of the location.
        lat (float): Latitude.
        lon (float): Longitude.
        trust_score (float): Normalized score based on reviews.
    """
```

### For Flutter (`lib/`):
- Use **Flutter with Dart** and follow standard idiomatic practices
- Separate UI into `screens/`, `widgets/`, `models/`
- Logic that talks to Python API must be in `services/` or similar
- Avoid business logic in widgets

---

## 🧾 OUTPUT RULES FOR AI AGENTS

✅ Always:
- Write full implementation (no TODO stubs)
- Use proper naming, comments, and indentation
- Explain key design choices in comments

❌ Never:
- Use vague commit messages
- Leave placeholder code
- Skip docstrings or function annotations

---

## 📣 FINAL NOTE

You are contributing to a prototype that may become a commercial product.  
All logic written here is governed under the **Business Source License 1.1**  
Commercial deployment requires separate licensing.

Let’s build WanderTopo — a new way to explore.
