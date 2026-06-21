# Changelog

All notable changes to **TravelMate AI** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-06-10

### Added
- **AI Travel Assistant**: Integration of Streamlit's native chat elements querying a local SQLite database for context-aware queries.
- **Home Landing Page**: A styled hero header, search bar, and featured destination cards.
- **Country Guide**: Comprehensive profile section with visa details, pre-departure checklists, rules, etiquette, safety guidelines, and contact numbers.
- **City Info Page**: Features tourist attractions, local cuisines (vegetarian/non-vegetarian), stays (budget/mid-range/luxury), transit instructions, and Google Maps Location & Directions links.
- **Itinerary Planner**: Day-by-day activity timelines, custom budget allocations, and budget visualizer using a Plotly Pie Chart.
- **Test Suite**: Added `pytest` framework with spec-style tests to ensure query parsing, location lookup, and DB operations are working correctly.

### Changed
- Refactored transit, safety, and airport details to bullet-point layouts for better readability.
- Re-organized city details to show clean tourist attraction layouts, dining choices, and hotel tiers.
- Configured project gitignore to untrack python cache files and other unwanted metadata.

### Fixed
- Fixed `ModuleNotFoundError` during local test executions and streamlit page routing by configuring `sys.path` dynamically.
- Restored sidebar navigation links and fixed the icon text display bug.
- Resolved database connection issues by ensuring DB initialization runs automatically on startup.
