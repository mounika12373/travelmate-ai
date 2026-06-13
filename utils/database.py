import os
import sqlite3

DB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "database")
DB_PATH = os.path.join(DB_DIR, "travel.db")


def get_connection():
    """Returns a connection to the SQLite database with Row factory enabled."""
    os.makedirs(DB_DIR, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Creates the tables if they do not exist and populates them if empty."""
    conn = get_connection()
    cursor = conn.cursor()

    # Enable foreign key support
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Create countries table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country_name TEXT UNIQUE NOT NULL,
        capital TEXT NOT NULL,
        currency TEXT NOT NULL,
        language TEXT NOT NULL,
        timezone TEXT NOT NULL,
        emergency_number TEXT NOT NULL,
        visa_info TEXT NOT NULL,
        rules TEXT NOT NULL,
        etiquette TEXT NOT NULL,
        safety_tips TEXT NOT NULL
    );
    """)

    # Create cities table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        country_id INTEGER NOT NULL,
        city_name TEXT NOT NULL,
        description TEXT NOT NULL,
        transport_info TEXT NOT NULL,
        food_info TEXT NOT NULL,
        tourist_places TEXT NOT NULL, -- JSON string storing attractions list
        hotel_info TEXT NOT NULL,     -- JSON string storing hotel list by tier
        shopping_areas TEXT NOT NULL, -- JSON or comma-separated string
        airport_details TEXT NOT NULL,
        safety_recommendations TEXT NOT NULL,
        FOREIGN KEY (country_id) REFERENCES countries (id) ON DELETE CASCADE,
        UNIQUE(country_id, city_name)
    );
    """)

    conn.commit()

    # Check if empty. If so, seed database with sample data.
    cursor.execute("SELECT COUNT(*) as count FROM countries;")
    row = cursor.fetchone()
    if row["count"] == 0:
        conn.close()
        # Seed from sample_data module
        from data.sample_data import populate_database

        populate_database()
    else:
        conn.close()


def get_all_countries():
    """Fetches all countries."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM countries ORDER BY country_name ASC;")
    rows = cursor.fetchall()
    conn.close()
    from utils.i18n import translate_db_record
    return [translate_db_record(dict(row), "country") for row in rows]


def get_cities_by_country(country_id):
    """Fetches all cities for a specific country."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cities WHERE country_id = ? ORDER BY city_name ASC;", (country_id,))
    rows = cursor.fetchall()
    conn.close()
    from utils.i18n import translate_db_record
    return [translate_db_record(dict(row), "city") for row in rows]


def get_country_details(country_id):
    """Fetches details of a specific country by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM countries WHERE id = ?;", (country_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        from utils.i18n import translate_db_record
        return translate_db_record(dict(row), "country")
    return None


def get_country_by_name(country_name):
    """Fetches details of a country by name (case-insensitive)."""
    from utils.i18n import get_english_term, translate_db_record
    eng_name = get_english_term(country_name)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM countries WHERE LOWER(country_name) = LOWER(?);", (eng_name.strip(),))
    row = cursor.fetchone()
    conn.close()
    if row:
        return translate_db_record(dict(row), "country")
    return None


def get_city_details(city_id):
    """Fetches details of a specific city by ID."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cities WHERE id = ?;", (city_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        from utils.i18n import translate_db_record
        return translate_db_record(dict(row), "city")
    return None


def get_city_by_name(city_name):
    """Fetches details of a city by name (case-insensitive)."""
    from utils.i18n import get_english_term, translate_db_record
    eng_name = get_english_term(city_name)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cities WHERE LOWER(city_name) = LOWER(?);", (eng_name.strip(),))
    row = cursor.fetchone()
    conn.close()
    if row:
        return translate_db_record(dict(row), "city")
    return None


def search_locations(query):
    """
    Searches for matching countries and cities.
    Returns a dict with key 'countries' and 'cities' containing matching rows.
    """
    if not query or not query.strip():
        return {"countries": [], "cities": []}

    from utils.i18n import get_english_term, translate_db_record
    eng_query = get_english_term(query)
    q = f"%{eng_query.strip()}%"
    conn = get_connection()
    cursor = conn.cursor()

    # Search countries
    cursor.execute(
        """
        SELECT * FROM countries 
        WHERE country_name LIKE ? OR capital LIKE ? OR language LIKE ?;
<<<<<<< HEAD
    """, (q, q, q))
    countries = [translate_db_record(dict(row), "country") for row in cursor.fetchall()]
=======
    """,
        (q, q, q),
    )
    countries = [dict(row) for row in cursor.fetchall()]
>>>>>>> be75e90 (Fix compliance checks and tooling)

    # Search cities
    cursor.execute(
        """
        SELECT cities.*, countries.country_name 
        FROM cities 
        JOIN countries ON cities.country_id = countries.id
        WHERE city_name LIKE ? OR description LIKE ? OR tourist_places LIKE ?;
<<<<<<< HEAD
    """, (q, q, q))
    cities = [translate_db_record(dict(row), "city") for row in cursor.fetchall()]
=======
    """,
        (q, q, q),
    )
    cities = [dict(row) for row in cursor.fetchall()]
>>>>>>> be75e90 (Fix compliance checks and tooling)

    conn.close()
    return {"countries": countries, "cities": cities}
