# Setup and Installation Guide

This guide walks you through setting up and running **TravelMate AI** on your local machine.

---

## 📋 Prerequisites
Before you start, make sure you have the following installed:
- **Python**: Version 3.8 to 3.12 (highly recommended). Check version with `python --version`.
- **Git**: For version control.

---

## ⚙️ Step-by-Step Installation

### Step 1: Clone the Project
If you haven't already, download the project codebase:
```bash
git clone https://github.com/<your-username>/travelmate-ai.git
cd "Travel Information and Guidance Platform"
```

### Step 2: Create a Virtual Environment (Recommended)
Creating a virtual environment ensures dependencies do not conflict with other Python projects on your machine.

**For Windows (PowerShell / Command Prompt):**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**For macOS / Linux (Terminal):**
```bash
python3 -m venv venv
source venv/bin/activate
```

*(You will know the virtual environment is active when you see `(venv)` prepended to your command prompt.)*

### Step 3: Install Required Dependencies
All libraries are listed in `requirements.txt`. Install them using:
```bash
pip install -r requirements.txt
```

### Step 4: Initialize and Seed the Database
TravelMate AI queries a local SQLite database for travel information, rules, and AI chatbot references.
To populate the database with seed data:
```bash
python -m data.sample_data
```
This command creates the database file at `database/travel.db` and populates the schema and sample destinations.

### Step 5: Run the Streamlit Application
Launch the web interface locally using:
```bash
streamlit run app.py
```

Streamlit will print a local URL in your console (usually `http://localhost:8501`). Open it in your web browser.

---

## 🧪 Running the Test Suite
The project utilizes `pytest` along with spec plugins for behavior-driven assertion reporting.
To run the automated tests, execute:
```bash
pytest
```

---

## 🔍 Troubleshooting

### 1. `ModuleNotFoundError: No module named 'utils'`
If you encounter import issues during test runs or while running scripts:
- Ensure you run all commands from the project root directory (`Travel Information and Guidance Platform`).
- The project includes dynamic `sys.path` appending in files to prevent this, but keeping your working directory at the root is still required.

### 2. Database files locked or missing
- If `database/travel.db` is missing, rerun the seeding command: `python -m data.sample_data`.
- If the application reports database errors, verify that you have write permissions to the `database` folder.
