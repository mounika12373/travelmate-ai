# Tasks: TravelMate AI - Smart Travel Companion

**Input**: Design documents from [spec.md](file:///c:/Users/hp/Documents/Travel%20Information%20and%20Guidance%20Platform/spec.md) and [plan.md](file:///c:/Users/hp/Documents/Travel%20Information%20and%20Guidance%20Platform/plan.md)

**Prerequisites**: plan.md (required), spec.md (required)

**Organization**: Tasks are grouped by implementation phase and feature area to ensure testability and isolation.

---

## Phase 1: Setup & Code Quality (Tooling)

**Purpose**: Setup the foundations for Python package metadata, style checks, and environment configurations.

- [x] T001 Initialize SpecKit project structure (`.specify/` configuration & agent skills)
- [x] T002 Configure Python linting rules in `ruff.toml`
- [x] T003 Configure Python project metadata and test tool options in `pyproject.toml`
- [x] T004 Create template env configuration file `.env.example`

---

## Phase 2: Foundational (Database Infrastructure)

**Purpose**: Setup the database connector and schema definitions.

- [x] T005 Implement SQLite database initialization and seeding scripts (`utils/database.py` and `data/sample_data.py`)
- [x] T006 Add database retrieval APIs (`get_all_countries`, `get_cities_by_country`, `get_country_details`, `get_city_details`)
- [x] T007 Implement database location search querying (`search_locations`)

---

## Phase 3: User Story 1 - Destination Exploration & Search (P1)

**Purpose**: Build the home landing page and search panel.

- [x] T008 Implement Home View UI structure and search bar redirect (`pages/home.py`)
- [x] T009 Integrate custom dynamic styling helper cards for featured destinations (`utils/styles.py`)

---

## Phase 4: User Story 2 - Regulatory & Cultural Safety Guidelines (P1)

**Purpose**: View local pre-departure visa rules, checklists, etiquette, and safety guidelines.

- [x] T010 Implement country guide view displaying pre-departure visa checklist and laws (`pages/country_info.py`)
- [x] T011 Implement city detail explorer with accommodation levels, transit, and airport guidelines (`pages/city_info.py`)

---

## Phase 5: User Story 3 - Itinerary Planner & Budget Analysis (P2)

**Purpose**: Automated budget allocation with data visualization charts.

- [x] T012 Implement travel planner user input form (days, budget level) and morning/afternoon/evening schedule compiler (`pages/planner.py`)
- [x] T013 Integrate interactive Plotly Pie Chart representing budget breakdown allocation (`pages/planner.py`)

---

## Phase 6: User Story 4 - Context-Aware Chatbot Assistant (P2)

**Purpose**: Keyword matching parser with active session context.

- [x] T014 Implement response parser with entity and topic detection (`generate_bot_response` in `pages/chatbot.py`)
- [x] T015 Integrate Streamlit chat history state management (`pages/chatbot.py`)

---

## Phase 7: Testing Suite Extensions (High Quality)

**Purpose**: Validate utility modules, routing, and bot parser.

- [x] T016 Implement unit tests for style helper functions (`tests/test_styles_spec.py`)
- [x] T017 Implement unit tests for chatbot response parsing and fallbacks (`tests/test_chatbot_spec.py`)
- [x] T018 Implement unit tests for app config and routing elements (`tests/test_app_spec.py`)

---

## Phase 8: Continuous Integration (CI/CD)

**Purpose**: Automate linting and test execution on push.

- [x] T019 Create `.gitlab-ci.yml` pipeline containing ruff lint checks and pytest runs

---

## Phase 9: Verification

- [x] T020 Run localized test suite execution (`pytest`)
- [x] T021 Run code style enforcement checks (`ruff check .`)
- [ ] T022 Commit and push changes to GitLab remote repository
