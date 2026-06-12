import json

import streamlit as st

# UI Translations Dictionary
UI_TRANSLATIONS = {
    "en": {
        "app_subtitle": "Your Smart Travel Companion",
        "home_hero_subtitle": "Discover essential local laws, cultural etiquette, transit guides, top foods, and safety advice before you arrive.",
        "trend_tokyo_title": "Shibuya, Tokyo",
        "trend_tokyo_desc": "Experience the high-tech neon lights, historical shrines, and Michelin-starred culinary scene of Japan's heart.",
        "most_popular": "Most Popular",
        "trend_hyd_title": "Old City, Hyderabad",
        "trend_hyd_desc": "Savor world-famous Biryani, stand before the historic Charminar, and buy pearls in Nizam's heritage bazaar.",
        "cultural_choice": "Cultural Choice",
        "trend_sg_title": "Garden City, Singapore",
        "trend_sg_desc": "Walk through futuristic gardens, stand in awe of Marina Bay Sands, and discover local hawker food courts.",
        "safest_destination": "Safest Destination",
        "quick_search": "🔍 Quick Search",
        "search_placeholder": "e.g., Tokyo, India, Biryani, temples...",
        "matching_countries": "##### Matching Countries",
        "matching_cities": "##### Matching Cities",
        "no_matching_countries": "No matching countries found.",
        "no_matching_cities": "No matching cities found.",
        "destination_guide": "🗺️ Destination Guide",
        "no_travel_data": "No travel data available. Please initialize the database.",
        "select_country": "Select Country",
        "view_country_guide": "📖 View Country Guide",
        "select_city": "Select City",
        "view_city_details": "🏙️ View City Details",
        "no_cities_available": "No cities available for this country.",
        "featured_destinations": "⭐ Featured Destinations",
        "explore_tokyo": "Explore Tokyo",
        "explore_hyderabad": "Explore Hyderabad",
        "explore_singapore": "Explore Singapore",
        "explore_another_country": "Explore another country",
        "select_destination": "Select Destination",
        "country_label": "Country",
        "city_label": "City",
        "no_cities_warning": "No cities in this country.",
        "attractions_tab": "🎡 Attractions & Shopping",
        "food_tab": "🍲 Local Delicacies",
        "stays_tab": "🏨 Recommended Stays",
        "transit_tab": "🚌 Transit & Airport Guide",
        "top_attractions": "### 🎡 Top Attractions to Visit",
        "famous_shopping": "### 🛍️ Famous Shopping Spots",
        "must_try_dishes": "### 🍲 Must-Try Famous Dishes",
        "veg_delights": "#### 🟢 Vegetarian Delights",
        "non_veg_specials": "#### 🔴 Non-Vegetarian Specials",
        "local_favorites": "#### 🌟 Local Favorites",
        "recommended_accommodations": "### 🏨 Recommended Accommodations",
        "budget_friendly": "#### 🪙 Budget Friendly",
        "mid_range_comfort": "#### 🏢 Mid-Range Comfort",
        "luxury_stay": "#### 💎 Luxury Stay",
        "airport_access": "### ✈️ Airport Access Details",
        "public_transport": "### 🚌 Local Public Transportation",
        "safety_recommendations_for": "🛡️ Safety Recommendations for ",
        "smart_planner_title": "📅 Smart Travel Planner",
        "smart_planner_subtitle": "Plan your custom itinerary, calculate your budget breakdown, and view customized hotel recommendations.",
        "customize_trip": "⚙️ Customize Your Trip",
        "where_to_go": "Where do you want to go?",
        "number_of_days": "Number of Days",
        "choose_budget_tier": "Choose Budget Tier",
        "custom_itinerary": "🗺️ Custom Itinerary: {days} Days in {city}",
        "recommended_stay_label": "🏨 Recommended Stay ({tier}):",
        "estimated_budget_breakdown": "### 💰 Estimated Budget Breakdown",
        "total_estimated_expenses": "Total Estimated Expenses",
        "for_days_tier": "For {days} days • {tier} tier",
        "detailed_allocation_table": "##### Detailed Allocation Table",
        "important_travel_tips": "### ℹ️ Important Travel Tips",
        "airport_transfer_label": "✈️ Airport Transfer:",
        "city_transit_label": "🚇 City Transit:",
        "ai_chatbot_title": "💬 AI Travel Assistant",
        "ai_chatbot_subtitle": "Ask questions about local rules, etiquette, food, attractions, and safety tips. Answers are based on our travel database.",
        "suggested_questions": "##### 💡 Suggested Questions",
        "suggest_hyd_food": "🍽️ Hyderabad food?",
        "suggest_sg_rules": "🚦 Singapore rules?",
        "suggest_tokyo_etiq": "👘 Tokyo etiquette?",
        "chat_placeholder": "Ask about rules, food, stays, or safety...",
        "chat_bot_welcome": "Hello! I am your TravelMate AI Assistant. Ask me anything about local rules, etiquette, food, and stays for India, Japan, or Singapore.",
        "capital_label": "Capital",
        "currency_label": "Currency",
        "language_label": "Language",
        "timezone_label": "Timezone",
        "explore_country_title": "Explore {country}",
        "country_hero_subtitle": "Essential facts, visa details, local laws, and cultural etiquette for visiting {country}.",
        "country_profile": "### 📊 Country Profile",
        "emergency_numbers_label": "🚨 Emergency Numbers:",
        "visa_tab": "📑 Visa & Entry Requirements",
        "rules_tab": "📜 Rules & Cultural Etiquette",
        "safety_tab": "🛡️ Safety & Travel Tips",
        "visa_requirements_title": "### 📑 Visa & Entry Requirements",
        "pre_departure_checklist": "#### ✈️ Quick Pre-Departure Checklist",
        "checklist_passport": "Check passport validity (should have at least 6 months validity from departure date).",
        "checklist_visa_sg": "Complete visa or online entry forms (e.g. SG Arrival Card).",
        "checklist_visa_evisa": "Complete visa or online entry forms (e.g. eVisa application).",
        "checklist_insurance": "Secure health or travel insurance covering local medical systems.",
        "checklist_bank": "Inform your bank about travel dates to prevent card locks.",
        "important_rules_title": "### 📜 Important Rules & Regulations",
        "cultural_dos_donts": "### 🤝 Cultural Dos & Don'ts",
        "health_safety_guidelines": "#### 🌟 Health & Safety Guidelines",
        "local_travel_warnings": "#### 🗺️ Local Travel Warnings",
        "cities_in_country": "🏙️ Cities in {country}",
        "explore_city_btn": "Explore {city}",
        "go_to_country_btn": "Go to {country}",
        "vegetarian_badge": "Vegetarian",
        "non_vegetarian_badge": "Non-Vegetarian",
        "shopping_area_badge": "Shopping Area",
        "made_with_love": "Made with ❤️ for Travelers",
        "home": "Home",
        "explore": "Explore",
        "plan_ask": "Plan & Ask",
        "country_info_title": "Country Information",
        "city_info_title": "City Information",
        "planner_title": "Travel Planner",
        "chatbot_title": "AI Travel Assistant",
        "budget_economy": "Economy (Cost-Effective)",
        "budget_mid_range": "Mid-Range (Balanced)",
        "budget_luxury": "Luxury (Premium Experience)",
        "day_title": "📅 Day {day} - Exploring the Heart of the City",
        "morning_activity": "☀️ Morning: Visit {name}",
        "lunch_activity": "😋 Lunch: Try local {name}",
        "afternoon_activity": "⛅ Afternoon: Tour {name}",
        "evening_shop": "🛍️ Evening: Shop at {name}",
        "evening_free": "🌆 Evening: Free exploration and dining",
        "evening_free_desc": "Walk through local streets, discover street food stalls, and interact with the local culture.",
        "category_accommodation": "🏨 Accommodation",
        "category_food": "🍜 Food & Dining",
        "category_transport": "🚌 Transport",
        "category_sightseeing": "🎟️ Sightseeing",
        "category_shopping": "🎁 Shopping/Misc",
        "bot_food_city": "🍲 **Here are the must-try foods in {city} ({country}):**\n\n{list}\n\n*Make sure to check out local street food stalls for the most authentic taste!*",
        "bot_attract_city": "🎡 **Top tourist attractions in {city}:**\n\n{list}",
        "bot_hotel_city": "🏨 **Recommended stays in {city}:**\n\n{list}",
        "bot_transit_city": "🚌 **Transit guide for {city}:**\n\n- **Public Transport:** {transit}\n\n- **Airport Details:** {airport}",
        "bot_safety_city": "🛡️ **Safety Recommendations for {city}:**\n\n{safety}",
        "bot_rules_city": "📜 **Rules & Etiquette to follow in {city} (referencing {country} guidelines):**\n\n**Rules:**\n{rules}\n\n**Cultural Etiquette:**\n{etiquette}",
        "bot_welcome_city": "🏙️ **Welcome to {city}!**\n\n{desc}\n\nAsk me specific questions like:\n- *What food should I try in {city}?*\n- *What are the tourist attractions in {city}?*\n- *How is the public transport in {city}?*",
        "bot_rules_country": "📜 **Important Rules & Regulations to follow in {country}:**\n\n{rules}\n\n*Violating local regulations can lead to hefty fines, so keep these in mind!*",
        "bot_etiquette_country": "🤝 **Cultural Dos and Don'ts for {country}:**\n\n{etiquette}",
        "bot_safety_country": "🛡️ **Safety Guidelines for {country}:**\n\n{safety}\n\n🚨 **Emergency Numbers:** {emergency}",
        "bot_visa_country": "📑 **Visa & Entry information for {country}:**\n\n{visa}",
        "bot_welcome_country": "🌍 **Welcome to {country}!**\n\n- **Capital:** {capital}\n- **Currency:** {currency}\n- **Language:** {language}\n- **Timezone:** {timezone}\n\nAsk me specific questions like:\n- *What are the traffic rules in {country}?*\n- *What is the cultural etiquette in {country}?*\n- *How do I get a visa for {country}?*",
        "bot_fallback": "👋 Hello! I am your AI Travel Companion.\n\nI can answer questions regarding **local laws, customs, safety, transport, delicacies, and hotels** for the following destinations currently in my database:\n- **India** (Hyderabad, Visakhapatnam)\n- **Japan** (Tokyo, Osaka)\n- **Singapore** (Singapore City/Downtown Core)\n\nTry asking me queries like:\n- *What should I know before visiting Tokyo?*\n- *What are the traffic rules in Singapore?*\n- *What food should I try in Hyderabad?*\n- *What is the currency in Japan?*"
    },
    "hi": {
        "app_subtitle": "आपका स्मार्ट यात्रा साथी",
        "home_hero_subtitle": "आगमन से पहले आवश्यक स्थानीय कानूनों, सांस्कृतिक शिष्टाचार, पारगमन गाइड, शीर्ष खाद्य पदार्थों और सुरक्षा सलाह की खोज करें।",
        "trend_tokyo_title": "शिबुया, टोक्यो",
        "trend_tokyo_desc": "जापान के दिल की हाई-टेक नियॉन रोशनी, ऐतिहासिक मंदिरों और मिशेलिन-तारांकित भोजन परिदृश्य का अनुभव करें।",
        "most_popular": "सबसे लोकप्रिय",
        "trend_hyd_title": "पुराना शहर, हैदराबाद",
        "trend_hyd_desc": "विश्व प्रसिद्ध बिरयानी का स्वाद लें, ऐतिहासिक चारमीनार के सामने खड़े हों, और निज़ाम के विरासत बाज़ार में मोती खरीदें।",
        "cultural_choice": "सांस्कृतिक विकल्प",
        "trend_sg_title": "गार्डन सिटी, सिंगापुर",
        "trend_sg_desc": "भविष्य के बगीचों में टहलें, मरीना बे सैंड्स को देखकर अचंभित हों, और स्थानीय हॉकर फूड कोर्ट की खोज करें।",
        "safest_destination": "सबसे सुरक्षित गंतव्य",
        "quick_search": "🔍 त्वरित खोज",
        "search_placeholder": "जैसे, टोक्यो, भारत, बिरयानी, मंदिर...",
        "matching_countries": "##### मेल खाने वाले देश",
        "matching_cities": "##### मेल खाने वाले शहर",
        "no_matching_countries": "कोई मेल खाते देश नहीं मिले।",
        "no_matching_cities": "कोई मेल खाते शहर नहीं मिले।",
        "destination_guide": "🗺️ गंतव्य मार्गदर्शिका",
        "no_travel_data": "कोई यात्रा डेटा उपलब्ध नहीं है। कृपया डेटाबेस प्रारंभ करें।",
        "select_country": "देश चुनें",
        "view_country_guide": "📖 देश की मार्गदर्शिका देखें",
        "select_city": "शहर चुनें",
        "view_city_details": "🏙️ शहर का विवरण देखें",
        "no_cities_available": "इस देश के लिए कोई शहर उपलब्ध नहीं है।",
        "featured_destinations": "⭐ चुनिंदा गंतव्य",
        "explore_tokyo": "टोक्यो देखें",
        "explore_hyderabad": "हैदराबाद देखें",
        "explore_singapore": "सिंगापुर देखें",
        "explore_another_country": "दूसरे देश का अन्वेषण करें",
        "select_destination": "गंतव्य चुनें",
        "country_label": "देश",
        "city_label": "शहर",
        "no_cities_warning": "इस देश में कोई शहर नहीं है।",
        "attractions_tab": "🎡 आकर्षण और खरीदारी",
        "food_tab": "🍲 स्थानीय व्यंजन",
        "stays_tab": "🏨 अनुशंसित ठहराव",
        "transit_tab": "🚌 पारगमन और हवाई अड्डा मार्गदर्शिका",
        "top_attractions": "### 🎡 घूमने के लिए शीर्ष आकर्षण",
        "famous_shopping": "### 🛍️ प्रसिद्ध खरीदारी स्थल",
        "must_try_dishes": "### 🍲 अवश्य आज़माने वाले प्रसिद्ध व्यंजन",
        "veg_delights": "#### 🟢 शाकाहारी व्यंजन",
        "non_veg_specials": "#### 🔴 मांसाहारी विशेष",
        "local_favorites": "#### 🌟 स्थानीय पसंदीदा",
        "recommended_accommodations": "### 🏨 अनुशंसित आवास",
        "budget_friendly": "#### 🪙 बजट के अनुकूल",
        "mid_range_comfort": "#### 🏢 मध्यम श्रेणी का आराम",
        "luxury_stay": "#### 💎 लक्जरी ठहराव",
        "airport_access": "### ✈️ हवाई अड्डा पहुंच विवरण",
        "public_transport": "### 🚌 स्थानीय सार्वजनिक परिवहन",
        "safety_recommendations_for": "🛡️ सुरक्षा सिफारिशें - ",
        "smart_planner_title": "📅 स्मार्ट यात्रा योजनाकार",
        "smart_planner_subtitle": "अपनी कस्टम यात्रा कार्यक्रम की योजना बनाएं, अपने बजट विश्लेषण की गणना करें, और अनुकूलित होटल सिफारिशें देखें।",
        "customize_trip": "⚙️ अपनी यात्रा को अनुकूलित करें",
        "where_to_go": "आप कहाँ जाना चाहते हैं?",
        "number_of_days": "दिनों की संख्या",
        "choose_budget_tier": "बजट श्रेणी चुनें",
        "custom_itinerary": "🗺️ कस्टम यात्रा कार्यक्रम: {city} में {days} दिन",
        "recommended_stay_label": "🏨 अनुशंसित ठहराव ({tier}):",
        "estimated_budget_breakdown": "### 💰 अनुमानित बजट विवरण",
        "total_estimated_expenses": "कुल अनुमानित खर्च",
        "for_days_tier": "{days} दिनों के लिए • {tier} श्रेणी",
        "detailed_allocation_table": "##### विस्तृत आवंटन तालिका",
        "important_travel_tips": "### ℹ️ महत्वपूर्ण यात्रा सुझाव",
        "airport_transfer_label": "✈️ हवाई अड्डा स्थानांतरण:",
        "city_transit_label": "🚇 शहर पारगमन:",
        "ai_chatbot_title": "💬 एआई यात्रा सहायक",
        "ai_chatbot_subtitle": "स्थानीय नियमों, शिष्टाचार, भोजन, आकर्षण और सुरक्षा युक्तियों के बारे में प्रश्न पूछें। उत्तर हमारे यात्रा डेटाबेस पर आधारित हैं।",
        "suggested_questions": "##### 💡 सुझाए गए प्रश्न",
        "suggest_hyd_food": "🍽️ हैदराबाद भोजन?",
        "suggest_sg_rules": "🚦 सिंगापुर नियम?",
        "suggest_tokyo_etiq": "👘 टोक्यो शिष्टाचार?",
        "chat_placeholder": "नियम, भोजन, ठहराव या सुरक्षा के बारे में पूछें...",
        "chat_bot_welcome": "नमस्ते! मैं आपका ट्रेवलमेट एआई सहायक हूँ। भारत, जापान या सिंगापुर के स्थानीय नियमों, शिष्टाचार, भोजन और ठहराव के बारे में कुछ भी पूछें।",
        "capital_label": "राजधानी",
        "currency_label": "मुद्रा",
        "language_label": "भाषा",
        "timezone_label": "समय क्षेत्र",
        "explore_country_title": "अन्वेषण करें - {country}",
        "country_hero_subtitle": "{country} की यात्रा के लिए आवश्यक तथ्य, वीजा विवरण, स्थानीय कानून और सांस्कृतिक शिष्टाचार।",
        "country_profile": "### 📊 देश प्रोफ़ाइल",
        "emergency_numbers_label": "🚨 आपातकालीन नंबर:",
        "visa_tab": "📑 वीजा और प्रवेश आवश्यकताएं",
        "rules_tab": "📜 नियम और सांस्कृतिक शिष्टाचार",
        "safety_tab": "🛡️ सुरक्षा और यात्रा युक्तियाँ",
        "visa_requirements_title": "### 📑 वीजा और प्रवेश आवश्यकताएं",
        "pre_departure_checklist": "#### ✈️ प्रस्थान पूर्व त्वरित चेकलिस्ट",
        "checklist_passport": "पासपोर्ट की वैधता जांचें (प्रस्थान तिथि से कम से कम 6 महीने की वैधता होनी चाहिए)।",
        "checklist_visa_sg": "वीजा या ऑनलाइन प्रवेश पत्र पूरा करें (जैसे एसजी आगमन कार्ड)।",
        "checklist_visa_evisa": "वीजा या ऑनलाइन प्रवेश पत्र पूरा करें (जैसे ई-वीजा आवेदन)।",
        "checklist_insurance": "स्थानीय चिकित्सा प्रणालियों को कवर करने वाला स्वास्थ्य या यात्रा बीमा सुरक्षित करें।",
        "checklist_bank": "कार्ड लॉक को रोकने के लिए अपने बैंक को यात्रा की तारीखों के बारे में सूचित करें।",
        "important_rules_title": "### 📜 महत्वपूर्ण नियम और कानून",
        "cultural_dos_donts": "### 🤝 सांस्कृतिक क्या करें और क्या न करें",
        "health_safety_guidelines": "#### 🌟 स्वास्थ्य और सुरक्षा दिशानिर्देश",
        "local_travel_warnings": "#### 🗺️ स्थानीय यात्रा चेतावनी",
        "cities_in_country": "{country} में शहर",
        "explore_city_btn": "{city} का अन्वेषण करें",
        "go_to_country_btn": "{country} पर जाएं",
        "vegetarian_badge": "शाकाहारी",
        "non_vegetarian_badge": "मांशाहारी",
        "shopping_area_badge": "खरीदारी क्षेत्र",
        "made_with_love": "यात्रियों के लिए ❤️ के साथ बनाया गया",
        "home": "होम",
        "explore": "अन्वेषण करें",
        "plan_ask": "योजना और पूछें",
        "country_info_title": "देश की जानकारी",
        "city_info_title": "शहर की जानकारी",
        "planner_title": "यात्रा योजनाकार",
        "chatbot_title": "एआई यात्रा सहायक",
        "budget_economy": "इकोनॉमी (लागत प्रभावी)",
        "budget_mid_range": "मिड-रेंज (संतुलित)",
        "budget_luxury": "लक्जरी (प्रीमियम अनुभव)",
        "day_title": "📅 दिन {day} - शहर के केंद्र की खोज",
        "morning_activity": "☀️ सुबह: {name} की यात्रा करें",
        "lunch_activity": "😋 दोपहर का भोजन: स्थानीय {name} आज़माएं",
        "afternoon_activity": "⛅ दोपहर बाद: {name} का दौरा करें",
        "evening_shop": "🛍️ शाम: {name} में खरीदारी करें",
        "evening_free": "🌆 शाम: मुफ्त अन्वेषण और भोजन",
        "evening_free_desc": "स्थानीय सड़कों पर चलें, स्ट्रीट फूड स्टालों की खोज करें, और स्थानीय संस्कृति के साथ बातचीत करें।",
        "category_accommodation": "🏨 आवास",
        "category_food": "🍜 भोजन और डाइनिंग",
        "category_transport": "🚌 परिवहन",
        "category_sightseeing": "🎟️ दर्शनीय स्थल",
        "category_shopping": "🎁 खरीदारी/विविध",
        "bot_food_city": "🍲 **यहाँ {city} ({country}) के अवश्य आज़माने वाले व्यंजन दिए गए हैं:**\n\n{list}\n\n*सबसे प्रामाणिक स्वाद के लिए स्थानीय स्ट्रीट फूड स्टालों को अवश्य देखें!*",
        "bot_attract_city": "🎡 **{city} में शीर्ष पर्यटक आकर्षण:**\n\n{list}",
        "bot_hotel_city": "🏨 **{city} में अनुशंसित ठहराव:**\n\n{list}",
        "bot_transit_city": "🚌 **{city} के लिए पारगमन मार्गदर्शिका:**\n\n- **सार्वजनिक परिवहन:** {transit}\n\n- **हवाई अड्डा विवरण:** {airport}",
        "bot_safety_city": "🛡️ **{city} के लिए सुरक्षा सिफारिशें:**\n\n{safety}",
        "bot_rules_city": "📜 **{city} में पालन करने योग्य नियम और शिष्टाचार ({country} के दिशानिर्देश):**\n\n**नियम:**\n{rules}\n\n**सांस्कृतिक शिष्टाचार:**\n{etiquette}",
        "bot_welcome_city": "🏙️ **{city} में आपका स्वागत है!**\n\n{desc}\n\nमुझसे विशिष्ट प्रश्न पूछें जैसे:\n- *{city} में मुझे क्या खाना चाहिए?*\n- *{city} में पर्यटक आकर्षण क्या हैं?*\n- *{city} में सार्वजनिक परिवहन कैसा है?*",
        "bot_rules_country": "📜 **{country} में पालन करने योग्य महत्वपूर्ण नियम और कानून:**\n\n{rules}\n\n*स्थानीय नियमों का उल्लंघन करने पर भारी जुर्माना हो सकता है, इसलिए इन्हें ध्यान में रखें!*",
        "bot_etiquette_country": "🤝 **{country} के लिए सांस्कृतिक क्या करें और क्या न करें:**\n\n{etiquette}",
        "bot_safety_country": "🛡️ **{country} के लिए सुरक्षा दिशानिर्देश:**\n\n{safety}\n\n🚨 **आपातकालीन नंबर:** {emergency}",
        "bot_visa_country": "📑 **{country} के लिए वीजा और प्रवेश जानकारी:**\n\n{visa}",
        "bot_welcome_country": "🌍 **{country} में आपका स्वागत है!**\n\n- **राजधानी:** {capital}\n- **मुद्रा:** {currency}\n- **भाषा:** {language}\n- **समय क्षेत्र:** {timezone}\n\nमुझसे विशिष्ट प्रश्न पूछें जैसे:\n- *{country} में यातायात के नियम क्या हैं?*\n- *{country} में सांस्कृतिक शिष्टाचार क्या है?*\n- *{country} के लिए वीजा कैसे प्राप्त करें?*",
        "bot_fallback": "👋 नमस्ते! मैं आपका एआई यात्रा साथी हूँ।\n\nमैं वर्तमान में मेरे डेटाबेस में मौजूद निम्नलिखित गंतव्यों के लिए स्थानीय कानूनों, रीति-रिवाजों, सुरक्षा, परिवहन, व्यंजनों और होटलों के बारे में प्रश्नों के उत्तर दे सकता हूँ:\n- **भारत** (हैदराबाद, विशाखापत्तनम)\n- **जापान** (टोक्यो, ओसाका)\n- **सिंगापुर** (सिंगापुर सिटी/डाउनटाउन कोर)\n\nमुझसे इस तरह के प्रश्न पूछने का प्रयास करें:\n- *टोक्यो जाने से पहले मुझे क्या पता होना चाहिए?*\n- *सिंगापुर में यातायात के नियम क्या हैं?*\n- *हैदराबाद में मुझे क्या खाना चाहिए?*\n- *जापान में मुद्रा क्या है?*"
    },
    "te": {
        "app_subtitle": "మీ స్మార్ట్ ప్రయాణ తోడు",
        "home_hero_subtitle": "మీరు రాకముందే అవసరమైన స్థానిక చట్టాలు, సాంస్కృతిక మర్యాదలు, రవాణా మార్గదర్శకాలు, అగ్ర ఆహారాలు మరియు భద్రతా సలహాలను కనుగొనండి.",
        "trend_tokyo_title": "షిబుయా, టోక్యో",
        "trend_tokyo_desc": "జపాన్ నడిబొడ్డున ఉన్న హై-టెక్ నియాన్ లైట్లు, చారిత్రాత్మక మందిరాలు మరియు మిషిలిన్-స్టార్డ్ వంటకాల అనుభవాన్ని పొందండి.",
        "most_popular": "అత్యంత ప్రజాదరణ పొందినది",
        "trend_hyd_title": "పాత బస్తీ, హైదరాబాద్",
        "trend_hyd_desc": "ప్రపంచ ప్రసిద్ధ బిర్యానీని రుచి చూడండి, చారిత్రాత్మక చార్మినార్ ముందు నిలబడండి మరియు నిజాంల హెరిటేజ్ బజార్‌లో ముత్యాలను కొనండి.",
        "cultural_choice": "సాంస్కృతిక ఎంపిక",
        "trend_sg_title": "గార్డెన్ సిటీ, సింగపూర్",
        "trend_sg_desc": "భవిష్యత్ తోటల గుండా నడవండి, మెరీనా బే సాండ్స్ చూసి ఆశ్చర్యపోండి మరియు స్థానిక హాకర్ ఫుడ్ కోర్టులను కనుగొనండి.",
        "safest_destination": "అత్యంత సురక్షితమైన గమ్యస్థానం",
        "quick_search": "🔍 త్వరిత శోధన",
        "search_placeholder": "ఉదా. టోక్యో, ఇండియా, బిర్యానీ, దేవాలయాలు...",
        "matching_countries": "##### సరిపోలే దేశాలు",
        "matching_cities": "##### సరిపోలే నగరాలు",
        "no_matching_countries": "సరిపోలే దేశాలు ఏవీ కనుగొనబడలేదు.",
        "no_matching_cities": "సరిపోలే నగరాలు ఏవీ కనుగొనబడలేదు.",
        "destination_guide": "🗺️ గమ్యస్థాన మార్గదర్శిని",
        "no_travel_data": "ప్రయాణ డేటా అందుబాటులో లేదు. దయచేసి డేటాబేస్ ప్రారంభించండి.",
        "select_country": "దేశాన్ని ఎంచుకోండి",
        "view_country_guide": "📖 देश మార్గదర్శిని చూడండి",
        "select_city": "నగరాన్ని ఎంచుకోండి",
        "view_city_details": "🏙️ నగర వివరాలను చూడండి",
        "no_cities_available": "ఈ దేశానికి నగరాలు అందుబాటులో లేవు.",
        "featured_destinations": "⭐ ఫీచర్ చేయబడిన గమ్యస్థానాలు",
        "explore_tokyo": "టోక్యోని అన్వేషించండి",
        "explore_hyderabad": "హైదరాబాద్‌ని అన్వేషించండి",
        "explore_singapore": "సింగపూర్‌ని అన్వేషించండి",
        "explore_another_country": "మరొక దేశాన్ని అన్వేషించండి",
        "select_destination": "గమ్యస్థానాన్ని ఎంచుకోండి",
        "country_label": "దేశం",
        "city_label": "నగరం",
        "no_cities_warning": "ఈ దేశంలో నగరాలు లేవు.",
        "attractions_tab": "🎡 ఆకర్షణలు & షాపింగ్",
        "food_tab": "🍲 స్థానిక వంటకాలు",
        "stays_tab": "🏨 సిఫార్సు చేయబడిన బసలు",
        "transit_tab": "🚌 రవాణా & విమానాశ్రయ మార్గదర్శిని",
        "top_attractions": "### 🎡 సందర్శించవలసిన ప్రధాన ఆకర్షణలు",
        "famous_shopping": "### 🛍️ ప్రసిద్ధ షాపింగ్ ప్రదేశాలు",
        "must_try_dishes": "### 🍲 తప్పక రుచి చూడవలసిన ప్రసిద్ధ వంటకాలు",
        "veg_delights": "#### 🟢 శాఖాహార రుచులు",
        "non_veg_specials": "#### 🔴 మాంసాహార ప్రత్యేకతలు",
        "local_favorites": "#### 🌟 స్థానిక ఇష్టమైనవి",
        "recommended_accommodations": "### 🏨 సిఫార్సు చేయబడిన వసతి గృహాలు",
        "budget_friendly": "#### 🪙 బడ్జెట్ అనుకూలమైనవి",
        "mid_range_comfort": "#### 🏢 మిడ్-రేంజ్ కంఫర్ట్",
        "luxury_stay": "#### 💎 లగ్జరీ బస",
        "airport_access": "### ✈️ విమానాశ్రయ ప్రాప్యత వివరాలు",
        "public_transport": "### 🚌 స్థానిక ప్రజా రవాణా",
        "safety_recommendations_for": "🛡️ భద్రతా సిఫార్సులు - ",
        "smart_planner_title": "📅 స్మార్ట్ ట్రావెల్ ప్లానర్",
        "smart_planner_subtitle": "మీ కస్టమ్ ప్రయాణ ప్రణాళికను సిద్ధం చేసుకోండి, మీ బడ్జెట్ విభజనను లెక్కించండి మరియు అనుకూలీకరించిన హోటల్ సిఫార్సులను చూడండి.",
        "customize_trip": "⚙️ మీ ప్రయాణాన్ని అనుకూలీకరించండి",
        "where_to_go": "మీరు ఎక్కడికి వెళ్లాలనుకుంటున్నారు?",
        "number_of_days": "రోజుల సంఖ్య",
        "choose_budget_tier": "బడ్జెట్ శ్రేణిని ఎంచుకోండి",
        "custom_itinerary": "🗺️ అనుకూలీకరించిన ప్రయాణ ప్రణాళిక: {city} లో {days} రోజులు",
        "recommended_stay_label": "🏨 సిఫార్సు చేయబడిన బస ({tier}):",
        "estimated_budget_breakdown": "### 💰 అంచనా బడ్జెట్ విభజన",
        "total_estimated_expenses": "మొత్తం అంచనా వ్యయం",
        "for_days_tier": "{days} రోజులకు • {tier} శ్రేణి",
        "detailed_allocation_table": "##### వివరణాత్మక కేటాయింపు పట్టిక",
        "important_travel_tips": "### ℹ️ ముఖ్యమైన ప్రయాణ చిట్కాలు",
        "airport_transfer_label": "✈️ విమానాశ్రయం బదిలీ:",
        "city_transit_label": "🚇 సిటీ రవాణా:",
        "ai_chatbot_title": "💬 ఎఐ ట్రావెల్ అసిస్టెంట్",
        "ai_chatbot_subtitle": "స్థానిక నిబంధనలు, మర్యాదలు, ఆహారం, ఆకర్షణలు మరియు భద్రతా చిట్కాల గురించి ప్రశ్నలు అడగండి. సమాధానాలు మా ప్రయాణ డేటాబేస్ ఆధారంగా ఉంటాయి.",
        "suggested_questions": "##### 💡 సూచించబడిన ప్రశ్నలు",
        "suggest_hyd_food": "🍽️ హైదరాబాద్ ఆహారం?",
        "suggest_sg_rules": "🚦 సింగపూర్ నిబంధనలు?",
        "suggest_tokyo_etiq": "👘 టోక్యో మర్యాదలు?",
        "chat_placeholder": "నిబంధనలు, ఆహారం, బసలు లేదా భద్రత గురించి అడगండి...",
        "chat_bot_welcome": "హలో! నేను మీ ట్రావెల్‌మేట్ ఎఐ అసిస్టెంట్‌ని. భారతదేశం, జపాన్ లేదా సింగపూర్ యొక్క స్థానిక నిబంధనలు, మర్యాదలు, ఆహారం మరియు బస గురించి ఏదైనా అడగండి.",
        "capital_label": "రాజధాని",
        "currency_label": "కరెన్సీ",
        "language_label": "భాష",
        "timezone_label": "సమయ మండలి",
        "explore_country_title": "{country} అన్వేషించండి",
        "country_hero_subtitle": "{country} సందర్శించడానికి అవసరమైన వాస్తవాలు, వీసా వివరాలు, స్థానిక చట్టాలు మరియు సాంస్కృతిక మర్యాదలు.",
        "country_profile": "### 📊 దేశం ప్రొఫైల్",
        "emergency_numbers_label": "🚨 అత్యవసర సంఖ్యలు:",
        "visa_tab": "📑 వీసా & ప్రవేశ అవసరాలు",
        "rules_tab": "📜 నిబంధనలు & సాంస్కృతిక మర్యాదలు",
        "safety_tab": "🛡️ భద్రత & ప్రయాణ చిట్కాలు",
        "visa_requirements_title": "### 📑 వీసా & ప్రవేశ అవసరాలు",
        "pre_departure_checklist": "#### ✈️ త్వరిక నిష్క్రమణకు ముందు తనిఖీ జాబితా",
        "checklist_passport": "పాస్‌పోర్ట్ చెల్లుబాటును తనిఖీ చేయండి (నిష్క్రమణ తేదీ నుండి కనీసం 6 నెలల చెల్లుబాటు ఉండాలి).",
        "checklist_visa_sg": "వీసా లేదా ఆన్‌లైన్ ప్రవేశ ఫారమ్‌లను పూర్తి చేయండి (ఉదా. SG అరైవల్ కార్డ్).",
        "checklist_visa_evisa": "వీసా లేదా ఆన్‌లైన్ ప్రవేశ ఫారమ్‌లను పూర్తి చేయండి (ఉదా. ఇ-వీసా దరఖాస్తు).",
        "checklist_insurance": "స్థానిక వైద్య వ్యవస్థలను కవర్ చేసే ఆరోగ్య లేదా ప్రయాణ బీమాను పొందండి.",
        "checklist_bank": "కార్డ్ లాక్‌లను నిరోధించడానికి ప్రయాణ తేదీల గురించి మీ బ్యాంక్‌కు తెలియజేయండి.",
        "important_rules_title": "### 📜 ముఖ్యమైన నిబంధనలు & చట్టాలు",
        "cultural_dos_donts": "### 🤝 సాంస్కృతిక చేయవలసినవి & చేయకూడనివి",
        "health_safety_guidelines": "#### 🌟 ఆరోగ్యం & భద్రత మార్గదర్శకాలు",
        "local_travel_warnings": "#### 🗺️ స్థానిక ప్రయాణ హెచ్చరికలు",
        "cities_in_country": "{country} లోని నగరాలు",
        "explore_city_btn": "{city} అన్వేషించండి",
        "go_to_country_btn": "{country} కి వెళ్ళండి",
        "vegetarian_badge": "శాఖాహారం",
        "non_vegetarian_badge": "మాంసాహారం",
        "shopping_area_badge": "షాపింగ్ ప్రాంతం",
        "made_with_love": "ప్రయాణీకుల కోసం ❤️ తో తయారు చేయబడింది",
        "home": "హోమ్",
        "explore": "అన్వేషించండి",
        "plan_ask": "ప్రణాళిక & అడగండి",
        "country_info_title": "దేశ సమాచారం",
        "city_info_title": "నగర సమాచారం",
        "planner_title": "ప్రయాణ ప్లానర్",
        "chatbot_title": "ఎఐ ప్రయాణ సహాయకుడు",
        "budget_economy": "ఎకానమీ (బడ్జెట్ అనుకూల)",
        "budget_mid_range": "మిడ్-రేంజ్ (సమతుల్య)",
        "budget_luxury": "లగ్జరీ (ప్రీమియం అనుభవం)",
        "day_title": "📅 రోజు {day} - నగరం నడిబొడ్డును అన్వేషించడం",
        "morning_activity": "☀️ ఉదయం: {name} సందర్శించండి",
        "lunch_activity": "😋 మధ్యాహ్నం భోజనం: స్థానిక {name} రుచి చూడండి",
        "afternoon_activity": "⛅ మధ్యాహ్నం: {name} విహారయాత్ర",
        "evening_shop": "🛍️ సాయంత్రం: {name} లో షాపింగ్",
        "evening_free": "🌆 సాయంత్రం: ఉచిత అన్వేషణ మరియు భోజనం",
        "evening_free_desc": "స్థానిక వీధుల గుండా నడవండి, వీధి ఆహార దుకాణాలను కనుగొనండి మరియు స్థానిక సంస్కృతిని తెలుసుకోండి.",
        "category_accommodation": "🏨 వసతి",
        "category_food": "🍜 ఆహారం & భోజనం",
        "category_transport": "🚌 రవాణా",
        "category_sightseeing": "🎟️ సందర్శన",
        "category_shopping": "🎁 షాపింగ్/ఇతరాలు",
        "bot_food_city": "🍲 **{city} ({country}) లో తప్పక రుచి చూడవలసిన కొన్ని వంటకాలు ఇక్కడ ఉన్నాయి:**\n\n{list}\n\n*అసలైన రుచి కోసం స్థానిక వీధి ఆహార దుకాణాలను సందర్శించడం మర్చిపోవద్దు!*",
        "bot_attract_city": "🎡 **{city} లోని ప్రధాన పర్యాటక ఆకర్షణలు:**\n\n{list}",
        "bot_hotel_city": "🏨 **{city} లో సిఫార్సు చేయబడిన బసలు:**\n\n{list}",
        "bot_transit_city": "🚌 **{city} రవాణా మార్గదర్శిని:**\n\n- **ప్రజా రవాణా:** {transit}\n\n- **విమానాశ్రయం వివరాలు:** {airport}",
        "bot_safety_city": "🛡️ **{city} కోసం భద్రతా సిఫార్సులు:**\n\n{safety}",
        "bot_rules_city": "📜 **{city} లో పాటించవలసిన నిబంధనలు & మర్యాదలు ({country} మార్గదర్శకాల ప్రకారం):**\n\n**నిబంధనలు:**\n{rules}\n\n**సాంస్కృతిక మర్యాదలు:**\n{etiquette}",
        "bot_welcome_city": "🏙️ **{city} కి స్వాగతం!**\n\n{desc}\n\nనన్ను ఇలాంటి ప్రశ్నలు అడగండి:\n- *{city} లో ఏ ఆహారం రుచి చూడాలి?*\n- *{city} లోని సందర్శనీయ స్థలాలు ఏమిటి?*\n- *{city} లో ప్రజా రవాణా ఎలా ఉంది?*",
        "bot_rules_country": "📜 **{country} లో పాటించవలసిన ముఖ్యమైన నిబంధనలు & చట్టాలు:**\n\n{rules}\n\n*స్థానిక నిబంధనలను ఉల్లంఘిస్తే భారీ జరిమానాలు విధించబడతాయి, కాబట్టి వీటిని గుర్తుంచుకోండి!*",
        "bot_etiquette_country": "🤝 **{country} కోసం సాంస్కృతిక చేయవలసినవి & చేయకూడనివి:**\n\n{etiquette}",
        "bot_safety_country": "🛡️ **{country} కోసం భద్రతా మార్గదర్శకాలు:**\n\n{safety}\n\n🚨 **అత్యవసర సంఖ్యలు:** {emergency}",
        "bot_visa_country": "📑 **{country} కోసం వీసా & ప్రవేశ సమాచారం:**\n\n{visa}",
        "bot_welcome_country": "🌍 **{country} కి స్వాగతం!**\n\n- **రాజధాని:** {capital}\n- **కరెన్సీ:** {currency}\n- **భాష:** {language}\n- **సమయ మండలి:** {timezone}\n\nనన్ను ఇలాంటి ప్రశ్నలు అడగండి:\n- *{country} లో ట్రాఫిక్ నిబంధనలు ఏమిటి?*\n- *{country} లో సాంస్కృతిక మర్యాదలు ఏమిటి?*\n- *{country} కి వీసా ఎలా పొందాలి?*",
        "bot_fallback": "👋 హలో! నేను మీ ఎఐ ట్రావెల్ కంపానియన్‌ని.\n\nప్రస్తుతం నా డేటాబేస్‌లో ఉన్న క్రింది గమ్యస్థానాల కోసం స్థానిక చట్టాలు, ఆచారాలు, భద్రత, రవాణా, వంటకాలు మరియు హోటళ్లకు సంబంధించిన ప్రశ్నలకు నేను సమాధానం ఇవ్వగలను:\n- **భారతదేశం** (హైదరాబాద్, విశాఖపట్నం)\n- **జపాన్** (టోక్యో, ఒసాకా)\n- **సింగపూర్** (సింగపూర్ సిటీ/డౌన్‌టౌన్ కోర్)\n\nనన్ను ఇలాంటి ప్రశ్నలు అడగడానికి ప్రయత్నించండి:\n- *టోక్యో సందర్శించే ముందు నేను ఏమి తెలుసుకోవాలి?*\n- *సింగపూర్‌లో ట్రాఫిక్ నిబంధనలు ఏమిటి?*\n- *హైదరాబాద్‌లో ఏ ఆహారం రుచి చూడాలి?*\n- *జపాన్ లో కరెన్సీ ఏమిటి?*"
    }
}

