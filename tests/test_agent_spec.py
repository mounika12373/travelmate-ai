from unittest.mock import MagicMock, AsyncMock, patch
import pytest
from utils import database as db
from utils import chatbot_agent as agent

def setup_temp_db(monkeypatch, tmp_path):
    temp_dir = tmp_path / "database"
    temp_db = temp_dir / "travel.db"
    monkeypatch.setattr(db, "DB_DIR", str(temp_dir))
    monkeypatch.setattr(db, "DB_PATH", str(temp_db))
    db.init_db()
    return db

def describe_agent_kit_tools():
    def it_gets_country_info_from_db(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        info = agent.get_country_info("Japan")
        assert info is not None
        assert info["country_name"] == "Japan"
        assert info["capital"] == "Tokyo"
        assert "currency" in info

    def it_returns_error_for_invalid_country(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        info = agent.get_country_info("NonExistentCountry")
        assert "error" in info

    def it_gets_city_info_from_db(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        info = agent.get_city_info("Hyderabad")
        assert info is not None
        assert info["city_name"] == "Hyderabad"
        assert isinstance(info["food_info"], list)
        assert isinstance(info["tourist_places"], list)

    def it_returns_error_for_invalid_city(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        info = agent.get_city_info("NonExistentCity")
        assert "error" in info

    def it_searches_destinations_correctly(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        res = agent.search_destinations("Singapore")
        assert len(res["countries"]) > 0 or len(res["cities"]) > 0

def describe_agent_kit_status():
    def it_is_disabled_when_adk_is_unavailable():
        with patch.object(agent, "ADK_AVAILABLE", False):
            assert not agent.is_agent_enabled()

    def it_is_disabled_when_gemini_key_is_missing(monkeypatch):
        monkeypatch.delenv("GEMINI_API_KEY", raising=False)
        with patch.object(agent, "_runner_instance", None):
            assert not agent.is_agent_enabled()

    def it_is_enabled_when_key_is_present(monkeypatch):
        monkeypatch.setenv("GEMINI_API_KEY", "test_key")
        mock_runner = MagicMock()
        with patch.object(agent, "ADK_AVAILABLE", True):
            with patch("utils.chatbot_agent.get_agent_runner", return_value=mock_runner):
                assert agent.is_agent_enabled()

def describe_agent_query_execution():
    def it_executes_agent_runner_loop(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)
        
        # Mock Event and Runner
        mock_event = MagicMock()
        mock_event.is_final_response.return_value = True
        mock_part = MagicMock()
        mock_part.text = "Hello traveler! I recommend visiting Kyoto."
        mock_event.content.parts = [mock_part]
        
        # Set up an async generator mock for run_async
        async def mock_run_async(*args, **kwargs):
            yield mock_event
            
        mock_runner = MagicMock()
        mock_runner.run_async = mock_run_async
        
        with patch("utils.chatbot_agent.get_agent_runner", return_value=mock_runner):
            with patch("utils.chatbot_agent.ADK_AVAILABLE", True):
                # Test the sync wrapper
                res = agent.run_agent_query(
                    user_id="test@example.com",
                    session_id="en",
                    query_text="Where should I go in Japan?",
                    active_country_id=None,
                    active_city_id=None
                )
                assert res == "Hello traveler! I recommend visiting Kyoto."
