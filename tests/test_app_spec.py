import sys
from unittest.mock import MagicMock


class MockSessionState(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)
    def __setattr__(self, name, value):
        self[name] = value

def describe_app_router():
    def it_initializes_session_state_and_configures_navigation(monkeypatch):
        # Clear app module from cache if it exists
        sys.modules.pop("app", None)

        # Mock streamlit module
        mock_st = MagicMock()
        mock_session_state = MockSessionState()
        mock_st.session_state = mock_session_state

        # Mock database calls
        mock_db = MagicMock()
        mock_db.get_all_countries.return_value = [{"id": 1, "country_name": "India"}]
        mock_db.get_cities_by_country.return_value = [{"id": 10, "city_name": "Hyderabad"}]

        # Mock styles calls
        mock_styles = MagicMock()

        # Patch sys.modules
        monkeypatch.setitem(sys.modules, "streamlit", mock_st)
        monkeypatch.setitem(sys.modules, "utils.database", mock_db)
        monkeypatch.setitem(sys.modules, "utils.styles", mock_styles)

        # Import app to trigger initialization
        import app

        # Verify page configuration and side-effects
        assert mock_st.set_page_config.called
        assert mock_styles.inject_global_css.called

        # Verify default session state variables were set
        assert "selected_country_id" in mock_session_state
        assert "selected_city_id" in mock_session_state
        assert "search_query" in mock_session_state
        assert mock_session_state["selected_country_id"] == 1
        assert mock_session_state["selected_city_id"] == 10

        # Verify navigation routes setup
        assert mock_st.Page.call_count == 5
        assert mock_st.navigation.called
        assert mock_st.navigation.return_value.run.called
