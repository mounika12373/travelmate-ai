import json

import pandas as pd
import plotly.express as px
import streamlit as st

from utils.database import get_all_countries, get_cities_by_country, get_city_details, get_country_details
from utils.i18n import translate_ui
from utils.styles import render_hero, render_html

# Render localized hero
render_hero(translate_ui("smart_planner_title"), translate_ui("smart_planner_subtitle"))

# Load destinations list
countries = get_all_countries()
all_cities = []
for c in countries:
    cities = get_cities_by_country(c["id"])
    for ct in cities:
        all_cities.append(
            {"id": ct["id"], "city_name": ct["city_name"], "country_name": c["country_name"], "country_id": c["id"]}
        )

if not all_cities:
    st.error(translate_ui("no_cities_warning"))
    st.stop()

# 1. Inputs Section
st.subheader(translate_ui("customize_trip"))
col_in1, col_in2, col_in3 = st.columns(3)

with col_in1:
    city_options = [f"{c['city_name']} ({c['country_name']})" for c in all_cities]
    selected_option = st.selectbox(translate_ui("where_to_go"), city_options)

    # Extract selected city details
    sel_city_index = city_options.index(selected_option)
    selected_city_meta = all_cities[sel_city_index]
    city_id = selected_city_meta["id"]
    city = get_city_details(city_id)
    country = get_country_details(city["country_id"])

with col_in2:
    num_days = st.slider(translate_ui("number_of_days"), min_value=1, max_value=7, value=3)

with col_in3:
    economy_label = translate_ui("budget_economy")
    mid_range_label = translate_ui("budget_mid_range")
    luxury_label = translate_ui("budget_luxury")

    budget_tier = st.selectbox(translate_ui("choose_budget_tier"), [economy_label, mid_range_label, luxury_label])
    # Simplify budget string key
    if budget_tier == economy_label:
        budget_key = "budget"
        budget_tier_display = "Economy"
    elif budget_tier == mid_range_label:
        budget_key = "mid_range"
        budget_tier_display = "Mid-Range"
    else:
        budget_key = "luxury"
        budget_tier_display = "Luxury"

st.divider()

# Process data
try:
    attractions = json.loads(city["tourist_places"])
except Exception:
    attractions = []

try:
    hotels = json.loads(city["hotel_info"])
except Exception:
    hotels = {}

try:
    shopping = json.loads(city["shopping_areas"])
except Exception:
    shopping = []

try:
    foods = json.loads(city["food_info"])
except Exception:
    foods = []

# Dynamic Budget calculations
currency_symbol = "S$"
currency_code = "SGD"
base_daily_rates = {}  # Rates in local currency

# Note: country name might be returned translated! Check orig name or check both
c_name_lower = country["country_name"].lower()
is_india = c_name_lower in ["india", "भारत", "భారతదేశం"]
is_japan = c_name_lower in ["japan", "जापान", "జపాన్"]

if is_india:
    currency_symbol = "₹"
    currency_code = "INR"
    if budget_key == "budget":
        base_daily_rates = {"accommodation": 3000, "food": 1000, "transport": 400, "sightseeing": 500, "shopping": 600}
    elif budget_key == "mid_range":
        base_daily_rates = {
            "accommodation": 7500,
            "food": 2500,
            "transport": 1200,
            "sightseeing": 1500,
            "shopping": 2000,
        }
    else:
        base_daily_rates = {
            "accommodation": 25000,
            "food": 6000,
            "transport": 4000,
            "sightseeing": 4000,
            "shopping": 8000,
        }

elif is_japan:
    currency_symbol = "¥"
    currency_code = "JPY"
    if budget_key == "budget":
        base_daily_rates = {
            "accommodation": 6500,
            "food": 3000,
            "transport": 1000,
            "sightseeing": 1500,
            "shopping": 1500,
        }
    elif budget_key == "mid_range":
        base_daily_rates = {
            "accommodation": 22000,
            "food": 8000,
            "transport": 2500,
            "sightseeing": 4000,
            "shopping": 5000,
        }
    else:
        base_daily_rates = {
            "accommodation": 80000,
            "food": 20000,
            "transport": 10000,
            "sightseeing": 12000,
            "shopping": 15000,
        }

