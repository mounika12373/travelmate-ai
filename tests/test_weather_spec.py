import os

import streamlit as st

from utils import database as db
from utils.i18n import translate_weather_record


def setup_temp_db(monkeypatch, tmp_path):
    temp_dir = tmp_path / "database"
    temp_db = temp_dir / "travel.db"
    monkeypatch.setattr(db, "DB_DIR", str(temp_dir))
    monkeypatch.setattr(db, "DB_PATH", str(temp_db))
    db.init_db()
    return db


def describe_weather_history():
    def it_seeds_twelve_months_of_weather_data_per_city(monkeypatch, tmp_path):
        db_module = setup_temp_db(monkeypatch, tmp_path)

        # Fetch a city
        city = db_module.get_city_by_name("Tokyo")
        assert city is not None

        weather = db_module.get_weather_history(city["id"])
        assert len(weather) == 12

        # Verify month sequence and basic fields
        for idx, row in enumerate(weather):
            assert row["month_num"] == idx + 1
            assert "avg_temp" in row
            assert "rainfall" in row
            assert "description" in row
            assert "recommendation" in row

    def it_translates_weather_records_for_hindi_locale(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)

        # Setup session state language mock
        monkeypatch.setitem(st.session_state, "language", "hi")

        record = {
            "city_name": "Tokyo",
            "month_name": "January",
            "month_num": 1,
            "avg_temp": 5.0,
            "rainfall": 45.0,
            "description": "Cold & Sunny",
            "recommendation": "Carry a heavy winter coat, gloves, and scarf. Great for hot springs.",
        }

        translated = translate_weather_record(record)
        assert translated["month_name"] == "जनवरी"
        assert translated["description"] == "ठंडा और धूपदार"
        assert "भारी सर्दियों के कोट" in translated["recommendation"]

    def it_translates_weather_records_for_telugu_locale(monkeypatch, tmp_path):
        setup_temp_db(monkeypatch, tmp_path)

        # Setup session state language mock
        monkeypatch.setitem(st.session_state, "language", "te")

        record = {
            "city_name": "Tokyo",
            "month_name": "January",
            "month_num": 1,
            "avg_temp": 5.0,
            "rainfall": 45.0,
            "description": "Cold & Sunny",
            "recommendation": "Carry a heavy winter coat, gloves, and scarf. Great for hot springs.",
        }

        translated = translate_weather_record(record)
        assert translated["month_name"] == "జనవరి"
        assert translated["description"] == "చల్లగా & ఎండగా"
        assert "భారీ శీతాకాలపు కోటు" in translated["recommendation"]
