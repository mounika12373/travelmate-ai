import os
import sys

# Ensure the root of the project is in the python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import streamlit as st

from utils.database import get_all_countries, get_cities_by_country, init_db
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

# Import i18n helpers
from utils.i18n import translate_ui

# Custom Sidebar Header styling
render_html(f"""
    <div style='text-align: center; padding: 10px 0;'>
        <h2 style='margin:0; font-weight:800; color:var(--primary-color); font-size:1.8rem;'>✈️ TravelMate AI</h2>
        <p style='color:gray; font-size:0.85rem; margin-top:5px;'>{translate_ui("app_subtitle")}</p>
    </div>
    <hr style='margin-top:0; margin-bottom:15px; border-color:rgba(128,128,128,0.2);'>
""", sidebar=True)

# Global Language Selector in Sidebar
selected_lang = st.sidebar.selectbox(
    "🌐 Language / भाषा / భాష",
    ["English", "Hindi (हिन्दी)", "Telugu (తెలుగు)"],
    index=0,
    key="language_selector_ui"
)
lang_map = {
    "English": "en",
    "Hindi (हिन्दी)": "hi",
    "Telugu (తెలుగు)": "te"
}
st.session_state.language = lang_map.get(selected_lang, "en")

# Initialize session state for cross-page navigation
if "selected_country_id" not in st.session_state:
    # Default to India if exists, otherwise first country
    countries = get_all_countries()
    if countries:
        india_list = [c for c in countries if c["country_name"].lower() in ["india", "भारत", "భారతదేశం"]]
        st.session_state.selected_country_id = india_list[0]["id"] if india_list else countries[0]["id"]
    else:
        st.session_state.selected_country_id = None

if "selected_city_id" not in st.session_state:
    # Default to Hyderabad or first city of default country
    if st.session_state.selected_country_id:
        cities = get_cities_by_country(st.session_state.selected_country_id)
        if cities:
            hyd_list = [c for c in cities if c["city_name"].lower() in ["hyderabad", "हैदराबाद", "హైదరాబాద్"]]
            st.session_state.selected_city_id = hyd_list[0]["id"] if hyd_list else cities[0]["id"]
        else:
            st.session_state.selected_city_id = None
    else:
        st.session_state.selected_city_id = None

if "search_query" not in st.session_state:
    st.session_state.search_query = ""

# Define Pages with Titles, Icons, and File paths (localized)
home_page = st.Page("pages/home.py", title=translate_ui("home"), icon="🏠", default=True)
country_page = st.Page("pages/country_info.py", title=translate_ui("country_info_title"), icon="🌍")
city_page = st.Page("pages/city_info.py", title=translate_ui("city_info_title"), icon="🏙️")
planner_page = st.Page("pages/planner.py", title=translate_ui("planner_title"), icon="📅")
chatbot_page = st.Page("pages/chatbot.py", title=translate_ui("chatbot_title"), icon="💬")

# Create Navigation Router (localized headers)
pg = st.navigation({
    translate_ui("explore"): [home_page, country_page, city_page],
    translate_ui("plan_ask"): [planner_page, chatbot_page]
})

# Run the Navigation router
pg.run()

# Custom Sidebar Footer
render_html(f"""
    <div style='position: fixed; bottom: 10px; width: 100%; text-align: left; padding: 10px; font-size:0.8rem; color:gray;'>
        {translate_ui("made_with_love")}
    </div>
""", sidebar=True)
