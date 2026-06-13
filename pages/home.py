import streamlit as st

from utils.database import get_all_countries, get_cities_by_country, search_locations
from utils.i18n import translate_ui
from utils.styles import render_hero, render_image_card

# Page Title inside sidebar context (optional, since router does it, but we can set content)
render_hero(
    "TravelMate AI",
<<<<<<< HEAD
    translate_ui("home_hero_subtitle"),
    image_path="assets/travelmate_banner.png"
)

# 1. Quick Search Section
st.subheader(translate_ui("quick_search"))
search_input = st.text_input(
    translate_ui("search_placeholder"),
    value="",
    placeholder=translate_ui("search_placeholder")
=======
    "Discover essential local laws, cultural etiquette, transit guides, top foods, and safety advice before you arrive.",
    image_path="assets/travelmate_banner.png",
)

# 1. Quick Search Section
st.subheader("🔍 Quick Search")
search_input = st.text_input(
    "Search for a country or city...", value="", placeholder="e.g., Tokyo, India, Biryani, temples..."
>>>>>>> be75e90 (Fix compliance checks and tooling)
)

if search_input:
    results = search_locations(search_input)
    if st.session_state.get("user") and st.session_state.get("last_logged_search") != search_input:
        from utils.database import log_activity
        log_activity(st.session_state.user["id"], "search", search_input)
        st.session_state.last_logged_search = search_input

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(translate_ui("matching_countries"))
        if results["countries"]:
            for country in results["countries"]:
                country_name = country["country_name"]
                # Create a card with a button inside
                with st.container(border=True):
                    st.markdown(f"**🌍 {country_name}**")
                    # Capital and Currency labels translated dynamically
                    st.write(f"{translate_ui('capital_label')}: {country['capital']} | {translate_ui('currency_label')}: {country['currency']}")
                    if st.session_state.get("user"):
                        from utils.database import save_trip, get_saved_trips
                        saved = get_saved_trips(st.session_state.user["id"], "destination")
                        is_saved = any(s["name"] == country_name for s in saved)
                        if is_saved:
                            st.caption("⭐️ Bookmarked")
                        else:
                            if st.button("Bookmark Country", key=f"bk_c_{country['id']}", use_container_width=True):
                                save_trip(st.session_state.user["id"], "destination", country_name, "My Saved Trips", {"country_id": country["id"], "description": f"Capital: {country['capital']}, Currency: {country['currency']}"})
                                st.success(f"Bookmarked {country_name}!")
                                st.rerun()
                    btn_label = translate_ui("go_to_country_btn").format(country=country_name)
                    if st.button(btn_label, key=f"btn_c_{country['id']}", use_container_width=True):
                        st.session_state.selected_country_id = country["id"]
                        st.switch_page("pages/country_info.py")
        else:
            st.info(translate_ui("no_matching_countries"))

    with col2:
        st.markdown(translate_ui("matching_cities"))
        if results["cities"]:
            for city in results["cities"]:
                city_name = city["city_name"]
                with st.container(border=True):
                    st.markdown(f"**🏙️ {city_name}** ({city['country_name']})")
                    st.write(city["description"][:100] + "...")
                    if st.session_state.get("user"):
                        from utils.database import save_trip, get_saved_trips
                        saved = get_saved_trips(st.session_state.user["id"], "destination")
                        is_saved = any(s["name"] == city_name for s in saved)
                        if is_saved:
                            st.caption("⭐️ Bookmarked")
                        else:
                            if st.button("Bookmark City", key=f"bk_ct_{city['id']}", use_container_width=True):
                                save_trip(st.session_state.user["id"], "destination", city_name, "My Saved Trips", {"city_id": city["id"], "country_id": city["country_id"], "description": city["description"]})
                                st.success(f"Bookmarked {city_name}!")
                                st.rerun()
                    btn_label = translate_ui("explore_city_btn").format(city=city_name)
                    if st.button(btn_label, key=f"btn_ct_{city['id']}", use_container_width=True):
                        st.session_state.selected_country_id = city["country_id"]
                        st.session_state.selected_city_id = city["id"]
                        st.switch_page("pages/city_info.py")
        else:
            st.info(translate_ui("no_matching_cities"))
    st.divider()

# 2. Main Navigation Selectors
st.subheader(translate_ui("destination_guide"))
countries = get_all_countries()

if not countries:
    st.warning(translate_ui("no_travel_data"))
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
<<<<<<< HEAD
            translate_ui("select_country"),
            country_names,
            index=selected_c_index if selected_c_index < len(country_names) else 0,
            key="country_select"
=======
            "Select Country", country_names, index=selected_c_index, key="country_select"
