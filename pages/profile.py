import streamlit as st
import json
import base64
from utils.database import get_user_by_id, update_user_profile, get_dashboard_stats
from utils.auth_utils import logout_user
from utils.styles import render_hero, render_html, render_card

# Initialize page
if not st.session_state.get("user"):
    st.warning("⚠️ Access Denied. Please log in to view your profile dashboard.")
    st.button("Go to Sign In", on_click=lambda: st.switch_page("pages/auth.py"))
    st.stop()

# Get fresh data from the database
user_id = st.session_state.user["id"]
user = get_user_by_id(user_id)

# Fallback profile pic
avatar = user.get("profile_pic")
if not avatar:
    avatar = "https://www.w3schools.com/howto/img_avatar.png"

# Fetch analytics metrics
stats = get_dashboard_stats(user_id)

# Render premium header
render_hero("👤 My Profile & Dashboard", f"Welcome back, {user['full_name']} | Account Dashboard")

# Create two layout columns: Left for profile details, Right for dashboard metrics
col_left, col_right = st.columns([1, 2.2])

# ==========================================
# LEFT COLUMN: USER INFO & ACCOUNT SETTINGS
# ==========================================
with col_left:
    # Render profile card
    render_html(f"""
        <div class="travel-card" style="text-align: center;">
            <img src="{avatar}" style="width: 110px; height: 110px; border-radius: 50%; object-fit: cover; border: 3px solid var(--primary-color); box-shadow: 0 4px 10px rgba(0,0,0,0.15); margin-bottom: 15px;">
            <h3 style="margin-top: 0; margin-bottom: 5px;">{user['full_name']}</h3>
            <p style="color: gray; font-size: 0.88rem; margin-bottom: 15px;">📍 {user['city'] or 'N/A'}, {user['country'] or 'N/A'}</p>
            <hr style="border-color: rgba(128,128,128,0.15); margin: 15px 0;">
            <div style="text-align: left; font-size: 0.88rem; line-height: 1.6;">
                <strong>✉️ Email:</strong> {user['email']}<br>
                <strong>📞 Phone:</strong> {user['phone'] or 'N/A'}<br>
                <strong>📅 Joined:</strong> {user['created_at'][:10]}
            </div>
        </div>
    """)
    
    # Edit Profile details
    with st.expander("📝 Edit Profile Details"):
        with st.form("edit_profile_form"):
            new_name = st.text_input("Full Name", value=user["full_name"])
            new_phone = st.text_input("Phone Number", value=user["phone"] or "")
            new_country = st.text_input("Country", value=user["country"] or "")
            new_city = st.text_input("City", value=user["city"] or "")
            new_avatar = st.file_uploader("Change Photo", type=["png", "jpg", "jpeg"])
            
            # Select preferences
            pref_options = [
                "Adventure & Sports", "Cultural Heritage & Arts", "Beaches & Coastal",
                "Nature & Wildlife", "Luxury & Relaxation", "Spiritual & Religious",
                "Culinary & Food Tours", "Budget-Conscious"
            ]
            
            try:
                current_prefs = json.loads(user["preferences"])
            except Exception:
                current_prefs = []
                
            new_prefs = st.multiselect("Update Travel Preferences", pref_options, default=current_prefs)
            
            save_btn = st.form_submit_button("Save Changes", use_container_width=True)
            
            if save_btn:
                b64_avatar = user["profile_pic"]
                if new_avatar:
                    # Convert to base64
                    encoded = base64.b64encode(new_avatar.read()).decode()
                    b64_avatar = f"data:image/png;base64,{encoded}"
                
                success = update_user_profile(
                    user_id=user_id,
                    full_name=new_name,
                    phone=new_phone,
                    country=new_country,
                    city=new_city,
                    profile_pic=b64_avatar,
                    preferences=json.dumps(new_prefs)
                )
                if success:
                    # Refresh session state user reference
                    st.session_state.user["full_name"] = new_name
                    st.session_state.user["profile_pic"] = b64_avatar
                    st.success("Profile updated successfully!")
                    st.rerun()

    # Logout Button
    if st.button("🚪 Logout of Account", use_container_width=True, type="secondary"):
        logout_user()
        st.success("Successfully logged out.")
        st.switch_page("pages/home.py")

# ==========================================
# RIGHT COLUMN: ANALYTICS & TRAVEL STATISTICS
# ==========================================
with col_right:
    st.subheader("📊 Travel Dashboard Metrics")
    
    # KPI metrics row
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    
    with kpi_col1:
        render_html(f"""
            <div class="metric-box">
                <div class="metric-label">🗺️ Trips Planned</div>
                <div class="metric-value">{stats['total_trips']}</div>
            </div>
        """)
        
    with kpi_col2:
        render_html(f"""
            <div class="metric-box">
                <div class="metric-label">🌎 Countries Explored</div>
                <div class="metric-value">{stats['countries_explored']} / 3</div>
            </div>
        """)
        
    with kpi_col3:
        render_html(f"""
            <div class="metric-box">
                <div class="metric-label">💾 Saved Items</div>
                <div class="metric-value">{stats['saved_destinations']}</div>
            </div>
        """)
        
    st.write("")
    
    # 2. Activity Statistics & Preferences Card
    col_sub1, col_sub2 = st.columns(2)
    
    with col_sub1:
        st.markdown("#### 🌟 Travel Preferences")
        try:
            prefs = json.loads(user["preferences"])
        except Exception:
            prefs = []
            
        if prefs:
            pref_html = "".join([f'<span class="tag-badge" style="margin-bottom: 8px;">✨ {p}</span>' for p in prefs])
            render_html(f"<div class='travel-card'>{pref_html}</div>")
        else:
            st.info("No preferences saved. Update profile to add yours.")
            
    with col_sub2:
        st.markdown("#### 📈 AI Usage Stats")
        with st.container(border=True):
            st.write(f"🤖 **Chatbot Queries:** {stats['ai_usage']['chatbot_interactions']}")
            st.write(f"📅 **Itineraries Generated:** {stats['ai_usage']['itineraries_generated']}")

    st.divider()

    # 3. Upcoming Trips Timeline
    st.markdown("#### 📅 Upcoming Trips Timeline")
    upcoming = stats["upcoming_trips"]
    
    if upcoming:
        for trip in upcoming:
            try:
                details = json.loads(trip["details"])
            except Exception:
                details = {}
            st.info(f"✈️ **{trip['name']}** - Planned Date: **{trip['travel_date']}** | Budget Level: **{details.get('budget_tier', 'N/A')}**")
    else:
        st.info("No upcoming trips found. Create a plan in the [Travel Planner](pages/planner.py) page and save it with a travel date!")

    st.divider()

    # 4. Recent Searches
    st.markdown("#### 🔍 Recent Search Queries")
    recent = stats["recent_searches"]
    if recent:
        for idx, item in enumerate(recent):
            st.markdown(f"{idx+1}. **{item['query']}** (searched at {item['created_at'][:16]})")
    else:
        st.info("Your destination searches will appear here once you search from the home screen.")
