from pages.chatbot import generate_bot_response
from utils import database as db


def setup_temp_db(monkeypatch, tmp_path):
    temp_dir = tmp_path / "database"
    temp_db = temp_dir / "travel.db"
    monkeypatch.setattr(db, "DB_DIR", str(temp_dir))
    monkeypatch.setattr(db, "DB_PATH", str(temp_db))
    db.init_db()
    return db

def describe_chatbot_response():
    def it_handles_greeting_fallback_when_no_match(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        response = generate_bot_response("hello companion", None, None)
        assert "Hello! I am your AI Travel Companion" in response

    def it_responds_with_food_specials_for_matched_city(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        response = generate_bot_response("What food should I try in Hyderabad?", None, None)
        assert "must-try foods" in response
        assert "Hyderabad" in response

    def it_responds_with_attractions_for_matched_city(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        response = generate_bot_response("What are the attractions in Tokyo?", None, None)
        assert "tourist attractions" in response
        assert "Tokyo" in response

    def it_falls_back_to_active_city_context_for_food(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        hyd = db.get_city_by_name("Hyderabad")
        response = generate_bot_response("Tell me what food to try", None, hyd["id"])
        assert "must-try foods in Hyderabad" in response

    def it_responds_with_country_rules_when_country_matched(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        response = generate_bot_response("What are the traffic rules in Singapore?", None, None)
        assert "Rules & Regulations" in response
        assert "Singapore" in response

    def it_responds_with_hotels_for_matched_city(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        response = generate_bot_response("Where can I stay in Osaka?", None, None)
        assert "Recommended stays in Osaka" in response

    def it_responds_with_transit_info_for_matched_city(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        response = generate_bot_response("How is transport in Tokyo?", None, None)
        assert "Transit guide for Tokyo" in response

    def it_responds_with_safety_info_for_matched_city(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        response = generate_bot_response("Is Tokyo safe?", None, None)
        assert "Safety Recommendations for Tokyo" in response

    def it_responds_with_visa_info_for_country(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        response = generate_bot_response("Visa guidelines for Japan", None, None)
        assert "Visa & Entry information for Japan" in response
