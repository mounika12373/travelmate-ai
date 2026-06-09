import json
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.database import get_all_countries, get_cities_by_country, get_city_details, get_country_details
from utils.styles import render_hero, render_html

render_hero("📅 Smart Travel Planner", "Plan your custom itinerary, calculate your budget breakdown, and view customized hotel recommendations.")

# Load destinations list
countries = get_all_countries()
all_cities = []
for c in countries:
    cities = get_cities_by_country(c["id"])
    for ct in cities:
        all_cities.append({
            "id": ct["id"],
            "city_name": ct["city_name"],
            "country_name": c["country_name"],
            "country_id": c["id"]
        })

if not all_cities:
    st.error("No cities available in the database. Please seed the database.")
    st.stop()

# 1. Inputs Section
st.subheader("⚙️ Customize Your Trip")
col_in1, col_in2, col_in3 = st.columns(3)

with col_in1:
    city_options = [f"{c['city_name']} ({c['country_name']})" for c in all_cities]
    selected_option = st.selectbox("Where do you want to go?", city_options)
    
    # Extract selected city details
    sel_city_index = city_options.index(selected_option)
    selected_city_meta = all_cities[sel_city_index]
    city_id = selected_city_meta["id"]
    city = get_city_details(city_id)
    country = get_country_details(city["country_id"])

with col_in2:
    num_days = st.slider("Number of Days", min_value=1, max_value=7, value=3)

with col_in3:
    budget_tier = st.selectbox(
        "Choose Budget Tier", 
        ["Economy (Cost-Effective)", "Mid-Range (Balanced)", "Luxury (Premium Experience)"]
    )
    # Simplify budget string key
    budget_key = "budget" if "Economy" in budget_tier else ("mid_range" if "Mid-Range" in budget_tier else "luxury")

st.divider()

# Process data
try:
    attractions = json.loads(city["tourist_places"])
except:
    attractions = []

try:
    hotels = json.loads(city["hotel_info"])
except:
    hotels = {}

try:
    shopping = json.loads(city["shopping_areas"])
except:
    shopping = []

try:
    foods = json.loads(city["food_info"])
except:
    foods = []

# Dynamic Budget calculations
currency_symbol = "S$"
currency_code = "SGD"
base_daily_rates = {} # Rates in local currency

if country["country_name"].lower() == "india":
    currency_symbol = "₹"
    currency_code = "INR"
    if budget_key == "budget":
        base_daily_rates = {"accommodation": 3000, "food": 1000, "transport": 400, "sightseeing": 500, "shopping": 600}
    elif budget_key == "mid_range":
        base_daily_rates = {"accommodation": 7500, "food": 2500, "transport": 1200, "sightseeing": 1500, "shopping": 2000}
    else:
        base_daily_rates = {"accommodation": 25000, "food": 6000, "transport": 4000, "sightseeing": 4000, "shopping": 8000}
        
elif country["country_name"].lower() == "japan":
    currency_symbol = "¥"
    currency_code = "JPY"
    if budget_key == "budget":
        base_daily_rates = {"accommodation": 6500, "food": 3000, "transport": 1000, "sightseeing": 1500, "shopping": 1500}
    elif budget_key == "mid_range":
        base_daily_rates = {"accommodation": 22000, "food": 8000, "transport": 2500, "sightseeing": 4000, "shopping": 5000}
    else:
        base_daily_rates = {"accommodation": 80000, "food": 20000, "transport": 10000, "sightseeing": 12000, "shopping": 15000}

