import json

import pandas as pd
import plotly.express as px
import streamlit as st

from utils.database import delete_saved_trip, get_saved_trips, save_trip
from utils.styles import render_hero

# Verify authentication
if not st.session_state.get("user"):
    st.warning("⚠️ Access Denied. Please log in to manage your saved trips and collections.")
    st.button("Go to Sign In", on_click=lambda: st.switch_page("pages/auth.py"))
    st.stop()

user_id = st.session_state.user["id"]

render_hero(
    "💾 Saved Trips & Collections",
    "Manage your saved itineraries, bookmarked destinations, and custom travel collections",
)

# Create custom collection helper form
st.sidebar.subheader("📁 Manage Collections")
with st.sidebar.form("create_collection_form"):
    new_collection = st.text_input("New Collection Name", placeholder="e.g. Kyoto Trip 2026").strip()
    create_btn = st.form_submit_button("Create Collection")
    if create_btn:
        if new_collection:
            # We can save a dummy bookmark to instantiate the collection
            save_trip(
                user_id=user_id,
                trip_type="destination",
                name="Placeholder",
                collection_name=new_collection,
                details={"info": "Collection created."},
            )
            st.toast(f"Collection '{new_collection}' created!")
            st.rerun()

# Get all saved trips
all_saved = get_saved_trips(user_id)

# Filter unique collection names (ignore Placeholder items in user view if we filter them out)
collections = sorted(list({t["collection_name"] for t in all_saved}))
if "My Saved Trips" not in collections:
    collections.insert(0, "My Saved Trips")

# Select collection to display
selected_collection = st.selectbox("📂 Choose Travel Collection", collections)

# Filter items in the current collection
collection_items = [t for t in all_saved if t["collection_name"] == selected_collection and t["name"] != "Placeholder"]

# Tabs for different item types
tab_itineraries, tab_destinations, tab_hotels, tab_flights = st.tabs(
    ["🗺️ Saved Itineraries", "🌍 Bookmarked Destinations", "🏨 Saved Hotels", "✈️ Saved Flights"]
)

# ==========================================
# TAB 1: SAVED ITINERARIES
# ==========================================
with tab_itineraries:
    itineraries = [t for t in collection_items if t["trip_type"] == "itinerary"]
    if not itineraries:
        st.info(f"No saved itineraries in '{selected_collection}' yet. Generate one in the Travel Planner and save it!")
    else:
        for idx, item in enumerate(itineraries):
            try:
                details = json.loads(item["details"])
            except Exception:
                details = {}

            with st.container(border=True):
                col_header1, col_header2 = st.columns([4, 1])
                with col_header1:
                    st.markdown(f"### 🗺️ {item['name']}")
                    st.caption(
                        f"Planned Date: **{item['travel_date'] or 'Not Set'}** | Saved on {item['created_at'][:10]}"
                    )
                with col_header2:
                    if st.button("🗑️ Remove", key=f"del_it_{item['id']}", use_container_width=True):
                        delete_saved_trip(item["id"], user_id)
                        st.success("Itinerary removed!")
                        st.rerun()

                # Render itinerary details
                col_info, col_chart = st.columns([3, 2])
                with col_info:
                    st.markdown(f"**Budget Level:** {details.get('budget_tier', 'Mid-Range')}")
                    if st.checkbox("👁️ Show Day-by-Day Itinerary Plan", key=f"show_detail_it_{item['id']}"):
                        st.write(details.get("itinerary_text", ""))

                with col_chart:
                    if "budget_breakdown" in details:
                        # Re-render budget breakdown pie chart!
                        df_budget = pd.DataFrame(details["budget_breakdown"])
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
                        st.plotly_chart(fig, use_container_width=True, key=f"saved_chart_{item['id']}")

# ==========================================
# TAB 2: BOOKMARKED DESTINATIONS
# ==========================================
with tab_destinations:
    destinations = [t for t in collection_items if t["trip_type"] == "destination"]
    if not destinations:
        st.info(
            f"No bookmarked destinations in '{selected_collection}'. Search and bookmark them from the Home dashboard!"
        )
    else:
        # Loop and render destinations
        for item in destinations:
            try:
                details = json.loads(item["details"])
            except Exception:
                details = {}

            with st.container(border=True):
                col_d1, col_d2 = st.columns([4, 1])
                with col_d1:
                    st.markdown(f"#### 🏙️ {item['name']}")
                    st.write(details.get("description", "Bookmarked destination."))
                with col_d2:
                    if st.button("🗑️ Unbookmark", key=f"del_dest_{item['id']}", use_container_width=True):
                        delete_saved_trip(item["id"], user_id)
                        st.success("Destination unbookmarked!")
                        st.rerun()

                # Provide a quick navigate button
                if "city_id" in details:
                    if st.button("🗺️ Explore City Guide", key=f"explore_nav_{item['id']}", use_container_width=True):
                        st.session_state.selected_city_id = details["city_id"]
                        st.session_state.selected_country_id = details.get("country_id")
                        st.switch_page("pages/city_info.py")

# ==========================================
# TAB 3: SAVED HOTELS
# ==========================================
with tab_hotels:
    hotels = [t for t in collection_items if t["trip_type"] == "hotel"]
    if not hotels:
        st.info("No saved hotels yet. Save recommended stays from the Travel Planner!")
    else:
        for item in hotels:
            try:
                details = json.loads(item["details"])
            except Exception:
                details = {}

            with st.container(border=True):
                col_h1, col_h2 = st.columns([4, 1])
                with col_h1:
                    st.markdown(f"##### 🏨 {item['name']}")
                    st.write(details.get("desc", ""))
                    st.markdown(f"💰 **Estimated Cost:** {details.get('price', 'N/A')}")
                with col_h2:
                    if st.button("🗑️ Remove Hotel", key=f"del_ht_{item['id']}", use_container_width=True):
                        delete_saved_trip(item["id"], user_id)
                        st.success("Hotel removed!")
                        st.rerun()

# ==========================================
# TAB 4: SAVED FLIGHTS
# ==========================================
with tab_flights:
    flights = [t for t in collection_items if t["trip_type"] == "flight"]
    if not flights:
        st.info("No saved flights yet. Search flights in our city explorer guides and bookmark them!")
    else:
        for item in flights:
            try:
                details = json.loads(item["details"])
            except Exception:
                details = {}

            with st.container(border=True):
                col_f1, col_f2 = st.columns([4, 1])
                with col_f1:
                    st.markdown(f"##### ✈️ {item['name']}")
                    st.write(f"Airline Carrier: **{details.get('airline', 'N/A')}**")
                    st.write(
                        f"Departure: **{details.get('departure_time', 'N/A')}** | Arrival: **{details.get('arrival_time', 'N/A')}**"
                    )
                    st.markdown(f"💰 **Fare Cost:** {details.get('price', 'N/A')}")
                with col_f2:
                    if st.button("🗑️ Remove Flight", key=f"del_fl_{item['id']}", use_container_width=True):
                        delete_saved_trip(item["id"], user_id)
                        st.success("Flight removed!")
                        st.rerun()
