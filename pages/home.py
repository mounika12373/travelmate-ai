import streamlit as st
from utils.database import get_all_countries, get_cities_by_country, search_locations
from utils.styles import render_hero, render_card, render_html, render_image_card


# Page Title inside sidebar context (optional, since router does it, but we can set content)
render_hero(
    "TravelMate AI", 
    "Discover essential local laws, cultural etiquette, transit guides, top foods, and safety advice before you arrive.",
    image_path="assets/travelmate_banner.png"
)

# 1. Quick Search Section
st.subheader("🔍 Quick Search")
search_input = st.text_input("Search for a country or city...", value="", placeholder="e.g., Tokyo, India, Biryani, temples...")

if search_input:
    results = search_locations(search_input)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("##### Matching Countries")
        if results["countries"]:
            for country in results["countries"]:
                country_name = country["country_name"]
                # Create a card with a button inside
                with st.container(border=True):
                    st.markdown(f"**🌍 {country_name}**")
                    st.write(f"Capital: {country['capital']} | Currency: {country['currency']}")
                    if st.button(f"Go to {country_name}", key=f"btn_c_{country['id']}", use_container_width=True):
                        st.session_state.selected_country_id = country["id"]
                        st.switch_page("pages/country_info.py")
        else:
            st.info("No matching countries found.")
            
    with col2:
        st.markdown("##### Matching Cities")
        if results["cities"]:
            for city in results["cities"]:
                city_name = city["city_name"]
                with st.container(border=True):
                    st.markdown(f"**🏙️ {city_name}** ({city['country_name']})")
                    st.write(city["description"][:100] + "...")
                    if st.button(f"Explore {city_name}", key=f"btn_ct_{city['id']}", use_container_width=True):
                        st.session_state.selected_country_id = city["country_id"]
                        st.session_state.selected_city_id = city["id"]
                        st.switch_page("pages/city_info.py")
        else:
            st.info("No matching cities found.")
    st.divider()

# 2. Main Navigation Selectors
st.subheader("🗺️ Destination Guide")
countries = get_all_countries()

if not countries:
    st.warning("No travel data available. Please initialize the database.")
else:
    # Selected country mapping
    country_names = [c["country_name"] for c in countries]
    
    # Get current selected index from session state
    selected_c_index = 0
    if st.session_state.selected_country_id:
        for idx, c in enumerate(countries):
            if c["id"] == st.session_state.selected_country_id:
                selected_c_index = idx
                break
                
    sel_col1, sel_col2 = st.columns(2)
    
    with sel_col1:
        selected_country_name = st.selectbox(
            "Select Country", 
            country_names, 
            index=selected_c_index,
            key="country_select"
        )
        # Find matching country object
        selected_country = next(c for c in countries if c["country_name"] == selected_country_name)
        st.session_state.selected_country_id = selected_country["id"]
        
        # Display short summary
        st.markdown(f"""
        **Capital:** {selected_country['capital']}  
        **Currency:** {selected_country['currency']}  
        **Language:** {selected_country['language']}  
        """)
        if st.button("📖 View Country Guide", use_container_width=True):
            st.switch_page("pages/country_info.py")
            
    with sel_col2:
        cities = get_cities_by_country(selected_country["id"])
        if cities:
            city_names = [ct["city_name"] for ct in cities]
            
            selected_ct_index = 0
            if st.session_state.selected_city_id:
                for idx, ct in enumerate(cities):
                    if ct["id"] == st.session_state.selected_city_id:
                        selected_ct_index = idx
                        break
            
            selected_city_name = st.selectbox(
                "Select City", 
                city_names, 
                index=selected_ct_index if selected_ct_index < len(city_names) else 0,
                key="city_select"
            )
            selected_city = next(ct for ct in cities if ct["city_name"] == selected_city_name)
            st.session_state.selected_city_id = selected_city["id"]
            
            st.markdown(f"""
            **Description:**  
            {selected_city['description'][:140]}...
            """)
            if st.button("🏙️ View City Details", use_container_width=True):
                st.switch_page("pages/city_info.py")
        else:
            st.info("No cities available for this country.")

st.divider()

# 3. Trending Destinations Showcase
st.subheader("⭐ Featured Destinations")

col_trend1, col_trend2, col_trend3 = st.columns(3)

with col_trend1:
    render_image_card(
        title="Shibuya, Tokyo",
        content="Experience the high-tech neon lights, historical shrines, and Michelin-starred culinary scene of Japan's heart.",
        image_path="assets/tokyo_city.png",
        badges=["4.9 ⭐", "Most Popular"]
    )
    if st.button("Explore Tokyo", key="trend_tokyo", use_container_width=True):
        tokyo_city = next((ct for c in get_cities_by_country(2) if ct["city_name"].lower() == "tokyo"), None)
        if tokyo_city:
            st.session_state.selected_country_id = 2 # Japan ID is 2
            st.session_state.selected_city_id = tokyo_city["id"]
            st.switch_page("pages/city_info.py")

with col_trend2:
    render_image_card(
        title="Old City, Hyderabad",
        content="Savor world-famous Biryani, stand before the historic Charminar, and buy pearls in Nizam's heritage bazaar.",
        image_path="assets/hyderabad_city.png",
        badges=["4.7 ⭐", "Cultural Choice"]
    )
    if st.button("Explore Hyderabad", key="trend_hyd", use_container_width=True):
        hyd_city = next((ct for ct in get_cities_by_country(1) if ct["city_name"].lower() == "hyderabad"), None)
        if hyd_city:
            st.session_state.selected_country_id = 1 # India ID is 1
            st.session_state.selected_city_id = hyd_city["id"]
            st.switch_page("pages/city_info.py")

with col_trend3:
    render_image_card(
        title="Garden City, Singapore",
        content="Walk through futuristic gardens, stand in awe of Marina Bay Sands, and discover local hawker food courts.",
        image_path="assets/singapore_city.png",
        badges=["4.8 ⭐", "Safest Destination"]
    )
    if st.button("Explore Singapore", key="trend_sg", use_container_width=True):
        sg_city = next((ct for ct in get_cities_by_country(3) if ct["city_name"].lower() == "singapore city"), None)
        if sg_city:
            st.session_state.selected_country_id = 3 # Singapore ID is 3
            st.session_state.selected_city_id = sg_city["id"]
            st.switch_page("pages/city_info.py")
