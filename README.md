# 💬 TravelMate AI — Smart Travel Companion

[![CI Pipeline](https://img.shields.io/badge/CI%2FCD-GitLab%20Pipeline-blue.svg)](https://code.swecha.org/mounikapatnaik/travel-information-and-guide)
[![Pre-Commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Python Version](https://img.shields.io/badge/Python-3.9+-yellow.svg?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-AGPLv3-red.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

TravelMate AI is a comprehensive, Streamlit-based travel companion application designed to assist tourists in understanding countries and cities before visiting. The platform integrates emergency contact details, visa checklists, local laws, cultural dos and don'ts, recommended hotel stays, local cuisines, and personalized daily itinerary planners.

It also integrates a context-aware **AI Travel Assistant**—a chatbot that queries a local SQLite database to provide instant answers to traveler questions ON time

---

## 📌 Table of Contents

1. [Features](#🚀-features)
2. [Tech Stack](#🛠️-tech-stack)
3. [Project Structure](#📂-project-structure)
4. [Installation & Setup](#💻-installation--running-locally)
5. [Testing & Quality Assurance](#🧪-testing--quality-assurance)
6. [Pre-commit Hooks & Standards](#🪝-pre-commit-hooks--standards)
7. [Repository Documentation Links](#📄-repository-documentation-links)
8. [License](#📄-license)

---

## 🚀 Features

* **Home Dashboard**: Beautiful hero header, featuring destination cards and a global search lookup across attractions, countries, capitals, and cuisines.
* **Country Guide**: Local profiles detailing official languages, timezone information, currency, emergency contacts, visa check-lists, and cultural etiquette.
* **City Explorer**: Rated tourist spots, localized vegetarian and non-vegetarian cuisines, and hotel accommodations segmented into budget, mid-range, and luxury.
* **Smart Travel Planner**: Dynamic day-by-day itineraries (1-7 days) matched with budget visualizers utilizing interactive Plotly diagrams.
* **AI Travel Assistant**: Multi-lingual (English, Hindi, Telugu) chatbot with smart context fallbacks linked to the active country/city selection.

---

## 🛠️ Tech Stack

* **UI Framework**: Streamlit (v1.35.0+)
* **Data Visualization**: Pandas, Plotly Express
* **Database**: SQLite3 (Embedded Database)
* **Styling**: Custom CSS and Google Fonts (Outfit)
* **Linting & Code Quality**: Ruff, Mypy, Bandit, Vulture, Pylint, Flake8, Semgrep, Pyupgrade
* **Security Scanning**: Gitleaks (Secret Scanning), pip-audit (Vulnerability Audit)
* **Changelog Automation**: Git-Cliff (Conventional Commits)

---

## 📂 Project Structure

```text
TravelMate AI /
├── .agents/                 # SpecKit agent configurations
├── .specify/                # Spec-Driven Development rules & templates
├── app.py                   # Main entry point and navigation setup
├── database/
│   └── travel.db            # Local SQLite database (initialized automatically)
├── data/
│   └── sample_data.py       # Seed dataset definitions
├── pages/                   # Frontend view components
│   ├── home.py              # Main landing dashboard
│   ├── country_info.py      # Regulatory and cultural profiles
│   ├── city_info.py         # Attractions and accommodation listings
│   ├── planner.py           # Daily trip scheduler & budget chart
│   └── chatbot.py           # Context-aware AI assistant
├── utils/                   # Shared helpers and backend modules
│   ├── database.py          # SQLite database connection & query APIs
│   ├── i18n.py              # Internationalization & translation dictionary
│   └── styles.py            # Global custom styling sheet & injections
├── tests/                   # Spec-style test suite
└── pyproject.toml           # Project metadata & configurations
```

---

## 💻 Installation & Running Locally

### 1. Prerequisites
Ensure you have **Python 3.9+** and `git` installed.

### 2. Clone the Repository
```bash
git clone https://code.swecha.org/mounikapatnaik/travel-information-and-guide.git
cd travel-information-and-guide
```

### 3. Install Dependencies
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Running the Web Application
```bash
streamlit run app.py
```
This will open the local URL in your web browser (typically `http://localhost:8501`).

---

## 🧪 Testing & Quality Assurance

To execute the unit tests and check test coverage, run:

```bash
# Run pytest with spec-style report format
PYTHONPATH=. pytest

# Run pytest with test coverage reports
PYTHONPATH=. pytest --cov=. --cov-report=term-missing
```

---

## 🪝 Pre-commit Hooks & Standards

This project enforces strict coding quality, format consistency, and security audits before every commit.

### 1. Install Pre-commit
Ensure pre-commit is installed and configured in your environment:
```bash
pre-commit install
```

### 2. Manual Pre-commit Check
To run all configured quality, security, and format checks manually:
```bash
pre-commit run --all-files
```

### 3. Configured Checks
* **Format & Lint**: `ruff` and `ruff-format`
* **Static Analysis**: `mypy` (type-checking), `bandit` (security flaws), `pylint`, `flake8`
* **Dead Code Detection**: `vulture`
* **Secret Scanning**: `gitleaks` (prevents keys/passwords leaks)
* **Vulnerabilities Audit**: `pip-audit` (audits packages against databases)
* **Automated Changelog**: `git-cliff` (updates `CHANGELOG.md` using conventional commits)

---

## 📄 Repository Documentation Links

For further information regarding project rules, contributions, security, or guidelines, refer to the following documents:

* 📚 **[User Manual](USER_MANUAL.md)** — Guide on using the application features.
* ⚙️ **[Setup Guide](docs/SETUP_GUIDE.md)** — Detailed system setup instructions.
* 📐 **[Development Spec](spec.md)** — Core functionality specifications.
* 🤝 **[Contributing Guidelines](CONTRIBUTING.md)** — How to contribute to this repository.
* 🛡️ **[Security Policy](SECURITY.md)** — Security disclosure protocol.
* 💬 **[Code of Conduct](CODE_OF_CONDUCT.md)** — Project community standards.
* 🛠️ **[Support Page](SUPPORT.md)** — Getting assistance and reporting issues.

---

## 📄 License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**. For details, see the [LICENSE](LICENSE) file.
