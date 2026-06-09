import json
import time
import streamlit as st
from utils.database import get_all_countries, get_cities_by_country, get_city_by_name, get_country_by_name, get_city_details, get_country_details
from utils.styles import render_hero

render_hero("💬 AI Travel Assistant", "Ask questions about local rules, etiquette, food, attractions, and safety tips. Answers are based on our travel database.")

# Helper function to match keywords and generate context-rich answers
def generate_bot_response(user_query, active_country_id, active_city_id):
    query = user_query.lower().strip()
    
    # 1. Database details for active session state (context fallbacks)
    active_city = get_city_details(active_city_id) if active_city_id else None
    active_country = get_country_details(active_country_id) if active_country_id else None
    
    # 2. Extract country/city names from query
    matched_country = None
    matched_city = None
    
    countries = get_all_countries()
    for c in countries:
        if c["country_name"].lower() in query:
            matched_country = c
            break
            
    # List all cities in DB
    for c in countries:
        cities = get_cities_by_country(c["id"])
        for ct in cities:
            if ct["city_name"].lower() in query:
                matched_city = ct
                break
                
    # 3. Determine target entity (City has priority, then Country, then active context)
    target_city = matched_city if matched_city else (active_city if not matched_country else None)
    target_country = matched_country if matched_country else (active_country if not target_city else None)
    
    # If target city is set, get its country details too
    if target_city and not target_country:
        target_country = get_country_details(target_city["country_id"])
        
    # Topic detection
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
                return f"🍲 **Here are the must-try foods in {city_name} ({country_name}):**\n\n{food_list}\n\n*Make sure to check out local street food stalls for the most authentic taste!*"
            except:
                return f"🍲 Stored food info for {city_name}: {target_city['food_info']}"
                
        elif is_attraction:
            try:
                places = json.loads(target_city["tourist_places"])
                place_list = "\n".join([f"- **{p['name']}** ({p.get('rating', '4.5')}) - {p['desc']} Best visited in the *{p.get('time', 'day')}*." for p in places])
                return f"🎡 **Top tourist attractions in {city_name}:**\n\n{place_list}"
            except:
                return f"🎡 Stored attractions for {city_name}: {target_city['tourist_places']}"
                
        elif is_hotel:
            try:
                hotels = json.loads(target_city["hotel_info"])
                hotel_list = ""
                for tier, details in hotels.items():
                    hotel_list += f"- **{tier.upper()}**: {details['name']} ({details.get('price', '')}) - *{details['desc']}*\n"
                return f"🏨 **Recommended stays in {city_name}:**\n\n{hotel_list}"
            except:
                return f"🏨 Stored hotels for {city_name}: {target_city['hotel_info']}"
                
        elif is_transport:
            return f"🚌 **Transit guide for {city_name}:**\n\n- **Public Transport:** {target_city['transport_info']}\n\n- **Airport Details:** {target_city['airport_details']}"
            
        elif is_safety:
            return f"🛡️ **Safety Recommendations for {city_name}:**\n\n{target_city['safety_recommendations']}"
            
        elif is_rules or is_etiquette:
            # Fallback to country rules since rules are usually country-wide
            return f"📜 **Rules & Etiquette to follow in {city_name} (referencing {country_name} guidelines):**\n\n**Rules:**\n{target_country['rules']}\n\n**Cultural Etiquette:**\n{target_country['etiquette']}"
            
        else:
            # General city info response
            return f"🏙️ **Welcome to {city_name}!**\n\n{target_city['description']}\n\nAsk me specific questions like:\n- *What food should I try in {city_name}?*\n- *What are the tourist attractions in {city_name}?*\n- *How is the public transport in {city_name}?*"

    elif target_country:
        country_name = target_country["country_name"]
        
        if is_rules:
            rules_formatted = "\n".join([f"- {r}" for r in target_country["rules"].split("\n") if r.strip()])
            return f"📜 **Important Rules & Regulations to follow in {country_name}:**\n\n{rules_formatted}\n\n*Violating local regulations can lead to hefty fines, so keep these in mind!*"
            
        elif is_etiquette:
            et_formatted = "\n".join([f"- {e}" for e in target_country["etiquette"].split("\n") if e.strip()])
            return f"🤝 **Cultural Dos and Don'ts for {country_name}:**\n\n{et_formatted}"
            
        elif is_safety:
            safety_formatted = "\n".join([f"- {s}" for s in target_country["safety_tips"].split("\n") if s.strip()])
            return f"🛡️ **Safety Guidelines for {country_name}:**\n\n{safety_formatted}\n\n🚨 **Emergency Numbers:** {target_country['emergency_number']}"
            
        elif is_visa:
            return f"📑 **Visa & Entry information for {country_name}:**\n\n{target_country['visa_info']}"
            
        else:
            # General country info response
            return f"🌍 **Welcome to {country_name}!**\n\n- **Capital:** {target_country['capital']}\n- **Currency:** {target_country['currency']}\n- **Language:** {target_country['language']}\n- **Timezone:** {target_country['timezone']}\n\nAsk me specific questions like:\n- *What are the traffic rules in {country_name}?*\n- *What is the cultural etiquette in {country_name}?*\n- *How do I get a visa for {country_name}?*"

    # Fallback when no keywords or locations matched
    return (
        "👋 Hello! I am your AI Travel Companion.\n\n"
        "I can answer questions regarding **local laws, customs, safety, transport, delicacies, and hotels** "
        "for the following destinations currently in my database:\n"
        "- **India** (Hyderabad, Visakhapatnam)\n"
        "- **Japan** (Tokyo, Osaka)\n"
        "- **Singapore** (Singapore City)\n\n"
        "Try asking me queries like:\n"
        "- *What should I know before visiting Tokyo?*\n"
        "- *What are the traffic rules in Singapore?*\n"
        "- *What food should I try in Hyderabad?*\n"
        "- *What is the currency in Japan?*"
    )


# 4. Chat Interface
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I am your TravelMate AI Assistant. Ask me anything about local rules, etiquette, food, and stays for India, Japan, or Singapore."}
    ]

# Display quick suggest options
st.markdown("##### 💡 Suggested Questions")
sug_col1, sug_col2, sug_col3 = st.columns(3)

with sug_col1:
    if st.button("🍽️ Hyderabad food?", use_container_width=True):
        st.session_state.prompt_trigger = "What food should I try in Hyderabad?"
with sug_col2:
    if st.button("🚦 Singapore rules?", use_container_width=True):
        st.session_state.prompt_trigger = "What are the rules in Singapore?"
with sug_col3:
    if st.button("👘 Tokyo etiquette?", use_container_width=True):
        st.session_state.prompt_trigger = "What is the cultural etiquette in Tokyo?"

# Process quick triggers
user_prompt = None
if "prompt_trigger" in st.session_state and st.session_state.prompt_trigger:
    user_prompt = st.session_state.prompt_trigger
    st.session_state.prompt_trigger = None # Reset trigger
else:
    # Get user input from chat input box
    user_prompt = st.chat_input("Ask about rules, food, stays, or safety...")

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
    response = generate_bot_response(
        user_prompt, 
        st.session_state.get("selected_country_id"),
        st.session_state.get("selected_city_id")
    )
    
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
