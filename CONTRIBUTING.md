# Contributing to TravelMate AI

First off, thank you for considering contributing to **TravelMate AI**! Contributions make the open-source community an amazing place to learn, inspire, and create.

---

## 🛠️ Getting Started

### 1. Fork and Clone the Repository
Fork the repository on GitHub and clone your fork locally:
```bash
git clone https://github.com/<your-username>/travelmate-ai.git
cd travelmate-ai
```

### 2. Set Up a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies:
```bash
# On Windows:
python -m venv venv
venv\Scripts\activate

# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all required libraries including development/testing dependencies:
```bash
pip install -r requirements.txt
```

### 4. Seed the Database
Seed the database with sample locations, attractions, hotels, and safety guidelines:
```bash
python -m data.sample_data
```

---

## 🧪 Running Tests

We use `pytest` for unit testing. To run the tests, run:
```bash
pytest
```

Ensure all tests pass before proposing any changes. If you are adding a new feature, please write accompanying unit tests under the `tests/` directory.

---

## 📝 Coding Standards

- **Python PEP 8**: Ensure your code conforms to standard PEP 8 formatting rules.
- **Naming Conventions**: Use `snake_case` for functions/variables, and `PascalCase` for classes.
- **Modularity**: Place helper functions in the `utils/` directory and keep Streamlit page logic clean in the `pages/` directory.
- **Comments & Docstrings**: Document functions and classes clearly, especially where logic is complex (such as SQL queries or Plotly calculations).

---

## 🚀 Submitting Your Changes

1. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Commit Your Changes**:
   Write descriptive commit messages that explain *what* you changed and *why*:
   ```bash
   git commit -m "Add dynamic travel budgeting options to itinerary planner"
   ```
3. **Push to Your Branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
4. **Open a Pull Request (PR)**:
   - Provide a clear description of the problem solved or feature added.
   - Attach screenshots or GIFs for UI-related changes if possible.
   - Confirm that all existing tests pass and new tests are written.
