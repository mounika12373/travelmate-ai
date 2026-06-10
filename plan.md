# Implementation Plan: TravelMate AI - Smart Travel Companion

**Branch**: `main` | **Date**: 2026-06-10 | **Spec**: [spec.md](file:///c:/Users/hp/Documents/Travel%20Information%20and%20Guidance%20Platform/spec.md)

## Summary

TravelMate AI is structured as a Streamlit multi-page web application that utilizes a local SQLite database for content storage. The application is styled dynamically using custom HTML and inline CSS injections to guarantee a premium user interface. The chatbot assistant maps keywords and uses active session context to query the SQLite tables.

## Technical Context

- **Language/Version**: Python 3.8+
- **Primary Dependencies**: Streamlit (>= 1.35.0), Pandas (>= 2.0.0), Plotly Express (>= 5.15.0)
- **Storage**: SQLite3 database (`database/travel.db`)
- **Testing**: Pytest (>= 8.0.0) with `pytest-spec` and `pytest-describe`
- **Target Platform**: Python environments, Streamlit cloud or hosting instances
- **Project Type**: Streamlit Multi-page Web Application

## Constitution Check

The architecture strictly adheres to the core rules defined in the [constitution.md](file:///c:/Users/hp/Documents/Travel%20Information%20and%20Guidance%20Platform/.specify/memory/constitution.md):
- **Spec-Driven Development**: `spec.md`, `plan.md`, and `tasks.md` are documented before coding.
- **Keep Core Clean**: Pages in `pages/` handle UI formatting. Backend requests and styling details are isolated inside `utils/database.py` and `utils/styles.py`.
- **Database Access Isolation**: Database initialization, connections, and query operations are encapsulated inside `utils/database.py`. No raw SQL commands or SQLite transactions are performed directly in the view pages.
- **Testing Rigor**: Spec-style tests are written under the `tests/` folder using nested `describe` and `it_` testing blocks.

## Project Structure

```text
Travel Information and Guidance Platform/
├── .agents/
│   └── skills/                 # SpecKit agent workflows
├── .specify/
│   ├── memory/
│   │   └── constitution.md     # Project Constitution
│   ├── templates/              # Markdown templates
│   └── integrations.json       # CLI tool settings
├── app.py                      # Main entry point and page router
├── database/
│   └── travel.db               # SQLite database file (created on startup)
├── data/
│   └── sample_data.py          # Data seeding script & mock datasets
├── pages/                      # Frontend views (Layout & UI rendering)
│   ├── home.py                 # Welcome dashboard & search panel
│   ├── country_info.py         # Visa, rules, and etiquette guide
│   ├── city_info.py            # Attractions, dining, transit, and stays
│   ├── planner.py              # Custom itinerary and budget calculator
│   └── chatbot.py              # Context-aware travel chatbot
├── utils/                      # Backend services and modules
│   ├── database.py             # SQLite database connector & retrieval APIs
│   └── styles.py               # Central styling stylesheet & HTML injections
├── tests/                      # Testing suite
│   ├── test_database_spec.py   # Database unit tests
│   ├── test_styles_spec.py     # Styling helper tests
│   ├── test_chatbot_spec.py    # Keyword matching and context tests
│   └── test_app_spec.py        # Streamlit configuration tests
├── requirements.txt            # System dependencies
├── ruff.toml                   # Code quality rules
└── pyproject.toml              # Project metadata & tool settings
```

## Database Schema Design

The SQLite database consists of two tables with a one-to-many relationship:

### `countries` Table
- `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
- `country_name` (TEXT UNIQUE NOT NULL)
- `capital` (TEXT NOT NULL)
- `currency` (TEXT NOT NULL)
- `language` (TEXT NOT NULL)
- `timezone` (TEXT NOT NULL)
- `emergency_number` (TEXT NOT NULL)
- `visa_info` (TEXT NOT NULL)
- `rules` (TEXT NOT NULL)
- `etiquette` (TEXT NOT NULL)
- `safety_tips` (TEXT NOT NULL)

### `cities` Table
- `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
- `country_id` (INTEGER NOT NULL, FOREIGN KEY REFERENCES countries(id))
- `city_name` (TEXT NOT NULL)
- `description` (TEXT NOT NULL)
- `transport_info` (TEXT NOT NULL)
- `food_info` (TEXT NOT NULL, JSON format listing local dishes)
- `tourist_places` (TEXT NOT NULL, JSON format listing attractions)
- `hotel_info` (TEXT NOT NULL, JSON format listing accommodation options)
- `shopping_areas` (TEXT NOT NULL)
- `airport_details` (TEXT NOT NULL)
- `safety_recommendations` (TEXT NOT NULL)

## Central Styling Architecture
A dynamic aesthetic is achieved by injecting CSS styles from `utils/styles.py` using `st.markdown(..., unsafe_allow_html=True)`. Key features include:
- **Typography**: The custom Google Font **Outfit** is loaded globally.
- **Glassmorphism & Cards**: A custom `.travel-card` wrapper class with transitions, background images (base64-encoded local files), and box-shadow highlights.
- **Color Palette**: Curated primary color palettes and modern gradients for pricing, rating, and badge structures.
