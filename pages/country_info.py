import streamlit as st
from utils.database import get_all_countries, get_country_details, get_cities_by_country
from utils.styles import render_hero, render_html


# Sidebar Country Quick Selector
countries = get_all_countries()
if not countries:
    st.error("No countries found. Please seed the database.")
    st.stop()

country_names = [c["country_name"] for c in countries]
current_c_index = 0
if st.session_state.selected_country_id:
    for idx, c in enumerate(countries):
        if c["id"] == st.session_state.selected_country_id:
            current_c_index = idx
            break

st.sidebar.subheader("Explore another country")
selected_country_name = st.sidebar.selectbox(
    "Select Country", 
    country_names, 
    index=current_c_index, 
    key="country_info_select"
)

# Sync with state
selected_country = next(c for c in countries if c["country_name"] == selected_country_name)
st.session_state.selected_country_id = selected_country["id"]

# Fetch latest country details
country = get_country_details(st.session_state.selected_country_id)

# Hero header for the country
render_hero(f"Explore {country['country_name']}", f"Essential facts, visa details, local laws, and cultural etiquette for visiting {country['country_name']}.")

# 1. Quick Facts Grid
st.markdown("### 📊 Country Profile")
qcol1, qcol2, qcol3, qcol4 = st.columns(4)

with qcol1:
    render_html(f"""
        <div class="metric-box">
            <div class="metric-label">Capital City</div>
            <div class="metric-value">🏛️ {country['capital']}</div>
        </div>
    """)
with qcol2:
    render_html(f"""
        <div class="metric-box">
            <div class="metric-label">Local Currency</div>
            <div class="metric-value">💵 {country['currency']}</div>
        </div>
    """)
with qcol3:
    render_html(f"""
        <div class="metric-box">
            <div class="metric-label">Spoken Languages</div>
            <div class="metric-value">🗣️ {country['language']}</div>
        </div>
    """)
with qcol4:
    render_html(f"""
        <div class="metric-box">
            <div class="metric-label">Standard Timezone</div>
            <div class="metric-value">⏰ {country['timezone']}</div>
        </div>
    """)

st.write("")

# Emergency numbers highlighted
st.warning(f"🚨 **Emergency Numbers:** {country['emergency_number']}")

# 2. Main Content Tabs
tab_visa, tab_rules, tab_safety = st.tabs([
    "📑 Visa & Entry Requirements", 
    "📜 Rules & Cultural Etiquette", 
    "🛡️ Safety & Travel Tips"
])

with tab_visa:
    st.markdown("### 📑 Visa & Entry Requirements")
    st.info(country["visa_info"])
    
    st.markdown("#### ✈️ Quick Pre-Departure Checklist")
    st.markdown(f"""
    - [ ] Check passport validity (should have at least 6 months validity from departure date).
    - [ ] Complete visa or online entry forms (e.g. { 'SG Arrival Card' if country['country_name'].lower() == 'singapore' else 'eVisa application' }).
    - [ ] Secure health or travel insurance covering local medical systems.
    - [ ] Inform your bank about travel dates to prevent card locks.
    """)

with tab_rules:
    col_rules, col_etiquette = st.columns(2)
    
    with col_rules:
        st.markdown("### 📜 Important Rules & Regulations")
        # Split rules by newline or number to present nicely
        rules_list = country["rules"].split("\n")
        for rule in rules_list:
            if rule.strip():
                # Extract description if formatting is like "1. Name: desc"
                render_html(f"<div style='background-color:rgba(239, 68, 68, 0.05); padding:10px; border-left:3px solid #EF4444; border-radius:4px; margin-bottom:10px;'>{rule}</div>")
                
    with col_etiquette:
        st.markdown("### 🤝 Cultural Dos & Don'ts")
        etiquette_list = country["etiquette"].split("\n")
        for et in etiquette_list:
            if et.strip():
                render_html(f"<div style='background-color:rgba(16, 185, 129, 0.05); padding:10px; border-left:3px solid #10B981; border-radius:4px; margin-bottom:10px;'>{et}</div>")

with tab_safety:
    st.markdown("### 🛡️ Safety & Travel Tips")
    tips_list = country["safety_tips"].split("\n")
    
    col_tips1, col_tips2 = st.columns(2)
    
    with col_tips1:
        st.markdown("#### 🌟 Health & Safety Guidelines")
        for tip in tips_list[:2]:
            if tip.strip():
                st.markdown(f"- {tip}")
                
    with col_tips2:
        st.markdown("#### 🗺️ Local Travel Warnings")
        for tip in tips_list[2:]:
            if tip.strip():
                st.markdown(f"- {tip}")
                
# List of available cities in this country as a quick jumping point
st.divider()
st.subheader(f"🏙️ Cities in {country['country_name']}")
cities = get_cities_by_country(country["id"])
if cities:
    ccols = st.columns(len(cities))
    for idx, city in enumerate(cities):
        with ccols[idx]:
            with st.container(border=True):
                st.markdown(f"**{city['city_name']}**")
                st.write(city["description"][:90] + "...")
                if st.button(f"Explore {city['city_name']}", key=f"c_btn_{city['id']}", use_container_width=True):
                    st.session_state.selected_city_id = city["id"]
                    st.switch_page("pages/city_info.py")
else:
    st.write("No cities found for this country.")
