import streamlit as st

from utils.i18n import get_english_term, translate_db_record, translate_ui


def describe_i18n_module():
    def it_translates_ui_keys_correctly_based_on_language():
        # Test English
        st.session_state.language = "en"
        assert translate_ui("quick_search") == "🔍 Quick Search"
        assert translate_ui("made_with_love") == "Made with ❤️ for Travelers"

        # Test Hindi
        st.session_state.language = "hi"
        assert translate_ui("quick_search") == "🔍 त्वरित खोज"
        assert translate_ui("made_with_love") == "यात्रियों के लिए ❤️ के साथ बनाया गया"

        # Test Telugu
        st.session_state.language = "te"
        assert translate_ui("quick_search") == "🔍 త్వరిత శోధన"
        assert translate_ui("made_with_love") == "ప్రయాణీకుల కోసం ❤️ తో తయారు చేయబడింది"

    def it_normalizes_multilingual_search_terms_back_to_english():
        # Hindi mapping
        assert get_english_term("टोक्यो") == "Tokyo"
        assert get_english_term("हैदराबाद का खाना") == "Hyderabad का food"

        # Telugu mapping
        assert get_english_term("హైదరాబాద్") == "Hyderabad"
        assert get_english_term("జపాన్ కరెన్సీ") == "Japan కరెన్సీ"

        # English (unchanged)
        assert get_english_term("Tokyo food") == "Tokyo food"

    def it_leaves_records_intact_when_language_is_english():
        st.session_state.language = "en"
        country_record = {"country_name": "India", "capital": "New Delhi"}
        translated = translate_db_record(country_record, "country")
        assert translated == country_record

    def it_translates_country_db_records_to_hindi_and_telugu():
        country_record = {
            "country_name": "India",
            "capital": "New Delhi",
            "currency": "Indian Rupee (INR, ₹)"
        }

        # Hindi country record translation
        st.session_state.language = "hi"
        translated_hi = translate_db_record(country_record, "country")
        assert translated_hi["country_name"] == "भारत"
        assert translated_hi["capital"] == "नई दिल्ली"

        # Telugu country record translation
        st.session_state.language = "te"
        translated_te = translate_db_record(country_record, "country")
        assert translated_te["country_name"] == "భారతదేశం"
        assert translated_te["capital"] == "న్యూఢిల్లీ"

    def it_translates_city_db_records_and_nested_json():
        import json
        city_record = {
            "city_name": "Hyderabad",
            "description": "Original description in English.",
            "food_info": json.dumps([
                {"name": "Hyderabadi Biryani", "desc": "Rice cooked with meat", "type": "Non-Veg"}
            ])
        }

        st.session_state.language = "hi"
        translated = translate_db_record(city_record, "city")
        assert translated["city_name"] == "हैदराबाद"
        assert translated["description"] != city_record["description"]
        
        # Verify nested JSON translated successfully
        translated_food = json.loads(translated["food_info"])
        assert translated_food[0]["name"] == "हैदराबादी बिरयानी"