else:  # Singapore
    currency_symbol = "S$"
    currency_code = "SGD"
    if budget_key == "budget":
        base_daily_rates = {"accommodation": 120, "food": 30, "transport": 10, "sightseeing": 20, "shopping": 20}
    elif budget_key == "mid_range":
        base_daily_rates = {"accommodation": 280, "food": 75, "transport": 25, "sightseeing": 50, "shopping": 60}
    else:
        base_daily_rates = {"accommodation": 800, "food": 200, "transport": 90, "sightseeing": 150, "shopping": 250}

# Calculate total budget
accommodation_cost = base_daily_rates["accommodation"] * num_days
food_cost = base_daily_rates["food"] * num_days
transport_cost = base_daily_rates["transport"] * num_days
sightseeing_cost = base_daily_rates["sightseeing"] * num_days
shopping_cost = base_daily_rates["shopping"] * num_days

total_budget = accommodation_cost + food_cost + transport_cost + sightseeing_cost + shopping_cost

# Present Layout
col_plan, col_budget = st.columns([3, 2])

with col_plan:
    st.markdown(translate_ui("custom_itinerary").format(days=num_days, city=city["city_name"]))

    # Hotel recommendation
    hotel_suggestion = hotels.get(
        budget_key, {"name": "Local Stay", "desc": "Conveniently located accommodation.", "price": ""}
    )
    rec_stay_lbl = translate_ui("recommended_stay_label").format(tier=budget_tier_display)
    st.info(
        f"🏨 **{rec_stay_lbl}** **{hotel_suggestion['name']}**\n\n*{hotel_suggestion['desc']}* (Est: {hotel_suggestion.get('price', '')})"
    )
    st.write("")

    # Distribute elements dynamically
    for day in range(1, num_days + 1):
        day_hdr = translate_ui("day_title").format(day=day)
        render_html(f"""
            <div class="timeline-day">
                <h4 style="color: var(--primary-color); margin-top:0;">{day_hdr}</h4>
            </div>
        """)

        # Determine morning/afternoon attractions based on index
        attract_indices = [(day * 2 - 2) % len(attractions), (day * 2 - 1) % len(attractions)] if attractions else []
        morning_att = attractions[attract_indices[0]] if len(attract_indices) > 0 and attractions else None
        afternoon_att = attractions[attract_indices[1]] if len(attract_indices) > 1 and attractions else None

        # Get food option
        food_opt = foods[(day - 1) % len(foods)] if foods else None
        # Get shopping option
        shop_opt = shopping[(day - 1) % len(shopping)] if shopping else None

        # Details
        if morning_att:
            morn_lbl = translate_ui("morning_activity").format(name=morning_att["name"])
            st.markdown(f"**{morn_lbl}**")
            st.caption(f"{morning_att['desc']} (Rating: {morning_att.get('rating', '4.5')})")

        if food_opt:
            lunch_lbl = translate_ui("lunch_activity").format(name=food_opt["name"])
            st.markdown(f"**{lunch_lbl}**")
            st.caption(f"{food_opt['desc']}")

        if afternoon_att:
            aft_lbl = translate_ui("afternoon_activity").format(name=afternoon_att["name"])
            st.markdown(f"**{aft_lbl}**")
            st.caption(f"{afternoon_att['desc']} (Rating: {afternoon_att.get('rating', '4.5')})")

        if shop_opt:
            eve_lbl = translate_ui("evening_shop").format(name=shop_opt["name"])
            st.markdown(f"**{eve_lbl}**")
            st.caption(f"{shop_opt['desc']}")
        else:
            st.markdown(f"**{translate_ui('evening_free')}**")
            st.caption(translate_ui("evening_free_desc"))

        st.divider()

