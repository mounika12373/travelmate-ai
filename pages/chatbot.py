import json
import time

import streamlit as st

from utils.database import (
    get_all_countries,
    get_cities_by_country,
    get_city_details,
    get_country_details,
)
from utils.i18n import get_english_term, translate_ui
from utils.styles import render_hero
from utils.chatbot_agent import is_agent_enabled, run_agent_query

render_hero(translate_ui("ai_chatbot_title"), translate_ui("ai_chatbot_subtitle"))

# AI Engine status indicator
if is_agent_enabled():
    st.markdown(
        """
        <div style='display:inline-flex; align-items:center; gap:8px; background:rgba(0,200,100,0.1); border:1px solid rgba(0,200,100,0.25); border-radius:100px; padding:6px 16px; margin-bottom:20px;'>
            <span style='width:8px; height:8px; background:#00c864; border-radius:50%; display:inline-block; box-shadow:0 0 8px #00c864;'></span>
            <span style='font-size:0.85rem; font-weight:700; color:#00c864;'>Agent Kit AI Engine Active (Autonomous Tools)</span>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <div style='display:inline-flex; align-items:center; gap:8px; background:rgba(128,128,128,0.1); border:1px solid rgba(128,128,128,0.2); border-radius:100px; padding:6px 16px; margin-bottom:20px;'>
            <span style='width:8px; height:8px; background:gray; border-radius:50%; display:inline-block;'></span>
            <span style='font-size:0.85rem; font-weight:700; color:gray;'>Offline Mode Active (Rule-based Fallback)</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# Helper function to match keywords and generate context-rich answers
def generate_bot_response(user_query, active_country_id, active_city_id):
    # Normalize user_query to English keywords
    eng_query = get_english_term(user_query)
    query = eng_query.lower().strip()

    # 1. Database details for active session state (context fallbacks)
    active_city = get_city_details(active_city_id) if active_city_id else None
    active_country = get_country_details(active_country_id) if active_country_id else None

    # 2. Extract country/city names from query
    matched_country = None
    matched_city = None

    countries = get_all_countries()
    for c in countries:
        # Match against either English query or raw user query (translated country names)
        if c["country_name"].lower() in query or c["country_name"].lower() in user_query.lower():
            matched_country = c
            break

    # List all cities in DB
    for c in countries:
        cities = get_cities_by_country(c["id"])
        for ct in cities:
            if ct["city_name"].lower() in query or ct["city_name"].lower() in user_query.lower():
                matched_city = ct
                break

    # 3. Determine target entity (City has priority, then Country, then active context)
    target_city = matched_city if matched_city else (active_city if not matched_country else None)
    target_country = matched_country if matched_country else (active_country if not target_city else None)

    # If target city is set, get its country details too
    if target_city and not target_country:
        target_country = get_country_details(target_city["country_id"])

    # Topic detection (on English normalized query)
    is_food = any(w in query for w in ["food", "eat", "try", "dish", "cuisine", "delicacies", "dining", "lunch", "dinner", "biryani", "sushi", "crab", "ramen"])
    is_rules = any(w in query for w in ["rule", "law", "traffic", "regulation", "fine", "forbidden", "prohibit", "chewing gum", "smoking"])
    is_etiquette = any(w in query for w in ["etiquette", "culture", "do", "don't", "respect", "bow", "tip", "shoe", "hand", "custom"])
    is_safety = any(w in query for w in ["safety", "safe", "scam", "crime", "emergency", "police", "ambulance", "water", "drinkable"])
    is_attraction = any(w in query for w in ["places", "attractions", "visit", "see", "sightseeing", "temple", "shrine", "monument", "tour"])
    is_hotel = any(w in query for w in ["hotel", "stay", "accommodation", "resort", "hostel"])
    is_transport = any(w in query for w in ["transport", "bus", "metro", "subway", "train", "taxi", "airport"])
    is_visa = any(w in query for w in ["visa", "entry", "passport", "arrival"])

    # Build response based on match
    if target_city:
        city_name = target_city["city_name"]
        country_name = target_country["country_name"] if target_country else ""

        if is_food:
            try:
                foods = json.loads(target_city["food_info"])
                food_list = "\n".join([f"- **{f['name']}** ({f['type']}): {f['desc']}" for f in foods])
                return translate_ui("bot_food_city").format(city=city_name, country=country_name, list=food_list)
            except Exception:
                return f"🍲 Stored food info for {city_name}: {target_city['food_info']}"

        elif is_attraction:
            try:
                places = json.loads(target_city["tourist_places"])
                place_list = "\n".join([f"- **{p['name']}** ({p.get('rating', '4.5')}) - {p['desc']} Best visited in the *{p.get('time', 'day')}*." for p in places])
                return translate_ui("bot_attract_city").format(city=city_name, list=place_list)
            except Exception:
                return f"🎡 Stored attractions for {city_name}: {target_city['tourist_places']}"

        elif is_hotel:
            try:
                hotels = json.loads(target_city["hotel_info"])
                hotel_list = ""
                for tier, details in hotels.items():
                    hotel_list += f"- **{tier.upper()}**: {details['name']} ({details.get('price', '')}) - *{details['desc']}*\n"
                return translate_ui("bot_hotel_city").format(city=city_name, list=hotel_list)
            except Exception:
                return f"🏨 Stored hotels for {city_name}: {target_city['hotel_info']}"

        elif is_transport:
            return translate_ui("bot_transit_city").format(city=city_name, transit=target_city['transport_info'], airport=target_city['airport_details'])

        elif is_safety:
            return translate_ui("bot_safety_city").format(city=city_name, safety=target_city['safety_recommendations'])

        elif is_rules or is_etiquette:
            # Fallback to country rules since rules are usually country-wide
            return translate_ui("bot_rules_city").format(city=city_name, country=country_name, rules=target_country['rules'], etiquette=target_country['etiquette'])

        else:
            # General city info response
            return translate_ui("bot_welcome_city").format(city=city_name, desc=target_city['description'])

    elif target_country:
        country_name = target_country["country_name"]

        if is_rules:
            rules_formatted = "\n".join([f"- {r}" for r in target_country["rules"].split("\n") if r.strip()])
            return translate_ui("bot_rules_country").format(country=country_name, rules=rules_formatted)

        elif is_etiquette:
            et_formatted = "\n".join([f"- {e}" for e in target_country["etiquette"].split("\n") if e.strip()])
            return translate_ui("bot_etiquette_country").format(country=country_name, etiquette=et_formatted)

        elif is_safety:
            safety_formatted = "\n".join([f"- {s}" for s in target_country["safety_tips"].split("\n") if s.strip()])
            return translate_ui("bot_safety_country").format(country=country_name, safety=safety_formatted, emergency=target_country['emergency_number'])

        elif is_visa:
            return translate_ui("bot_visa_country").format(country=country_name, visa=target_country['visa_info'])

        else:
            # General country info response
            return translate_ui("bot_welcome_country").format(
                country=country_name,
                capital=target_country['capital'],
                currency=target_country['currency'],
                language=target_country['language'],
                timezone=target_country['timezone']
            )

    # Fallback when no keywords or locations matched
    return translate_ui("bot_fallback")


# Clear chat history if language changes (ensures consistent language context)
if "chat_language" not in st.session_state:
    st.session_state.chat_language = st.session_state.get("language", "en")

if "messages" not in st.session_state or st.session_state.chat_language != st.session_state.get("language", "en"):
    st.session_state.messages = [
        {"role": "assistant", "content": translate_ui("chat_bot_welcome")}
    ]
    st.session_state.chat_language = st.session_state.get("language", "en")

# Display quick suggest options
st.markdown(translate_ui("suggested_questions"))
sug_col1, sug_col2, sug_col3 = st.columns(3)

with sug_col1:
    if st.button(translate_ui("suggest_hyd_food"), use_container_width=True):
        st.session_state.prompt_trigger = "What food should I try in Hyderabad?"
with sug_col2:
    if st.button(translate_ui("suggest_sg_rules"), use_container_width=True):
        st.session_state.prompt_trigger = "What are the rules in Singapore?"
with sug_col3:
    if st.button(translate_ui("suggest_tokyo_etiq"), use_container_width=True):
        st.session_state.prompt_trigger = "What is the cultural etiquette in Tokyo?"

# Process quick triggers
user_prompt = None
if "prompt_trigger" in st.session_state and st.session_state.prompt_trigger:
    user_prompt = st.session_state.prompt_trigger
    st.session_state.prompt_trigger = None # Reset trigger
else:
    # Get user input from chat input box
    user_prompt = st.chat_input(translate_ui("chat_placeholder"))

# Render chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Process new input
if user_prompt:
    # Display user query
    with st.chat_message("user"):
        st.markdown(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Generate response
    if is_agent_enabled():
        try:
            with st.spinner("TravelMate AI is thinking..."):
                response = run_agent_query(
                    user_id=st.session_state.user["email"] if st.session_state.get("user") else "guest_user",
                    session_id=st.session_state.get("chat_language", "en"),
                    query_text=user_prompt,
                    active_country_id=st.session_state.get("selected_country_id"),
                    active_city_id=st.session_state.get("selected_city_id")
                )
        except Exception as e:
            st.warning(f"Agent Kit encountered an error: {e}. Falling back to rule-based response.")
            response = generate_bot_response(
                user_prompt,
                st.session_state.get("selected_country_id"),
                st.session_state.get("selected_city_id")
            )
    else:
        response = generate_bot_response(
            user_prompt,
            st.session_state.get("selected_country_id"),
            st.session_state.get("selected_city_id")
        )

    # Auto-Log Chat Activity
    if st.session_state.get("user"):
        from utils.database import log_activity
        log_activity(st.session_state.user["id"], "chat", user_prompt, {"response": response})

    # Display assistant response with a simulated typing speed
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # Simulate stream typing
        for chunk in response.split(" "):
            full_response += chunk + " "
            time.sleep(0.04) # brief delay
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    st.session_state.messages.append({"role": "assistant", "content": response})
