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
    try:
        places = json.loads(city["tourist_places"])
        st.markdown("### 🎡 Top Attractions to Visit")
        
        # Grid of columns for attractions (2-column layout for spacious look)
        cols = st.columns(2)
        for idx, place in enumerate(places):
            col = cols[idx % 2]
            with col:
                badge_text = f"⭐ {place.get('rating', '4.5')}"
                if 'time' in place:
                    badge_text += f" | ⏰ {place['time']}"
                
                render_card(
                    title=f"📍 {place['name']}",
                    content=place["desc"],
                    badges=badge_text
                )
    except Exception as e:
        st.error("Error loading tourist places.")
        st.write(city["tourist_places"])
            
    st.markdown("---")
    
    try:
        shops = json.loads(city["shopping_areas"])
        st.markdown("### 🛍️ Famous Shopping Spots")
        
        # Grid of columns for shopping
        shop_cols = st.columns(2)
        for idx, shop in enumerate(shops):
            col = shop_cols[idx % 2]
            with col:
                render_card(
                    title=f"🛍️ {shop['name']}",
                    content=shop['desc'],
                    badges="Shopping Area"
                )
    except Exception as e:
        st.error("Error loading shopping areas.")
        st.write(city["shopping_areas"])

# 2. Local Food & Dining
with tab_food:
    try:
        foods = json.loads(city["food_info"])
        st.markdown("### 🍲 Must-Try Famous Dishes")
        
        # Categorize foods dynamically to avoid clutter
        veg_foods = []
        non_veg_foods = []
        other_foods = []
        
        for food in foods:
            ftype = food.get("type", "").lower()
            if "non-veg" in ftype:
                non_veg_foods.append(food)
            elif "veg" in ftype:
                veg_foods.append(food)
            else:
                other_foods.append(food)
        
        # Display side-by-side if both categories exist
        if veg_foods and non_veg_foods:
            col_veg, col_nonveg = st.columns(2)
            
            with col_veg:
                st.markdown("#### 🟢 Vegetarian Delights")
                for food in veg_foods:
                    render_card(
                        title=f"🍲 {food['name']}",
                        content=food["desc"],
                        badges=["Vegetarian"]
                    )
            
            with col_nonveg:
                st.markdown("#### 🔴 Non-Vegetarian Specials")
                for food in non_veg_foods:
                    render_card(
                        title=f"🍗 {food['name']}",
                        content=food["desc"],
                        badges=["Non-Vegetarian"]
                    )
                    
            if other_foods:
                st.markdown("#### 🌟 Local Favorites")
                other_cols = st.columns(2)
                for idx, food in enumerate(other_foods):
                    col = other_cols[idx % 2]
                    with col:
                        render_card(
                            title=f"🍽️ {food['name']}",
                            content=food["desc"],
                            badges=[food.get("type", "Local Spec")]
                        )
        else:
            # Fallback to standard clean 2-column grid if not mixed
            f_cols = st.columns(2)
            for i, food in enumerate(foods):
                col_idx = i % 2
                with f_cols[col_idx]:
                    ftype = food.get("type", "Local Spec")
                    emoji = "🍲"
                    if "non-veg" in ftype.lower():
                        emoji = "🍗"
                    elif "veg" in ftype.lower():
                        emoji = "🟢"
                    render_card(
                        title=f"{emoji} {food['name']}",
                        content=food["desc"],
                        badges=[ftype]
                    )
    except Exception as e:
        st.error("Error loading food details.")
        st.write(city["food_info"])

# 3. Recommended Stays (Hotels)
with tab_hotel:
    st.markdown("### 🏨 Recommended Accommodations")
    try:
        hotels = json.loads(city["hotel_info"])
        
        # Grid layout sorted from budget to luxury
        col_bud, col_mid, col_lux = st.columns(3)
        
        with col_bud:
            st.markdown("#### 🪙 Budget Friendly")
            bud = hotels.get("budget")
            if bud:
                render_card(
                    title=f"🏨 {bud['name']}",
                    content=bud["desc"],
                    price_badge=bud.get("price", "Budget")
                )
            else:
                st.caption("No budget accommodation listed.")
                
        with col_mid:
            st.markdown("#### 🏢 Mid-Range Comfort")
            mid = hotels.get("mid_range")
            if mid:
                render_card(
                    title=f"🏨 {mid['name']}",
                    content=mid["desc"],
                    price_badge=mid.get("price", "Mid-Range")
                )
            else:
                st.caption("No mid-range accommodation listed.")
                
        with col_lux:
            st.markdown("#### 💎 Luxury Stay")
            lux = hotels.get("luxury")
            if lux:
                render_card(
                    title=f"🏰 {lux['name']}",
                    content=lux["desc"],
                    price_badge=lux.get("price", "Luxury")
                )
            else:
                st.caption("No luxury accommodation listed.")
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
