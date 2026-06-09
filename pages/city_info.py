import json
import streamlit as st
from utils.database import get_all_countries, get_cities_by_country, get_city_details
from utils.styles import render_hero, render_card, render_html

# Sidebar selectors for quick context changing
countries = get_all_countries()
if not countries:
    st.error("No countries available. Please seed database.")
    st.stop()

# Sync country
country_names = [c["country_name"] for c in countries]
current_c_index = 0
if st.session_state.selected_country_id:
    for idx, c in enumerate(countries):
        if c["id"] == st.session_state.selected_country_id:
            current_c_index = idx
            break

st.sidebar.subheader("Select Destination")
selected_country_name = st.sidebar.selectbox(
    "Country", 
    country_names, 
    index=current_c_index, 
    key="city_info_country_select"
)
selected_country = next(c for c in countries if c["country_name"] == selected_country_name)
st.session_state.selected_country_id = selected_country["id"]

# Fetch cities for chosen country
cities = get_cities_by_country(st.session_state.selected_country_id)
if not cities:
    st.sidebar.warning("No cities in this country.")
    st.stop()

city_names = [ct["city_name"] for ct in cities]
current_ct_index = 0
if st.session_state.selected_city_id:
    for idx, ct in enumerate(cities):
        if ct["id"] == st.session_state.selected_city_id:
            current_ct_index = idx
            break

selected_city_name = st.sidebar.selectbox(
    "City", 
    city_names, 
    index=current_ct_index if current_ct_index < len(city_names) else 0,
    key="city_info_city_select"
)
selected_city = next(ct for ct in cities if ct["city_name"] == selected_city_name)
st.session_state.selected_city_id = selected_city["id"]

# Load specific city details
city = get_city_details(st.session_state.selected_city_id)

# Hero section for the city
render_hero(city["city_name"], city["description"])

# City details layout
tab_attract, tab_food, tab_hotel, tab_transit = st.tabs([
    "🎡 Attractions & Shopping", 
    "🍲 Local Delicacies", 
    "🏨 Recommended Stays", 
    "🚌 Transit & Airport Guide"
])

# 1. Attractions & Shopping
with tab_attract:
    col_attr, col_shop = st.columns([2, 1])
    
    with col_attr:
        st.markdown("### 🎡 Major Tourist Attractions")
        try:
            places = json.loads(city["tourist_places"])
            for place in places:
                # Render using custom styling card helper
                badge_text = f"⭐ {place.get('rating', '4.5')}"
                if 'time' in place:
                    badge_text += f" | {place['time']}"
                
                render_card(
                    title=place["name"],
                    content=place["desc"],
                    badges=badge_text
                )
        except Exception as e:
            st.error("Error loading tourist places.")
            st.write(city["tourist_places"])
            
    with col_shop:
        st.markdown("### 🛍️ Famous Shopping Spots")
        try:
            shops = json.loads(city["shopping_areas"])
            for shop in shops:
                render_html(f"""
                    <div style="background-color: var(--secondary-background-color); border: 1px solid rgba(128,128,128,0.1); border-radius: 10px; padding: 15px; margin-bottom: 15px;">
                        <h5 style="margin: 0 0 5px 0; font-weight:600; font-size:1.05rem;">🛍️ {shop['name']}</h5>
                        <p style="margin: 0; font-size: 0.85rem; color: gray;">{shop['desc']}</p>
                    </div>
                """)
        except Exception as e:
            st.error("Error loading shopping areas.")
            st.write(city["shopping_areas"])

# 2. Local Food & Dining
with tab_food:
    st.markdown("### 🍲 Must-Try Famous Dishes")
    try:
        foods = json.loads(city["food_info"])
        # Grid of foods
        f_cols = st.columns(2)
        for i, food in enumerate(foods):
            col_idx = i % 2
            with f_cols[col_idx]:
                render_card(
                    title=food["name"],
                    content=food["desc"],
                    badges=[food["type"]]
                )
    except Exception as e:
        st.error("Error loading food details.")
        st.write(city["food_info"])

# 3. Recommended Stays (Hotels)
with tab_hotel:
    st.markdown("### 🏨 Recommended Accommodation options")
    try:
        hotels = json.loads(city["hotel_info"])
        
        col_lux, col_mid, col_bud = st.columns(3)
        
        with col_lux:
            st.markdown("##### 💎 Luxury (High-End)")
            lux = hotels.get("luxury")
            if lux:
                render_card(
                    title=lux["name"],
                    content=lux["desc"],
                    price_badge=lux.get("price", "Luxury")
                )
                
        with col_mid:
            st.markdown("##### 🏢 Mid-Range (Moderate)")
            mid = hotels.get("mid_range")
            if mid:
                render_card(
                    title=mid["name"],
                    content=mid["desc"],
                    price_badge=mid.get("price", "Mid-Range")
                )
                
        with col_bud:
            st.markdown("##### 🪙 Budget (Value)")
            bud = hotels.get("budget")
            if bud:
                render_card(
                    title=bud["name"],
                    content=bud["desc"],
                    price_badge=bud.get("price", "Budget")
                )
    except Exception as e:
        st.error("Error loading accommodation details.")
        st.write(city["hotel_info"])

# 4. Transit & Airport Guide
with tab_transit:
    col_airport, col_metro = st.columns(2)
    
    with col_airport:
        st.markdown("### ✈️ Airport Access Details")
        st.info(city["airport_details"])
        
    with col_metro:
        st.markdown("### 🚌 Local Public Transportation")
        st.success(city["transport_info"])
        
    st.subheader("🛡️ Safety Recommendations for " + city["city_name"])
    st.warning(city["safety_recommendations"])
