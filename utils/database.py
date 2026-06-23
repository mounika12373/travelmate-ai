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

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT,
        country TEXT,
        city TEXT,
        profile_pic TEXT,            -- Base64 encoded image string or None
        password_hash TEXT NOT NULL,  -- hashed password
        preferences TEXT,            -- JSON array of strings
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Create travel_history table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS travel_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        activity_type TEXT NOT NULL, -- 'search', 'itinerary', 'hotel_search', 'flight_search', 'chat'
        query TEXT,
        details TEXT,                -- JSON string storing metadata/itinerary
        is_favorite INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    );
    """)

    # Create saved_trips table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS saved_trips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        trip_type TEXT NOT NULL,     -- 'itinerary', 'destination', 'hotel', 'flight'
        name TEXT NOT NULL,
        collection_name TEXT DEFAULT 'My Saved Trips',
        details TEXT NOT NULL,       -- JSON string containing details
        travel_date TEXT,            -- 'YYYY-MM-DD'
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
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
    """,
        (q, q, q),
    )
    countries = [translate_db_record(dict(row), "country") for row in cursor.fetchall()]

    # Search cities
    cursor.execute(
        """
        SELECT cities.*, countries.country_name 
        FROM cities 
        JOIN countries ON cities.country_id = countries.id
        WHERE city_name LIKE ? OR description LIKE ? OR tourist_places LIKE ?;
    """,
        (q, q, q),
    )
    cities = [translate_db_record(dict(row), "city") for row in cursor.fetchall()]

    conn.close()
    return {"countries": countries, "cities": cities}

# ==========================================
# NEW USER AUTH & PROFILE PERSISTENCE METHODS
# ==========================================

def create_user(full_name, email, phone, country, city, profile_pic, password_hash, preferences="[]"):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
        INSERT INTO users (full_name, email, phone, country, city, profile_pic, password_hash, preferences)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, (full_name, email.strip().lower(), phone, country, city, profile_pic, password_hash, preferences))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return user_id
    except sqlite3.IntegrityError:
        conn.close()
        return None

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE LOWER(email) = LOWER(?);", (email.strip(),))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?;", (user_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def update_user_profile(user_id, full_name, phone, country, city, profile_pic, preferences):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE users 
    SET full_name = ?, phone = ?, country = ?, city = ?, profile_pic = ?, preferences = ?
    WHERE id = ?;
    """, (full_name, phone, country, city, profile_pic, preferences, user_id))
    conn.commit()
    conn.close()
    return True

# ==========================================
# ACTIVITY TRACKING & TRAVEL HISTORY LOGS
# ==========================================

def log_activity(user_id, activity_type, query, details=None):
    import json
    if details and not isinstance(details, str):
        details = json.dumps(details)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO travel_history (user_id, activity_type, query, details)
    VALUES (?, ?, ?, ?);
    """, (user_id, activity_type, query, details))
    conn.commit()
    conn.close()