with col_budget:
    st.markdown(translate_ui("estimated_budget_breakdown"))

    # Display Key Metrics
    total_est_exp = translate_ui("total_estimated_expenses")
    details_lbl = translate_ui("for_days_tier").format(days=num_days, tier=budget_tier_display)
    render_html(f"""
        <div style="background-color: var(--secondary-background-color); border: 2px solid var(--primary-color); border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 25px;">
            <div style="font-size: 0.9rem; color: gray; text-transform: uppercase;">{total_est_exp}</div>
            <div style="font-size: 2.2rem; font-weight: 800; color: var(--primary-color);">{currency_symbol} {total_budget:,} {currency_code}</div>
            <div style="font-size: 0.85rem; color: gray; margin-top:5px;">{details_lbl}</div>
        </div>
    """)

    # Dataframe for table and chart
    budget_data = {
        "Expense Category": [
            translate_ui("category_accommodation"),
            translate_ui("category_food"),
            translate_ui("category_transport"),
            translate_ui("category_sightseeing"),
            translate_ui("category_shopping"),
        ],
        "Amount": [accommodation_cost, food_cost, transport_cost, sightseeing_cost, shopping_cost],
    }
    df_budget = pd.DataFrame(budget_data)

    # Plotly pie chart
    fig = px.pie(
        df_budget,
        values="Amount",
        names="Expense Category",
        color_discrete_sequence=px.colors.qualitative.Pastel,
        hole=0.4,
    )
    fig.update_layout(
        margin=dict(t=0, b=0, l=0, r=0),
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )

    st.plotly_chart(fig, use_container_width=True)

    # Cost Table
    st.markdown(translate_ui("detailed_allocation_table"))
    formatted_df = df_budget.copy()
    formatted_df["Amount"] = formatted_df["Amount"].apply(lambda x: f"{currency_symbol} {x:,} {currency_code}")
    st.table(formatted_df)

    # Local Transit & Safety Warning Card
    st.markdown(translate_ui("important_travel_tips"))
    with st.container(border=True):
        st.markdown(f"**{translate_ui('airport_transfer_label')}** {city['airport_details']}")
        st.markdown(f"**{translate_ui('city_transit_label')}** {city['transport_info']}")

# Track and Auto-Log Generated Itinerary
current_combination = f"{city_id}_{num_days}_{budget_key}"
if st.session_state.get("last_logged_itinerary_combination") != current_combination:
    if st.session_state.get("user"):
        from utils.database import log_activity

        details_log = {
            "days": num_days,
            "budget_tier": budget_tier_display,
            "city_id": city_id,
            "itinerary_text": f"Generated {num_days} Days itinerary in {city['city_name']} ({budget_tier_display}).",
            "budget_breakdown": budget_data,
        }
        log_activity(
            st.session_state.user["id"],
            "itinerary",
            f"{num_days} Days in {city['city_name']} ({budget_tier_display})",
            details_log,
        )
    st.session_state.last_logged_itinerary_combination = current_combination

# Save to Collection Form (Available for Authenticated Users)
if st.session_state.get("user"):
    from datetime import date

    with col_budget:
        st.divider()
        st.markdown("### 💾 Save to Travel Collections")
        from utils.database import get_saved_trips, save_trip

        saved_trips = get_saved_trips(st.session_state.user["id"])
        collections = list({t["collection_name"] for t in saved_trips})
        if "My Saved Trips" not in collections:
            collections.append("My Saved Trips")

        with st.form("save_itinerary_form"):
            target_col = st.selectbox("Select Collection Folder", collections)
            custom_col_name = st.text_input("Or create a new collection", placeholder="e.g. Summer Kyoto 2026")
            travel_date_val = st.date_input("Select travel date", value=date.today())

            save_it_btn = st.form_submit_button("Save Trip, Hotel & Flights")

            if save_it_btn:
                col_name = custom_col_name.strip() if custom_col_name.strip() else target_col

                # 1. Save Itinerary
                it_details = {
                    "days": num_days,
                    "budget_tier": budget_tier_display,
                    "city_id": city_id,
                    "itinerary_text": f"Itinerary for {num_days} days in {city['city_name']} ({budget_tier_display})",
                    "budget_breakdown": budget_data,
                }
                save_trip(
                    user_id=st.session_state.user["id"],
                    trip_type="itinerary",
                    name=f"{num_days} Days in {city['city_name']}",
                    collection_name=col_name,
                    details=it_details,
                    travel_date=travel_date_val.strftime("%Y-%m-%d"),
                )

                # 2. Save Recommended Hotel
                hotel_details = {"desc": hotel_suggestion.get("desc", ""), "price": hotel_suggestion.get("price", "")}
                save_trip(
                    user_id=st.session_state.user["id"],
                    trip_type="hotel",
                    name=hotel_suggestion["name"],
                    collection_name=col_name,
                    details=hotel_details,
                )

                # 3. Save Flight Recommendation
                flight_details = {
                    "airline": "TravelMate AI Charter",
                    "departure_time": "09:30 AM",
                    "arrival_time": "12:15 PM",
                    "price": "S$ 220"
                    if currency_code == "SGD"
                    else ("₹ 9,000" if currency_code == "INR" else "¥ 24,000"),
                }
                save_trip(
                    user_id=st.session_state.user["id"],
                    trip_type="flight",
                    name=f"Flight to {city['city_name']}",
                    collection_name=col_name,
                    details=flight_details,
                )

                st.success(f"Successfully saved to '{col_name}'!")
                st.rerun()
