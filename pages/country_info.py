import streamlit as st

from utils.database import get_all_countries, get_cities_by_country, get_country_details
from utils.i18n import translate_ui
from utils.styles import render_hero, render_html

# Sidebar Country Quick Selector
countries = get_all_countries()
if not countries:
    st.error(translate_ui("no_travel_data"))
    st.stop()

country_names = [c["country_name"] for c in countries]
current_c_index = 0
if st.session_state.selected_country_id:
    for idx, c in enumerate(countries):
        if c["id"] == st.session_state.selected_country_id:
            current_c_index = idx
            break

st.sidebar.subheader(translate_ui("explore_another_country"))
selected_country_name = st.sidebar.selectbox(
    translate_ui("select_country"),
    country_names,
    index=current_c_index if current_c_index < len(country_names) else 0,
    key="country_info_select",
)

# Sync with state
selected_country = next(c for c in countries if c["country_name"] == selected_country_name)
st.session_state.selected_country_id = selected_country["id"]

# Fetch latest country details
country = get_country_details(st.session_state.selected_country_id)

# Track and Auto-Log Country Info exploration
if st.session_state.get("user"):
    from utils.database import log_activity

    current_exploration = f"explore_country_{country['id']}"
    if st.session_state.get("last_logged_exploration") != current_exploration:
        log_activity(st.session_state.user["id"], "search", f"Explored country details: {country['country_name']}")
        st.session_state.last_logged_exploration = current_exploration

# Hero header for the country
title_text = translate_ui("explore_country_title").format(country=country["country_name"])
sub_text = translate_ui("country_hero_subtitle").format(country=country["country_name"])
render_hero(title_text, sub_text)

# 1. Quick Facts Grid
st.markdown(translate_ui("country_profile"))
qcol1, qcol2, qcol3, qcol4 = st.columns(4)

with qcol1:
    render_html(f"""
        <div class="metric-box">
            <div class="metric-label">{translate_ui("capital_label")}</div>
            <div class="metric-value">🏛️ {country["capital"]}</div>
        </div>
    """)
with qcol2:
    render_html(f"""
        <div class="metric-box">
            <div class="metric-label">{translate_ui("currency_label")}</div>
            <div class="metric-value">💵 {country["currency"]}</div>
        </div>
    """)
with qcol3:
    render_html(f"""
        <div class="metric-box">
            <div class="metric-label">{translate_ui("language_label")}</div>
            <div class="metric-value">🗣️ {country["language"]}</div>
        </div>
    """)
with qcol4:
    render_html(f"""
        <div class="metric-box">
            <div class="metric-label">{translate_ui("timezone_label")}</div>
            <div class="metric-value">⏰ {country["timezone"]}</div>
        </div>
    """)

st.write("")

# Emergency numbers highlighted
st.warning(f"{translate_ui('emergency_numbers_label')} {country['emergency_number']}")

# 2. Main Content Tabs
tab_visa, tab_rules, tab_safety = st.tabs(
    [translate_ui("visa_tab"), translate_ui("rules_tab"), translate_ui("safety_tab")]
)

with tab_visa:
    st.markdown(translate_ui("visa_requirements_title"))
    st.info(country["visa_info"])

    st.markdown(translate_ui("pre_departure_checklist"))
    is_sg = country["country_name"].lower() in ["singapore", "సింగపూర్", "सिंगापुर"]
    visa_form_msg = translate_ui("checklist_visa_sg") if is_sg else translate_ui("checklist_visa_evisa")
    st.markdown(f"""
    - [ ] {translate_ui("checklist_passport")}
    - [ ] {visa_form_msg}
    - [ ] {translate_ui("checklist_insurance")}
    - [ ] {translate_ui("checklist_bank")}
    """)

with tab_rules:
    col_rules, col_etiquette = st.columns(2)

    with col_rules:
        st.markdown(translate_ui("important_rules_title"))
        rules_list = country["rules"].split("\n")
        for rule in rules_list:
            if rule.strip():
                render_html(
                    f"<div style='background-color:rgba(239, 68, 68, 0.05); padding:10px; border-left:3px solid #EF4444; border-radius:4px; margin-bottom:10px;'>{rule}</div>"
                )

    with col_etiquette:
        st.markdown(translate_ui("cultural_dos_donts"))
        etiquette_list = country["etiquette"].split("\n")
        for et in etiquette_list:
            if et.strip():
                render_html(
                    f"<div style='background-color:rgba(16, 185, 129, 0.05); padding:10px; border-left:3px solid #10B981; border-radius:4px; margin-bottom:10px;'>{et}</div>"
                )

with tab_safety:
    st.markdown(translate_ui("safety_tab"))
    tips_list = country["safety_tips"].split("\n")

    col_tips1, col_tips2 = st.columns(2)

    with col_tips1:
        st.markdown(translate_ui("health_safety_guidelines"))
        for tip in tips_list[:2]:
            if tip.strip():
                st.markdown(f"- {tip}")

    with col_tips2:
        st.markdown(translate_ui("local_travel_warnings"))
        for tip in tips_list[2:]:
            if tip.strip():
                st.markdown(f"- {tip}")

# List of available cities in this country as a quick jumping point
st.divider()

st.subheader(translate_ui("cities_in_country").format(country=country["country_name"]))

cities = get_cities_by_country(country["id"])

if cities:
    ccols = st.columns(len(cities))

    for idx, city in enumerate(cities):
        with ccols[idx]:
            with st.container(border=True):
                st.markdown(f"**{city['city_name']}**")

                st.write(city["description"][:90] + "...")

                btn_lbl = translate_ui("explore_city_btn").format(city=city["city_name"])

                if st.button(
                    btn_lbl,
                    key=f"c_btn_{city['id']}",
                    use_container_width=True,
                ):
                    st.session_state.selected_city_id = city["id"]
                    st.switch_page("pages/city_info.py")
else:
    st.write(translate_ui("no_cities_warning"))
