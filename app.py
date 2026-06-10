import os
import sys
# Ensure the root of the project is in the python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from utils.database import init_db, get_all_countries, get_cities_by_country
from utils.styles import inject_global_css, render_html


# Initialize database schema and seed data if not present
init_db()

# Page configuration
st.set_page_config(
    page_title="TravelMate AI – Smart Travel Companion",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject custom global styling
inject_global_css()

# Initialize session state for cross-page navigation
if "selected_country_id" not in st.session_state:
    # Default to India if exists, otherwise first country
    countries = get_all_countries()
    if countries:
        india_list = [c for c in countries if c["country_name"].lower() == "india"]
        st.session_state.selected_country_id = india_list[0]["id"] if india_list else countries[0]["id"]
    else:
        st.session_state.selected_country_id = None

if "selected_city_id" not in st.session_state:
    # Default to Hyderabad or first city of default country
    if st.session_state.selected_country_id:
        cities = get_cities_by_country(st.session_state.selected_country_id)
        if cities:
            hyd_list = [c for c in cities if c["city_name"].lower() == "hyderabad"]
            st.session_state.selected_city_id = hyd_list[0]["id"] if hyd_list else cities[0]["id"]
        else:
            st.session_state.selected_city_id = None
    else:
        st.session_state.selected_city_id = None

if "search_query" not in st.session_state:
    st.session_state.search_query = ""

# Define Pages with Titles, Icons, and File paths
home_page = st.Page("pages/home.py", title="Home", icon="🏠", default=True)
country_page = st.Page("pages/country_info.py", title="Country Information", icon="🌍")
city_page = st.Page("pages/city_info.py", title="City Information", icon="🏙️")
planner_page = st.Page("pages/planner.py", title="Travel Planner", icon="📅")
chatbot_page = st.Page("pages/chatbot.py", title="AI Travel Assistant", icon="💬")

# Custom Sidebar Header styling
render_html("""
    <div style='text-align: center; padding: 10px 0;'>
        <h2 style='margin:0; font-weight:800; color:var(--primary-color); font-size:1.8rem;'>✈️ TravelMate AI</h2>
        <p style='color:gray; font-size:0.85rem; margin-top:5px;'>Your Smart Travel Companion</p>
    </div>
    <hr style='margin-top:0; margin-bottom:15px; border-color:rgba(128,128,128,0.2);'>
""", sidebar=True)

# Create Navigation Router
pg = st.navigation({
    "Explore": [home_page, country_page, city_page],
    "Plan & Ask": [planner_page, chatbot_page]
})

# Run the Navigation router
pg.run()

# Custom Sidebar Footer
render_html("""
    <div style='position: fixed; bottom: 10px; width: 100%; text-align: left; padding: 10px; font-size:0.8rem; color:gray;'>
        Made with ❤️ for Travelers
    </div>
""", sidebar=True)