# English term lookup mapping for search inputs in Hindi and Telugu
SEARCH_TERM_MAP = {
    # Countries
    "भारत": "India",
    "भारतदेशं": "India",
    "భారతదేశం": "India",
    "जापान": "Japan",
    "జపాన్": "Japan",
    "सिंगापुर": "Singapore",
    "సింగపూర్": "Singapore",
    
    # Cities
    "हैदराबाद": "Hyderabad",
    "హైదరాబాద్": "Hyderabad",
    "विशाखापत्तनम": "Visakhapatnam",
    "విశాఖపట్నం": "Visakhapatnam",
    "मुंबई": "Mumbai",
    "ముంబై": "Mumbai",
    "दिल्ली": "Delhi",
    "ఢిల్లీ": "Delhi",
    "बंगलौर": "Bangalore",
    "बैंगलोर": "Bangalore",
    "బెంగళూరు": "Bangalore",
    "चेन्नई": "Chennai",
    "చెన్నై": "Chennai",
    "कोलकाता": "Kolkata",
    "కోల్‌కతా": "Kolkata",
    "जयपुर": "Jaipur",
    "జైపూర్": "Jaipur",
    "आगरा": "Agra",
    "ఆగ్రా": "Agra",
    "वाराणसी": "Varanasi",
    "వారణాసి": "Varanasi",
    "कोच्चि": "Kochi",
    "కొచ్చి": "Kochi",
    "गोवा": "Goa",
    "గోవా": "Goa",
    "उदयपुर": "Udaipur",
    "ఉదయపూర్": "Udaipur",
    "पुणे": "Pune",
    "పూణే": "Pune",
    "अहमदाबाद": "Ahmedabad",
    "అహ్మదాబాద్": "Ahmedabad",
    "अमृतसर": "Amritsar",
    "అమృత్‌సర్": "Amritsar",
    "श्रीनगर": "Srinagar",
    "శ్రీనగర్": "Srinagar",
    "शिमला": "Shimla",
    "సిమ్లా": "Shimla",
    "दार्जिलिंग": "Darjeeling",
    "డార్జిలింగ్": "Darjeeling",
    "मैसूर": "Mysore",
    "మైసూర్": "Mysore",
    "टोक्यो": "Tokyo",
    "టోక్యో": "Tokyo",
    "ओसाका": "Osaka",
    "ఒసాకా": "Osaka",
    "क्योटो": "Kyoto",
    "క్యోటో": "Kyoto",
    
    # Topics / Keywords
    "भोजन": "food",
    "खाना": "food",
    "व्यंजन": "food",
    "బిర్యానీ": "biryani",
    "ఆహారం": "food",
    "వంటకాలు": "food",
    "नियम": "rules",
    "कानून": "rules",
    "నిబంధనలు": "rules",
    "చట్టాలు": "rules",
    "शिष्टाचार": "etiquette",
    "संस्कृति": "etiquette",
    "మర్యాదలు": "etiquette",
    "సంస్కృతి": "etiquette",
    "सुरक्षा": "safety",
    "भय": "safety",
    "భద్రత": "safety",
    "ఆకర్షణలు": "attractions",
    "ఆకర్షణ": "attractions",
    "पर्यटन": "attractions",
    "आकर्षण": "attractions",
    "घूमने की जगह": "attractions",
    "होटल": "hotel",
    "ठहरने": "hotel",
    "హోటల్": "hotel",
    "బస": "hotel",
    "रवाना": "transport",
    "यातायात": "transport",
    "రవాణా": "transport",
    "వీసా": "visa",
    "वीजा": "visa"
}

