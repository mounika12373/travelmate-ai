# TravelMate AI - User Manual

Welcome to the **TravelMate AI** user manual. This guide will walk you through launching the application, navigating the interactive screens, generating custom travel itineraries, and interacting with the context-aware chatbot assistant.

---

## Table of Contents
1. [Getting Started](#getting-started)
2. [Home Dashboard & Search](#home-dashboard--search)
3. [Country Information Guide](#country-information-guide)
4. [City Explorer](#city-explorer)
5. [Smart Travel Itinerary Planner](#smart-travel-itinerary-planner)
6. [AI Travel Assistant Chatbot](#ai-travel-assistant-chatbot)
7. [Troubleshooting & FAQs](#troubleshooting--faqs)

---

## Getting Started

### Prerequisites
Ensure you have the following installed:
- **Python 3.9+**
- **pip** or **uv** (recommended)

### Installation
1. Clone the repository and navigate into the project directory:
   ```bash
   cd "Travel Information and Guidance Platform"
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the database seeding script to populate destinations (optional, the app does this automatically on startup):
   ```bash
   python -m data.sample_data
   ```

### Launching the Web App
Start the Streamlit application server:
```bash
streamlit run app.py
```
Open the local browser URL (usually `http://localhost:8501`) displayed in your terminal.

---

## Home Dashboard & Search

The **Home View** serves as your landing pad:
1. **Search Bar**: Type names of countries, capitals, languages, cities, or sightseeing spots to filter matched options instantly.
2. **Featured Destination Cards**: Click on any showcased city card to view detailed recommendations.
3. **Sidebar Controls**: Use the dropdown selector in the sidebar to choose your active country and city, which sets the context for subsequent pages.

---

## Country Information Guide

Accessible via the **Explore > Country Information** sidebar option:
- **Profile Summary**: Displays general country data (capital, currency code, official language, local timezone, and emergency numbers).
- **Pre-departure Checklist**: Lists essential visa guidelines and items to prepare before you depart.
- **Rules & Etiquette**: Important cultural dos and don'ts to prevent offense and comply with local laws.
- **Safety Tips**: Localized guidance and precaution advisories.

---

## City Explorer

Accessible via the **Explore > City Information** sidebar option:
- **Sightseeing & Attractions**: Shows rated spots (out of 5 stars) and recommended time of day to visit.
- **Stays & Accommodations**: Stays classified into *Budget*, *Mid-range*, and *Luxury* tiers with estimated price guidelines.
- **Cuisines & Dining**: Lists popular local vegetarian and non-vegetarian dishes.
- **Transit Guidelines**: Directions for getting around the city and airport connection routes.

---

## Smart Travel Itinerary Planner

Accessible via the **Plan & Ask > Travel Planner** sidebar option:
1. **Customize Your Trip**: Select the number of days (1-7 days) and choose a budget tier (Economy, Mid-Range, Luxury).
2. **Day-by-Day Timeline**: Generates a timeline detailing morning sightseeing, lunch suggestions, afternoon tourist spots, and evening exploration.
3. **Interactive Budget Breakdown**: Displays a Plotly Pie Chart representing cost allocations across stays, food, transit, and shopping, with a detailed pricing table.

---

## AI Travel Assistant Chatbot

Accessible via the **Plan & Ask > AI Travel Assistant** sidebar option:
- **Natural Language Interaction**: Type questions such as:
  - *"What are the traffic rules in Singapore?"*
  - *"Where should I stay in Tokyo?"*
  - *"What is the emergency number in Japan?"*
- **Context-Aware Fallbacks**: If you do not specify a location name, the chatbot automatically uses the active city/country selected in the sidebar session state (e.g. asking *"Tell me what food to try"* will retrieve food details for the selected city).
- **Suggested Queries**: Click on pre-defined query chips to instantly run test questions.

---

## Troubleshooting & FAQs

### Q: Why is my search returning no matches?
**A**: Ensure spelling matches the database. Currently, the database is pre-seeded with destinations in India (e.g. Hyderabad, Visakhapatnam), Japan (e.g. Tokyo, Osaka, Kyoto), and Singapore.

### Q: How do I reset the SQLite database?
**A**: Delete the `database/travel.db` file and restart the Streamlit server; the application will automatically reinitialize and seed clean sample data.