>>>>>>> be75e90 (Fix compliance checks and tooling)
        )
        # Find matching country object
        selected_country = next(c for c in countries if c["country_name"] == selected_country_name)
        st.session_state.selected_country_id = selected_country["id"]

        # Display short summary
        st.markdown(f"""
<<<<<<< HEAD
        **{translate_ui('capital_label')}:** {selected_country['capital']}  
        **{translate_ui('currency_label')}:** {selected_country['currency']}  
        **{translate_ui('language_label')}:** {selected_country['language']}  
=======
        **Capital:** {selected_country["capital"]}  
        **Currency:** {selected_country["currency"]}  
        **Language:** {selected_country["language"]}  
>>>>>>> be75e90 (Fix compliance checks and tooling)
        """)
        if st.session_state.get("user"):
            from utils.database import save_trip, get_saved_trips
            saved = get_saved_trips(st.session_state.user["id"], "destination")
            is_saved = any(s["name"] == selected_country_name for s in saved)
            if is_saved:
                st.caption("⭐️ Bookmarked")
            else:
                if st.button("Bookmark Country", key="bk_sel_c", use_container_width=True):
                    save_trip(st.session_state.user["id"], "destination", selected_country_name, "My Saved Trips", {"country_id": selected_country["id"], "description": f"Capital: {selected_country['capital']}, Currency: {selected_country['currency']}"})
                    st.success(f"Bookmarked {selected_country_name}!")
                    st.rerun()
        if st.button(translate_ui("view_country_guide"), use_container_width=True):
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
                translate_ui("select_city"),
                city_names,
                index=selected_ct_index if selected_ct_index < len(city_names) else 0,
                key="city_select",
            )
            selected_city = next(ct for ct in cities if ct["city_name"] == selected_city_name)
            st.session_state.selected_city_id = selected_city["id"]

            st.markdown(f"""
<<<<<<< HEAD
            **{translate_ui('description') if 'description' in selected_city else 'Description'}:**  
            {selected_city['description'][:140]}...
=======
            **Description:**  
            {selected_city["description"][:140]}...
>>>>>>> be75e90 (Fix compliance checks and tooling)
            """)
            if st.session_state.get("user"):
                from utils.database import save_trip, get_saved_trips
                saved = get_saved_trips(st.session_state.user["id"], "destination")
                is_saved = any(s["name"] == selected_city_name for s in saved)
                if is_saved:
                    st.caption("⭐️ Bookmarked")
                else:
                    if st.button("Bookmark City", key="bk_sel_ct", use_container_width=True):
                        save_trip(st.session_state.user["id"], "destination", selected_city_name, "My Saved Trips", {"city_id": selected_city["id"], "country_id": selected_city["country_id"], "description": selected_city["description"]})
                        st.success(f"Bookmarked {selected_city_name}!")
                        st.rerun()
            if st.button(translate_ui("view_city_details"), use_container_width=True):
                st.switch_page("pages/city_info.py")
        else:
            st.info(translate_ui("no_cities_warning"))

st.divider()

# 3. Trending Destinations Showcase
st.subheader(translate_ui("featured_destinations"))

col_trend1, col_trend2, col_trend3 = st.columns(3)

with col_trend1:
    render_image_card(
        title=translate_ui("trend_tokyo_title"),
        content=translate_ui("trend_tokyo_desc"),
        image_path="assets/tokyo_city.png",
<<<<<<< HEAD
        badges=["4.9 ⭐", translate_ui("most_popular")]
=======
        badges=["4.9 ⭐", "Most Popular"],
>>>>>>> be75e90 (Fix compliance checks and tooling)
    )
    btn_label = translate_ui("explore_tokyo")
    if st.button(btn_label, key="trend_tokyo", use_container_width=True):
        tokyo_city = next((ct for c in get_cities_by_country(2) if ct["city_name"].lower() in ["tokyo", "टोक्यो", "టోక్యో"]), None)
        if tokyo_city:
            st.session_state.selected_country_id = 2  # Japan ID is 2
            st.session_state.selected_city_id = tokyo_city["id"]
            st.switch_page("pages/city_info.py")

with col_trend2:
    render_image_card(
        title=translate_ui("trend_hyd_title"),
        content=translate_ui("trend_hyd_desc"),
        image_path="assets/hyderabad_city.png",
<<<<<<< HEAD
        badges=["4.7 ⭐", translate_ui("cultural_choice")]
=======
        badges=["4.7 ⭐", "Cultural Choice"],
>>>>>>> be75e90 (Fix compliance checks and tooling)
    )
    btn_label = translate_ui("explore_hyderabad")
    if st.button(btn_label, key="trend_hyd", use_container_width=True):
        hyd_city = next((ct for ct in get_cities_by_country(1) if ct["city_name"].lower() in ["hyderabad", "हैदराबाद", "హైదరాబాద్"]), None)
        if hyd_city:
            st.session_state.selected_country_id = 1  # India ID is 1
            st.session_state.selected_city_id = hyd_city["id"]
            st.switch_page("pages/city_info.py")

with col_trend3:
    render_image_card(
        title=translate_ui("trend_sg_title"),
        content=translate_ui("trend_sg_desc"),
        image_path="assets/singapore_city.png",
<<<<<<< HEAD
        badges=["4.8 ⭐", translate_ui("safest_destination")]
=======
        badges=["4.8 ⭐", "Safest Destination"],
>>>>>>> be75e90 (Fix compliance checks and tooling)
    )
    btn_label = translate_ui("explore_singapore")
    if st.button(btn_label, key="trend_sg", use_container_width=True):
        sg_city = next((ct for c in get_cities_by_country(3) if ct["city_name"].lower() in ["singapore city", "downtown core", "डाउनटाउन कोर", "డౌన్‌టౌన్ కోర్"]), None)
        if sg_city:
            st.session_state.selected_country_id = 3  # Singapore ID is 3
            st.session_state.selected_city_id = sg_city["id"]
            st.switch_page("pages/city_info.py")
