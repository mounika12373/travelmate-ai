# TravelMate AI – Smart Travel Companion

TravelMate AI is a comprehensive Streamlit-based travel companion application designed to help tourists understand countries and cities before visiting. The platform offers critical local regulations, safety instructions, transit rules, cultural dos & don'ts, recommended hotel stays, famous cuisines, and custom-tailored daily travel planners.

It also integrates an **AI Travel Assistant**—a smart, context-aware chatbot that queries the local SQLite database to answer tourist queries instantly

---

## 🚀 Features

1. **Home Landing Page**:
   - A beautifully styled hero header.
   - Comprehensive **Search bar** to lookup countries, cities, tourist spots, or cuisines with one-click redirects.
   - Dynamic **Destination Selector** for choosing countries and cities.
   - Featured destinations showcase cards.

2. **Country Information Guide**:
   - Country profiles showing capitals, currencies, official languages, and time zones.
   - Highlighted emergency numbers and contact details.
   - Dedicated sections for **Visa and Pre-Departure checklists**, **Important Rules/Laws**, **Cultural Etiquette (Dos and Don'ts)**, and **Safety Tips**.

3. **City Details Explorer**:
   - Deep-dives into tourist attractions, rated out of 5 stars with timing recommendations.
   - Interactive sections for local dishes (vegetarian and non-vegetarian).
   - Accommodation selections categorized into **Budget**, **Mid-range**, and **Luxury** options.
   - Local transit guidelines, airport transfer suggestions, and localized city safety warnings.

4. **Day-by-Day Travel Planner**:
   - Customizable number of days (1-7 days) and budget levels.
   - Generates morning, afternoon, and evening activity timelines.
   - Recommends specific stays fitting the chosen budget.
   - Dynamic localized budget calculator displaying expense breakdowns (Accommodation, Food, Transit, Sightseeing, Shopping).
   - Interactive **Plotly Pie Chart** visualizing the cost allocation.

5. **AI Travel Assistant**:
   - Conversational chatbot utilizing Streamlit's native chat elements.
   - Parses questions such as:
     - *"What food should I try in Hyderabad?"*
     - *"What are the traffic rules in Singapore?"*
     - *"What should I know before visiting Tokyo?"*
   - Context-aware logic: uses the traveler's current active city/country view to answer generic questions (e.g. *"What are the safety guidelines?"*).
   - Includes quick-suggest query buttons.

---

## 🛠️ Tech Stack

- **UI Framework**: Streamlit (v1.35.0+)
- **Data & Visualization**: Pandas, Plotly Express
- **Database**: SQLite3
- **Styling**: Custom CSS and HTML component injection

---

## 📂 Project Structure

```text
Travel Information and Guidance Platform/
│
├── app.py                     # Main router and configuration file
├── database/
│   └── travel.db              # SQLite Database file (generated automatically)
├── data/
│   └── sample_data.py         # Seed dataset and database populate script
├── pages/
│   ├── home.py                # Dashboard landing page
│   ├── country_info.py        # Visa, rules, and etiquette guide
│   ├── city_info.py           # Attractions, dining, transit, and stays
│   ├── planner.py             # Custom itinerary and budget calculator
│   └── chatbot.py             # Context-aware travel chatbot
├── utils/
│   ├── database.py            # SQLite database connection & retrieval methods
│   └── styles.py              # Custom CSS and global HTML design components
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## 💻 Installation & Running Locally

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your system.

### 2. Clone the Project
Navigate to your workspace directory containing the files:
```bash
cd "Travel Information and Guidance Platform"
```

### 3. Install Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

### 4. Run the test suite
Run the spec-style test suite with:
```bash
pytest
```

### 5. Seed the Database
*Note: The application will automatically check and initialize the database on startup.* However, if you want to manually seed or reset it, run:
```bash
python -m data.sample_data
```

### 5. Launch the Application
Run the Streamlit application:
```bash
streamlit run app.py
```

Open the local URL displayed in the terminal (usually `http://localhost:8501`) in your web browser.