def get_travel_history(user_id, activity_type=None, search_query=None, start_date=None, end_date=None, country=None):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM travel_history WHERE user_id = ?"
    params = [user_id]
    
    if activity_type:
        query += " AND activity_type = ?"
        params.append(activity_type)
        
    if search_query:
        query += " AND (query LIKE ? OR details LIKE ?)"
        params.append(f"%{search_query}%")
        params.append(f"%{search_query}%")
        
    if start_date:
        query += " AND date(created_at) >= date(?)"
        params.append(start_date)
        
    if end_date:
        query += " AND date(created_at) <= date(?)"
        params.append(end_date)
        
    if country:
        query += " AND (query LIKE ? OR details LIKE ?)"
        params.append(f"%{country}%")
        params.append(f"%{country}%")
        
    query += " ORDER BY created_at DESC"
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def delete_history_item(history_id, user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM travel_history WHERE id = ? AND user_id = ?;", (history_id, user_id))
    conn.commit()
    conn.close()

def clear_user_history(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM travel_history WHERE user_id = ?;", (user_id,))
    conn.commit()
    conn.close()

def toggle_history_favorite(history_id, user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT is_favorite FROM travel_history WHERE id = ? AND user_id = ?;", (history_id, user_id))
    row = cursor.fetchone()
    if row:
        new_val = 1 if row["is_favorite"] == 0 else 0
        cursor.execute("UPDATE travel_history SET is_favorite = ? WHERE id = ? AND user_id = ?;", (new_val, history_id, user_id))
        conn.commit()
    conn.close()

# ==========================================
# SAVED TRIPS & BOOKMARKS SYSTEMS
# ==========================================

def save_trip(user_id, trip_type, name, collection_name, details, travel_date=None):
    import json
    if details and not isinstance(details, str):
        details = json.dumps(details)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO saved_trips (user_id, trip_type, name, collection_name, details, travel_date)
    VALUES (?, ?, ?, ?, ?, ?);
    """, (user_id, trip_type, name, collection_name, details, travel_date))
    conn.commit()
    conn.close()

def get_saved_trips(user_id, trip_type=None, collection_name=None):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM saved_trips WHERE user_id = ?"
    params = [user_id]
    if trip_type:
        query += " AND trip_type = ?"
        params.append(trip_type)
    if collection_name:
        query += " AND collection_name = ?"
        params.append(collection_name)
    query += " ORDER BY created_at DESC"
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def delete_saved_trip(saved_trip_id, user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM saved_trips WHERE id = ? AND user_id = ?;", (saved_trip_id, user_id))
    conn.commit()
    conn.close()

# ==========================================
# DASHBOARD ANALYTICS & STATS AGGREGATORS
# ==========================================

def get_dashboard_stats(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. Total Trips Planned
    cursor.execute("SELECT COUNT(*) as count FROM saved_trips WHERE user_id = ? AND trip_type = 'itinerary';", (user_id,))
    total_saved_itineraries = cursor.fetchone()["count"]
    
    cursor.execute("SELECT COUNT(*) as count FROM travel_history WHERE user_id = ? AND activity_type = 'itinerary';", (user_id,))
    total_generated_itineraries = cursor.fetchone()["count"]
    
    # 2. Countries Explored (distinct country keyword from history and saved)
    cursor.execute("SELECT DISTINCT query FROM travel_history WHERE user_id = ? AND activity_type IN ('search', 'itinerary');", (user_id,))
    searches = [r["query"] for r in cursor.fetchall() if r["query"]]
    
    cursor.execute("SELECT DISTINCT name FROM saved_trips WHERE user_id = ? AND trip_type = 'destination';", (user_id,))
    destinations = [r["name"] for r in cursor.fetchall() if r["name"]]
    
    countries_set = set()
    for text in searches + destinations:
        t_lower = text.lower()
        if any(w in t_lower for w in ["india", "भारत", "భారతదేశం", "hyderabad", "visakhapatnam", "mumbai", "delhi", "bangalore", "chennai", "kolkata", "jaipur", "agra", "varanasi", "kochi", "goa", "udaipur", "pune", "ahmedabad", "amritsar", "srinagar", "shimla", "darjeeling", "mysore"]):
            countries_set.add("India")
        if any(w in t_lower for w in ["japan", "जापान", "జపాన్", "tokyo", "osaka", "kyoto", "yokohama", "nagoya", "sapporo", "fukuoka", "kobe", "hiroshima", "nara", "okinawa", "kanazawa", "hakodate", "nagasaki", "sendai", "takayama", "himeji", "kamakura", "nikko", "matsumoto"]):
            countries_set.add("Japan")
        if any(w in t_lower for w in ["singapore", "सिंगापुर", "సింగపూర్", "downtown", "sentosa", "orchard", "chinatown", "little india", "katong", "tampines", "jurong", "woodlands", "changi", "yishun", "ang mo kio", "bedok", "queenstown", "novena", "bukit timah", "punggol", "clementi", "serangoon"]):
            countries_set.add("Singapore")
            
    countries_explored = len(countries_set)
    if countries_explored == 0 and (total_saved_itineraries > 0 or total_generated_itineraries > 0):
        countries_explored = 1
        
    # 3. Saved Destinations Count
    cursor.execute("SELECT COUNT(*) as count FROM saved_trips WHERE user_id = ? AND trip_type = 'destination';", (user_id,))
    saved_destinations = cursor.fetchone()["count"]
    
    # 4. Recent Searches (top 5)
    cursor.execute("SELECT DISTINCT query, created_at FROM travel_history WHERE user_id = ? AND activity_type = 'search' ORDER BY created_at DESC LIMIT 5;", (user_id,))
    recent_searches = [dict(row) for row in cursor.fetchall()]
    
    # 5. AI Usage Statistics
    cursor.execute("SELECT COUNT(*) as count FROM travel_history WHERE user_id = ? AND activity_type = 'chat';", (user_id,))
    chat_interactions = cursor.fetchone()["count"]
    
    # 6. Upcoming Trips Timeline
    cursor.execute("""
        SELECT * FROM saved_trips 
        WHERE user_id = ? AND trip_type = 'itinerary' AND travel_date IS NOT NULL AND travel_date != '' 
        ORDER BY date(travel_date) ASC;
    """, (user_id,))
    upcoming_trips = [dict(row) for row in cursor.fetchall()]
    
    conn.close()
    return {
        "total_trips": total_saved_itineraries + total_generated_itineraries,
        "countries_explored": countries_explored,
        "saved_destinations": saved_destinations,
        "recent_searches": recent_searches,
        "ai_usage": {
            "itineraries_generated": total_generated_itineraries,
            "chatbot_interactions": chat_interactions
        },
        "upcoming_trips": upcoming_trips
    }