# Database Translation Content Dictionary
DB_TRANSLATIONS = {
    "hi": {
        "countries": {
            "India": {
                "country_name": "भारत",
                "capital": "नई दिल्ली",
                "currency": "भारतीय रुपया (INR, ₹)",
                "language": "हिंदी, अंग्रेजी",
                "timezone": "IST (UTC+5:30)",
                "emergency_number": "112 (राष्ट्रीय आपातकालीन), 100 (पुलिस), 102 (एम्बुलेंस), 101 (अग्निशमन)",
                "visa_info": "160 से अधिक देशों के पर्यटकों के लिए ई-वीजा उपलब्ध है। प्रस्थान से कम से कम 4-7 दिन पहले ऑनलाइन आवेदन करें। पासपोर्ट की वैधता कम से कम 6 महीने होनी चाहिए।",
                "rules": "1. सार्वजनिक स्थानों पर धूम्रपान सख्त वर्जित है।\n2. स्थानीय धार्मिक रीति-रिवाजों का सम्मान करें: मंदिरों या मस्जिदों में प्रवेश करने से पहले अपना सिर ढकें और जूते उतारें।\n3. विशेष रूप से धार्मिक स्थलों पर शालीन कपड़े पहनें।\n4. सार्वजनिक रूप से स्नेह प्रदर्शित करने से बचें।",
                "etiquette": "1. हाथ जोड़कर 'नमस्ते' कहकर स्थानीय लोगों का अभिवादन करें।\n2. किसी के घर में प्रवेश करने से पहले अपने जूते उतारें।\n3. खाना खाते समय, कोई वस्तु देते या लेते समय हमेशा अपने दाहिने हाथ का उपयोग करें।\n4. लोगों या धार्मिक समारोहों की तस्वीरें लेने से पहले अनुमति लें।",
                "safety_tips": "1. केवल बोतलबंद या शुद्ध पानी पिएं। सड़क की बर्फ से बचें।\n2. हवाई अड्डों पर आधिकारिक प्रीपेड टैक्सी काउंटरों या ओला/उबर जैसे मानक राइड-हेलिंग ऐप्स का उपयोग करें।\n3. जेबकतरों से बचने के लिए भीड़-भाड़ वाले पर्यटन स्थलों पर अपने बैग सुरक्षित रखें।\n4. स्थानीय मानदंडों का सम्मान करने और अवांछित ध्यान से बचने के लिए उचित कपड़े पहनें।"
            },
            "Japan": {
                "country_name": "जापान",
                "capital": "टोक्यो",
                "currency": "जापानी येन (JPY, ¥)",
                "language": "जापानी",
                "timezone": "JST (UTC+9)",
                "emergency_number": "110 (पुलिस), 119 (एम्बुलेंस और अग्निशमन)",
                "visa_info": "अनेक देशों के पर्यटकों को 90 दिनों तक वीजा-मुक्त प्रवेश मिलता है। अन्य देशों के नागरिक पहले से वीजा आवेदन करें। पासपोर्ट की वैधता कम से कम 6 महीने होनी चाहिए।",
                "rules": "1. कचरा फैलाना सख्त मना है; अपना कचरा अपने साथ रखें।\n2. सड़क पर चलते समय धूम्रपान न करें, केवल निर्दिष्ट धूम्रपान क्षेत्रों का उपयोग करें।\n3. ट्रेन में फोन पर बात करना वर्जित है; मोबाइल को साइलेंट मोड पर रखें।\n4. एस्केलेटर पर बाईं ओर खड़े हों (ओसाका में दाईं ओर)।",
                "etiquette": "1. मिलते समय हल्का झुककर अभिवादन करें।\n2. टिप देने की कोई प्रथा नहीं है; रेस्तरां में अतिरिक्त पैसे छोड़ना अशिष्ट माना जाता है।\n3. घरों और पारंपरिक रेस्तरां में प्रवेश करते समय जूते उतारें और चप्पल पहनें।\n4. सार्वजनिक स्थानों पर नाक साफ करने से बचें।",
                "safety_tips": "1. जापान दुनिया के सबसे सुरक्षित देशों में से एक है, लेकिन रात में सुनसान गलियों में सतर्क रहें।\n2. नल का पानी पीने के लिए पूरी तरह से सुरक्षित है।\n3. प्राकृतिक आपदाओं (भूकंप) के प्रति सचेत रहें और होटल के आपातकालीन निकास मार्गों को नोट करें।"
            },
            "Singapore": {
                "country_name": "सिंगापुर",
                "capital": "सिंगापुर",
                "currency": "सिंगापुर डॉलर (SGD, S$)",
                "language": "अंग्रेजी, मलय, मंदारिन, तमिल",
                "timezone": "SGT (UTC+8)",
                "emergency_number": "999 (पुलिस), 995 (एम्बुलेंस और अग्निशमन)",
                "visa_info": "प्रवेश से 3 दिन पहले पर्यटकों को ऑनलाइन 'SG Arrival Card' भरना होगा। पश्चिमी और एशियाई देशों के नागरिकों को वीजा-मुक्त प्रवेश मिलता है।",
                "rules": "1. चिंगम बेचना या आयात करना सख्त मना है; जुर्माना हो सकता है।\n2. गंदगी फैलाना, थूकना और जेवॉकिंग (सड़क गलत तरीके से पार करना) पर भारी जुर्माना है।\n3. ट्रेन और स्टेशनों पर खाना-पीना सख्त वर्जित है।\n4. खुले सार्वजनिक वाई-फाई से बिना अनुमति जुड़ना अवैध माना जा सकता है।",
                "etiquette": "1. एस्केलेटर पर बाईं ओर रहें और दाईं ओर से लोगों को आगे बढ़ने दें।\n2. 'चोपिंग': स्थानीय लोग टेबल आरक्षित करने के लिए टिशू पेपर रखते हैं, वहां न बैठें।\n3. फूड कोर्ट में खाना खाने के बाद अपनी ट्रे खुद साफ करना कानूनी रूप से अनिवार्य है।\n4. उंगली से इशारा करना अशिष्ट है, पूरे हाथ का प्रयोग करें।",
                "safety_tips": "1. सिंगापुर बेहद सुरक्षित है, रात में अकेले घूमना सुरक्षित है।\n2. नल का पानी पीने के लिए सुरक्षित और साफ है।\n3. धार्मिक स्थलों पर शालीन कपड़े पहनें और जूते उतारें।"
            }
        },
        "cities": {
            "Hyderabad": {
                "city_name": "हैदराबाद",
                "description": "मोतियों का शहर, हैदराबाद निज़ाम-कालीन इतिहास, शाही वास्तुकला और एक आधुनिक सूचना प्रौद्योगिकी केंद्र का एक सुंदर मिश्रण है।",
                "transport_info": "हैदराबाद मेट्रो रेल, स्थानीय टीएसआरटीसी बसों, ऑटो-रिक्शा और उबर/ओला कैब के माध्यम से अत्यधिक सुलभ है।",
                "airport_details": "राजीव गांधी अंतर्राष्ट्रीय हवाई अड्डा (HYD) शमशाबाद में स्थित है, जो शहर से लगभग 24 किमी दूर है।",
                "safety_recommendations": "आमतौर पर बहुत सुरक्षित है। चारमीनार जैसे भीड़भाड़ वाले क्षेत्रों में अपने बैग सुरक्षित रखें।",
                "food_info": [
                    {"name": "हैदराबादी बिरयानी", "desc": "मसालेदार मांस, दही और केसर के साथ दम पर पकाया गया सुगंधित बासमती चावल।", "type": "Non-Veg"},
                    {"name": "हलीम", "desc": "गेहूं, दाल और मांस का धीमी आंच पर पकाया गया समृद्ध स्टू, जिसे घी से सजाया जाता है।", "type": "Non-Veg"},
                    {"name": "खुबानी का मीठा", "desc": "क्रीम या कस्टर्ड के साथ परोसा जाने वाला पारंपरिक खुबानी-आधारित मीठा व्यंजन।", "type": "Veg"}
                ],
                "tourist_places": [
                    {"name": "चारमीनार", "desc": "पुरानी दिल्ली की तर्ज पर पुराने शहर के केंद्र में एक भव्य 16वीं शताब्दी की मस्जिद और ऐतिहासिक स्थल।", "rating": "4.6 ⭐", "time": "Morning"},
                    {"name": "गोलकोंडा किला", "desc": "ध्वनिक चमत्कारों और विशाल प्राचीर वाला एक मध्ययुगीन किला।", "rating": "4.7 ⭐", "time": "Afternoon"},
                    {"name": "हुसैन सागर झील", "desc": "केंद्र में बुद्ध की विशाल प्रतिमा वाली एक सुंदर दिल के आकार की झील।", "rating": "4.3 ⭐", "time": "Evening"}
                ],
                "hotel_info": {
                    "luxury": {"name": "ताज फलकनुमा पैलेस", "desc": "एक पुनर्निर्मित 19वीं सदी का शाही महल होटल।", "price": "₹35,000+ प्रति रात"},
                    "mid_range": {"name": "नोवोटेल हैदराबाद हाईटेक सिटी", "desc": "प्रौद्योगिकी कॉरिडोर के पास आधुनिक प्रीमियम ठहराव।", "price": "₹9,000 प्रति रात"},
                    "budget": {"name": "रेड फॉक्स होटल, हाईटेक सिटी", "desc": "स्वच्छ और बजट-अनुकूल व्यावसायिक होटल।", "price": "₹3,200 प्रति रात"}
                },
                "shopping_areas": [
                    {"name": "लाड बाजार", "desc": "कांच की चूड़ियों और मोतियों के लिए प्रसिद्ध पारंपरिक बाजार।"},
                    {"name": "इनऑर्बिट मॉल", "desc": "वैश्विक ब्रांडों वाला बड़ा आधुनिक शॉपिंग कॉम्प्लेक्स।"}
                ]
            },
            "Visakhapatnam": {
                "city_name": "विशाखापत्तनम",
                "description": "आंध्र प्रदेश का एक सुंदर तटीय बंदरगाह शहर, जो पहाड़ियों और बंगाल की खाड़ी से घिरा हुआ है, और अपने साफ समुद्र तटों के लिए जाना जाता है।",
                "transport_info": "स्थानीय एपीएसआरटीसी बसें, ऑटो-रिक्शा और उबर/ओला सेवाएं व्यापक रूप से उपलब्ध हैं।",
                "airport_details": "विशाखापत्तनम अंतर्राष्ट्रीय हवाई अड्डा (VTZ) शहर के केंद्र से लगभग 12 किमी दूर स्थित है।",
                "safety_recommendations": "समुद्र तटों पर तेज धाराओं से अत्यधिक सावधान रहें और गहरे पानी में न जाएं।",
                "food_info": [
                    {"name": "बांबू चिकन", "desc": "बिना तेल के बांस के टुकड़ों में पकाया गया स्वादिष्ट आदिवासी चिकन व्यंजन।", "type": "Non-Veg"},
                    {"name": "आंध्र थाली", "desc": "चावल, दाल, सब्जी और अचार के साथ परोसा जाने वाला मसालेदार क्षेत्रीय भोजन।", "type": "Veg"}
                ],
                "tourist_places": [
                    {"name": "आरके बीच", "desc": "पार्कों, संग्रहालयों और फूड स्टालों से घिरा लोकप्रिय समुद्र तट।", "rating": "4.5 ⭐", "time": "Evening"},
                    {"name": "कुरुसुरा पनडुब्बी संग्रहालय", "desc": "सार्वजनिक दौरों के लिए समुद्र तट पर खड़ी एक वास्तविक सोवियत पनडुब्बी।", "rating": "4.8 ⭐", "time": "Afternoon"}
                ],
                "hotel_info": {
                    "luxury": {"name": "नोवोटेल वरुण बीच", "desc": "समुद्र के मनोरम दृश्यों वाला आधुनिक लक्जरी होटल।", "price": "₹12,000+ प्रति रात"},
                    "mid_range": {"name": "द गेटवे होटल ताज", "desc": "ताज आतिथ्य के साथ समुद्र के किनारे आरामदायक ठहराव।", "price": "₹7,500 प्रति रात"},
                    "budget": {"name": "होटल डॉल्फिन", "desc": "शहर के केंद्र में प्रतिष्ठित बजट-अनुकूल व्यावसायिक होटल।", "price": "₹3,000 प्रति रात"}
                },
                "shopping_areas": [
                    {"name": "जगदंबा जंक्शन", "desc": "कपड़ा और इलेक्ट्रॉनिक्स बाजारों वाला व्यावसायिक शॉपिंग जिला।"},
                    {"name": "सीएमआर सेंट्रल", "desc": "फैशन ब्रांडों और सिनेमाघरों वाला लोकप्रिय शॉपिंग मॉल।"}
                ]
            },
            "Tokyo": {
                "city_name": "टोक्यो",
                "description": "जापान की राजधानी, जो भविष्य की गगनचुंबी इमारतों को ऐतिहासिक मंदिरों और बगीचों के साथ मिलाती है।",
                "transport_info": "अविश्वसनीय रूप से जटिल, अत्यधिक कुशल मेट्रो प्रणाली (मेट्रो और जेआर लाइनें)। सुइका कार्ड का उपयोग करें।",
                "airport_details": "शहर के नजदीक हानेदा हवाई अड्डे (HND) और थोड़ा दूर नरीता हवाई अड्डे (NRT) द्वारा सेवा प्रदान की जाती है।",
                "safety_recommendations": "अत्यधिक सुरक्षित। रोपोंगी/काबुकीचो में संदिग्ध बार प्रमोटरों से बचें।",
                "food_info": [
                    {"name": "सुशी", "desc": "सिरका लगे चावलों के ऊपर ताजा कच्चा सीफूड।", "type": "Non-Veg"},
                    {"name": "रामेन", "desc": "पोर्क, सोया या मिसो शोरबा में नूडल सूप।", "type": "Non-Veg"}
                ],
                "tourist_places": [
                    {"name": "सेंसो-जी मंदिर", "desc": "असाकुसा में स्थित ऐतिहासिक बौद्ध मंदिर।", "rating": "4.7 ⭐", "time": "Morning"},
                    {"name": "शिबुया क्रॉसिंग", "desc": "दुनिया का सबसे व्यस्त पैदल यात्री क्रॉसिंग चौराहा।", "rating": "4.5 ⭐", "time": "Evening"}
                ],
                "hotel_info": {
                    "luxury": {"name": "अमन टोक्यो", "desc": "व्यावसायिक जिले में स्थित एक शांत शानदार गगनचुंबी होटल।", "price": "¥150,000+ प्रति रात"},
                    "mid_range": {"name": "होटल ग्रेसरी शिंजुकु", "desc": "गॉडज़िला हेड के लिए प्रसिद्ध शिनजुकु का केंद्रीय होटल।", "price": "¥30,000 प्रति रात"},
                    "budget": {"name": "नाइन ऑवर्स कैप्सूल होटल", "desc": "भविष्य के कैप्सूल स्लीपिंग पॉड्स।", "price": "¥6,000 प्रति रात"}
                },
                "shopping_areas": [
                    {"name": "गिंजा जिला", "desc": "अंतर्राष्ट्रीय ब्रांडों वाला उच्च श्रेणी का शॉपिंग क्षेत्र।"},
                    {"name": "अकिहाबारा", "desc": "इलेक्ट्रॉनिक्स और एनीमे सामानों के लिए प्रसिद्ध उपसंस्कृति राजधानी।"}
                ]
            },
            "Downtown Core": {
                "city_name": "डाउनटाउन कोर",
                "description": "सिंगापुर का केंद्रीय वित्तीय जिला, जो गगनचुंबी इमारतों और औपनिवेशिक ऐतिहासिक स्थलों से भरा हुआ है।",
                "transport_info": "रैफल्स प्लेस और सिटी हॉल एमआरटी स्टेशनों के माध्यम से उत्कृष्ट जुड़ाव।",
                "airport_details": "सिंगापुर चांगी हवाई अड्डे (SIN) से टैक्सी या एमआरटी द्वारा आसानी से पहुंचा जा सकता है।",
                "safety_recommendations": "बेहद सुरक्षित। कानून का पालन करें और कूड़ा कचरा न फैलाएं।",
                "food_info": [
                    {"name": "हैनानी चिकन राइस", "desc": "चिकन शोरबा में पकाए गए सुगंधित चावल, निविदा चिकन के साथ परोसा जाता है।", "type": "Non-Veg"}
                ],
                "tourist_places": [
                    {"name": "मर्लियन पार्क", "desc": "पानी उगलने वाली प्रतिष्ठित मर्लियन मूर्ति वाला प्रसिद्ध वाटरफ्रंट पार्क।", "rating": "4.6 ⭐", "time": "Evening"},
                    {"name": "नेशनल गैलरी सिंगापुर", "desc": "पूर्व सिटी हॉल के अंदर दक्षिण पूर्व एशियाई कला का भव्य संग्रहालय।", "rating": "4.7 ⭐", "time": "Afternoon"}
                ],
                "hotel_info": {
                    "luxury": {"name": "द फुलरटन होटल", "desc": "एक ऐतिहासिक नवशास्त्रीय इमारत में बना लक्जरी 5-सितारा होटल।", "price": "S$550 प्रति रात"},
                    "mid_range": {"name": "एम होटल सिंगापुर", "desc": "वित्तीय केंद्र के पास आधुनिक प्रीमियम बिजनेस होटल।", "price": "S$250 प्रति रात"},
                    "budget": {"name": "आईबिस बजट क्लार्क की", "desc": "क्लार्क की नाइटलाइफ़ क्षेत्र के निकट स्वच्छ और किफायती ठहराव।", "price": "S$120 प्रति रात"}
                },
                "shopping_areas": [
                    {"name": "रैफल्स सिटी", "desc": "एमआरटी स्टेशन के ऊपर स्थित बड़ा आधुनिक शॉपिंग सेंटर।"}
                ]
            }
        }
    },
    "te": {
        "countries": {
            "India": {
                "country_name": "భారతదేశం",
                "capital": "న్యూఢిల్లీ",
                "currency": "భారతీయ రూపాయి (INR, ₹)",
                "language": "హిందీ, ఇంగ్లీష్",
                "timezone": "IST (UTC+5:30)",
                "emergency_number": "112 (జాతీయ అత్యవసర సంఖ్య), 100 (పోలీస్), 102 (అంబులెన్స్), 101 (ఫైర్)",
                "visa_info": "160 కంటే ఎక్కువ దేశాల నుండి వచ్చే పర్యాటకులకు ఇ-వీసా అందుబాటులో ఉంది. ప్రయాణానికి కనీసం 4-7 రోజుల ముందు ఆన్‌లైన్‌లో దరఖాస్తు చేసుకోండి. పాస్‌పోర్ట్ కనీసం 6 నెలల చెల్లుబాటు కలిగి ఉండాలి.",
                "rules": "1. బహిరంగ ప్రదేశాలలో ధూమపానం ఖచ్చితంగా నిషేధించబడింది.\n2. స్థానిక మత ఆచారాలను గౌరవించండి: దేవాలయాలు లేదా మసీదులలోకి ప్రవేశించే ముందు మీ తల కప్పుకోండి మరియు బూట్లు విప్పండి.\n3. ముఖ్యంగా మతపరమైన ప్రదేశాలలో మర్యాదపూర్వకంగా దుస్తులు ధరించండి.\n4. బహిరంగంగా ప్రేమను ప్రదర్శించడం నివారించండి.",
                "etiquette": "1. చేతులు జోడించి 'నమస్తే' అని స్థానికులను పలకరించండి.\n2. ఎవరి ఇంట్లోకి అయినా ప్రవేశించే ముందు మీ బూట్లను విప్పండి.\n3. తినేటప్పుడు, వస్తువులను ఇచ్చేటప్పుడు లేదా తీసుకునేటప్పుడు ఎల్లప్పుడూ మీ కుడి చేతిని ఉపయోగించండి.\n4. వ్యక్తుల లేదా మతపరమైన వేడుకల ఫోటోలు తీసే ముందు అనుమతి తీసుకోండి.",
                "safety_tips": "1. సీసా నీరు లేదా శుద్ధి చేసిన నీటిని మాత్రమే త్రాగాలి. వీధి ఐస్ నివారించండి.\n2. విమానాశ్రయాలలో అధికారిక ప్రీపెయిడ్ టాక్సీ కౌంటర్లు లేదా ఓలా/ఉబర్ వంటి ప్రామాణిక రైడ్-హెయిలింగ్ యాప్‌లను ఉపయోగించండి.\n3. జేబుదొంగల నుండి రక్షించుకోవడానికి రద్దీగా ఉండే పర్యాటక ప్రదేశాలలో మీ బ్యాగ్‌లను భద్రంగా ఉంచుకోండి.\n4. స్థానిక నిబంధనలను గౌరవించడానికి మరియు అవాంఛిత దృష్టిని నివారించడానికి తగిన విధంగా దుస్తులు ధరించండి."
            },
            "Japan": {
                "country_name": "జపాన్",
                "capital": "టోక్యో",
                "currency": "జపనీస్ యెన్ (JPY, ¥)",
                "language": "జపనీస్",
                "timezone": "JST (UTC+9)",
                "emergency_number": "110 (పోలీస్), 119 (అంబులెన్స్ మరియు ఫైర్)",
                "visa_info": "అనేక దేశాల పర్యాటకులకు 90 రోజుల వరకు వీసా రహిత ప్రవేశం లభిస్తుంది. ఇతర దేశాల పౌరులు ముందుగానే వీసా దరఖాస్తు చేసుకోండి.",
                "rules": "1. చెత్తను రోడ్లపై పడేయడం నిషేధం; మీ చెత్తను మీతోనే ఉంచుకోండి.\n2. నడుస్తున్నప్పుడు ధూమపానం చేయవద్దు, నిర్దేశించిన ధూమపాన ప్రాంతాలను మాత్రమే ఉపయోగించండి.\n3. రైళ్లలో ఫోన్ మాట్లాడటం నిషేధం; మొబైల్‌ను సైలెంట్ మోడ్‌లో ఉంచండి.\n4. ఎస్కలేటర్‌పై ఎడమ వైపు నిలబడండి (ఒసాకాలో కుడి వైపు).",
                "etiquette": "1. కలిసినప్పుడు కొద్దిగా వంగి నమస్కరించండి.\n2. టిప్ ఇచ్చే అలవాటు లేదు; రెస్టారెంట్లలో అదనపు డబ్బులు వదిలేయడం అమర్యాదగా పరిగణించబడుతుంది.\n3. ఇళ్లు మరియు సాంప్రదాయ రెస్టారెంట్లలోకి ప్రవేశించేటప్పుడు బూట్లు విప్పండి.\n4. బహిరంగ ప్రదేశాలలో ముక్కు తుడుచుకోవడం నివారించండి.",
                "safety_tips": "1. జపాన్ ప్రపంచంలోనే అత్యంత సురక్షితమైన దేశాలలో ఒకటి, కానీ రాత్రి వేళల్లో అప్రమత్తంగా ఉండండి.\n2. పంపు నీరు త్రాగడానికి పూర్తిగా సురక్షితం.\n3. భూకంపాల పట్ల అప్రమత్తంగా ఉండండి మరియు హోటల్ అత్యవసర నిష్క్రమణ మార్గాలను గమనించండి."
            },
            "Singapore": {
                "country_name": "సింగపూర్",
                "capital": "సింగపూర్",
                "currency": "సింగపూర్ డాలర్ (SGD, S$)",
                "language": "ఇంగ్లీష్, మలేయ్, మాండరిన్, తమిళ్",
                "timezone": "SGT (UTC+8)",
                "emergency_number": "999 (పోలీస్), 995 (అంబులెన్స్ మరియు ఫైర్)",
                "visa_info": "ప్రవేశానికి 3 రోజుల ముందు పర్యాటకులు ఆన్‌లైన్ 'SG Arrival Card' నింపాలి. పాస్‌పోర్ట్ కనీసం 6 నెలల చెల్లుబాటు కలిగి ఉండాలి.",
                "rules": "1. చూయింగ్ గమ్ అమ్మడం లేదా దిగుమతి చేయడం నిషేధం; జరిమానా విధించబడుతుంది.\n2. చెత్త వేయడం, ఉమ్మివేయడం మరియు రోడ్డును తప్పుగా దాటడం వంటి వాటికి భారీ జరిమానాలు ఉన్నాయి.\n3. రైళ్లు మరియు స్టేషన్లలో ఆహారం, పానీయాలు తీసుకోవడం నిషేధించబడింది.\n4. అనుమతి లేకుండా పబ్లిక్ వై-ఫైకి కనెక్ట్ కావడం చట్టవిరుద్ధం.",
                "etiquette": "1. ఎస్కలేటర్లపై ఎడమ వైపున ఉండండి, ఇతరులను కుడి వైపు నుండి వెళ్ళనివ్వండి.\n2. 'చోపింగ్': టేబుల్‌లను రిజర్వ్ చేయడానికి టిష్యూ ప్యాకెట్‌లను ఉంచుతారు. అక్కడ కూర్చోవద్దు.\n3. ఫుడ్ కోర్టులలో తిన్న తర్వాత ప్లేట్లను తిరిగి క్లియర్ చేయడం చట్టబద్ధంగా తప్పనిసరి.\n4. వేలితో చూపించడం అమర్యాదకరం, పూర్తి చేతిని ఉపయోగించండి.",
                "safety_tips": "1. సింగపూర్ అత్యంత సురక్షితం, రాత్రి పూట కూడా ఒంటరిగా నడవవచ్చు.\n2. పంపు నీరు శుభ్రంగా ఉంటుంది, త్రాగడానికి సురక్షితం.\n3. మతపరమైన ప్రదేశాలలో దుస్తులు మర్యాదపూర్వకంగా ధరించండి మరియు బూట్లు విప్పండి."
            }
        },
        "cities": {
            "Hyderabad": {
                "city_name": "హైదరాబాద్",
                "description": "ముత్యాల నగరం, హైదరాబాద్ నిజాం కాలం నాటి చరిత్ర, రాజభవనాలు మరియు అత్యాధునిక ఐటి హబ్ యొక్క అద్భుతమైన కలయిక.",
                "transport_info": "హైదరాబాద్ మెట్రో రైలు, స్థానిక TSRTC బస్సులు, ఆటో-రిక్షాలు మరియు ఉబర్/ఓలా క్యాబ్స్ ద్వారా సులభంగా ప్రయాణించవచ్చు.",
                "airport_details": "రాజీవ్ గాంధీ అంతర్జాతీయ విమానాశ్రయం (HYD) శంషాబాద్‌లో ఉంది, ఇది నగరం నుండి 24 కి.మీ దూరంలో ఉంటుంది.",
                "safety_recommendations": "సాధారణంగా చాలా సురక్షితం. చార్మినార్ వంటి రద్దీ ప్రదేశాలలో మీ బ్యాగ్‌ల పట్ల జాగ్రత్త వహించండి.",
                "food_info": [
                    {"name": "హైదరాబాదీ బిర్యానీ", "desc": "మసాలాలు, పెరుగు మరియు కుంకుమపువ్వుతో దమ్ బిర్యానీ పద్ధతిలో వండిన బాస్మతి బియ్యం వంటకం.", "type": "Non-Veg"},
                    {"name": "హలీమ్", "desc": "గోధుమలు, పప్పులు మరియు మాంసంతో నెయ్యి వేసి నెమ్మదిగా వండిన సాంప్రదాయ వంటకం.", "type": "Non-Veg"},
                    {"name": "ఖుబానీ కా మీఠా", "desc": "ఆప్రికాట్‌లతో తయారు చేసి ఐస్‌క్రీమ్ లేదా క్రీమ్‌తో అందించే సాంప్రదాయ తీపి వంటకం.", "type": "Veg"}
                ],
                "tourist_places": [
                    {"name": "చార్మినార్", "desc": "పాత బస్తీ మధ్యలో ఉన్న 16వ శతాబ్దపు చారిత్రాత్మక మసీదు మరియు కట్టడం.", "rating": "4.6 ⭐", "time": "Morning"},
                    {"name": "గోల్కొండ కోట", "desc": "ద్వని తరంగాల వింతలు మరియు భారీ గోడలు ఉన్న ఒక మధ్యయుగ కోట.", "rating": "4.7 ⭐", "time": "Afternoon"},
                    {"name": "హుస్సేన్ సాగర్ లేక్", "desc": "మధ్యలో పెద్ద బుద్ధుని విగ్రహం ఉన్న అందమైన గుండె ఆకారపు సరస్సు.", "rating": "4.3 ⭐", "time": "Evening"}
                ],
                "hotel_info": {
                    "luxury": {"name": "తాజ్ ఫలక్‌నుమా ప్యాలెస్", "desc": "పునరుద్ధరించబడిన 19వ శతాబ్దపు రాజభవన హోటల్.", "price": "₹35,000+ ఒక రాత్రికి"},
                    "mid_range": {"name": "నోవోటెల్ హైదరాబాద్ హైటెక్ సిటీ", "desc": "ఐటి హబ్ సమీపంలో ఉన్న అత్యాధునిక హోటల్.", "price": "₹9,000 ఒక రాత్రికి"},
                    "budget": {"name": "రెడ్ ఫాక్స్ హోటల్, హైటెక్ సిటీ", "desc": "పరిశుభ్రమైన మరియు తక్కువ బడ్జెట్ బిజినెస్ హోటల్.", "price": "₹3,200 ఒక రాత్రికి"}
                },
                "shopping_areas": [
                    {"name": "లాడ్ బజార్", "desc": "గాజు గాజులు మరియు ముత్యాలకు ప్రసిద్ధి చెందిన పాత బజార్.", "desc_en": "Traditional bazaar famous for lacquer bangles and pearls."},
                    {"name": "ఇనార్బిట్ మాల్", "desc": "అంతర్జాతీయ బ్రాండ్‌లు ఉన్న పెద్ద ఆధునిక షాపింగ్ మాల్.", "desc_en": "Large modern shopping complex featuring global fashion brands."}
                ]
            },
            "Visakhapatnam": {
                "city_name": "విశాఖపట్నం",
                "description": "ఆంధ్రప్రదేశ్‌లోని ఒక అందమైన తీరప్రాంత ఓడరేవు నగరం, కొండలు మరియు బంగాళాఖాతంతో చుట్టబడి ఉంటుంది, శుభ్రమైన బీచ్‌లకు ప్రసిద్ధి చెందింది.",
                "transport_info": "స్థానిక APSRTC బస్సులు, ఆటో-రిక్షాలు మరియు ఉబర్/ఓలా సేవలు విస్తృతంగా అందుబాటులో ఉన్నాయి.",
                "airport_details": "విశాఖపట్నం అంతర్జాతీయ విమానాశ్రయం (VTZ) నగరం నుండి 12 కి.మీ దూరంలో ఉంటుంది.",
                "safety_recommendations": "సముద్రతీరంలో ఉన్న బలమైన నీటి అలల ప్రవాహం పట్ల చాలా జాగ్రత్తగా ఉండండి.",
                "food_info": [
                    {"name": "బొంగు చికెన్", "desc": "నూనె లేకుండా బొంగులలో పెట్టి కాల్చిన రుచికరమైన సాంప్రదాయ చికెన్ వంటకం.", "type": "Non-Veg"},
                    {"name": "ఆంధ్రా థాలి", "desc": "అన్నం, పప్పు, కూరలు మరియు పచ్చళ్లతో కూడిన కారంగా ఉండే భోజనం.", "type": "Veg"}
                ],
                "tourist_places": [
                    {"name": "ఆర్.కె. బీచ్", "desc": "పార్కులు, మ్యూజియంలు మరియు తినుబండారాల దుకాణాలతో కూడిన ప్రసిద్ధ బీచ్.", "rating": "4.5 ⭐", "time": "Evening"},
                    {"name": "కుర్సురా సబ్‌మెరైన్ మ్యూజియం", "desc": "సందర్శకుల కోసం బీచ్ ఒడ్డున ఉంచిన నిజమైన సోవియట్ జలాంతర్గామి.", "rating": "4.8 ⭐", "time": "Afternoon"}
                ],
                "hotel_info": {
                    "luxury": {"name": "నోవోటెల్ వరుణ్ బీచ్", "desc": "అందమైన సముద్ర వీక్షణలు కలిగిన ఆధునిక లగ్జరీ హోటల్.", "price": "₹12,000+ ఒక రాత్రికి"},
                    "mid_range": {"name": "ది గేట్‌వే హోటల్ తాజ్", "desc": "తాజ్ ఆతిథ్యంతో సముద్రతీరంలో సౌకర్యవంతమైన బస.", "price": "₹7,500 ఒక రాత్రికి"},
                    "budget": {"name": "హోటల్ డాల్ఫిన్", "desc": "నగరం మధ్యలో ఉన్న బడ్జెట్ అనుకూల బిజినెస్ హోటల్.", "price": "₹3,000 ఒక రాత్రికి"}
                },
                "shopping_areas": [
                    {"name": "జగదాంబ జంక్షన్", "desc": "బట్టలు మరియు ఎలక్ట్రానిక్స్ షాపింగ్‌కు ప్రసిద్ధి చెందిన కేంద్రం.", "desc_en": "Commercial shopping district with textile and electronics markets."},
                    {"name": "సీఎమ్ఆర్ సెంట్రల్", "desc": "థియేటర్లు మరియు బ్రాండెడ్ దుకాణాలు ఉన్న ప్రసిద్ధ షాపింగ్ మాల్.", "desc_en": "Popular shopping mall with fashion labels and cinemas."}
                ]
            },
            "Tokyo": {
                "city_name": "టోక్యో",
                "description": "జపాన్ రాజధాని, ఇది భవిష్యత్ ఆకాశహర్మ్యాలను చారిత్రాత్మక దేవాలయాలు మరియు అందమైన తోటలతో మిళితం చేస్తుంది.",
                "transport_info": "అత్యంత సమర్థవంతమైన మెట్రో మరియు JR రైలు వ్యవస్థ. ప్రయాణానికి సుయికా (Suica) కార్డ్ ఉపయోగించండి.",
                "airport_details": "నగరానికి సమీపంలో హనేడా విమానాశ్రయం (HND) మరియు కొద్దిగా దూరంలో నరిటా విమానాశ్రయం (NRT) సేవలు అందిస్తాయి.",
                "safety_recommendations": "చాలా సురక్షితమైన నగరం. రోప్పోంగి/కబుకిచో ప్రాంతాలలో అపరిచితుల పట్ల జాగ్రత్తగా ఉండండి.",
                "food_info": [
                    {"name": "సుశి", "desc": "ప్రత్యేకమైన అన్నం మీద తాజా పచ్చి చేప ముక్కలు ఉంచి అందించే సాంప్రదాయ వంటకం.", "type": "Non-Veg"},
                    {"name": "రామెన్", "desc": "నూడుల్స్ మరియు వివిధ రకాల మాంసపు రసంతో కూడిన సూప్ వంటకం.", "type": "Non-Veg"}
                ],
                "tourist_places": [
                    {"name": "సేన్సో-జి టెంపుల్", "desc": "అసకుసాలో ఉన్న అతి పురాతన బౌద్ధ దేవాలయం.", "rating": "4.7 ⭐", "time": "Morning"},
                    {"name": "షిబుయా క్రాసింగ్", "desc": "ప్రపంచంలోనే అత్యంత రద్దీగా ఉండే రోడ్డు దాటే కూడలి.", "rating": "4.5 ⭐", "time": "Evening"}
                ],
                "hotel_info": {
                    "luxury": {"name": "అమన్ టోక్యో", "desc": "నగరం మధ్యలో ఉన్న విలాసవంతమైన ఆకాశహర్మ్య హోటల్.", "price": "¥150,000+ ఒక రాత్రికి"},
                    "mid_range": {"name": "హోటల్ గ్రేసరీ షింజుకు", "desc": "గాడ్జిల్లా బొమ్మతో ప్రసిద్ధి చెందిన షింజుకులోని హోటల్.", "price": "¥30,000 ఒక రాత్రికి"},
                    "budget": {"name": "నైన్ అవర్స్ క్యాప్సూల్ హోటల్", "desc": "ఆధునిక పద్ధతిలో ఉండే చిన్న పడక గదులు (క్యాప్సూల్స్).", "price": "¥6,000 ఒక రాత్రికి"}
                },
                "shopping_areas": [
                    {"name": "గింజా ప్రాంతం", "desc": "అంతర్జాతీయ బ్రాండ్లు ఉన్న విలాసవంతమైన షాపింగ్ వీధి."},
                    {"name": "అకిహబారా", "desc": "ఎలక్ట్రానిక్స్ మరియు యానిమే వస్తువులకు ప్రసిద్ధి చెందిన ప్రాంతం."}
                ]
            },
            "Downtown Core": {
                "city_name": "డౌన్‌టౌన్ కోర్",
                "description": "సింగపూర్ కేంద్ర ఆర్థిక జిల్లా, ఆకాశహర్మ్యాలు మరియు చారిత్రాత్మక కట్టడాలతో నిండి ఉంటుంది.",
                "transport_info": "రాఫెల్స్ ప్లేస్ మరియు సిటీ హాల్ MRT స్టేషన్ల ద్వారా అద్భుతమైన ప్రజా రవాణా సౌకర్యం.",
                "airport_details": "సింగపూర్ చాంగి విమానాశ్రయం (SIN) నుండి టాక్సీ లేదా MRT ద్వారా సులభంగా చేరుకోవచ్చు.",
                "safety_recommendations": "అత్యంత సురక్షితమైన ప్రదేశం. చట్టాలను గౌరవించండి మరియు రోడ్లపై చెత్త వేయకండి.",
                "food_info": [
                    {"name": "హైనాన్ చికెన్ రైస్", "desc": "సువాసనగల అన్నం మరియు ఉడికించిన చికెన్‌తో అందించే సింగపూర్ జాతీయ వంటకం.", "type": "Non-Veg"}
                ],
                "tourist_places": [
                    {"name": "మెర్లయన్ పార్క్", "desc": "నీటిని చిమ్మే సగం సింహం, సగం చేప రూపంలో ఉన్న సింగపూర్ ఐకానిక్ విగ్రహం.", "rating": "4.6 ⭐", "time": "Evening"},
                    {"name": "నేషనల్ గ్యాలరీ సింగపూర్", "desc": "మాజీ సిటీ హాల్ భవనంలో ఉన్న ఆగ్నేయాసియా కళల మ్యూజియం.", "rating": "4.7 ⭐", "time": "Afternoon"}
                ],
                "hotel_info": {
                    "luxury": {"name": "ది ఫుల్లెర్టన్ హోటల్", "desc": "చారిత్రాత్మక పోస్టాఫీసు భవనంలో నిర్మించిన 5-స్టార్ లగ్జరీ హోటల్.", "price": "S$550 ఒక రాత్రికి"},
                    "mid_range": {"name": "ఎమ్ హోటల్ సింగపూర్", "desc": "ఆర్థిక కేంద్రానికి సమీపంలో ఉన్న బిజినెస్ హోటల్.", "price": "S$250 ఒక రాత్రికి"},
                    "budget": {"name": "ఐబిస్ బడ్జెట్ క్లార్క్ కీ", "desc": "క్లార్క్ కీ నైట్‌లైఫ్ ప్రాంతానికి సమీపంలో ఉన్న బడ్జెట్ హోటల్.", "price": "S$120 ఒక రాత్రికి"}
                },
                "shopping_areas": [
                    {"name": "రాఫెల్స్ సిటీ", "desc": "రద్దీగా ఉండే పెద్ద ఆధునిక షాపింగ్ సెంటర్."}
                ]
            }
        }
    }
}

