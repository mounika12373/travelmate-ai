import json

from utils import database as db


def setup_temp_db(monkeypatch, tmp_path):
    temp_dir = tmp_path / "database"
    temp_db = temp_dir / "travel.db"
    monkeypatch.setattr(db, "DB_DIR", str(temp_dir))
    monkeypatch.setattr(db, "DB_PATH", str(temp_db))
    return db


def describe_history_and_profile():
    def it_creates_users_and_verifies_profile_updates(monkeypatch, tmp_path):
        db_module = setup_temp_db(monkeypatch, tmp_path)
        db_module.init_db()

        # Create user
        email = "test@example.com"
        user_id = db_module.create_user(
            full_name="Test User",
            email=email,
            phone="+91 99999 99999",
            country="India",
            city="Hyderabad",
            profile_pic="data:image/png;base64,xxxx",
            password_hash="hashed_test_password",  # nosec B106
            preferences="[]",
        )
        assert user_id is not None

        # Verify retrieval
        user = db_module.get_user_by_email(email)
        assert user is not None
        assert user["full_name"] == "Test User"
        assert user["city"] == "Hyderabad"

        # Update profile
        db_module.update_user_profile(
            user_id=user_id,
            full_name="Updated User",
            phone="+91 88888 88888",
            country="India",
            city="Secunderabad",
            profile_pic="data:image/png;base64,yyyy",
            preferences='["Adventure"]',
        )

        user_updated = db_module.get_user_by_id(user_id)
        assert user_updated["full_name"] == "Updated User"
        assert user_updated["city"] == "Secunderabad"
        assert "Adventure" in json.loads(user_updated["preferences"])

    def it_logs_activities_and_filters_history(monkeypatch, tmp_path):
        db_module = setup_temp_db(monkeypatch, tmp_path)
        db_module.init_db()

        user_id = db_module.create_user("User", "user@example.com", "123", "India", "Visakhapatnam", "", "pwd")

        # Log searches and itineraries
        db_module.log_activity(user_id, "search", "Kyoto")
        db_module.log_activity(user_id, "itinerary", "Tokyo 3 Days Plan", {"days": 3, "budget": "mid_range"})
        db_module.log_activity(user_id, "chat", "What food is in Tokyo?")

        # Retrieve history
        history = db_module.get_travel_history(user_id)
        assert len(history) == 3

        # Filter by type
        searches = db_module.get_travel_history(user_id, activity_type="search")
        assert len(searches) == 1
        assert searches[0]["query"] == "Kyoto"

        # Favorite trigger
        db_module.toggle_history_favorite(history[0]["id"], user_id)
        hist_updated = db_module.get_travel_history(user_id)
        assert hist_updated[0]["is_favorite"] == 1

        # Delete single item
        db_module.delete_history_item(history[0]["id"], user_id)
        assert len(db_module.get_travel_history(user_id)) == 2

        # Clear history
        db_module.clear_user_history(user_id)
        assert len(db_module.get_travel_history(user_id)) == 0

    def it_saves_trips_to_collections_and_calculates_dashboard_stats(monkeypatch, tmp_path):
        db_module = setup_temp_db(monkeypatch, tmp_path)
        db_module.init_db()

        user_id = db_module.create_user("Analyst", "analyst@example.com", "123", "Japan", "Tokyo", "", "pwd")

        # Save destination and itinerary
        db_module.save_trip(user_id, "destination", "Kyoto", "My Saved Trips", {"city_id": 3})
        db_module.save_trip(
            user_id,
            "itinerary",
            "3 Days in Hyderabad",
            "Summer Vacation 2026",
            {"days": 3, "budget_tier": "Economy"},
            "2026-07-15",
        )

        # Log search activities to affect dashboard
        db_module.log_activity(user_id, "search", "Hyderabad")
        db_module.log_activity(user_id, "itinerary", "3 Days in Hyderabad")
        db_module.log_activity(user_id, "chat", "Biryani query")

        # Fetch stats
        stats = db_module.get_dashboard_stats(user_id)
        assert stats["total_trips"] == 2  # 1 saved itinerary + 1 generated in log
        assert stats["saved_destinations"] == 1
        assert len(stats["recent_searches"]) == 1
        assert stats["ai_usage"]["chatbot_interactions"] == 1
        assert len(stats["upcoming_trips"]) == 1
        assert stats["upcoming_trips"][0]["travel_date"] == "2026-07-15"
