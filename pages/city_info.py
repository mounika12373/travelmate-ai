import json

import streamlit as st

from utils.database import get_all_countries, get_cities_by_country, get_city_details
from utils.i18n import translate_ui
from utils.styles import render_card, render_hero


def make_maps_link(item_name, city_name):
    query = f"{item_name} {city_name}".replace(" ", "+")
    return f"<a href='https://www.google.com/maps/search/?api=1&query={query}' target='_blank' style='text-decoration:none; color:var(--primary-color); font-weight:600; font-size:0.88rem; display:inline-block; margin-top:5px;'>🗺️ Location & Directions ↗</a>"


# Sidebar selectors for quick context changing
countries = get_all_countries()
if not countries:
    st.error(translate_ui("no_travel_data"))
    st.stop()

# Sync country
country_names = [c["country_name"] for c in countries]
current_c_index = 0
if st.session_state.selected_country_id:
    for idx, c in enumerate(countries):
        if c["id"] == st.session_state.selected_country_id:
            current_c_index = idx
            break

st.sidebar.subheader(translate_ui("select_destination"))
selected_country_name = st.sidebar.selectbox(
<<<<<<< HEAD
    translate_ui("country_label"),
    country_names,
    index=current_c_index if current_c_index < len(country_names) else 0,
    key="city_info_country_select"
=======
    "Country", country_names, index=current_c_index, key="city_info_country_select"
>>>>>>> be75e90 (Fix compliance checks and tooling)
)
selected_country = next(c for c in countries if c["country_name"] == selected_country_name)
st.session_state.selected_country_id = selected_country["id"]

# Fetch cities for chosen country
cities = get_cities_by_country(st.session_state.selected_country_id)
if not cities:
    st.sidebar.warning(translate_ui("no_cities_warning"))
    st.stop()

city_names = [ct["city_name"] for ct in cities]
current_ct_index = 0
if st.session_state.selected_city_id:
    for idx, ct in enumerate(cities):
        if ct["id"] == st.session_state.selected_city_id:
            current_ct_index = idx
            break

selected_city_name = st.sidebar.selectbox(
<<<<<<< HEAD
    translate_ui("city_label"),
    city_names,
    index=current_ct_index if current_ct_index < len(city_names) else 0,
    key="city_info_city_select"
=======
    "City", city_names, index=current_ct_index if current_ct_index < len(city_names) else 0, key="city_info_city_select"
>>>>>>> be75e90 (Fix compliance checks and tooling)
)
selected_city = next(ct for ct in cities if ct["city_name"] == selected_city_name)
st.session_state.selected_city_id = selected_city["id"]

# Load specific city details
city = get_city_details(st.session_state.selected_city_id)

# Track and Auto-Log City Info exploration
if st.session_state.get("user"):
    from utils.database import log_activity
    current_exploration = f"explore_city_{city['id']}"
    if st.session_state.get("last_logged_exploration") != current_exploration:
        log_activity(st.session_state.user["id"], "search", f"Explored city details: {city['city_name']}")
        st.session_state.last_logged_exploration = current_exploration

# Hero section for the city
render_hero(city["city_name"], city["description"])

# City details layout
<<<<<<< HEAD
tab_attract, tab_food, tab_hotel, tab_transit = st.tabs([
    translate_ui("attractions_tab"),
    translate_ui("food_tab"),
    translate_ui("stays_tab"),
    translate_ui("transit_tab")
])
=======
tab_attract, tab_food, tab_hotel, tab_transit = st.tabs(
    ["🎡 Attractions & Shopping", "🍲 Local Delicacies", "🏨 Recommended Stays", "🚌 Transit & Airport Guide"]
)
>>>>>>> be75e90 (Fix compliance checks and tooling)

# 1. Attractions & Shopping
with tab_attract:
    try:
        places = json.loads(city["tourist_places"])
        st.markdown(translate_ui("top_attractions"))

        # Grid of columns for attractions (2-column layout for spacious look)
        cols = st.columns(2)
        for idx, place in enumerate(places):
            col = cols[idx % 2]
            with col:
                badge_text = f"⭐ {place.get('rating', '4.5')}"
                if "time" in place:
                    badge_text += f" | ⏰ {place['time']}"

                render_card(
                    title=f"📍 {place['name']}",
                    content=place["desc"],
                    badges=badge_text,
                    extra_html=make_maps_link(place["name"], city["city_name"]),
                )
    except Exception:
        st.error("Error loading tourist places.")
        st.write(city["tourist_places"])

    st.markdown("---")

    try:
        shops = json.loads(city["shopping_areas"])
        st.markdown(translate_ui("famous_shopping"))

        # Grid of columns for shopping
        shop_cols = st.columns(2)
        for idx, shop in enumerate(shops):
            col = shop_cols[idx % 2]
            with col:
                render_card(
                    title=f"🛍️ {shop['name']}",
<<<<<<< HEAD
                    content=shop['desc'],
                    badges=translate_ui("shopping_area_badge"),
                    extra_html=make_maps_link(shop['name'], city['city_name'])
=======
                    content=shop["desc"],
                    badges="Shopping Area",
                    extra_html=make_maps_link(shop["name"], city["city_name"]),
>>>>>>> be75e90 (Fix compliance checks and tooling)
                )
    except Exception:
        st.error("Error loading shopping areas.")
        st.write(city["shopping_areas"])

