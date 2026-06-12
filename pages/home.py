import streamlit as st

from utils.database import get_all_countries, get_cities_by_country, search_locations
from utils.i18n import translate_ui
from utils.styles import render_hero, render_image_card

# Page Title inside sidebar context (optional, since router does it, but we can set content)
render_hero(
    "TravelMate AI",
    translate_ui("home_hero_subtitle"),
    image_path="assets/travelmate_banner.png"
)

# 1. Quick Search Section
st.subheader(translate_ui("quick_search"))
search_input = st.text_input(
    translate_ui("search_placeholder"),
    value="",
    placeholder=translate_ui("search_placeholder")
)

if search_input:
    results = search_locations(search_input)

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
            translate_ui("select_country"),
            country_names,
            index=selected_c_index if selected_c_index < len(country_names) else 0,
            key="country_select"
        )
        # Find matching country object
        selected_country = next(c for c in countries if c["country_name"] == selected_country_name)
        st.session_state.selected_country_id = selected_country["id"]

        # Display short summary
        st.markdown(f"""
        **{translate_ui('capital_label')}:** {selected_country['capital']}  
        **{translate_ui('currency_label')}:** {selected_country['currency']}  
        **{translate_ui('language_label')}:** {selected_country['language']}  
        """)
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
                key="city_select"
            )
            selected_city = next(ct for ct in cities if ct["city_name"] == selected_city_name)
            st.session_state.selected_city_id = selected_city["id"]

            st.markdown(f"""
            **{translate_ui('description') if 'description' in selected_city else 'Description'}:**  
            {selected_city['description'][:140]}...
            """)
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
        badges=["4.9 ⭐", translate_ui("most_popular")]
    )
    btn_label = translate_ui("explore_tokyo")
    if st.button(btn_label, key="trend_tokyo", use_container_width=True):
        tokyo_city = next((ct for c in get_cities_by_country(2) if ct["city_name"].lower() in ["tokyo", "टोक्यो", "టోక్యో"]), None)
        if tokyo_city:
            st.session_state.selected_country_id = 2 # Japan ID is 2
            st.session_state.selected_city_id = tokyo_city["id"]
            st.switch_page("pages/city_info.py")

with col_trend2:
    render_image_card(
        title=translate_ui("trend_hyd_title"),
        content=translate_ui("trend_hyd_desc"),
        image_path="assets/hyderabad_city.png",
        badges=["4.7 ⭐", translate_ui("cultural_choice")]
    )
    btn_label = translate_ui("explore_hyderabad")
    if st.button(btn_label, key="trend_hyd", use_container_width=True):
        hyd_city = next((ct for ct in get_cities_by_country(1) if ct["city_name"].lower() in ["hyderabad", "हैदराबाद", "హైదరాబాద్"]), None)
        if hyd_city:
            st.session_state.selected_country_id = 1 # India ID is 1
            st.session_state.selected_city_id = hyd_city["id"]
            st.switch_page("pages/city_info.py")

with col_trend3:
    render_image_card(
        title=translate_ui("trend_sg_title"),
        content=translate_ui("trend_sg_desc"),
        image_path="assets/singapore_city.png",
        badges=["4.8 ⭐", translate_ui("safest_destination")]
    )
    btn_label = translate_ui("explore_singapore")
    if st.button(btn_label, key="trend_sg", use_container_width=True):
        sg_city = next((ct for c in get_cities_by_country(3) if ct["city_name"].lower() in ["singapore city", "downtown core", "डाउनटाउन कोर", "డౌన్‌టౌన్ కోర్"]), None)
        if sg_city:
            st.session_state.selected_country_id = 3 # Singapore ID is 3
            st.session_state.selected_city_id = sg_city["id"]
            st.switch_page("pages/city_info.py")