else: # Singapore
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
    st.markdown(f"### 🗺️ Custom Itinerary: {num_days} Days in {city['city_name']}")
    
    # Hotel recommendation
    hotel_suggestion = hotels.get(budget_key, {"name": "Local Stay", "desc": "Conveniently located accommodation.", "price": ""})
    st.info(f"🏨 **Recommended Stay ({budget_tier.split(' ')[0]}):** **{hotel_suggestion['name']}**\n\n*{hotel_suggestion['desc']}* (Est: {hotel_suggestion.get('price', '')})")
    st.write("")
    
    # Distribute elements dynamically
    for day in range(1, num_days + 1):
        render_html(f"""
            <div class="timeline-day">
                <h4 style="color: var(--primary-color); margin-top:0;">📅 Day {day} - Exploring the Heart of the City</h4>
            </div>
        """)
        
        # Determine morning/afternoon attractions based on index
        attract_indices = [(day*2 - 2) % len(attractions), (day*2 - 1) % len(attractions)] if attractions else []
        morning_att = attractions[attract_indices[0]] if len(attract_indices) > 0 and attractions else None
        afternoon_att = attractions[attract_indices[1]] if len(attract_indices) > 1 and attractions else None
        
        # Get food option
        food_opt = foods[(day - 1) % len(foods)] if foods else None
        # Get shopping option
        shop_opt = shopping[(day - 1) % len(shopping)] if shopping else None
        
        # Details
        if morning_att:
            st.markdown(f"**☀️ Morning: Visit {morning_att['name']}**")
            st.caption(f"{morning_att['desc']} (Rating: {morning_att.get('rating', '4.5')})")
            
        if food_opt:
            st.markdown(f"**😋 Lunch: Try local {food_opt['name']}**")
            st.caption(f"{food_opt['desc']}")
            
        if afternoon_att:
            st.markdown(f"**⛅ Afternoon: Tour {afternoon_att['name']}**")
            st.caption(f"{afternoon_att['desc']} (Rating: {afternoon_att.get('rating', '4.5')})")
            
        if shop_opt:
            st.markdown(f"**🛍️ Evening: Shop at {shop_opt['name']}**")
            st.caption(f"{shop_opt['desc']}")
        else:
            st.markdown("**🌆 Evening: Free exploration and dining**")
            st.caption("Walk through local streets, discover street food stalls, and interact with the local culture.")
            
        st.divider()

with col_budget:
    st.markdown("### 💰 Estimated Budget Breakdown")
    
    # Display Key Metrics
    render_html(f"""
        <div style="background-color: var(--secondary-background-color); border: 2px solid var(--primary-color); border-radius: 12px; padding: 20px; text-align: center; margin-bottom: 25px;">
            <div style="font-size: 0.9rem; color: gray; text-transform: uppercase;">Total Estimated Expenses</div>
            <div style="font-size: 2.2rem; font-weight: 800; color: var(--primary-color);">{currency_symbol} {total_budget:,} {currency_code}</div>
            <div style="font-size: 0.85rem; color: gray; margin-top:5px;">For {num_days} days &bull; {budget_tier.split(' ')[0]} tier</div>
        </div>
    """)
    
    # Dataframe for table and chart
    budget_data = {
        "Expense Category": ["🏨 Accommodation", "🍜 Food & Dining", "🚌 Transport", "🎟️ Sightseeing", "🎁 Shopping/Misc"],
        "Amount": [accommodation_cost, food_cost, transport_cost, sightseeing_cost, shopping_cost]
    }
    df_budget = pd.DataFrame(budget_data)
    
    # Plotly pie chart
    fig = px.pie(
        df_budget, 
        values="Amount", 
        names="Expense Category",
        color_discrete_sequence=px.colors.qualitative.Pastel,
        hole=0.4
    )
    fig.update_layout(
        margin=dict(t=0, b=0, l=0, r=0),
        legend=dict(orientation="h", yanchor="bottom", y=-0.1, xanchor="center", x=0.5),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Cost Table
    st.markdown("##### Detailed Allocation Table")
    formatted_df = df_budget.copy()
    formatted_df["Amount"] = formatted_df["Amount"].apply(lambda x: f"{currency_symbol} {x:,} {currency_code}")
    st.table(formatted_df)
    
    # Local Transit & Safety Warning Card
    st.markdown("### ℹ️ Important Travel Tips")
    with st.container(border=True):
        st.markdown(f"**✈️ Airport Transfer:** {city['airport_details']}")
        st.markdown(f"**🚇 City Transit:** {city['transport_info']}")
