# TravelMate AI Constitution

This document defines the core identity, principles, guidelines, and standards for the TravelMate AI project. All contributors—both humans and AI agents—must adhere to these rules when specification planning, planning, and implementing features.

---

## 1. Project Overview
**TravelMate AI** is a Streamlit-based smart travel companion application designed to help tourists explore and navigate new cities and countries. The platform integrates localized travel checklists, safety warnings, cultural dos & don'ts, automated daily itinerary planners with budget analysis, and a context-aware AI travel chatbot querying a SQLite database.

---

## 2. Core Principles
* **Spec-Driven Development (SDD)**: Define functional specifications and implementation plans before modifying or creating code.
* **Keep Core Clean**: Page files under `pages/` must focus strictly on UI layout and routing, leaving backend queries, database configuration, and styling definition to the respective modules in `utils/`.
* **Testing Rigor**: All modules must have accompanying tests in the `tests/` directory written in a specification style (`pytest-describe` and `pytest-spec`).
* **Database Access Isolation**: Do not hardcode database sessions or execution logic within UI files. All operations must route through [utils/database.py](file:///c:/Users/hp/Documents/Travel%20Information%20and%20Guidance%20Platform/utils/database.py).

---

## 3. Technology Stack & Standards
* **Python**: Version 3.8+
* **Web UI Framework**: Streamlit (>= 1.35.0)
* **Data Processing**: Pandas (>= 2.0.0)
* **Visualization**: Plotly Express (>= 5.15.0)
* **Database**: SQLite3
* **Testing Suite**: Pytest (>= 8.0.0) with `pytest-spec` and `pytest-describe`
* **Styling**: Inject custom CSS from [utils/styles.py](file:///c:/Users/hp/Documents/Travel%20Information%20and%20Guidance%20Platform/utils/styles.py) to keep layout/aesthetics consistent and modular.

---

## 4. Directory & File Organization
Adhere to the following directory rules when creating new components:

```text
Travel Information and Guidance Platform/
├── .specify/
│   └── memory/
│       └── constitution.md     # This file (Project Guidelines)
├── app.py                      # Router & configuration entry point
├── database/
│   └── travel.db               # SQLite database file (auto-generated)
├── data/
│   └── sample_data.py          # Data seeding script & core sample datasets
├── pages/                      # Streamlit multipage view modules
│   ├── home.py                 # Welcome dashboard & search panel
│   ├── country_info.py         # Rules, checklists, safety, and cultural info
│   ├── city_info.py            # Attractions, accommodations, dining, & transit
│   ├── planner.py              # Custom travel planner & cost pie-charts
│   └── chatbot.py              # SQLite context-aware AI travel chatbot
├── utils/                      # Shared helper utility modules
│   ├── database.py             # Database connector and retrieval API
│   └── styles.py               # Central styling sheet & HTML components
├── tests/                      # Spec-style testing files
│   └── test_database_spec.py   # Database unit tests in spec format
├── pytest.ini                  # Pytest Spec configuration file
└── requirements.txt            # Dependency listings
```

---

## 5. Development & Testing Workflow

### Adding a New View / Page
1. Create a page file inside the `pages/` directory.
2. Load global styles using `from utils.styles import inject_custom_css` at the top of the file.
3. Fetch required data exclusively through functions defined in `utils/database.py`.

### Testing Execution
Tests must be executed via `pytest`. Output must run with spec format enabled:
```bash
pytest
```
All new test files should follow the `test_*_spec.py` naming convention and use nested `describe` and `it_` function blocks.
