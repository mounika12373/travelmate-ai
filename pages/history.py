import streamlit as st
import json
import pandas as pd
from datetime import datetime, date
from utils.database import (
    get_travel_history,
    delete_history_item,
    clear_user_history,
    toggle_history_favorite
)
from utils.styles import render_hero, render_html, render_card

# Verify authentication
if not st.session_state.get("user"):
    st.warning("⚠️ Access Denied. Please log in to view your travel history logs.")
    st.button("Go to Sign In", on_click=lambda: st.switch_page("pages/auth.py"))
    st.stop()

user_id = st.session_state.user["id"]

render_hero("⏳ Travel History & Logs", "Keep track of your generated itineraries, search queries, recommendations, and AI chats")

# Create filter sidebar columns or horizontal layout
st.subheader("🔍 Filter Logs")
col_f1, col_f2, col_f3, col_f4 = st.columns(4)

with col_f1:
    search_query = st.text_input("Search term", value="", placeholder="e.g. Tokyo, Biryani, hotel...")
with col_f2:
    activity_filter = st.selectbox(
        "Activity Type",
        ["All", "Destination Search", "Generated Itinerary", "Hotel / Flight Search", "AI Chat Bot"]
    )
    activity_map = {
        "All": None,
        "Destination Search": "search",
        "Generated Itinerary": "itinerary",
        "Hotel / Flight Search": "hotel_search",
        "AI Chat Bot": "chat"
    }
    act_type = activity_map[activity_filter]
with col_f3:
    country_filter = st.selectbox(
        "Country Location",
        ["All Countries", "India", "Japan", "Singapore"]
    )
    country_param = None if country_filter == "All Countries" else country_filter
with col_f4:
    date_choice = st.date_input("Date Range", value=(date(2026, 1, 1), date(2026, 12, 31)))

# Extract date params
start_d = date_choice[0].strftime("%Y-%m-%d") if isinstance(date_choice, tuple) and len(date_choice) > 0 else None
end_d = date_choice[1].strftime("%Y-%m-%d") if isinstance(date_choice, tuple) and len(date_choice) > 1 else None

# Retrieve history list
history_items = get_travel_history(
    user_id=user_id,
    activity_type=act_type,
    search_query=search_query if search_query.strip() else None,
    start_date=start_d,
    end_date=end_d,
    country=country_param
)

# Global Action buttons
st.divider()
action_col1, action_col2, action_col3, action_col4 = st.columns([1.5, 1.5, 1.5, 2])

# Prepare export data
df_list = []
for item in history_items:
    df_list.append({
        "ID": item["id"],
        "Type": item["activity_type"],
        "Query/Target": item["query"],
        "Details": item["details"],
        "Starred": "Yes" if item["is_favorite"] else "No",
        "Timestamp": item["created_at"]
    })
df_history = pd.DataFrame(df_list)

with action_col1:
    # Export to Excel (CSV)
    if not df_history.empty:
        csv_data = df_history.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📊 Export to Excel (CSV)",
            data=csv_data,
            file_name=f"travelmate_history_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True
        )
    else:
        st.button("📊 Export to Excel (CSV)", disabled=True, use_container_width=True)

with action_col2:
    # Export to PDF (Markdown Text Report)
    if not df_history.empty:
        report_text = f"# TravelMate AI History Log Report\nGenerated on {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
        for item in history_items:
            fav_star = "★ " if item["is_favorite"] else ""
            report_text += f"### {fav_star}[{item['activity_type'].upper()}] {item['query']} ({item['created_at']})\n"
            if item["details"]:
                try:
                    det = json.loads(item["details"])
                    if isinstance(det, dict):
                        for k, v in det.items():
                            report_text += f"- **{k}:** {v}\n"
                    else:
                        report_text += f"{det}\n"
                except Exception:
                    report_text += f"{item['details']}\n"
            report_text += "\n---\n\n"
            
        st.download_button(
            label="📑 Export Document (.MD)",
            data=report_text,
            file_name=f"travelmate_report_{datetime.now().strftime('%Y%m%d')}.md",
            mime="text/markdown",
            use_container_width=True
        )
    else:
        st.button("📑 Export Document (.MD)", disabled=True, use_container_width=True)

with action_col3:
    # Delete All History
    if st.button("🗑️ Clear All History", type="secondary", use_container_width=True):
        clear_user_history(user_id)
        st.success("All travel history logs cleared!")
        st.rerun()

with action_col4:
    # Toggle Favorites Only filter
    show_favs_only = st.checkbox("⭐ Show Favorite Trips Only", value=False)

st.divider()

# Loop and display logs
if not history_items:
    st.info("No logs match your selected filter criteria.")
else:
    for item in history_items:
        # Check favorite filter
        if show_favs_only and not item["is_favorite"]:
            continue
            
        # Determine labels & icons based on activity
        act_icon = "🔍"
        act_title = "Query Search"
        if item["activity_type"] == "itinerary":
            act_icon = "📅"
            act_title = "Itinerary Planner"
        elif item["activity_type"] == "hotel_search":
            act_icon = "🏨"
            act_title = "Accommodation Guide"
        elif item["activity_type"] == "chat":
            act_icon = "💬"
            act_title = "AI Chat Interaction"
            
        # Star styling
        fav_label = "⭐ Favorited" if item["is_favorite"] else "☆ Favorite"
        
        with st.container(border=True):
            col_hdr1, col_hdr2 = st.columns([4, 1.2])
            with col_hdr1:
                st.markdown(f"#### {act_icon} {act_title}: **{item['query']}**")
                st.caption(f"Logged on {item['created_at']}")
            with col_hdr2:
                btn_cols = st.columns(2)
                with btn_cols[0]:
                    if st.button(fav_label, key=f"fav_{item['id']}", use_container_width=True):
                        toggle_history_favorite(item["id"], user_id)
                        st.rerun()
                with btn_cols[1]:
                    if st.button("🗑️", key=f"del_{item['id']}", use_container_width=True):
                        delete_history_item(item["id"], user_id)
                        st.success("Log item deleted!")
                        st.rerun()
            
            # Display details
            if item["details"]:
                try:
                    details = json.loads(item["details"])
                    
                    if item["activity_type"] == "itinerary":
                        # Render specific itinerary metadata
                        st.markdown(f"**Itinerary Parameters:** {details.get('days', 3)} Days • {details.get('budget_tier', 'Mid-Range')}")
                        if st.checkbox("👁️ View Full Saved Itinerary Plan", key=f"view_plan_{item['id']}"):
                            st.write(details.get("itinerary_text", ""))
                            if "budget_breakdown" in details:
                                st.write("💰 **Estimated Budget:**")
                                st.dataframe(pd.DataFrame(details["budget_breakdown"]))
                                
                    elif item["activity_type"] == "chat":
                        st.markdown(f"**Question:** *{item['query']}*")
                        st.markdown(f"**Answer:** {details.get('response', '')}")
                        
                    elif item["activity_type"] == "hotel_search":
                        st.markdown(f"**Recommended Stays:**")
                        st.write(details)
                        
                    else:
                        st.write(details)
                except Exception:
                    st.text(item["details"])
            else:
                st.write("Logged search query.")
