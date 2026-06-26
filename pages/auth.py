import base64
import json

import streamlit as st

from utils.auth_utils import hash_password, login_user, verify_password
from utils.database import create_user, get_user_by_email
from utils.styles import render_hero, render_html, render_skeleton_card

# Localized page titles
render_hero("🔐 Account Gateway", "Secure registration, login, and profile access for TravelMate AI")


def convert_img_to_base64(file_buffer) -> str:
    """Converts a Streamlit file uploader buffer to a Base64 data URI."""
    if file_buffer:
        encoded = base64.b64encode(file_buffer.read()).decode()
        return f"data:image/png;base64,{encoded}"
    return ""


# Tab structures
tab_login, tab_register, tab_forgot = st.tabs(["🔑 Sign In", "📝 Create Account", "🔄 Reset Password"])

# ==========================================
# TAB 1: USER SIGN IN
# ==========================================
with tab_login:
    col_in, col_google = st.columns([2, 1.2])

    with col_in:
        st.subheader("Login to Your Account")
        with st.form("login_form"):
            email_val = st.text_input("Email Address", key="login_email").strip()
            pass_val = st.text_input("Password", type="password", key="login_pass")
            remember_me = st.checkbox("Remember Me on this device", value=False)

            submit_login = st.form_submit_button("Sign In", use_container_width=True)

            if submit_login:
                if not email_val or not pass_val:
                    st.error("Please enter both your email address and password.")
                else:
                    # Query user
                    user = get_user_by_email(email_val)
                    if user and verify_password(pass_val, user["password_hash"]):
                        # Perform login
                        login_user(user, remember_me=remember_me)
                        st.success(f"Welcome back, {user['full_name']}!")
                        # Skeleton loader transition
                        with st.spinner("Setting up your dashboard..."):
                            render_skeleton_card()
                        st.rerun()
                    else:
                        st.error("Invalid email address or password. Please try again.")

    with col_google:
        st.subheader("Or Connect With")
        render_html("""
            <div style='text-align: center; margin-top: 15px;'>
                <p style='color: gray; font-size: 0.85rem;'>Sign in instantly using your social account credentials.</p>
            </div>
        """)

        # Google OAuth simulation
        if st.button("🔴 Continue with Google", use_container_width=True):
            # Create a mock Google user in database or retrieve existing
            google_email = "google.traveler@gmail.com"
            google_user = get_user_by_email(google_email)

            if not google_user:
                # Seed a default profile pic
                mock_pic = "https://www.w3schools.com/howto/img_avatar.png"
                mock_pass = hash_password("GoogleOAuth2026Secure")
                mock_prefs = json.dumps(["Adventure", "Nature & Wildlife"])
                user_id = create_user(
                    full_name="Google Traveler",
                    email=google_email,
                    phone="+1 (555) 019-2834",
                    country="United States",
                    city="Mountain View",
                    profile_pic=mock_pic,
                    password_hash=mock_pass,
                    preferences=mock_prefs,
                )
                google_user = get_user_by_email(google_email)

            login_user(google_user, remember_me=True)
            st.toast("Authenticated with Google successfully!")
            st.success(f"Welcome, {st.session_state.user['full_name']}!")
            st.rerun()

# ==========================================
# TAB 2: USER REGISTRATION
# ==========================================
with tab_register:
    st.subheader("Create Your TravelMate AI Account")

    with st.form("register_form"):
        col1, col2 = st.columns(2)

        with col1:
            reg_name = st.text_input("Full Name *", placeholder="John Doe")
            reg_email = st.text_input("Email Address *", placeholder="john.doe@example.com")
            reg_phone = st.text_input("Phone Number", placeholder="+91 98765 43210")
            reg_pass = st.text_input("Password *", type="password", placeholder="Minimum 6 characters")
            reg_pass_conf = st.text_input("Confirm Password *", type="password")

        with col2:
            reg_country = st.text_input("Home Country", placeholder="India")
            reg_city = st.text_input("Current City", placeholder="Hyderabad")
            reg_avatar = st.file_uploader("Profile Picture", type=["png", "jpg", "jpeg"])

            # Multi-select travel preferences
            pref_options = [
                "Adventure & Sports",
                "Cultural Heritage & Arts",
                "Beaches & Coastal",
                "Nature & Wildlife",
                "Luxury & Relaxation",
                "Spiritual & Religious",
                "Culinary & Food Tours",
                "Budget-Conscious",
            ]
            reg_prefs = st.multiselect("Travel Preferences", pref_options, default=["Adventure & Sports"])

        st.divider()
        submit_register = st.form_submit_button("Register Account", use_container_width=True)

        if submit_register:
            if not reg_name or not reg_email or not reg_pass:
                st.error("Please fill in all mandatory fields (*) to register.")
            elif reg_pass != reg_pass_conf:
                st.error("Passwords do not match. Please re-type your passwords.")
            elif len(reg_pass) < 6:
                st.error("Password must be at least 6 characters long.")
            else:
                # Check email duplicate
                existing = get_user_by_email(reg_email)
                if existing:
                    st.error("An account with this email address already exists.")
                else:
                    # Base64 avatar conversion
                    b64_pic = convert_img_to_base64(reg_avatar)

                    hashed_pwd = hash_password(reg_pass)
                    prefs_json = json.dumps(reg_prefs)

                    user_id = create_user(
                        full_name=reg_name,
                        email=reg_email,
                        phone=reg_phone,
                        country=reg_country,
                        city=reg_city,
                        profile_pic=b64_pic,
                        password_hash=hashed_pwd,
                        preferences=prefs_json,
                    )

                    if user_id:
                        st.success("Registration completed successfully! Please sign in using your credentials.")
                        st.balloons()
                    else:
                        st.error("Registration failed due to a database error. Please contact support.")

# ==========================================
# TAB 3: FORGOT PASSWORD
# ==========================================
with tab_forgot:
    st.subheader("Reset Password")
    st.write("Enter your registered email address, and we will send you instructions to reset your password.")

    with st.form("forgot_password_form"):
        forgot_email = st.text_input("Email Address", placeholder="registered.email@example.com").strip()
        submit_reset = st.form_submit_button("Send Reset Link", use_container_width=True)

        if submit_reset:
            if not forgot_email:
                st.error("Please enter your email address.")
            else:
                user = get_user_by_email(forgot_email)
                if user:
                    st.success("A password reset link has been simulated and sent to your email. Check your inbox.")
                    st.info(
                        "Simulation mode: Clicking this button confirms the account exists. Reset token has been dispatched."
                    )
                else:
                    st.error("No account found matching this email address.")