def translate_ui(key):
    """Translates a UI text key based on the selected language in session state."""
    lang = st.session_state.get("language", "en")
    return UI_TRANSLATIONS.get(lang, UI_TRANSLATIONS["en"]).get(key, key)

def get_english_term(query):
    """Maps localized query terms back to English for standard DB matches."""
    if not query:
        return ""
    q = query.strip()
    # Simple check for exact matches or word contains
    for local_word, eng_word in SEARCH_TERM_MAP.items():
        if local_word in q:
            # Replace the local word with the English counterpart
            q = q.replace(local_word, eng_word)
    return q

def translate_db_record(record, record_type):
    """
    Dynamically translates a database record dict (either 'country' or 'city')
    based on the current session state language.
    """
    if not record:
        return record

    lang = st.session_state.get("language", "en")
    if lang == "en":
        return record

    # Copy the record to prevent modifying cache or DB-level rows
    translated = dict(record)

    if record_type == "country":
        orig_name = record.get("country_name", "")
        lang_db = DB_TRANSLATIONS.get(lang, {}).get("countries", {})
        if orig_name in lang_db:
            c_trans = lang_db[orig_name]
            for field in [
                "country_name", "capital", "currency", "language", "timezone",
                "emergency_number", "visa_info", "rules", "etiquette", "safety_tips"
            ]:
                if field in c_trans:
                    translated[field] = c_trans[field]
        else:
            # Fallback translations for basic fields if country not fully mapped
            pass

    elif record_type == "city":
        orig_name = record.get("city_name", "")
        lang_db = DB_TRANSLATIONS.get(lang, {}).get("cities", {})
        if orig_name in lang_db:
            ct_trans = lang_db[orig_name]
            for field in [
                "city_name", "description", "transport_info", "airport_details",
                "safety_recommendations"
            ]:
                if field in ct_trans:
                    translated[field] = ct_trans[field]

            # Handle JSON fields if they are in the record
            if "food_info" in record:
                try:
                    foods = json.loads(record["food_info"])
                    trans_foods = ct_trans.get("food_info", [])
                    # Match foods by index or name
                    for idx, food in enumerate(foods):
                        if idx < len(trans_foods):
                            foods[idx]["name"] = trans_foods[idx]["name"]
                            foods[idx]["desc"] = trans_foods[idx]["desc"]
                    translated["food_info"] = json.dumps(foods)
                except Exception:
                    pass

            if "tourist_places" in record:
                try:
                    places = json.loads(record["tourist_places"])
                    trans_places = ct_trans.get("tourist_places", [])
                    for idx, place in enumerate(places):
                        if idx < len(trans_places):
                            places[idx]["name"] = trans_places[idx]["name"]
                            places[idx]["desc"] = trans_places[idx]["desc"]
                    translated["tourist_places"] = json.dumps(places)
                except Exception:
                    pass

            if "hotel_info" in record:
                try:
                    hotels = json.loads(record["hotel_info"])
                    trans_hotels = ct_trans.get("hotel_info", {})
                    for tier in ["budget", "mid_range", "luxury"]:
                        if tier in hotels and tier in trans_hotels:
                            hotels[tier]["name"] = trans_hotels[tier]["name"]
                            hotels[tier]["desc"] = trans_hotels[tier]["desc"]
                            if "price" in trans_hotels[tier]:
                                hotels[tier]["price"] = trans_hotels[tier]["price"]
                    translated["hotel_info"] = json.dumps(hotels)
                except Exception:
                    pass

            if "shopping_areas" in record:
                try:
                    shops = json.loads(record["shopping_areas"])
                    trans_shops = ct_trans.get("shopping_areas", [])
                    for idx, shop in enumerate(shops):
                        if idx < len(trans_shops):
                            shops[idx]["name"] = trans_shops[idx]["name"]
                            shops[idx]["desc"] = trans_shops[idx]["desc"]
                    translated["shopping_areas"] = json.dumps(shops)
                except Exception:
                    pass
        else:
            # Fallback: Translate the city name if we have a simple map
            # (e.g., for cities that aren't fully localized yet, translate the name to avoid English leaking in drop downs)
            simple_city_map = {
                "hi": {
                    "Mumbai": "मुंबई", "Delhi": "दिल्ली", "Bangalore": "बैंगलोर",
                    "Chennai": "चेन्नई", "Kolkata": "कोलकाता", "Jaipur": "जयपुर",
                    "Agra": "आगरा", "Varanasi": "वाराणसी", "Kochi": "कोच्चि",
                    "Goa": "गोवा", "Udaipur": "उदयपुर", "Pune": "पुणे",
                    "Ahmedabad": "अहमदाबाद", "Amritsar": "अमृतसर", "Srinagar": "श्रीनगर",
                    "Shimla": "शिमला", "Darjeeling": "दार्जिलिंग", "Mysore": "मैसूर",
                    "Osaka": "ओसाका", "Kyoto": "क्योटो"
                },
                "te": {
                    "Mumbai": "ముంబై", "Delhi": "ఢిల్లీ", "Bangalore": "బెంగళూరు",
                    "Chennai": "చెన్నై", "Kolkata": "కోల్‌కతా", "Jaipur": "జైపూర్",
                    "Agra": "ఆగ్రా", "Varanasi": "వారణాసి", "Kochi": "కొచ్చి",
                    "Goa": "గోవా", "Udaipur": "ఉదయపూర్", "Pune": "పూణే",
                    "Ahmedabad": "అహ్మదాబాద్", "Amritsar": "అమృత్‌సర్", "Srinagar": "శ్రీనగర్",
                    "Shimla": "సిమ్లా", "Darjeeling": "డార్జిలింగ్", "Mysore": "మైసూర్",
                    "Osaka": "ఒసాకా", "Kyoto": "క్యోటో"
                }
            }
            if lang in simple_city_map and orig_name in simple_city_map[lang]:
                translated["city_name"] = simple_city_map[lang][orig_name]

    return translated
