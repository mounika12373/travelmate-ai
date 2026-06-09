import os
from utils import database as db


def setup_temp_db(monkeypatch, tmp_path):
    temp_dir = tmp_path / "database"
    temp_db = temp_dir / "travel.db"
    monkeypatch.setattr(db, "DB_DIR", str(temp_dir))
    monkeypatch.setattr(db, "DB_PATH", str(temp_db))
    return db


def describe_database_module():
    def it_initializes_the_database_and_seeds_sample_data(monkeypatch, tmp_path):
        db_module = setup_temp_db(monkeypatch, tmp_path)
        db_module.init_db()

        assert os.path.exists(db_module.DB_PATH)
        assert db_module.get_all_countries(), "Database should contain seeded countries"

    def it_returns_country_details_by_name(monkeypatch, tmp_path):
        db_module = setup_temp_db(monkeypatch, tmp_path)
        db_module.init_db()

        country = db_module.get_country_by_name("India")
        assert country is not None
        assert country["country_name"] == "India"

    def it_returns_empty_results_for_blank_search_queries(monkeypatch, tmp_path):
        db_module = setup_temp_db(monkeypatch, tmp_path)
        db_module.init_db()

        result = db_module.search_locations(" ")
        assert result == {"countries": [], "cities": []}

    def it_searches_locations_for_matching_city_names(monkeypatch, tmp_path):
        db_module = setup_temp_db(monkeypatch, tmp_path)
        db_module.init_db()

        result = db_module.search_locations("Hyderabad")
        assert result["cities"]
        assert any("Hyderabad" in city.get("city_name", "") for city in result["cities"])