# 2. Local Food & Dining
with tab_food:
    try:
        foods = json.loads(city["food_info"])
        st.markdown(translate_ui("must_try_dishes"))

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
                st.markdown(translate_ui("veg_delights"))
                for food in veg_foods:
<<<<<<< HEAD
                    render_card(
                        title=f"🍲 {food['name']}",
                        content=food["desc"],
                        badges=[translate_ui("vegetarian_badge")]
                    )
=======
                    render_card(title=f"🍲 {food['name']}", content=food["desc"], badges=["Vegetarian"])
>>>>>>> be75e90 (Fix compliance checks and tooling)

            with col_nonveg:
                st.markdown(translate_ui("non_veg_specials"))
                for food in non_veg_foods:
<<<<<<< HEAD
                    render_card(
                        title=f"🍗 {food['name']}",
                        content=food["desc"],
                        badges=[translate_ui("non_vegetarian_badge")]
                    )
=======
                    render_card(title=f"🍗 {food['name']}", content=food["desc"], badges=["Non-Vegetarian"])
>>>>>>> be75e90 (Fix compliance checks and tooling)

            if other_foods:
                st.markdown(translate_ui("local_favorites"))
                other_cols = st.columns(2)
                for idx, food in enumerate(other_foods):
                    col = other_cols[idx % 2]
                    with col:
                        render_card(
                            title=f"🍽️ {food['name']}", content=food["desc"], badges=[food.get("type", "Local Spec")]
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
                        trans_badge = translate_ui("non_vegetarian_badge")
                    elif "veg" in ftype.lower():
                        emoji = "🟢"
<<<<<<< HEAD
                        trans_badge = translate_ui("vegetarian_badge")
                    else:
                        trans_badge = ftype
                    render_card(
                        title=f"{emoji} {food['name']}",
                        content=food["desc"],
                        badges=[trans_badge]
                    )
=======
                    render_card(title=f"{emoji} {food['name']}", content=food["desc"], badges=[ftype])
>>>>>>> be75e90 (Fix compliance checks and tooling)
    except Exception:
        st.error("Error loading food details.")
        st.write(city["food_info"])

# 3. Recommended Stays (Hotels)
with tab_hotel:
    st.markdown(translate_ui("recommended_accommodations"))
    try:
        hotels = json.loads(city["hotel_info"])

        # Grid layout sorted from budget to luxury
        col_bud, col_mid, col_lux = st.columns(3)

        with col_bud:
            st.markdown(translate_ui("budget_friendly"))
            bud = hotels.get("budget")
            if bud:
                render_card(
                    title=f"🏨 {bud['name']}",
                    content=bud["desc"],
                    price_badge=bud.get("price", "Budget"),
                    extra_html=make_maps_link(bud["name"], city["city_name"]),
                )
            else:
                st.caption("No budget accommodation listed.")

        with col_mid:
            st.markdown(translate_ui("mid_range_comfort"))
            mid = hotels.get("mid_range")
            if mid:
                render_card(
                    title=f"🏨 {mid['name']}",
                    content=mid["desc"],
                    price_badge=mid.get("price", "Mid-Range"),
                    extra_html=make_maps_link(mid["name"], city["city_name"]),
                )
            else:
                st.caption("No mid-range accommodation listed.")

        with col_lux:
            st.markdown(translate_ui("luxury_stay"))
            lux = hotels.get("luxury")
            if lux:
                render_card(
                    title=f"🏰 {lux['name']}",
                    content=lux["desc"],
                    price_badge=lux.get("price", "Luxury"),
                    extra_html=make_maps_link(lux["name"], city["city_name"]),
                )
            else:
                st.caption("No luxury accommodation listed.")
    except Exception:
        st.error("Error loading accommodation details.")
        st.write(city["hotel_info"])

# 4. Transit & Airport Guide
with tab_transit:
    import re

    def to_bullets(text):
        if not text:
            return ""
<<<<<<< HEAD
        # Split by period followed by whitespace and a capital letter or localized letters
        sentences = re.split(r'\.\s+(?=[A-Z]|[\u0900-\u097F]|[\u0C00-\u0C7F])', text.strip())
        return "\n".join(["- " + s.rstrip('.') + "." for s in sentences if s.strip()])
=======
        # Split by period followed by whitespace and a capital letter
        sentences = re.split(r"\.\s+(?=[A-Z])", text.strip())
        return "\n".join(["- " + s.rstrip(".") + "." for s in sentences if s.strip()])
>>>>>>> be75e90 (Fix compliance checks and tooling)

    col_airport, col_metro = st.columns(2)

    with col_airport:
        st.markdown(translate_ui("airport_access"))
        st.info(to_bullets(city["airport_details"]))

    with col_metro:
        st.markdown(translate_ui("public_transport"))
        st.success(to_bullets(city["transport_info"]))

    st.subheader(translate_ui("safety_recommendations_for") + city["city_name"])
    st.warning(to_bullets(city["safety_recommendations"]))
