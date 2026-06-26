import json

from utils.database import get_connection


def populate_database():
    """Populates the database with sample data for India, Japan, and Singapore."""
    conn = get_connection()
    cursor = conn.cursor()

    # Clean old data to prevent foreign key issues or duplicates
    cursor.execute("PRAGMA foreign_keys = OFF;")
    cursor.execute("DELETE FROM cities;")
    cursor.execute("DELETE FROM countries;")
    cursor.execute("PRAGMA foreign_keys = ON;")

    # -------------------------------------------------------------
    # 1. INDIA
    # -------------------------------------------------------------
    india_data = {
        "country_name": "India",
        "capital": "New Delhi",
        "currency": "Indian Rupee (INR, ₹)",
        "language": "Hindi, English",
        "timezone": "IST (UTC+5:30)",
        "emergency_number": "112 (National Emergency), 100 (Police), 102 (Ambulance), 101 (Fire)",
        "visa_info": "eVisa is available for tourists from over 160 countries. Apply online at least 4-7 days prior to departure. Requires 6 months passport validity.",
        "rules": "1. Smoking is strictly prohibited in public places.\n2. Respect local religious customs: cover your head and remove shoes before entering temples or mosques.\n3. Dress modestly, especially in religious sites.\n4. Avoid public displays of affection.",
        "etiquette": "1. Greet locals with a polite 'Namaste' with folded hands.\n2. Remove your shoes before entering someone's home.\n3. Always use your right hand when eating, giving, or receiving items (the left hand is traditionally considered unclean).\n4. Seek permission before taking photos of people or religious ceremonies.",
        "safety_tips": "1. Drink only bottled or purified water. Avoid street ice.\n2. Use official prepaid taxi counters at airports or standard ride-hailing apps like Ola/Uber.\n3. Keep your bags secure in crowded tourist spots to prevent pickpocketing.\n4. Dress appropriately to respect local norms and avoid unwanted attention.",
    }

    cursor.execute(
        """
    INSERT INTO countries (
        country_name, capital, currency, language, timezone, emergency_number, visa_info, rules, etiquette, safety_tips
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """,
        (
            india_data["country_name"],
            india_data["capital"],
            india_data["currency"],
            india_data["language"],
            india_data["timezone"],
            india_data["emergency_number"],
            india_data["visa_info"],
            india_data["rules"],
            india_data["etiquette"],
            india_data["safety_tips"],
        ),
    )
    india_id = cursor.lastrowid

    india_cities = [
        # 1. Hyderabad
        {
            "city_name": "Hyderabad",
            "description": "The City of Pearls, Hyderabad offers a beautiful blend of Nizam-era history, royal architecture, and a booming information technology hub.",
            "transport_info": "Highly accessible via the Hyderabad Metro Rail, local TSRTC buses, auto-rickshaws, and ride-hailing cabs like Uber/Ola.",
            "food_info": [
                {
                    "name": "Hyderabadi Biryani",
                    "desc": "Fragrant basmati rice slow-cooked with spiced meat, yogurt, and saffron.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Haleem",
                    "desc": "A slow-cooked, rich stew of wheat, lentils, and meat, seasoned with ghee.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Qubani ka Meetha",
                    "desc": "Traditional apricot-based dessert topped with cream or custard.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Charminar",
                    "desc": "A grand 16th-century mosque and landmark in the heart of old city.",
                    "rating": "4.6 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Golconda Fort",
                    "desc": "An acoustic medieval fort with massive ramparts and sound effects.",
                    "rating": "4.7 ⭐",
                    "time": "Afternoon",
                },
                {
                    "name": "Hussain Sagar Lake",
                    "desc": "A scenic heart-shaped lake with a giant Buddha statue in the center.",
                    "rating": "4.3 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Taj Falaknuma Palace",
                    "desc": "A restored 19th-century royal palace hotel.",
                    "price": "₹35,000+ per night",
                },
                "mid_range": {
                    "name": "Novotel Hyderabad HITEC City",
                    "desc": "Modern premium stay near the technology corridor.",
                    "price": "₹9,000 per night",
                },
                "budget": {
                    "name": "Red Fox Hotel, HITEC City",
                    "desc": "Clean and comfy budget-friendly business hotel.",
                    "price": "₹3,200 per night",
                },
            },
            "shopping_areas": [
                {"name": "Laad Bazaar", "desc": "Traditional bazaar famous for lacquer bangles and pearls."},
                {"name": "Inorbit Mall", "desc": "Large modern shopping complex featuring global fashion brands."},
            ],
            "airport_details": "Rajiv Gandhi International Airport (HYD) is located in Shamshabad, about 24 km from the city.",
            "safety_recommendations": "Generally very safe. Secure bags in crowded areas like Charminar.",
        },
        # 2. Visakhapatnam
        {
            "city_name": "Visakhapatnam",
            "description": "A beautiful coastal port city in Andhra Pradesh, surrounded by hills and the Bay of Bengal, known for its clean beaches.",
            "transport_info": "Local APSRTC buses, auto-rickshaws, and ride-hailing services (Ola/Uber) are widely available.",
            "food_info": [
                {
                    "name": "Bamboo Chicken",
                    "desc": "A delicious tribal chicken dish cooked inside bamboo shoots without oil.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Andhra Thali",
                    "desc": "Spicy regional meals served with rice, dal, curries, and pickles.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "RK Beach",
                    "desc": "Popular beach strip lined with parks, museums, and food stalls.",
                    "rating": "4.5 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Kursura Submarine Museum",
                    "desc": "A real decommissioned Soviet submarine parked on the beach for public tours.",
                    "rating": "4.8 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Novotel Varun Beach",
                    "desc": "Modern luxury hotel with panoramic ocean views.",
                    "price": "₹12,000+ per night",
                },
                "mid_range": {
                    "name": "The Gateway Hotel Taj",
                    "desc": "Seaside comfort with standard Taj hospitality.",
                    "price": "₹7,500 per night",
                },
                "budget": {
                    "name": "Hotel Dolphin",
                    "desc": "Reputable budget-friendly business hotel in the city center.",
                    "price": "₹3,000 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Jagadamba Junction",
                    "desc": "Commercial shopping district with textile and electronics markets.",
                },
                {"name": "CMR Central", "desc": "Popular shopping mall with fashion labels and cinemas."},
            ],
            "airport_details": "Visakhapatnam International Airport (VTZ) is located about 12 km from the city center.",
            "safety_recommendations": "Be highly cautious of strong undercurrents at the beaches.",
        },
        # 3. Mumbai
        {
            "city_name": "Mumbai",
            "description": "The financial and entertainment capital of India, famous for Bollywood, colonial history, and fast-paced coastal life.",
            "transport_info": "Lifeline local trains, local yellow taxis, auto-rickshaws, and Metro rail networks.",
            "food_info": [
                {
                    "name": "Vada Pav",
                    "desc": "Mumbai's iconic street food: a spicy potato fritter inside a bun.",
                    "type": "Veg",
                },
                {
                    "name": "Pav Bhaji",
                    "desc": "Spiced vegetable curry mashed and served with buttered soft buns.",
                    "type": "Veg",
                },
                {
                    "name": "Bhel Puri",
                    "desc": "Crunchy street snack made of puffed rice, vegetables, and sweet chutney.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Gateway of India",
                    "desc": "A magnificent stone arch monument built during the British Raj.",
                    "rating": "4.7 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Marine Drive",
                    "desc": "A scenic coastal crescent boulevard, also known as the Queen's Necklace.",
                    "rating": "4.8 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Elephanta Caves",
                    "desc": "Rock-cut temple cave complex on an island, dedicated to Lord Shiva.",
                    "rating": "4.5 ⭐",
                    "time": "Full Day",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Taj Mahal Palace",
                    "desc": "Iconic, historic luxury hotel overlooking the harbor.",
                    "price": "₹28,000+ per night",
                },
                "mid_range": {
                    "name": "Trident Bandra Kurla",
                    "desc": "Modern premium corporate hotel in the financial district.",
                    "price": "₹12,000 per night",
                },
                "budget": {
                    "name": "Ginger Hotel Andheri East",
                    "desc": "Clean and reliable value hotel for budget travelers.",
                    "price": "₹3,500 per night",
                },
            },
            "shopping_areas": [
                {"name": "Colaba Causeway", "desc": "Street market famous for jewelry, clothes, and antiques."},
                {"name": "Phoenix Palladium", "desc": "High-end luxury mall showcasing international fashion brands."},
            ],
            "airport_details": "Chhatrapati Shivaji Maharaj International Airport (BOM) is a premier global hub.",
            "safety_recommendations": "Very safe. Be mindful of pickpockets on crowded local trains.",
        },
        # 4. Delhi
        {
            "city_name": "Delhi",
            "description": "The capital of India, showcasing a blend of ancient history in Old Delhi and broad leafy avenues in New Delhi.",
            "transport_info": "World-class Delhi Metro network, auto-rickshaws, and ride-hailing services.",
            "food_info": [
                {
                    "name": "Butter Chicken",
                    "desc": "Tender chicken cooked in a rich, creamy tomato gravy with butter.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Chole Bhature",
                    "desc": "Spicy chickpeas served with fluffy, deep-fried leavened bread.",
                    "type": "Veg",
                },
                {
                    "name": "Paranthas",
                    "desc": "Stuffed flatbreads cooked with ghee, popular in Old Delhi.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "India Gate",
                    "desc": "A towering war memorial archway surrounded by lush lawns.",
                    "rating": "4.6 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Qutub Minar",
                    "desc": "A towering 73-meter brick minaret built in the 12th century.",
                    "rating": "4.7 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Red Fort",
                    "desc": "Massive red sandstone fortress of the Mughal dynasty.",
                    "rating": "4.5 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Leela Palace New Delhi",
                    "desc": "Ultra-luxury hotel combining Indian heritage and modern tech.",
                    "price": "₹24,000 per night",
                },
                "mid_range": {
                    "name": "Radisson Blu Marina Connaught Place",
                    "desc": "Centrally located premium business hotel.",
                    "price": "₹8,500 per night",
                },
                "budget": {
                    "name": "Bloomrooms @ Link Road",
                    "desc": "Bright, clean, and yellow-themed budget boutique hotel.",
                    "price": "₹3,000 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Chandni Chowk",
                    "desc": "Old Delhi's ancient market, famous for spices, sarees, and street food.",
                },
                {"name": "Khan Market", "desc": "High-end shopping street with elite bookshops, boutiques, and cafes."},
            ],
            "airport_details": "Indira Gandhi International Airport (DEL) is India's busiest airport hub.",
            "safety_recommendations": "Stay alert during late hours; prefer using metro rail or authorized taxis.",
        },
        # 5. Bangalore
        {
            "city_name": "Bangalore",
            "description": "Known as India's Silicon Valley and Garden City, famous for its pleasant climate, parks, and café culture.",
            "transport_info": "Namma Metro lines, city buses, and local ride-hailing applications.",
            "food_info": [
                {"name": "Masala Dosa", "desc": "Crispy rice crepes stuffed with spiced potato mash.", "type": "Veg"},
                {
                    "name": "Filter Coffee",
                    "desc": "Strong coffee brewed in a traditional metal filter and frothed with milk.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Bangalore Palace",
                    "desc": "A grand royal palace inspired by Windsor Castle.",
                    "rating": "4.4 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Lalbagh Botanical Garden",
                    "desc": "Historic 240-acre botanical garden with a glasshouse.",
                    "rating": "4.6 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Oberoi Bangalore",
                    "desc": "Award-winning luxury hotel with private balconies.",
                    "price": "₹18,000 per night",
                },
                "mid_range": {
                    "name": "ibis Bengaluru City Centre",
                    "desc": "Modern and practical hotel near the city park.",
                    "price": "₹5,000 per night",
                },
                "budget": {
                    "name": "Casa Cottage",
                    "desc": "Heritage English cottage guest house in a quiet spot.",
                    "price": "₹2,500 per night",
                },
            },
            "shopping_areas": [
                {"name": "Commercial Street", "desc": "Vibrant street market for fashion and footwear shopping."},
                {"name": "UB City Mall", "desc": "India's first luxury mall, filled with high-end designer stores."},
            ],
            "airport_details": "Kempegowda International Airport (BLR) is located about 35 km north of the city.",
            "safety_recommendations": "Generally very safe. Heavy traffic can cause long travel delays.",
        },
        # 6. Chennai
        {
            "city_name": "Chennai",
            "description": "Gateway to the South, Chennai is rich in artistic traditions, deep-fried street foods, and beaches.",
            "transport_info": "Chennai Metro, local buses, local auto-rickshaws, and suburb trains.",
            "food_info": [
                {"name": "Idli & Sambar", "desc": "Steamed savory rice cakes served with lentil stew.", "type": "Veg"},
                {
                    "name": "Chicken 65",
                    "desc": "Spicy, deep-fried chicken appetizer originating in Chennai.",
                    "type": "Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Marina Beach",
                    "desc": "One of the longest natural sandy beaches in the world.",
                    "rating": "4.4 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Kapaleeshwarar Temple",
                    "desc": "An ancient 7th-century Hindu temple dedicated to Lord Shiva.",
                    "rating": "4.7 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "ITC Grand Chola",
                    "desc": "Massive luxury palace hotel boasting Chola dynasty architecture.",
                    "price": "₹20,000 per night",
                },
                "mid_range": {
                    "name": "The Residency Towers Chennai",
                    "desc": "Premium hotel in T. Nagar with excellent rooftop dining.",
                    "price": "₹6,500 per night",
                },
                "budget": {
                    "name": "Hotel President Marina",
                    "desc": "Affordable budget rooms close to Marina Beach.",
                    "price": "₹2,500 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "T. Nagar",
                    "desc": "India's largest shopping district, famous for silk Kanjivaram sarees and gold.",
                },
                {"name": "Express Avenue", "desc": "Modern lifestyle mall in Royapettah with major fashion brands."},
            ],
            "airport_details": "Chennai International Airport (MAA) is situated in Tirusulam, inside city limits.",
            "safety_recommendations": "Generally safe. Dress conservatively when entering traditional temples.",
        },
        # 7. Kolkata
        {
            "city_name": "Kolkata",
            "description": "The City of Joy, Kolkata is the cultural capital of India, known for colonial architecture and sweets.",
            "transport_info": "India's oldest Metro network, iconic yellow taxis, local trams, and hand-pulled rickshaws.",
            "food_info": [
                {
                    "name": "Kathi Roll",
                    "desc": "Skewered kebab wrapped in paratha bread with spices and sauces.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Roshogolla",
                    "desc": "Spongy, round cottage-cheese dumplings soaked in sugar syrup.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Victoria Memorial",
                    "desc": "A majestic white marble palace built in memory of Queen Victoria.",
                    "rating": "4.7 ⭐",
                    "time": "Afternoon",
                },
                {
                    "name": "Howrah Bridge",
                    "desc": "A massive cantilever steel suspension bridge over the Hooghly River.",
                    "rating": "4.6 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Oberoi Grand Kolkata",
                    "desc": "Classic neo-classical colonial luxury hotel.",
                    "price": "₹16,000 per night",
                },
                "mid_range": {
                    "name": "The Peerless Inn Kolkata",
                    "desc": "Centrally located business hotel near Esplanade Metro.",
                    "price": "₹5,500 per night",
                },
                "budget": {
                    "name": "Broadway Hotel",
                    "desc": "Retro-style budget lodging dating back to colonial days.",
                    "price": "₹1,800 per night",
                },
            },
            "shopping_areas": [
                {"name": "New Market", "desc": "Historic shopping center containing over 2,000 street stalls."},
                {
                    "name": "Gariahat Market",
                    "desc": "Bustling open-air street market famous for sarees and accessories.",
                },
            ],
            "airport_details": "Netaji Subhash Chandra Bose International Airport (CCU) is in Dum Dum.",
            "safety_recommendations": "Very safe. Be prepared for crowds in markets and public transport.",
        },
        # 8. Jaipur
        {
            "city_name": "Jaipur",
            "description": "The Pink City, capital of Rajasthan, famous for royal palaces, forts, and gemstone markets.",
            "transport_info": "Jaipur Metro, auto-rickshaws, rental cabs, and elephant/camel rides at Amer Fort.",
            "food_info": [
                {
                    "name": "Dal Baati Churma",
                    "desc": "Baked wheat balls served with lentil curry and sweet crushed wheat.",
                    "type": "Veg",
                },
                {
                    "name": "Lal Maas",
                    "desc": "A fiery Rajasthani lamb curry cooked with red chilies and garlic.",
                    "type": "Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Hawa Mahal",
                    "desc": "The unique five-story Palace of Winds made of pink sandstone.",
                    "rating": "4.6 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Amber Palace",
                    "desc": "A majestic hilltop fortress featuring gorgeous mirrored halls.",
                    "rating": "4.8 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Rambagh Palace",
                    "desc": "Grand luxury hotel inside a former royal palace.",
                    "price": "₹40,000+ per night",
                },
                "mid_range": {
                    "name": "Alsisar Haveli",
                    "desc": "Beautifully restored heritage mansion with royal vibes.",
                    "price": "₹7,000 per night",
                },
                "budget": {
                    "name": "Umaid Bhawan Hotel",
                    "desc": "Cozy heritage budget hotel with colorful carvings.",
                    "price": "₹2,500 per night",
                },
            },
            "shopping_areas": [
                {"name": "Johari Bazaar", "desc": "Famed jewelry market specializing in gold, silver, and gemstones."},
                {"name": "Bapu Bazaar", "desc": "Traditional street market selling leather mojri shoes and textiles."},
            ],
            "airport_details": "Jaipur International Airport (JAI) is located in the suburb of Sanganer.",
            "safety_recommendations": "Ignore persistent street vendors and tour guides; book official entry tickets online.",
        },
        # 9. Agra
        {
            "city_name": "Agra",
            "description": "Home to the world-famous Taj Mahal, situated on the banks of the Yamuna River in Uttar Pradesh.",
            "transport_info": "Auto-rickshaws, electric battery buses near Taj Mahal, and local cabs.",
            "food_info": [
                {
                    "name": "Petha",
                    "desc": "A translucent, sweet candy made from ash gourd, native to Agra.",
                    "type": "Veg",
                },
                {
                    "name": "Bedai & Jalebi",
                    "desc": "Spicy puffed fried bread served with potato curry and sweet jalebis.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Taj Mahal",
                    "desc": "The world-famous white marble mausoleum, a monument of eternal love.",
                    "rating": "4.9 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Agra Fort",
                    "desc": "A massive 16th-century red sandstone fortress of the Mughal Emperors.",
                    "rating": "4.7 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Oberoi Amarvilas",
                    "desc": "Ultra-luxury hotel where all rooms offer Taj views.",
                    "price": "₹45,000+ per night",
                },
                "mid_range": {
                    "name": "DoubleTree by Hilton Agra",
                    "desc": "Modern hotel with an outdoor pool showing Taj glimpses.",
                    "price": "₹6,000 per night",
                },
                "budget": {
                    "name": "Howard Plaza The Fern",
                    "desc": "Comfortable budget-friendly hotel close to the Taj East Gate.",
                    "price": "₹3,000 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Sadar Bazaar",
                    "desc": "Vibrant market famous for leather goods, handicrafts, and sweet stores.",
                },
                {"name": "Kinari Bazaar", "desc": "Traditional wholesale market behind the historic Jama Masjid."},
            ],
            "airport_details": "Agra has a military airfield; tourists mostly arrive via train from Delhi (1.5 hours).",
            "safety_recommendations": "Pre-arrange authorized guides. Beware of vendors claiming to sell genuine marble.",
        },
        # 10. Varanasi
        {
            "city_name": "Varanasi",
            "description": "One of the oldest continuously inhabited cities in the world, the spiritual heart of Hinduism.",
            "transport_info": "Cycle-rickshaws, local boats on the Ganges River, and walking through narrow alleys.",
            "food_info": [
                {
                    "name": "Kachori Sabzi",
                    "desc": "Fried round pastry stuffed with lentils, served with spicy potato curry.",
                    "type": "Veg",
                },
                {
                    "name": "Banarasi Lassi",
                    "desc": "Creamy yogurt drink topped with rabri, served in earthen pots.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Dashashwamedh Ghat",
                    "desc": "The main riverfront ghat famous for the spectacular evening Ganga Aarti.",
                    "rating": "4.8 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Kashi Vishwanath Temple",
                    "desc": "Historic golden-spire temple dedicated to Lord Shiva.",
                    "rating": "4.7 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Brijrama Palace Varanasi",
                    "desc": "A 210-year-old heritage palace hotel right on the ghats.",
                    "price": "₹22,000 per night",
                },
                "mid_range": {
                    "name": "Radisson Hotel Varanasi",
                    "desc": "Modern and comfortable hotel in the city center area.",
                    "price": "₹8,000 per night",
                },
                "budget": {
                    "name": "Ganpati Guest House",
                    "desc": "Colorful budget hotel on the riverfront with a nice courtyard.",
                    "price": "₹2,500 per night",
                },
            },
            "shopping_areas": [
                {"name": "Chowk Area", "desc": "Ancient market streets famous for authentic Banarasi silk sarees."},
                {
                    "name": "Vishwanath Gali",
                    "desc": "Narrow market passage leading to temples, selling devotional items.",
                },
            ],
            "airport_details": "Lal Bahadur Shastri International Airport (VNS) is located 24 km from Varanasi.",
            "safety_recommendations": "Keep belongings close in crowded ghats. Beware of fake priests charging high fees.",
        },
        # 11. Kochi
        {
            "city_name": "Kochi",
            "description": "A historic port city in Kerala, displaying a rich mix of Portuguese, Dutch, British, and spice trade histories.",
            "transport_info": "Kochi Metro, water metro boats, auto-rickshaws, and taxi services.",
            "food_info": [
                {
                    "name": "Kerala Parotta & Beef Fry",
                    "desc": "Flaky layered flatbread served with spicy roasted beef.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Karimeen Pollichathu",
                    "desc": "Pearl spot fish marinated in local spices and baked in banana leaves.",
                    "type": "Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Fort Kochi & Chinese Fishing Nets",
                    "desc": "Scenic beach walkway displaying historic cantilevered fishing nets.",
                    "rating": "4.5 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Mattancherry Palace",
                    "desc": "Also known as the Dutch Palace, featuring spectacular mural paintings.",
                    "rating": "4.3 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Brunton Boatyard",
                    "desc": "Colonial-style luxury harbor hotel in Fort Kochi.",
                    "price": "₹15,000 per night",
                },
                "mid_range": {
                    "name": "Fragrant Nature Fort Kochi",
                    "desc": "Premium boutique hotel close to main historical sights.",
                    "price": "₹6,500 per night",
                },
                "budget": {
                    "name": "Old Harbour Hotel",
                    "desc": "Quaint heritage hotel converted from a colonial residence.",
                    "price": "₹3,500 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Jew Town Spice Market",
                    "desc": "Traditional spice trading street selling fresh cardamom, pepper, and tea.",
                },
                {"name": "Lulu Mall", "desc": "One of India's largest shopping malls, located in Edappally area."},
            ],
            "airport_details": "Cochin International Airport (COK) is the world's first fully solar-powered airport.",
            "safety_recommendations": "Very safe. Be sure to carry light cotton clothing due to humid tropical weather.",
        },
        # 12. Goa
        {
            "city_name": "Goa",
            "description": "India's coastal paradise, famous for its beaches, vibrant nightlife, Portuguese churches, and seafood.",
            "transport_info": "Renting a scooter/motorcycle is the most popular way to travel. Private taxis are available.",
            "food_info": [
                {
                    "name": "Goan Fish Curry Rice",
                    "desc": "Fresh fish simmered in a spicy, coconut milk and tamarind sauce.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Bebinca",
                    "desc": "A rich, layered traditional Goan dessert made with coconut milk and egg.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Basilica of Bom Jesus",
                    "desc": "UNESCO heritage church holding the mortal remains of St. Francis Xavier.",
                    "rating": "4.7 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Baga Beach",
                    "desc": "High-energy beach strip famous for watersports, beach shacks, and bars.",
                    "rating": "4.3 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Taj Mahal Tower Goa",
                    "desc": "Premium beachfront resort in Sinquerim, North Goa.",
                    "price": "₹22,000+ per night",
                },
                "mid_range": {
                    "name": "Lemon Tree Amarante Beach Resort",
                    "desc": "Charming mid-scale resort close to Candolim beach.",
                    "price": "₹7,500 per night",
                },
                "budget": {
                    "name": "Zostel Goa",
                    "desc": "Lively backpacker hostel offering clean dorms and private rooms.",
                    "price": "₹1,200 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Anjuna Flea Market",
                    "desc": "Wednesday beach market selling clothes, handicrafts, and souvenirs.",
                },
                {
                    "name": "Mapusa Friday Market",
                    "desc": "Traditional Goan market selling local spices, fish, and pottery.",
                },
            ],
            "airport_details": "Goa is served by Dabolim Airport (GOI) and the newer Manohar International Airport (GOX) in Mopa.",
            "safety_recommendations": "Use helmets when riding rental scooters. Avoid swimming in red-flagged beach zones.",
        },
        # 13. Udaipur
        {
            "city_name": "Udaipur",
            "description": "The City of Lakes and Venice of the East, famous for romantic palaces and scenic water landscapes.",
            "transport_info": "Auto-rickshaws, rental cabs, and boat cruises on Lake Pichola.",
            "food_info": [
                {
                    "name": "Rajasthani Kadhi",
                    "desc": "Spicy yogurt-based curry thickened with gram flour and fried pakoras.",
                    "type": "Veg",
                },
                {
                    "name": "Mirchi Bada",
                    "desc": "Spicy potato-stuffed green chilies deep fried in gram flour batter.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "City Palace Udaipur",
                    "desc": "A massive fort-palace complex built over 400 years overlooking the lake.",
                    "rating": "4.8 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Lake Pichola & Lake Palace",
                    "desc": "A gorgeous artificial freshwater lake featuring boat cruises.",
                    "rating": "4.7 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Taj Lake Palace",
                    "desc": "World-famous luxury hotel sitting in the middle of Lake Pichola.",
                    "price": "₹45,000+ per night",
                },
                "mid_range": {
                    "name": "Hotel Lakend",
                    "desc": "Lakeside premium hotel with a lovely infinity pool.",
                    "price": "₹9,000 per night",
                },
                "budget": {
                    "name": "Mewar Haveli",
                    "desc": "Traditional budget haveli overlooking Lake Pichola.",
                    "price": "₹2,500 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Hathi Pol Bazaar",
                    "desc": "Famous market for Rajasthani Pichwai paintings and leather shoes.",
                },
                {"name": "Bada Bazaar", "desc": "Busy street market selling gold, silverware, and bandhani textiles."},
            ],
            "airport_details": "Maharana Pratap Airport (UDR) is located about 22 km from the city center.",
            "safety_recommendations": "Book boat rides only through government-approved ticket counters.",
        },
        # 14. Pune
        {
            "city_name": "Pune",
            "description": "The cultural capital of Maharashtra and an educational center, offering a youthful city vibe.",
            "transport_info": "Pune Metro lines, city buses, and local cabs.",
            "food_info": [
                {
                    "name": "Misal Pav",
                    "desc": "A spicy sprout curry topped with crunchy sev, onion, and lime, served with buns.",
                    "type": "Veg",
                },
                {
                    "name": "Bakarwadi",
                    "desc": "Spicy and sweet fried pastry roll, a signature Maharashtrian snack.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Shaniwar Wada",
                    "desc": "The historic fortified seat of the Peshwas of the Maratha Empire.",
                    "rating": "4.4 ⭐",
                    "time": "Afternoon",
                },
                {
                    "name": "Aga Khan Palace",
                    "desc": "A grand palace built in 1892, serving as a prison for Mahatma Gandhi.",
                    "rating": "4.5 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "JW Marriott Hotel Pune",
                    "desc": "Contemporary luxury hotel featuring upscale restaurants.",
                    "price": "₹15,000 per night",
                },
                "mid_range": {
                    "name": "Pride Hotel Pune",
                    "desc": "Established business hotel offering warm Maharashtrian hospitality.",
                    "price": "₹5,500 per night",
                },
                "budget": {
                    "name": "E-Square The Fern",
                    "desc": "Eco-friendly budget business hotel with a rooftop pool.",
                    "price": "₹3,000 per night",
                },
            },
            "shopping_areas": [
                {"name": "Laxmi Road", "desc": "Bustling retail street famous for traditional clothes and jewelry."},
                {"name": "FC Road", "desc": "Popular student hangouts and pocket-friendly street shopping stalls."},
            ],
            "airport_details": "Pune Airport (PNQ) in Lohegaon is a domestic airport with limited international flights.",
            "safety_recommendations": "Generally very safe. Observe caution when crossing busy city streets.",
        },
        # 15. Ahmedabad
        {
            "city_name": "Ahmedabad",
            "description": "Gujarat's largest city, a UNESCO World Heritage City famous for historic monuments and textile heritage.",
            "transport_info": "Ahmedabad Metro, BRTS bus corridors, and auto-rickshaws.",
            "food_info": [
                {
                    "name": "Dhokla & Khaman",
                    "desc": "Soft, steamed savory cakes made of fermented chickpea flour.",
                    "type": "Veg",
                },
                {
                    "name": "Gujarati Thali",
                    "desc": "An elaborate vegetarian platter containing multiple curries, breads, and desserts.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Sabarmati Ashram",
                    "desc": "The quiet, historic riverside residence of Mahatma Gandhi.",
                    "rating": "4.8 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Adalaj Stepwell",
                    "desc": "A spectacular five-story deep underground carved stepwell.",
                    "rating": "4.7 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Hyatt Regency Ahmedabad",
                    "desc": "Modern luxury hotel located on the Ashram Road corridor.",
                    "price": "₹9,500 per night",
                },
                "mid_range": {
                    "name": "House of MG",
                    "desc": "A premier heritage boutique hotel inside a restored mansion.",
                    "price": "₹6,500 per night",
                },
                "budget": {
                    "name": "Lemon Tree Hotel",
                    "desc": "Clean, fun budget option in the commercial district.",
                    "price": "₹3,500 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Law Garden Night Market",
                    "desc": "Famed night bazaar selling embroidered Gujarati clothing.",
                },
                {"name": "Lal Darwaja Market", "desc": "Bustling budget street market in the heart of old city."},
            ],
            "airport_details": "Sardar Vallabhbhai Patel International Airport (AMD) is located 9 km from the city.",
            "safety_recommendations": "Alcohol consumption is prohibited in Gujarat without a tourist permit. Respect local laws.",
        },
        # 16. Amritsar
        {
            "city_name": "Amritsar",
            "description": "The spiritual center of the Sikh religion, home to the jaw-dropping Golden Temple.",
            "transport_info": "Auto-rickshaws, cycle-rickshaws, and free temple shuttle buses.",
            "food_info": [
                {
                    "name": "Amritsari Kulcha",
                    "desc": "Crispy, butter-glazed flatbread stuffed with spiced potatoes and paneer.",
                    "type": "Veg",
                },
                {
                    "name": "Sarson ka Saag & Makki di Roti",
                    "desc": "Traditional mustard greens dish served with flat cornbread.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Golden Temple (Harmandir Sahib)",
                    "desc": "The breathtakingly beautiful gold-plated temple surrounding a holy pool.",
                    "rating": "4.9 ⭐",
                    "time": "Morning/Evening",
                },
                {
                    "name": "Jallianwala Bagh",
                    "desc": "A historic memorial garden marking the 1919 massacre.",
                    "rating": "4.6 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Taj Swarna Amritsar",
                    "desc": "Upscale luxury hotel with modern design and pool.",
                    "price": "₹12,000 per night",
                },
                "mid_range": {
                    "name": "Hyatt Regency Amritsar",
                    "desc": "Premium hotel located near the Golden Temple bypass.",
                    "price": "₹6,000 per night",
                },
                "budget": {
                    "name": "Hotel Ritz Plaza",
                    "desc": "Comfortable, old-school value hotel in the Mall Road area.",
                    "price": "₹2,500 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Hall Bazaar",
                    "desc": "Historic entry market selling Punjabi jutti shoes, woolens, and handicrafts.",
                },
                {
                    "name": "Katra Jaimal Singh Market",
                    "desc": "Traditional market famous for phulkari embroidered fabrics and suits.",
                },
            ],
            "airport_details": "Sri Guru Ram Das Ji International Airport (ATQ) is located 11 km northwest of Amritsar.",
            "safety_recommendations": "Cover your head and remove shoes before entering the Golden Temple complex.",
        },
        # 17. Srinagar
        {
            "city_name": "Srinagar",
            "description": "The summer capital of Jammu & Kashmir, famous for houseboats, Mughal gardens, and lakes.",
            "transport_info": "Shikara boats on Dal Lake, auto-rickshaws, and local taxis.",
            "food_info": [
                {
                    "name": "Rogan Josh",
                    "desc": "A flavorful lamb dish cooked with yogurt, saffron, and red Kashmiri chilies.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Kahwa",
                    "desc": "Kashmiri green tea brewed with saffron, cardamoms, and crushed almonds.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Dal Lake",
                    "desc": "Scenic lake famous for stays in wooden houseboats and floating markets.",
                    "rating": "4.7 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Shalimar Bagh",
                    "desc": "A beautiful terraced Mughal garden built by Emperor Jahangir.",
                    "rating": "4.5 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Lalit Grand Palace Srinagar",
                    "desc": "Historic palace hotel with spectacular lake views.",
                    "price": "₹25,000 per night",
                },
                "mid_range": {
                    "name": "WelcomHeritage Gurkha Houseboats",
                    "desc": "Deluxe traditional wooden houseboats on Nigeen Lake.",
                    "price": "₹8,000 per night",
                },
                "budget": {
                    "name": "Hotel Mount View",
                    "desc": "Comfortable, budget-friendly option near major tourist routes.",
                    "price": "₹3,500 per night",
                },
            },
            "shopping_areas": [
                {"name": "Lal Chowk", "desc": "Commercial market famous for pashmina shawls and walnuts."},
                {"name": "Floating Market", "desc": "Early morning vegetable and flower market on boats in Dal Lake."},
            ],
            "airport_details": "Srinagar International Airport (SXR) is located 12 km from the city.",
            "safety_recommendations": "Dress warmly for nights. Confirm rates for Shikaras and houseboats beforehand.",
        },
        # 18. Shimla
        {
            "city_name": "Shimla",
            "description": "The summer capital of British India, a scenic Himalayan hill town famous for pine forests.",
            "transport_info": "Walking (pedestrian-only Mall Road), local buses, and taxis.",
            "food_info": [
                {
                    "name": "Sidu",
                    "desc": "A local steamed wheat bread stuffed with poppy seeds, eaten with ghee.",
                    "type": "Veg",
                },
                {
                    "name": "Chha Gosht",
                    "desc": "Spiced lamb cooked in a gravy of roasted gram flour and yogurt.",
                    "type": "Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "The Ridge & Mall Road",
                    "desc": "A wide open walking plaza offering gorgeous mountain views.",
                    "rating": "4.6 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Kalka Shimla Toy Train",
                    "desc": "A UNESCO heritage narrow-gauge train running through green hills.",
                    "rating": "4.8 ⭐",
                    "time": "Full Day",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Wildflower Hall, An Oberoi Resort",
                    "desc": "Super-luxury heritage resort high in the cedar forests.",
                    "price": "₹35,000+ per night",
                },
                "mid_range": {
                    "name": "Clarkes Hotel",
                    "desc": "Charming colonial-era heritage hotel on the Mall Road.",
                    "price": "₹9,500 per night",
                },
                "budget": {
                    "name": "Hotel Sangeet",
                    "desc": "Simple, budget hotel located within walking distance of The Mall.",
                    "price": "₹2,500 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Lakkar Bazaar",
                    "desc": "Traditional street market famous for wooden toys, walking sticks, and crafts.",
                },
                {"name": "Mall Road Shops", "desc": "Pedestrian road lined with boutiques, booksellers, and cafes."},
            ],
            "airport_details": "Shimla Airport (SLN) has limited flights; tourists usually arrive via train/road from Chandigarh.",
            "safety_recommendations": "Beware of monkeys on Mall Road and Jakhoo Temple; keep snacks inside bags.",
        },
        # 19. Darjeeling
        {
            "city_name": "Darjeeling",
            "description": "Famed for its black tea plantations and views of Mt. Kanchenjunga, India's third-highest peak.",
            "transport_info": "Local shared jeeps, walking, and the historic Darjeeling Himalayan Toy Train.",
            "food_info": [
                {
                    "name": "Momos",
                    "desc": "Tibetan-style steamed dumplings stuffed with vegetables or meat.",
                    "type": "Veg/Non-Veg",
                },
                {
                    "name": "Thukpa",
                    "desc": "A hearty noodle soup cooked with vegetables, spices, and chicken broth.",
                    "type": "Veg/Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Tiger Hill",
                    "desc": "Famous viewpoint to witness a spectacular sunrise over Mt. Kanchenjunga.",
                    "rating": "4.7 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Batasia Loop",
                    "desc": "A spiral toy train railway loop featuring a war memorial and gardens.",
                    "rating": "4.5 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Mayfair Darjeeling",
                    "desc": "Stunning luxury heritage hotel with colonial architecture.",
                    "price": "₹14,000 per night",
                },
                "mid_range": {
                    "name": "Windamere Hotel",
                    "desc": "Historic heritage hotel preserving the atmosphere of the British Raj.",
                    "price": "₹9,000 per night",
                },
                "budget": {
                    "name": "Dekeling Hotel",
                    "desc": "Cozy family-run budget hotel offering beautiful valley views.",
                    "price": "₹2,800 per night",
                },
            },
            "shopping_areas": [
                {"name": "Chowrasta Mall", "desc": "Central pedestrian square lined with shops and tea boutiques."},
                {
                    "name": "Ghoom Monastery Market",
                    "desc": "Local market selling Tibetan handicrafts, prayer wheels, and rugs.",
                },
            ],
            "airport_details": "The nearest airport is Bagdogra Airport (IXB), located 70 km south of Darjeeling.",
            "safety_recommendations": "Leave early for Tiger Hill sunrise to beat tourist traffic blockages.",
        },
        # 20. Mysore
        {
            "city_name": "Mysore",
            "description": "The cultural capital of Karnataka, celebrated for its spectacular palace and heritage structures.",
            "transport_info": "City buses, auto-rickshaws, and horse-drawn carriages (Tongas) near the palace.",
            "food_info": [
                {
                    "name": "Mysore Masala Dosa",
                    "desc": "Crispy dosa smeared with spicy red chutney and potato stuffing.",
                    "type": "Veg",
                },
                {
                    "name": "Mysore Pak",
                    "desc": "A rich, crumbly sweet sweet fudge made of gram flour, ghee, and sugar.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Mysore Palace",
                    "desc": "The grand royal palace of the Wodeyar dynasty, illuminated on Sundays.",
                    "rating": "4.8 ⭐",
                    "time": "Morning/Evening",
                },
                {
                    "name": "Chamundi Hill",
                    "desc": "Hilltop temple dedicated to Goddess Chamundeshwari, offering city views.",
                    "rating": "4.6 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Grand Mercure Mysore",
                    "desc": "Upscale premium hotel located close to the palace gate.",
                    "price": "₹8,000 per night",
                },
                "mid_range": {
                    "name": "Southern Star Mysore",
                    "desc": "Comfortable business hotel featuring a nice pool.",
                    "price": "₹5,000 per night",
                },
                "budget": {
                    "name": "The Roost",
                    "desc": "Modern budget hotel offering essential amenities at great prices.",
                    "price": "₹2,200 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Devaraja Market",
                    "desc": "Traditional, vibrant market selling incense, flowers, and local Mysore silk.",
                },
                {"name": "Sayyaji Rao Road", "desc": "Main commercial shopping street packed with silk shops."},
            ],
            "airport_details": "Mysore has a domestic airport (MYQ) with limited flights; most fly into Bangalore.",
            "safety_recommendations": "Generally very safe. Negotiate prices for silk only in state-run government outlets.",
        },
    ]

    for city in india_cities:
        cursor.execute(
            """
        INSERT INTO cities (
            country_id, city_name, description, transport_info, food_info, tourist_places, hotel_info, shopping_areas, airport_details, safety_recommendations
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """,
            (
                india_id,
                city["city_name"],
                city["description"],
                city["transport_info"],
                json.dumps(city["food_info"]),
                json.dumps(city["tourist_places"]),
                json.dumps(city["hotel_info"]),
                json.dumps(city["shopping_areas"]),
                city["airport_details"],
                city["safety_recommendations"],
            ),
        )

    # -------------------------------------------------------------
    # 2. JAPAN
    # -------------------------------------------------------------
    japan_data = {
        "country_name": "Japan",
        "capital": "Tokyo",
        "currency": "Japanese Yen (JPY, ¥)",
        "language": "Japanese",
        "timezone": "JST (UTC+9)",
        "emergency_number": "110 (Police), 119 (Fire & Ambulance), 118 (Coast Guard)",
        "visa_info": "Citizens of over 68 countries are exempt from visa requirements for short-term stays (up to 90 days). Others must apply at their local Japanese embassy. Ensure passport validity for the duration of stay.",
        "rules": "1. No tipping in Japan; it can be seen as insulting.\n2. Do not walk and eat at the same time; eat near the shop/vending machine.\n3. Littering is strictly forbidden; carry your trash with you as there are few public bins.\n4. Walk/stand on the left side of escalators (in Tokyo) or follow the local flow.\n5. Keep phone calls and loud talking minimal on trains.",
        "etiquette": "1. Bowing is the traditional greeting; a slight nod is sufficient for tourists.\n2. Take off shoes when entering homes, ryokans (traditional inns), temples, and some restaurants (look for shoe cubbies).\n3. Hand money or cards using both hands, placing them on the small tray provided at cash registers.\n4. Avoid pointing with fingers or chopsticks.",
        "safety_tips": "1. Japan has an extremely low crime rate, but stay aware of standard safety in nightlife zones (e.g., Roppongi or Kabukicho).\n2. Be familiar with earthquake evacuation signs and download disaster alert apps like Safety Tips.\n3. Cash is still highly favored in small shops; always carry some yen bills.",
    }

    cursor.execute(
        """
    INSERT INTO countries (
        country_name, capital, currency, language, timezone, emergency_number, visa_info, rules, etiquette, safety_tips
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """,
        (
            japan_data["country_name"],
            japan_data["capital"],
            japan_data["currency"],
            japan_data["language"],
            japan_data["timezone"],
            japan_data["emergency_number"],
            japan_data["visa_info"],
            japan_data["rules"],
            japan_data["etiquette"],
            japan_data["safety_tips"],
        ),
    )
    japan_id = cursor.lastrowid

    japan_cities = [
        # 1. Tokyo
        {
            "city_name": "Tokyo",
            "description": "Japan's capital, mixing futuristic skyscrapers with historic temples and gardens.",
            "transport_info": "Incredibly complex, highly efficient subway (Metro and JR lines). Get a Suica card.",
            "food_info": [
                {"name": "Sushi", "desc": "Fresh raw seafood over vinegared rice.", "type": "Non-Veg"},
                {"name": "Ramen", "desc": "Noodle soup in pork, soy, or miso broth.", "type": "Non-Veg"},
            ],
            "tourist_places": [
                {
                    "name": "Senso-ji Temple",
                    "desc": "Historic Buddhist temple in Asakusa.",
                    "rating": "4.7 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Shibuya Crossing",
                    "desc": "World's busiest scramble pedestrian crossing.",
                    "rating": "4.5 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Aman Tokyo",
                    "desc": "High-altitude sanctuary in the business district.",
                    "price": "¥150,000+ per night",
                },
                "mid_range": {
                    "name": "Hotel Gracery Shinjuku",
                    "desc": "Central hotel famous for the Godzilla Head.",
                    "price": "¥30,000 per night",
                },
                "budget": {
                    "name": "Nine Hours Capsule Hotel",
                    "desc": "Futuristic capsule sleeping pods.",
                    "price": "¥6,000 per night",
                },
            },
            "shopping_areas": [
                {"name": "Ginza District", "desc": "Elite, high-end shopping district with international brands."},
                {"name": "Akihabara", "desc": "Subculture capital for electronics and anime goods."},
            ],
            "airport_details": "Served by Haneda Airport (HND) close to the city and Narita Airport (NRT) further out.",
            "safety_recommendations": "Extremely safe. Avoid bar touts in Roppongi/Kabukicho.",
        },
        # 2. Osaka
        {
            "city_name": "Osaka",
            "description": "Japan's food and nightlife capital, known for okonomiyaki, takoyaki, and friendly residents.",
            "transport_info": "Osaka Metro network and JR Loop Line offer seamless coverage.",
            "food_info": [
                {
                    "name": "Takoyaki",
                    "desc": "Battered octopus balls topped with sauce and bonito flakes.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Okonomiyaki",
                    "desc": "Savory cabbage pancake cooked on an iron griddle.",
                    "type": "Non-Veg/Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Osaka Castle",
                    "desc": "A majestic historic castle surrounded by parks and moats.",
                    "rating": "4.6 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Dotonbori",
                    "desc": "Neon-lit canal street famous for restaurants and bars.",
                    "rating": "4.7 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Ritz-Carlton Osaka",
                    "desc": "Classic European-style luxury hotel.",
                    "price": "¥65,000+ per night",
                },
                "mid_range": {
                    "name": "Swissotel Nankai Osaka",
                    "desc": "Directly above Namba Station, great city views.",
                    "price": "¥30,000 per night",
                },
                "budget": {
                    "name": "Hotel Nikko Osaka",
                    "desc": "Value hotel right opposite Shinsaibashi arcade.",
                    "price": "¥14,000 per night",
                },
            },
            "shopping_areas": [
                {"name": "Shinsaibashi-suji", "desc": "A covered shopping avenue stretching over 600 meters."},
                {
                    "name": "Kuromon Ichiba Market",
                    "desc": "Lively food market famous for fresh seafood and wagyu beef.",
                },
            ],
            "airport_details": "Kansai International Airport (KIX) is built on an artificial island in the bay.",
            "safety_recommendations": "Stand on the right side of escalators in Osaka, unlike Tokyo!",
        },
        # 3. Kyoto
        {
            "city_name": "Kyoto",
            "description": "The cultural heart of Japan, featuring thousands of Buddhist temples, gardens, and shrines.",
            "transport_info": "Best navigated via Kyoto City Buses, subways, and bicycles.",
            "food_info": [
                {
                    "name": "Kaiseki Ryori",
                    "desc": "Multi-course traditional dinner displaying seasonal aesthetics.",
                    "type": "Veg/Non-Veg",
                },
                {"name": "Yudofu", "desc": "Simmered tofu cooked in kelp broth, popular at temples.", "type": "Veg"},
            ],
            "tourist_places": [
                {
                    "name": "Fushimi Inari Shrine",
                    "desc": "Path of thousands of vermilion torii gates up Mount Inari.",
                    "rating": "4.9 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Kinkaku-ji (Golden Pavilion)",
                    "desc": "Stunning Zen temple covered in gold leaf on a pond.",
                    "rating": "4.8 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Suiran, Luxury Collection",
                    "desc": "Traditional luxury ryokan-hotel in Arashiyama.",
                    "price": "¥120,000+ per night",
                },
                "mid_range": {
                    "name": "Hotel Granvia Kyoto",
                    "desc": "Premium hotel located directly inside Kyoto Station.",
                    "price": "¥30,000 per night",
                },
                "budget": {
                    "name": "Piece Hostel Kyoto",
                    "desc": "Hip, modern budget hostel with comfortable shared areas.",
                    "price": "¥7,500 per night",
                },
            },
            "shopping_areas": [
                {"name": "Nishiki Market", "desc": "Known as Kyoto's Kitchen, a narrow food market."},
                {"name": "Shijo-dori", "desc": "Kyoto's main high street for souvenirs and crafts."},
            ],
            "airport_details": "Use Osaka's Kansai Airport (KIX); take the JR Haruka Express train directly (75 mins).",
            "safety_recommendations": "Respect Geishas in Gion; do not take unauthorized photos.",
        },
        # 4. Yokohama
        {
            "city_name": "Yokohama",
            "description": "A relaxed harbor city just south of Tokyo, featuring a massive Chinatown and bay views.",
            "transport_info": "Minatomirai Subway Line, JR lines, and sea buses.",
            "food_info": [
                {"name": "Chuka Soba", "desc": "Yokohama-style Chinese noodles in soy sauce broth.", "type": "Non-Veg"},
                {"name": "Gyoza", "desc": "Pan-fried dumplings stuffed with meat and vegetables.", "type": "Non-Veg"},
            ],
            "tourist_places": [
                {
                    "name": "Minato Mirai 21",
                    "desc": "Futuristic seaside district with a landmark tower and ferris wheel.",
                    "rating": "4.6 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Yokohama Chinatown",
                    "desc": "Japan's largest Chinatown, packed with food stalls.",
                    "rating": "4.5 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Yokohama Bay Hotel Tokyu",
                    "desc": "Harborfront luxury hotel near the Ferris wheel.",
                    "price": "¥40,000 per night",
                },
                "mid_range": {
                    "name": "Yokohama Royal Park Hotel",
                    "desc": "Occupies the upper floors of the Landmark Tower.",
                    "price": "¥22,000 per night",
                },
                "budget": {
                    "name": "Hotel Edit Yokohama",
                    "desc": "Trendy, clean budget boutique hotel.",
                    "price": "¥10,000 per night",
                },
            },
            "shopping_areas": [
                {"name": "Motomachi Shopping Street", "desc": "Charming European-style pedestrian shopping street."},
                {
                    "name": "Red Brick Warehouses",
                    "desc": "Historic brick buildings converted into dining and shopping spaces.",
                },
            ],
            "airport_details": "Easily reached via train or bus from Tokyo Haneda Airport (30 mins).",
            "safety_recommendations": "Generally very safe. Enjoy waterfront walks late at night without concern.",
        },
        # 5. Nagoya
        {
            "city_name": "Nagoya",
            "description": "An industrial and automotive hub, home to Nagoya Castle and Toyota museums.",
            "transport_info": "Nagoya Subway lines and Meitetsu trains.",
            "food_info": [
                {
                    "name": "Hitsumabushi",
                    "desc": "Grilled eel served over rice, eaten in three traditional steps.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Miso Katsu",
                    "desc": "Fried pork cutlets served with a thick, sweet red miso sauce.",
                    "type": "Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Nagoya Castle",
                    "desc": "Historic castle famous for golden dolphin roof ornaments.",
                    "rating": "4.4 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "SCMAGLEV & Railway Park",
                    "desc": "Interactive train museum displaying bullet and maglev trains.",
                    "rating": "4.7 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Nagoya Marriott Associa Hotel",
                    "desc": "Luxury hotel located directly above Nagoya station.",
                    "price": "¥35,000 per night",
                },
                "mid_range": {
                    "name": "Nagoya JR Gate Tower Hotel",
                    "desc": "Premium hotel with direct station access.",
                    "price": "¥20,000 per night",
                },
                "budget": {
                    "name": "Unizo Inn Nagoya Sakae",
                    "desc": "Convenient, simple budget business hotel.",
                    "price": "¥7,500 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Osu Shopping District",
                    "desc": "Retro covered street market selling clothes, electronics, and street food.",
                },
                {"name": "Sakae District", "desc": "Nagoya's commercial downtown with department stores."},
            ],
            "airport_details": "Served by Chubu Centrair International Airport (NGO) on an artificial island.",
            "safety_recommendations": "Extremely safe. Pay attention to subway transfer signs at Nagoya station.",
        },
        # 6. Sapporo
        {
            "city_name": "Sapporo",
            "description": "Capital of Hokkaido, famous for its winter snow festival, beer, and dairy.",
            "transport_info": "Sapporo Subway network, streetcars, and JR trains.",
            "food_info": [
                {
                    "name": "Sapporo Miso Ramen",
                    "desc": "Hearty ramen cooked in miso broth topped with sweet corn and butter.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Jingisukan (Genghis Khan)",
                    "desc": "Mutton cooked on a dome-shaped metal skillet, named after the ruler.",
                    "type": "Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Odori Park",
                    "desc": "Broad central park dividing the city, hosting the Snow Festival.",
                    "rating": "4.4 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Sapporo Beer Museum",
                    "desc": "Historic brick museum detailing the history of beer in Japan.",
                    "rating": "4.5 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "JR Tower Hotel Nikko Sapporo",
                    "desc": "Premium skyscraper hotel connected to Sapporo station.",
                    "price": "¥30,000 per night",
                },
                "mid_range": {
                    "name": "Sapporo Grand Hotel",
                    "desc": "Historic upscale hotel with superb buffet dining.",
                    "price": "¥15,000 per night",
                },
                "budget": {
                    "name": "The Stay Sapporo",
                    "desc": "Comfortable budget hostel with cozy social spaces.",
                    "price": "¥5,000 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Tanukikoji Shopping Arcade",
                    "desc": "A covered shopping street packed with restaurants and drugstores.",
                },
                {"name": "Sapporo Factory", "desc": "Large shopping mall built inside a former brick brewery."},
            ],
            "airport_details": "New Chitose Airport (CTS) handles domestic and international flights.",
            "safety_recommendations": "Watch your step in winter as city sidewalks can become extremely icy.",
        },
        # 7. Fukuoka
        {
            "city_name": "Fukuoka",
            "description": "Kyushu's largest city, famous for outdoor food stalls (Yatai) and Hakata ramen.",
            "transport_info": "Fukuoka City Subway lines and Nishitetsu railways.",
            "food_info": [
                {
                    "name": "Hakata Tonkotsu Ramen",
                    "desc": "Ramen in a creamy pork bone broth with thin noodles.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Motsunabe",
                    "desc": "A rich hotpot stew cooked with beef offal, cabbage, and chives.",
                    "type": "Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Ohori Park",
                    "desc": "Beautiful central park featuring a massive lake and walking paths.",
                    "rating": "4.6 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Canal City Hakata",
                    "desc": "Huge entertainment and shopping complex built around a canal.",
                    "rating": "4.4 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Grand Hyatt Fukuoka",
                    "desc": "Luxury hotel integrated directly inside Canal City.",
                    "price": "¥38,000 per night",
                },
                "mid_range": {
                    "name": "Miyako Hotel Hakata",
                    "desc": "Stylish premium hotel located opposite Hakata Station.",
                    "price": "¥22,000 per night",
                },
                "budget": {
                    "name": "Fukuoka Hana Hostel",
                    "desc": "Friendly budget hostel situated near Nakasu nightlife.",
                    "price": "¥6,000 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Tenjin Underground Mall",
                    "desc": "Huge underground shopping avenue styled like 19th-century Europe.",
                },
                {
                    "name": "Hakata Station City",
                    "desc": "Massive shopping department store complex atop the railway station.",
                },
            ],
            "airport_details": "Fukuoka Airport (FUK) is incredibly close to the city (only 10 mins by subway).",
            "safety_recommendations": "Generally very safe. Observe normal safety practices in nightlife zones like Nakasu.",
        },
        # 8. Kobe
        {
            "city_name": "Kobe",
            "description": "A scenic port city tucked between the mountains and sea, famous for marbled Kobe Beef.",
            "transport_info": "Kobe Subway lines, Port Liner monorail, and Mount Rokko cable cars.",
            "food_info": [
                {
                    "name": "Kobe Beef",
                    "desc": "Highly marbleized premium beef cooked on a teppanyaki grill.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Akashiyaki",
                    "desc": "Soft egg-batter octopus dumplings dipped in light dashi broth.",
                    "type": "Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Kobe Harborland",
                    "desc": "Seaside shopping and dining district along the harbor.",
                    "rating": "4.5 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Mount Rokko",
                    "desc": "Mountain range offering stunning panoramic night views of the harbor.",
                    "rating": "4.7 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Oriental Hotel Kobe",
                    "desc": "Historic premium luxury hotel overlooking the port.",
                    "price": "¥40,000 per night",
                },
                "mid_range": {
                    "name": "Kobe Portopia Hotel",
                    "desc": "Large hotel located on Port Island with sea vistas.",
                    "price": "¥18,000 per night",
                },
                "budget": {
                    "name": "Hotel 1-2-3 Kobe",
                    "desc": "Clean and practical budget business hotel.",
                    "price": "¥8,000 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Sannomiya Center Plaza",
                    "desc": "Covered shopping arcade packed with boutiques and manga shops.",
                },
                {"name": "Nankinmachi (Chinatown)", "desc": "Lively tourist district selling steamed buns and snacks."},
            ],
            "airport_details": "Kobe Airport (UKB) is on a reclamation island; most tourists arrive via Shinkansen.",
            "safety_recommendations": "Very safe. Mount Rokko weather can change quickly, carry a light jacket.",
        },
        # 9. Hiroshima
        {
            "city_name": "Hiroshima",
            "description": "A city of peace and recovery, famous for its Peace Park and floating shrine gate.",
            "transport_info": "Hiroshima Electric Railway streetcars (trams) cover the city.",
            "food_info": [
                {
                    "name": "Hiroshima Okonomiyaki",
                    "desc": "Savory pancake layered with cabbage, noodles, pork, and egg.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Oysters (Kaki)",
                    "desc": "Fresh local oysters served grilled, raw, or deep-fried.",
                    "type": "Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Hiroshima Peace Memorial Park",
                    "desc": "Moving park dedicated to peace, featuring the Genbaku Dome.",
                    "rating": "4.8 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Itsukushima Shrine (Miyajima)",
                    "desc": "Famous Shinto shrine with a giant torii gate that floats at high tide.",
                    "rating": "4.9 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Sheraton Grand Hiroshima Hotel",
                    "desc": "Luxury hotel located next to Hiroshima station.",
                    "price": "¥30,000 per night",
                },
                "mid_range": {
                    "name": "Rihga Royal Hotel Hiroshima",
                    "desc": "Large upscale hotel situated next to Hiroshima Castle.",
                    "price": "¥16,000 per night",
                },
                "budget": {
                    "name": "Santiago Guesthouse Hiroshima",
                    "desc": "Fun backpacker budget hostel in the shopping arcade.",
                    "price": "¥5,000 per night",
                },
            },
            "shopping_areas": [
                {"name": "Hondori Street", "desc": "Pedestrian covered shopping arcade packed with stores and cafes."},
                {
                    "name": "Miyajima Omotesando Shopping Street",
                    "desc": "Famed street on the island selling wooden crafts and snacks.",
                },
            ],
            "airport_details": "Hiroshima Airport (HIJ) has flights; many travel via JR Sanyo Shinkansen bullet trains.",
            "safety_recommendations": "Be respectful when visiting peace monuments and taking photos.",
        },
        # 10. Nara
        {
            "city_name": "Nara",
            "description": "Japan's first permanent capital, famous for historic temples and free-roaming deer.",
            "transport_info": "Extremely walkable city. Local loop buses and rent-a-bicycles are available.",
            "food_info": [
                {
                    "name": "Kaki no Ha Sushi",
                    "desc": "Traditional sushi wrapped in persimmon leaves, popular in Nara.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Miwa Somin",
                    "desc": "Very thin wheat noodles served cold or hot in light broth.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Nara Park",
                    "desc": "Scenic park where hundreds of bowing deer roam freely.",
                    "rating": "4.8 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Todai-ji Temple",
                    "desc": "Historic temple housing one of Japan's largest bronze Buddha statues.",
                    "rating": "4.9 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Nara Hotel",
                    "desc": "Historic luxury hotel built in 1909 with palace-style architecture.",
                    "price": "¥40,000 per night",
                },
                "mid_range": {
                    "name": "Piazza Hotel Nara",
                    "desc": "Modern hotel located right outside JR Nara station.",
                    "price": "¥15,000 per night",
                },
                "budget": {
                    "name": "Oak Hostel Nara",
                    "desc": "Clean and budget-friendly hostel close to Nara Park.",
                    "price": "¥6,500 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Higashimuki Shopping Street",
                    "desc": "Covered arcade filled with souvenir shops and local cafes.",
                },
                {"name": "Sanjo-dori", "desc": "Main street leading from station to Nara Park with traditional shops."},
            ],
            "airport_details": "No airport; easily visited via JR/Kintetsu trains from Kyoto or Osaka (45 mins).",
            "safety_recommendations": "Deer are wild; feed them only official Shika-senbei crackers and do not tease them.",
        },
        # 11. Okinawa
        {
            "city_name": "Okinawa",
            "description": "A sub-tropical island paradise in the south, boasting coral reefs, beaches, and Ryukyu culture.",
            "transport_info": "Yui Rail monorail in Naha; renting a car is highly recommended for exploring the island.",
            "food_info": [
                {
                    "name": "Okinawa Soba",
                    "desc": "Wheat noodles served in pork broth, topped with sweet stewed pork belly.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Goya Champuru",
                    "desc": "Okinawan bitter melon stir-fry cooked with tofu, egg, and pork.",
                    "type": "Non-Veg/Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Shurijo Castle",
                    "desc": "Historic Ryukyu Kingdom palace displaying vibrant red architecture.",
                    "rating": "4.5 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Okinawa Churaumi Aquarium",
                    "desc": "World-class aquarium featuring massive whale sharks.",
                    "rating": "4.8 ⭐",
                    "time": "Full Day",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Terrace Club At Busena",
                    "desc": "High-end luxury beachfront resort in Nago.",
                    "price": "¥70,000+ per night",
                },
                "mid_range": {
                    "name": "Hyatt Regency Naha Okinawa",
                    "desc": "Stylish premium hotel located near Kokusai Street.",
                    "price": "¥22,000 per night",
                },
                "budget": {
                    "name": "Abest Cube Naha Kokusai Street",
                    "desc": "Smart value cabin hotel located in central Naha.",
                    "price": "¥8,000 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Kokusai Dori (International Street)",
                    "desc": "Main shopping street in Naha, packed with souvenir stores and bars.",
                },
                {
                    "name": "Makishi Public Market",
                    "desc": "Known as Naha's Kitchen, selling fresh fish and Okinawan ingredients.",
                },
            ],
            "airport_details": "Naha Airport (OKA) handles domestic flights and regional Asian routes.",
            "safety_recommendations": "Take caution against strong sun rays; wear sunscreen. Swim only in designated beach zones.",
        },
        # 12. Kanazawa
        {
            "city_name": "Kanazawa",
            "description": "A historic town famous for gold leaf crafts, geisha districts, and one of Japan's top landscape gardens.",
            "transport_info": "Kanazawa Loop Bus operates routes linking all major attractions.",
            "food_info": [
                {
                    "name": "Jibuni",
                    "desc": "Kyoto-style duck stew cooked with wheat gluten and seasonal vegetables.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Gold Leaf Ice Cream",
                    "desc": "Matcha soft-serve ice cream wrapped in a real sheet of edible gold leaf.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Kenroku-en Garden",
                    "desc": "Famed landscape garden considered one of the three great gardens of Japan.",
                    "rating": "4.8 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Higashi Chaya District",
                    "desc": "Historic district featuring preserved wooden geisha teahouses.",
                    "rating": "4.6 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Kanazawa Tokyu Hotel",
                    "desc": "Upscale luxury hotel situated in the downtown Korinbo district.",
                    "price": "¥24,000 per night",
                },
                "mid_range": {
                    "name": "Hotel Intergate Kanazawa",
                    "desc": "Premium hotel offering local craft experiences and workshops.",
                    "price": "¥14,000 per night",
                },
                "budget": {
                    "name": "Ksha Guesthouse Kanazawa",
                    "desc": "Charming, traditional budget guesthouse near the castle.",
                    "price": "¥6,000 per night",
                },
            },
            "shopping_areas": [
                {"name": "Omicho Market", "desc": "Bustling fresh food market famous for sea urchin and snow crab."},
                {
                    "name": "Korinbo District",
                    "desc": "Modern shopping hub featuring global boutiques and department stores.",
                },
            ],
            "airport_details": "Served by Komatsu Airport (KMQ); connected via 40-minute bus route to Kanazawa.",
            "safety_recommendations": "Very safe. Carry an umbrella as Kanazawa is known for its frequent rains.",
        },
        # 13. Hakodate
        {
            "city_name": "Hakodate",
            "description": "A scenic port city in southern Hokkaido, famous for fresh seafood and night vistas.",
            "transport_info": "Hakodate City Tram and local buses.",
            "food_info": [
                {
                    "name": "Hakodate Shio Ramen",
                    "desc": "Ramen in a light, clear salt-based broth topped with sliced pork.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Lucky Pierrot Burger",
                    "desc": "Unique local burger chain famous for sweet chili chicken burgers.",
                    "type": "Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Mount Hakodate Observatory",
                    "desc": "Ropeway leading to views of the illuminated city curves.",
                    "rating": "4.8 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Goryokaku Fort",
                    "desc": "A spectacular star-shaped Western citadel converted into a park.",
                    "rating": "4.7 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "La Vista Hakodate Bay",
                    "desc": "Premium hotel famous for its award-winning seafood breakfast buffet.",
                    "price": "¥28,000 per night",
                },
                "mid_range": {
                    "name": "Hakodate Kokusai Hotel",
                    "desc": "Centrally located harborfront hotel with hot spring baths.",
                    "price": "¥16,000 per night",
                },
                "budget": {
                    "name": "HakoBA Hakodate",
                    "desc": "Stylish hostel converted from a historic bank building.",
                    "price": "¥7,000 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Hakodate Morning Market",
                    "desc": "Famous market selling fresh crabs, melons, and squid fishing booths.",
                },
                {
                    "name": "Kanemori Red Brick Warehouses",
                    "desc": "Seaside red-brick buildings converted into shopping complexes.",
                },
            ],
            "airport_details": "Hakodate Airport (HKD) is located 20 minutes by shuttle bus from the station.",
            "safety_recommendations": "Extremely safe. Wrap up warm as coastal winds can feel very cold.",
        },
        # 14. Nagasaki
        {
            "city_name": "Nagasaki",
            "description": "A historic port city built on steep hills, reflecting centuries of Chinese and Dutch influence.",
            "transport_info": "Nagasaki Electric Tramway (streetcars) and local buses.",
            "food_info": [
                {
                    "name": "Nagasaki Champon",
                    "desc": "Rich pork broth soup filled with thick noodles, pork, seafood, and cabbage.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Castella Cake",
                    "desc": "A sweet sponge cake brought to Japan by Portuguese merchants in the 16th century.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Glover Garden",
                    "desc": "Open-air museum showcasing historic Western mansions on a hill.",
                    "rating": "4.5 ⭐",
                    "time": "Afternoon",
                },
                {
                    "name": "Nagasaki Peace Park",
                    "desc": "Moving memorial park dedicated to the atomic bomb victims.",
                    "rating": "4.7 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Garden Terrace Nagasaki Hotel",
                    "desc": "Stunning luxury hotel designed by Kengo Kuma.",
                    "price": "¥45,000 per night",
                },
                "mid_range": {
                    "name": "Hotel New Nagasaki",
                    "desc": "Premium hotel located right next to JR Nagasaki Station.",
                    "price": "¥18,000 per night",
                },
                "budget": {
                    "name": "Casa Blanca Guesthouse",
                    "desc": "Friendly, cozy budget hostel near Chinatown.",
                    "price": "¥6,000 per night",
                },
            },
            "shopping_areas": [
                {"name": "Nagasaki Chinatown", "desc": "Japan's oldest Chinatown, famous for street food stalls."},
                {"name": "Hamanmachi Arcade", "desc": "Bustling covered shopping street with department stores."},
            ],
            "airport_details": "Nagasaki Airport (NGS) is built on an island in Omura Bay.",
            "safety_recommendations": "Be prepared for steep hill walks and steps when visiting historical districts.",
        },
        # 15. Sendai
        {
            "city_name": "Sendai",
            "description": "The City of Trees and capital of Tohoku, famous for historic castles and gyutan.",
            "transport_info": "Sendai Subway network, Loople Sendai tourist bus, and JR trains.",
            "food_info": [
                {
                    "name": "Gyutan",
                    "desc": "Thinly sliced beef tongue grilled over charcoal, a Sendai specialty.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Zunda Mochi",
                    "desc": "Sweet rice cakes covered in a paste of sweetened crushed edamame.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Sendai Castle Ruins",
                    "desc": "Hilltop castle ruins offering views of Sendai and the Masamune statue.",
                    "rating": "4.4 ⭐",
                    "time": "Afternoon",
                },
                {
                    "name": "Zuihoden Mausoleum",
                    "desc": "Colorful, ornate mausoleum of Date Masamune, the founder of Sendai.",
                    "rating": "4.6 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Westin Sendai",
                    "desc": "Luxury high-rise hotel occupying upper floors of Sendai Trust Tower.",
                    "price": "¥35,000 per night",
                },
                "mid_range": {
                    "name": "Metropolitan Sendai East",
                    "desc": "Stylish premium hotel connected directly to Sendai station.",
                    "price": "¥18,000 per night",
                },
                "budget": {
                    "name": "Nine Hours Sendai",
                    "desc": "Futuristic design capsule hotel offering basic sleeping units.",
                    "price": "¥5,500 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Clis Road Shopping Arcade",
                    "desc": "Vibrant covered pedestrian street lined with retail outlets.",
                },
                {"name": "Aoba-dori", "desc": "Broad, tree-lined avenue featuring major department stores."},
            ],
            "airport_details": "Sendai Airport (SDJ) is connected to Sendai Station via the airport access line (25 mins).",
            "safety_recommendations": "Extremely safe. Pay attention to evacuation signage as Tohoku is seismically active.",
        },
        # 16. Takayama
        {
            "city_name": "Takayama",
            "description": "A beautifully preserved town in the Gifu Alps, famous for wooden merchant houses and festivals.",
            "transport_info": "Best explored on foot. Local Nohi buses serve outlying historic villages.",
            "food_info": [
                {
                    "name": "Hida Beef Bun",
                    "desc": "Steamed hot bun stuffed with savory marinated Hida beef.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Hoba Miso",
                    "desc": "Sweet miso paste mixed with mushrooms and vegetables, roasted on a magnolia leaf.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Takayama Old Town",
                    "desc": "Preserved streets lined with dark wooden merchant houses.",
                    "rating": "4.8 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Hida Folk Village",
                    "desc": "Open-air museum showcasing traditional steep thatched-roof houses.",
                    "rating": "4.7 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Wanosato",
                    "desc": "A traditional luxury ryokan with thatched roof and open hearth.",
                    "price": "¥70,000+ per night",
                },
                "mid_range": {
                    "name": "Takayama Ouan",
                    "desc": "Modern hotel designed with traditional tatami mats and hot springs.",
                    "price": "¥22,000 per night",
                },
                "budget": {
                    "name": "K's House Takayama",
                    "desc": "Award-winning cozy hostel located close to Takayama station.",
                    "price": "¥6,000 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Miyagawa Morning Market",
                    "desc": "Morning market stalls selling local fruits, vegetables, and crafts.",
                },
                {
                    "name": "Sanmachi Suji shops",
                    "desc": "Historic streets packed with sake breweries and wooden crafts.",
                },
            ],
            "airport_details": "No airport; easily reached via JR Hida Express train from Nagoya (2.5 hours).",
            "safety_recommendations": "Shops in Takayama close very early (usually by 5 PM); plan dining ahead.",
        },
        # 17. Himeji
        {
            "city_name": "Himeji",
            "description": "Famous for Himeji Castle, Japan's most spectacular and original samurai castle.",
            "transport_info": "Easily walkable; tourist buses connect the station and the castle grounds.",
            "food_info": [
                {
                    "name": "Himeji Oden",
                    "desc": "Simmered fishcakes and vegetables served with a unique ginger soy sauce.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Anago (Sea Eel)",
                    "desc": "Sweet, grilled sea eel served over rice bowls.",
                    "type": "Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Himeji Castle",
                    "desc": "The majestic 'White Heron Castle', a national treasure and UNESCO site.",
                    "rating": "4.9 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Koko-en Garden",
                    "desc": "A beautiful complex of nine traditional Japanese landscape gardens.",
                    "rating": "4.7 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Hotel Nikko Himeji",
                    "desc": "Upscale premium hotel located directly opposite Himeji station.",
                    "price": "¥18,000 per night",
                },
                "mid_range": {
                    "name": "Daiwa Roynet Hotel Himeji",
                    "desc": "Modern and comfortable hotel popular with travelers.",
                    "price": "¥12,000 per night",
                },
                "budget": {
                    "name": "Himeji 58 Hostel",
                    "desc": "Simple, cozy guest house close to the castle gates.",
                    "price": "¥5,000 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Miyuki-dori Shopping Street",
                    "desc": "Covered shopping arcade linking the station and Himeji Castle.",
                },
                {
                    "name": "Piole Himeji Mall",
                    "desc": "Modern fashion and dining mall built directly inside Himeji Station.",
                },
            ],
            "airport_details": "No airport; reach via JR Sanyo Shinkansen (1 hour from Kyoto/Osaka).",
            "safety_recommendations": "Generally very safe. Climbing Himeji Castle's top levels requires scaling steep wooden stairs.",
        },
        # 18. Kamakura
        {
            "city_name": "Kamakura",
            "description": "A historic seaside town south of Tokyo, famous for temples and a giant outdoor bronze Buddha.",
            "transport_info": "Kamakura trains, Enoden vintage tramway, and walking paths.",
            "food_info": [
                {
                    "name": "Shirasu Don",
                    "desc": "Rice bowl topped with fresh raw or boiled tiny white bait fish.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Hato Sabure",
                    "desc": "Famous dove-shaped sweet butter cookies native to Kamakura.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Kotoku-in (Great Buddha)",
                    "desc": "A massive outdoor bronze statue of Amida Buddha dating to 1252.",
                    "rating": "4.7 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Hase-dera Temple",
                    "desc": "Hilltop temple dedicated to Kannon, offering ocean views and hydrangea gardens.",
                    "rating": "4.6 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Kamakura Prince Hotel",
                    "desc": "Oceanfront luxury hotel offering views of Enoshima and Fuji.",
                    "price": "¥35,000 per night",
                },
                "mid_range": {
                    "name": "Hotel Metropolitan Kamakura",
                    "desc": "Centrally located premium hotel near Kamakura Station.",
                    "price": "¥22,000 per night",
                },
                "budget": {
                    "name": "WeBase Kamakura Hostel",
                    "desc": "Stylish beachside budget hostel with a yoga studio.",
                    "price": "¥7,500 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Komachi-dori",
                    "desc": "Busy shopping street packed with trendy cafes, boutiques, and street food stalls.",
                },
                {
                    "name": "Hase Station Street",
                    "desc": "Traditional lane leading to temples, selling local woodcrafts and sweets.",
                },
            ],
            "airport_details": "Access via JR train lines from Tokyo (1 hour) or Haneda Airport.",
            "safety_recommendations": "Watch out for black kites (birds of prey) that may snatch food right out of your hand.",
        },
        # 19. Nikko
        {
            "city_name": "Nikko",
            "description": "A mountain town famous for Nikko Toshogu, Japan's most lavishly decorated Shinto shrine.",
            "transport_info": "Nikko World Heritage buses, local Tobu trains, and hiking paths.",
            "food_info": [
                {
                    "name": "Yuba",
                    "desc": "Tofu skin delicacy prepared in soups, fried rolls, or raw sashimi style.",
                    "type": "Veg",
                },
                {
                    "name": "Nikko Soba",
                    "desc": "Fresh handmade buckwheat noodles served in local mountain spring water.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Toshogu Shrine",
                    "desc": "Ornate, gold-leaf decorated shrine holding the mausoleum of Tokugawa Ieyasu.",
                    "rating": "4.9 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Kegon Falls",
                    "desc": "A spectacular 97-meter-high waterfall draining Lake Chuzenji.",
                    "rating": "4.7 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Ritz-Carlton Nikko",
                    "desc": "High-end luxury resort overlooking Lake Chuzenji.",
                    "price": "¥90,000+ per night",
                },
                "mid_range": {
                    "name": "Nikko Kanaya Hotel",
                    "desc": "Japan's oldest resort hotel, blending Western and Japanese designs.",
                    "price": "¥26,000 per night",
                },
                "budget": {
                    "name": "Nikko Park Lodge",
                    "desc": "Cozy, pine-wood budget lodge near the train station.",
                    "price": "¥9,500 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Nikko Kaido shopping street",
                    "desc": "Scenic road leading to shrines, lined with wooden craft shops and Yuba cafes.",
                },
                {
                    "name": "Chuzenji Lakeside souvenir shops",
                    "desc": "Shops selling local wood engravings and mountain honey.",
                },
            ],
            "airport_details": "Reach via Tobu Spacia Express trains from Tokyo's Asakusa station (2 hours).",
            "safety_recommendations": "Nikko can be cold and damp due to mountains; carry layers. Temple grounds have loose pebbles.",
        },
        # 20. Matsumoto
        {
            "city_name": "Matsumoto",
            "description": "A gateway to the Northern Alps, famous for Matsumoto Castle, one of Japan's original castles.",
            "transport_info": "Matsumoto Town Sneaker loop buses and local trains.",
            "food_info": [
                {
                    "name": "Sanzoku-yaki",
                    "desc": "Deep-fried garlic and onion soy-sauce marinated chicken cutlet.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Shinshu Soba",
                    "desc": "Highly regarded Nagano buckwheat noodles served cold with dipping sauce.",
                    "type": "Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Matsumoto Castle",
                    "desc": "The historic 'Crow Castle', featuring a unique black-and-white wooden keep.",
                    "rating": "4.8 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Nawate-dori (Frog Street)",
                    "desc": "Charming pedestrian shopping lane themed around frogs, offering street food.",
                    "rating": "4.5 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Myojinkan",
                    "desc": "Luxury hot spring ryokan nestled in the mountains outside town.",
                    "price": "¥60,000+ per night",
                },
                "mid_range": {
                    "name": "Matsumoto Hotel Kagetsu",
                    "desc": "Charming, historic hotel featuring local wooden furniture.",
                    "price": "¥18,000 per night",
                },
                "budget": {
                    "name": "Ace Inn Matsumoto",
                    "desc": "Simple, clean budget business hotel right next to the station.",
                    "price": "¥8,500 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Nakamachi-dori",
                    "desc": "Historic street lined with traditional merchant storehouses (kura) selling crafts.",
                },
                {
                    "name": "Matsumoto Station shopping mall",
                    "desc": "Modern mall selling regional sake, crafts, and wasabi snacks.",
                },
            ],
            "airport_details": "Shinshu Matsumoto Airport (MMJ) has limited domestic flights; reach via JR Shinano trains.",
            "safety_recommendations": "Generally very safe. Keep cash handy as some traditional craft shops don't accept cards.",
        },
    ]

    for city in japan_cities:
        cursor.execute(
            """
        INSERT INTO cities (
            country_id, city_name, description, transport_info, food_info, tourist_places, hotel_info, shopping_areas, airport_details, safety_recommendations
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """,
            (
                japan_id,
                city["city_name"],
                city["description"],
                city["transport_info"],
                json.dumps(city["food_info"]),
                json.dumps(city["tourist_places"]),
                json.dumps(city["hotel_info"]),
                json.dumps(city["shopping_areas"]),
                city["airport_details"],
                city["safety_recommendations"],
            ),
        )

    # -------------------------------------------------------------
    # 3. SINGAPORE
    # -------------------------------------------------------------
    # Since Singapore is a city-state, we split it into 20 distinct tourist
    # planning areas and neighborhoods, styled as destinations in the app.
    singapore_data = {
        "country_name": "Singapore",
        "capital": "Singapore",
        "currency": "Singapore Dollar (SGD, S$)",
        "language": "English, Malay, Mandarin, Tamil",
        "timezone": "SGT (UTC+8)",
        "emergency_number": "999 (Police), 995 (Ambulance & Fire)",
        "visa_info": "Visitors must complete the online SG Arrival Card within 3 days before entry. Citizens from many Western, Asian, and ASEAN nations receive visa-free entry. Passport validity must be at least 6 months.",
        "rules": "1. No chewing gum import or sale; chewing gum in public can result in fines.\n2. Littering, spitting, and jaywalking are strictly enforced with high fines.\n3. Smoking is only allowed in designated outdoor zones.\n4. Eating or drinking is strictly prohibited on MRT trains and in stations.\n5. Connecting to unsecured public Wi-Fi without permission can be considered hacking.",
        "etiquette": "1. Keep left on escalators and let others pass on the right.\n2. Choping: locals reserve tables at hawker centres using tissue packets or umbrellas. Do not sit at a table with a tissue pack on it.\n3. Clear your food trays at food courts and hawker centers (mandatory by law).\n4. Pointing with your index finger is considered impolite; use your whole hand instead.",
        "safety_tips": "1. Singapore is one of the safest cities in the world. It is safe to walk alone at night.\n2. Drinkable tap water: tap water is safe and clean.\n3. Respect local religious temples: dress modestly, remove shoes, and do not take photos inside unless permitted.",
    }

    cursor.execute(
        """
    INSERT INTO countries (
        country_name, capital, currency, language, timezone, emergency_number, visa_info, rules, etiquette, safety_tips
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """,
        (
            singapore_data["country_name"],
            singapore_data["capital"],
            singapore_data["currency"],
            singapore_data["language"],
            singapore_data["timezone"],
            singapore_data["emergency_number"],
            singapore_data["visa_info"],
            singapore_data["rules"],
            singapore_data["etiquette"],
            singapore_data["safety_tips"],
        ),
    )
    singapore_id = cursor.lastrowid

    singapore_areas = [
        # 1. Downtown Core
        {
            "city_name": "Downtown Core",
            "description": "Singapore's central financial district, packed with towering skyscrapers and colonial historical sites.",
            "transport_info": "Served heavily by Raffles Place and City Hall MRT stations.",
            "food_info": [
                {
                    "name": "Hainanese Chicken Rice",
                    "desc": "Fragrant rice cooked in chicken broth, served with tender chicken.",
                    "type": "Non-Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Merlion Park",
                    "desc": "Famous waterfront park featuring the iconic half-fish, half-lion statue spitting water.",
                    "rating": "4.6 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "National Gallery Singapore",
                    "desc": "Grand museum of Southeast Asian art inside the former City Hall.",
                    "rating": "4.7 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Fullerton Hotel Singapore",
                    "desc": "Historic 5-star hotel built in a neoclassical post office.",
                    "price": "S$550 per night",
                },
                "mid_range": {
                    "name": "Carlton Hotel",
                    "desc": "Modern upscale hotel offering city views near MRT.",
                    "price": "S$250 per night",
                },
                "budget": {
                    "name": "Heritage Hostel",
                    "desc": "Clean and simple dorm beds near the commercial offices.",
                    "price": "S$60 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Raffles City Shopping Centre",
                    "desc": "Large retail complex featuring designer boutiques and dining.",
                },
                {"name": "Marina Square Mall", "desc": "Spacious retail mall containing major stores."},
            ],
            "airport_details": "Connected directly to Changi Airport (SIN) via East-West MRT Line (40 mins).",
            "safety_recommendations": "Extremely safe. Stay clear of designated smoking zones in public plazas.",
        },
        # 2. Marina Bay
        {
            "city_name": "Marina Bay",
            "description": "Futuristic waterfront district celebrated for high-tech gardens and iconic hotel resorts.",
            "transport_info": "Bayfront MRT station connects you directly to all attractions.",
            "food_info": [
                {
                    "name": "Chilli Crab",
                    "desc": "Crab cooked in a sweet, savory, and spicy tomato-egg gravy.",
                    "type": "Non-Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Gardens by the Bay",
                    "desc": "A futuristic park featuring giant metal Supertrees and flower domes.",
                    "rating": "4.8 ⭐",
                    "time": "Afternoon",
                },
                {
                    "name": "Marina Bay Sands",
                    "desc": "Iconic resort building containing the Observation Deck and infinity pool.",
                    "rating": "4.8 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Marina Bay Sands Hotel",
                    "desc": "World-famous hotel featuring the rooftop infinity pool.",
                    "price": "S$850 per night",
                },
                "mid_range": {
                    "name": "Marina Mandarin",
                    "desc": "Premium hotel with a giant central atrium and city views.",
                    "price": "S$350 per night",
                },
                "budget": {
                    "name": "Pod @ Beach Road",
                    "desc": "Clean boutique capsule hotel located nearby.",
                    "price": "S$80 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "The Shoppes at Marina Bay Sands",
                    "desc": "Luxury shopping center featuring canals with gondolas.",
                },
                {"name": "Suntec City", "desc": "Large mall containing the famous Fountain of Wealth."},
            ],
            "airport_details": "Access via Downtown MRT line directly from Changi Airport.",
            "safety_recommendations": "Drinkable tap water. Secure reservations for Gardens by the Bay domes online.",
        },
        # 3. Orchard Road
        {
            "city_name": "Orchard Road",
            "description": "Singapore's premier retail boulevard, lined with dozens of mega shopping malls.",
            "transport_info": "Served by Orchard, Somerset, and Dhoby Ghaut MRT stations.",
            "food_info": [
                {
                    "name": "Orchard Road Ice Cream Sandwich",
                    "desc": "A slice of ice cream wrapped in colorful sweet bread, sold by street uncles.",
                    "type": "Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Emerald Hill",
                    "desc": "Historic neighborhood featuring colorful, restored Chinese Baroque terrace houses.",
                    "rating": "4.5 ⭐",
                    "time": "Afternoon",
                },
                {
                    "name": "Istana Heritage Gallery",
                    "desc": "Exhibition details the history of Singapore's Presidential Palace.",
                    "rating": "4.3 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Ritz-Carlton Millenia",
                    "desc": "Top-tier hotel famous for hexagonal bathroom windows and art collections.",
                    "price": "S$650 per night",
                },
                "mid_range": {
                    "name": "Orchard Rendezvous Hotel",
                    "desc": "Premium family-friendly hotel on the shopping strip.",
                    "price": "S$220 per night",
                },
                "budget": {
                    "name": "YOTEL Orchard Road",
                    "desc": "Smart cabin-style rooms featuring robotic room service.",
                    "price": "S$150 per night",
                },
            },
            "shopping_areas": [
                {"name": "ION Orchard Mall", "desc": "Futuristic design mega-mall filled with designer boutiques."},
                {"name": "Ngee Ann City (Takashimaya)", "desc": "Huge Japanese department store and bookshop complex."},
            ],
            "airport_details": "Easily reached via taxi from Changi Airport (20-25 mins).",
            "safety_recommendations": "No chewing gum sale on Orchard road. Walk on designated pedestrian walkways.",
        },
        # 4. Chinatown
        {
            "city_name": "Chinatown",
            "description": "A vibrant historic enclave blending traditional shophouses, markets, and temples.",
            "transport_info": "Chinatown and Maxwell MRT stations connect to major sights.",
            "food_info": [
                {
                    "name": "Bak Kut Teh",
                    "desc": "A peppery, pork rib soup simmered with garlic and herbs.",
                    "type": "Non-Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Buddha Tooth Relic Temple",
                    "desc": "A spectacular five-story Tang-style Buddhist temple.",
                    "rating": "4.7 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Sri Mariamman Temple",
                    "desc": "Singapore's oldest Dravidian Hindu temple, featuring colorful tower sculptures.",
                    "rating": "4.6 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Amara Singapore",
                    "desc": "Stylish luxury hotel located near Tanjong Pagar.",
                    "price": "S$380 per night",
                },
                "mid_range": {
                    "name": "Hotel Mono",
                    "desc": "Minimalist black-and-white design hotel inside historic shophouses.",
                    "price": "S$160 per night",
                },
                "budget": {
                    "name": "Chinatown CUBE Boutique Capsule Hotel",
                    "desc": "Comfortable, modern capsule hotel.",
                    "price": "S$65 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Chinatown Street Market",
                    "desc": "Pedestrian lanes selling souvenirs, crafts, and street snacks.",
                },
                {
                    "name": "People's Park Complex",
                    "desc": "Retro high-rise commercial center selling herbs and local goods.",
                },
            ],
            "airport_details": "Access via Chinatown MRT station directly linking to terminal lines.",
            "safety_recommendations": "Remove shoes when entering temples. Avoid littering to prevent heavy fines.",
        },
        # 5. Little India
        {
            "city_name": "Little India",
            "description": "A bustling historic district filled with colorful flower garland shops, spices, and temples.",
            "transport_info": "Served by Little India and Farrer Park MRT stations.",
            "food_info": [
                {
                    "name": "Roti Prata",
                    "desc": "Flaky southern Indian flatbread served with lentil or chicken curry.",
                    "type": "Veg/Non-Veg",
                },
                {
                    "name": "Fish Head Curry",
                    "desc": "Spicy Indian-Chinese style curry containing a whole sea bass head.",
                    "type": "Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Sri Veeramakaliamman Temple",
                    "desc": "One of Singapore's oldest Hindu temples, dedicated to Goddess Kali.",
                    "rating": "4.6 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "House of Tan Teng Niah",
                    "desc": "The last surviving colorful Chinese villa in Little India.",
                    "rating": "4.4 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "One Farrer Hotel",
                    "desc": "Modern luxury hotel featuring massive pools and medical suites.",
                    "price": "S$300 per night",
                },
                "mid_range": {
                    "name": "Park Hotel Farrer Park",
                    "desc": "Contemporary loft-style rooms right above MRT.",
                    "price": "S$180 per night",
                },
                "budget": {
                    "name": "Vintage Inn Boutique Capsule Hostel",
                    "desc": "Cozy heritage capsule hostel near temples.",
                    "price": "S$55 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Mustafa Centre",
                    "desc": "Famous 24-hour department store selling everything at budget prices.",
                },
                {
                    "name": "Little India Arcade",
                    "desc": "Covered alleyways selling traditional Indian clothing, sweets, and henna.",
                },
            ],
            "airport_details": "Farrer Park MRT connects directly to the airport train network.",
            "safety_recommendations": "Observe strict liquor ban laws in public areas on weekends.",
        },
        # 6. Sentosa Island
        {
            "city_name": "Sentosa Island",
            "description": "Singapore's premier resort island, packed with beaches, theme parks, and golf courses.",
            "transport_info": "Sentosa Express Monorail, cable cars, or walking via the Sentosa Boardwalk.",
            "food_info": [
                {
                    "name": "Singapore Sling",
                    "desc": "Famous gin-based cherry brandy cocktail served at beach bars.",
                    "type": "Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Universal Studios Singapore (USS)",
                    "desc": "World-class theme park featuring movie-themed rides.",
                    "rating": "4.7 ⭐",
                    "time": "Full Day",
                },
                {
                    "name": "Siloso Beach",
                    "desc": "Sandy beach strip with volleyball courts and beach shacks.",
                    "rating": "4.4 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Capella Singapore",
                    "desc": "Ultra-luxury hotel inside historic manor houses on a hill.",
                    "price": "S$950 per night",
                },
                "mid_range": {
                    "name": "Oasia Resort Sentosa",
                    "desc": "Wellness-themed resort hotel near the monorail station.",
                    "price": "S$280 per night",
                },
                "budget": {
                    "name": "Siloso Beach Resort",
                    "desc": "Eco-friendly beach resort with a natural spring water pool.",
                    "price": "S$160 per night",
                },
            },
            "shopping_areas": [
                {"name": "VivoCity Mall", "desc": "Singapore's largest shopping mall, located at the Sentosa gateway."},
                {
                    "name": "Resorts World Sentosa Galleria",
                    "desc": "Elite shopping avenue featuring luxury international brands.",
                },
            ],
            "airport_details": "Access via taxi (30 mins) or taking the MRT to HarbourFront Station.",
            "safety_recommendations": "Keep hydrated in high humidity. Stay within marked swimming zones.",
        },
        # 7. Katong & Geylang
        {
            "city_name": "Katong & Geylang",
            "description": "Historic Peranakan neighborhood famous for colorful shophouses and spicy laksa.",
            "transport_info": "East Coast road buses and Dakota MRT station.",
            "food_info": [
                {
                    "name": "Katong Laksa",
                    "desc": "Spicy coconut milk noodle soup topped with cockles and fishcakes.",
                    "type": "Non-Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Joo Chiat Peranakan Shophouses",
                    "desc": "Stunning heritage houses with pastel-colored facades.",
                    "rating": "4.6 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Geylang Serai Market",
                    "desc": "Traditional Malay cultural market and food court.",
                    "rating": "4.5 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Grand Mercure Roxy",
                    "desc": "Upscale hotel ideally located close to East Coast Park.",
                    "price": "S$220 per night",
                },
                "mid_range": {
                    "name": "Village Hotel Katong",
                    "desc": "Peranakan-themed rooms near historical restaurants.",
                    "price": "S$160 per night",
                },
                "budget": {
                    "name": "ibis budget Singapore Joo Chiat",
                    "desc": "No-frills clean rooms in the heart of Katong.",
                    "price": "S$90 per night",
                },
            },
            "shopping_areas": [
                {"name": "Katong Square", "desc": "Boutique retail complex featuring heritage Peranakan craft shops."},
                {"name": "i12 Katong Mall", "desc": "Modern family shopping mall containing boutiques and cinemas."},
            ],
            "airport_details": "Very close to Changi Airport; only 15 minutes by taxi.",
            "safety_recommendations": "Generally safe. Geylang is a busy area; stick to main streets at night.",
        },
        # 8. Tampines
        {
            "city_name": "Tampines",
            "description": "A vibrant regional hub in the East, offering a local residential lifestyle experience.",
            "transport_info": "Tampines MRT station, East-West Line and Downtown Line.",
            "food_info": [
                {
                    "name": "Mee Rebus",
                    "desc": "Noodles in a thick, sweet and spicy sweet potato gravy.",
                    "type": "Veg/Non-Veg option",
                }
            ],
            "tourist_places": [
                {
                    "name": "Our Tampines Hub",
                    "desc": "Singapore's largest integrated community and sports center.",
                    "rating": "4.6 ⭐",
                    "time": "Afternoon",
                },
                {
                    "name": "Tampines Eco Green",
                    "desc": "An eco-friendly park featuring hiking trails and bird hides.",
                    "rating": "4.3 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Dusit Thani Laguna Singapore",
                    "desc": "Luxury golf resort hotel located close to Tampines.",
                    "price": "S$320 per night",
                },
                "mid_range": {
                    "name": "Park Avenue Changi",
                    "desc": "Stylish apartment-style hotel close to the Business Park.",
                    "price": "S$190 per night",
                },
                "budget": {
                    "name": "Tampines Lodges",
                    "desc": "Simple value guest rooms catering to business travelers.",
                    "price": "S$100 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Tampines Mall & Century Square",
                    "desc": "Lively shopping hubs surrounding the train station.",
                },
                {
                    "name": "IKEA Tampines",
                    "desc": "Massive retail warehouse popular for home goods and Swedish meatballs.",
                },
            ],
            "airport_details": "Located next to the airport; 10 minutes by taxi or 3 stops on the East-West MRT line.",
            "safety_recommendations": "Very safe. Follow cycling path rules when using local shared bicycles.",
        },
        # 9. Jurong East
        {
            "city_name": "Jurong East",
            "description": "Known as Singapore's second CBD, featuring massive retail malls and science museums.",
            "transport_info": "Jurong East MRT interchange linking East-West and North-South lines.",
            "food_info": [
                {
                    "name": "Satay Bee Hoon",
                    "desc": "Rice vermicelli topped with spicy peanut gravy and seafood.",
                    "type": "Non-Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Science Centre Singapore",
                    "desc": "Interactive science museum featuring Omni-Theatre dome.",
                    "rating": "4.6 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Chinese Garden",
                    "desc": "Scenic park featuring pagodas and stone bridges over Jurong Lake.",
                    "rating": "4.5 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Genting Hotel Jurong",
                    "desc": "Eco-themed premium hotel featuring roof gardens.",
                    "price": "S$220 per night",
                },
                "mid_range": {
                    "name": "Santa Grand Hotel West Coast",
                    "desc": "Comfortable, modern business rooms.",
                    "price": "S$140 per night",
                },
                "budget": {
                    "name": "Jurong Value Stay",
                    "desc": "Simple budget lodging close to transport hubs.",
                    "price": "S$90 per night",
                },
            },
            "shopping_areas": [
                {"name": "Jem & Westgate Malls", "desc": "Mega shopping complexes connected directly to MRT."},
                {
                    "name": "IMM Outlet Mall",
                    "desc": "Singapore's largest outlet mall offering permanent fashion discounts.",
                },
            ],
            "airport_details": "Access via East-West MRT line (55 mins directly to Changi Airport).",
            "safety_recommendations": "Extremely safe. Ensure you watch out for cyclists on pedestrian paths.",
        },
        # 10. Woodlands
        {
            "city_name": "Woodlands",
            "description": "Northern gateway border town facing Malaysia, offering parks and local residential vibes.",
            "transport_info": "Woodlands MRT station, North-South and Thomson-East Coast lines.",
            "food_info": [
                {
                    "name": "Nasi Lemak",
                    "desc": "Coconut rice served with fried fish, anchovies, egg, and chili paste.",
                    "type": "Non-Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Woodlands Waterfront Park",
                    "desc": "Park featuring a long jetty overlooking the Johor Strait to Malaysia.",
                    "rating": "4.5 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Admiralty Park",
                    "desc": "Large park featuring 26 distinct children slide playgrounds.",
                    "rating": "4.4 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Orchid Country Club",
                    "desc": "Resort style hotel with golf courses in neighboring Yishun.",
                    "price": "S$220 per night",
                },
                "mid_range": {
                    "name": "Woodlands Premium Stay",
                    "desc": "Modern serviced apartments near Causeway Point.",
                    "price": "S$150 per night",
                },
                "budget": {
                    "name": "Hometel Woodlands",
                    "desc": "Simple budget lodging catering to daily cross-border travelers.",
                    "price": "S$90 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Causeway Point Mall",
                    "desc": "Huge commercial shopping center with department stores and food courts.",
                },
                {"name": "Woodlands Civic Centre", "desc": "Local retail block containing bookstores and cafes."},
            ],
            "airport_details": "Access via taxi (25 mins) or taking buses linking to northern transit loops.",
            "safety_recommendations": "Be prepared for traffic delays if traveling near the Malaysia Causeway checkpoint.",
        },
        # 11. Changi
        {
            "city_name": "Changi",
            "description": "Eastern coastal district hosting the world's best airport and tranquil beach walks.",
            "transport_info": "Changi Airport MRT, local buses, and ferries from Changi Point.",
            "food_info": [
                {
                    "name": "Changi Village Nasi Lemak",
                    "desc": "Famed local coconut rice served with sweet sambal chili and wings.",
                    "type": "Non-Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Jewel Changi Airport",
                    "desc": "Stunning retail complex featuring a giant indoor waterfall.",
                    "rating": "4.9 ⭐",
                    "time": "Afternoon",
                },
                {
                    "name": "Changi Boardwalk",
                    "desc": "Scenic coastal pathway famous for viewing sunset over Johor Strait.",
                    "rating": "4.5 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Crowne Plaza Changi Airport",
                    "desc": "Award-winning hotel directly linked to airport terminals.",
                    "price": "S$380 per night",
                },
                "mid_range": {
                    "name": "Changi Cove",
                    "desc": "Charming, green retreat hotel near Changi Village.",
                    "price": "S$170 per night",
                },
                "budget": {
                    "name": "Village Hotel Changi",
                    "desc": "Relaxed value hotel offering a rooftop pool overlooking the sea.",
                    "price": "S$130 per night",
                },
            },
            "shopping_areas": [
                {"name": "Jewel Retail Shops", "desc": "Mega shopping complex containing global flagship stores."},
                {"name": "Changi Village Market", "desc": "Local hawker center block with craft shops and bakeries."},
            ],
            "airport_details": "Directly inside Changi Airport (SIN) sector; zero commute needed.",
            "safety_recommendations": "Extremely safe. Follow airport security rules strictly at all times.",
        },
        # 12. Yishun
        {
            "city_name": "Yishun",
            "description": "A residential district in the North, known for natural hot springs and local heritage parks.",
            "transport_info": "Yishun MRT station on the North-South Line, and local buses.",
            "food_info": [
                {
                    "name": "Laksa Yong Tau Foo",
                    "desc": "Stuffed tofu and vegetables served in a rich spicy curry broth.",
                    "type": "Non-Veg/Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Sembawang Hot Spring Park",
                    "desc": "Singapore's only natural geothermal hot spring park.",
                    "rating": "4.4 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Yishun Park",
                    "desc": "Scenic park housing a large tropical fruit tree orchard.",
                    "rating": "4.2 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Orchid Country Club Resort",
                    "desc": "Quiet golf resort with a massive swimming pool complex.",
                    "price": "S$240 per night",
                },
                "mid_range": {
                    "name": "Yishun Serviced Suites",
                    "desc": "Modern suites close to Northpoint City Mall.",
                    "price": "S$160 per night",
                },
                "budget": {
                    "name": "Local Room Stay Yishun",
                    "desc": "Affordable budget private rooms in local flats.",
                    "price": "S$85 per night",
                },
            },
            "shopping_areas": [
                {"name": "Northpoint City", "desc": "The largest retail shopping mall in Northern Singapore."},
                {"name": "Wisteria Mall", "desc": "Cozy lifestyle neighborhood mall featuring supermarkets and cafes."},
            ],
            "airport_details": "Access via taxi (20 mins) or taking North-South MRT linking to transit loops.",
            "safety_recommendations": "Safe residential area. Bring your own bucket to soak feet at the hot springs.",
        },
        # 13. Ang Mo Kio
        {
            "city_name": "Ang Mo Kio",
            "description": "A mature residential town in the Central region, boasting spacious parks and local food courts.",
            "transport_info": "Ang Mo Kio MRT station, North-South line, and local buses.",
            "food_info": [
                {
                    "name": "Claypot Rice",
                    "desc": "Rice slow-cooked in claypots with chicken, sausage, and dark soy sauce.",
                    "type": "Non-Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Bishan-Ang Mo Kio Park",
                    "desc": "Beautiful 62-hectare park with a naturalized meandering river.",
                    "rating": "4.7 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Kebun Baru Bird Singing Corner",
                    "desc": "Traditional bird singing cage display corner.",
                    "rating": "4.3 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "The Clan Hotel",
                    "desc": "Luxury hotel located a short train ride away in CBD.",
                    "price": "S$380 per night",
                },
                "mid_range": {
                    "name": "Metro Loft Suites",
                    "desc": "Cozy residential suites near MRT.",
                    "price": "S$160 per night",
                },
                "budget": {
                    "name": "AMK Budget Rooms",
                    "desc": "Simple budget rooms catering to long-stay value travelers.",
                    "price": "S$90 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "AMK Hub Mall",
                    "desc": "Multi-story shopping mall containing cinemas, supermarkets, and stores.",
                },
                {"name": "Djitsun Mall", "desc": "Neighborhood lifestyle block with fitness centers and dining."},
            ],
            "airport_details": "Located 20 minutes by taxi from Changi Airport via CTE expressway.",
            "safety_recommendations": "Generally very safe. Clean up your trays at hawker centers.",
        },
        # 14. Bedok
        {
            "city_name": "Bedok",
            "description": "A popular residential town in the East, famous for Bedok Reservoir and food markets.",
            "transport_info": "Bedok MRT station, East-West Line, and feeder bus networks.",
            "food_info": [
                {
                    "name": "Bak Chor Mee",
                    "desc": "Minced pork noodles served dry with chili, vinegar, and meatballs.",
                    "type": "Non-Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Bedok Reservoir Park",
                    "desc": "Scenic reservoir park popular for water sports and runs.",
                    "rating": "4.5 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Forest Adventure",
                    "desc": "An outdoor treetop zip-line adventure course in the reservoir park.",
                    "rating": "4.6 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Dusit Thani Laguna",
                    "desc": "Luxury golf resort located nearby.",
                    "price": "S$320 per night",
                },
                "mid_range": {
                    "name": "Q Loft Hotels @ Bedok",
                    "desc": "Clean and stylish boutique hotel.",
                    "price": "S$140 per night",
                },
                "budget": {
                    "name": "Bedok Guest House",
                    "desc": "Simple budget accommodation close to local food markets.",
                    "price": "S$80 per night",
                },
            },
            "shopping_areas": [
                {"name": "Bedok Mall", "desc": "Modern retail complex built directly underneath Bedok MRT station."},
                {
                    "name": "Bedok Interchange Hawker Centre",
                    "desc": "Huge food center block packed with famous local food stalls.",
                },
            ],
            "airport_details": "Located 15 minutes by taxi or 4 stops on East-West MRT from Changi Airport.",
            "safety_recommendations": "Extremely safe. Use caution when participating in water sports at the reservoir.",
        },
        # 15. Queenstown
        {
            "city_name": "Queenstown",
            "description": "Singapore's first satellite residential town, famous for heritage blocks and outlet shopping.",
            "transport_info": "Queenstown MRT station on the East-West line.",
            "food_info": [
                {
                    "name": "Curry Rice",
                    "desc": "Hainanese-style pork chop curry rice, a local favorite.",
                    "type": "Non-Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Wessex Estate",
                    "desc": "Charming colonial black-and-white houses set in lush green forests.",
                    "rating": "4.4 ⭐",
                    "time": "Afternoon",
                },
                {
                    "name": "Queenstown Library",
                    "desc": "Singapore's oldest public library, a preserved heritage building.",
                    "rating": "4.3 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Park Hotel Alexandra",
                    "desc": "Upscale premium hotel featuring a lovely pool terrace.",
                    "price": "S$240 per night",
                },
                "mid_range": {
                    "name": "ibis budget Singapore Mount Faber",
                    "desc": "Clean, value-oriented business hotel.",
                    "price": "S$130 per night",
                },
                "budget": {
                    "name": "Queenstown Hostel",
                    "desc": "Simple backpacker style rooms near transit links.",
                    "price": "S$60 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Anchorpoint Shopping Centre",
                    "desc": "Outlet mall selling international brands at discounted rates.",
                },
                {
                    "name": "Queensway Shopping Centre",
                    "desc": "Famed complex for sports shoes and racket restringing services.",
                },
            ],
            "airport_details": "Access via East-West MRT line (30 mins from Changi Airport).",
            "safety_recommendations": "Generally very safe. Exercise caution on busy traffic crossroads.",
        },
        # 16. Novena
        {
            "city_name": "Novena",
            "description": "A bustling commercial and medical hub located just north of Orchard Road.",
            "transport_info": "Novena MRT station on the North-South Line, and local buses.",
            "food_info": [
                {
                    "name": "Curry Chicken Noodles",
                    "desc": "Noodles served in a rich, spicy coconut curry broth with chicken.",
                    "type": "Non-Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Sun Yat Sen Nanyang Memorial Hall",
                    "desc": "Preserved historic villa highlighting revolutionary leader Sun Yat-sen.",
                    "rating": "4.5 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Novena Church",
                    "desc": "Famous gothic-style Catholic church, a local architectural landmark.",
                    "rating": "4.6 ⭐",
                    "time": "Afternoon",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Oasia Hotel Novena",
                    "desc": "Premium wellness-themed hotel with club lounge access.",
                    "price": "S$260 per night",
                },
                "mid_range": {
                    "name": "Courtyard by Marriott Singapore Novena",
                    "desc": "Stylish hotel featuring a rooftop infinity pool.",
                    "price": "S$220 per night",
                },
                "budget": {
                    "name": "Value Hotel Thomson",
                    "desc": "Clean and budget-friendly hotel along Balestier Road.",
                    "price": "S$100 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Velocity @ Novena Square",
                    "desc": "Sports-themed shopping mall containing major athletic brands.",
                },
                {
                    "name": "United Square Mall",
                    "desc": "Shopping mall specializing in children education and kids stores.",
                },
            ],
            "airport_details": "Located 20 minutes by taxi or via North-South MRT connection from Changi Airport.",
            "safety_recommendations": "Extremely safe. Highly popular residential and commercial area.",
        },
        # 17. Bukit Timah
        {
            "city_name": "Bukit Timah",
            "description": "An upscale residential district hosting Singapore's highest peak and rainforests.",
            "transport_info": "Downtown MRT line (Beauty World and King Albert Park stations).",
            "food_info": [
                {
                    "name": "Satay",
                    "desc": "Grilled chicken or beef skewers served with sweet peanut dip sauce.",
                    "type": "Non-Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Bukit Timah Nature Reserve",
                    "desc": "Singapore's highest hill containing primary rainforests.",
                    "rating": "4.7 ⭐",
                    "time": "Morning",
                },
                {
                    "name": "Singapore Botanic Gardens",
                    "desc": "UNESCO World Heritage botanic garden containing orchid collections.",
                    "rating": "4.8 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Shangri-La Singapore",
                    "desc": "Luxury sanctuary resort hotel located nearby.",
                    "price": "S$450 per night",
                },
                "mid_range": {
                    "name": "Mercure Singapore on Stevens",
                    "desc": "Stylish premium hotel in leafy suburbs.",
                    "price": "S$200 per night",
                },
                "budget": {
                    "name": "Bukit Timah Guest House",
                    "desc": "Affordable private rooms close to nature reserves.",
                    "price": "S$120 per night",
                },
            },
            "shopping_areas": [
                {
                    "name": "Beauty World Centre",
                    "desc": "Classic shopping complex famous for local food stalls on the roof.",
                },
                {"name": "Bukit Timah Plaza", "desc": "Cozy mall containing grocery stores and cafes."},
            ],
            "airport_details": "Access via Downtown MRT line directly from Changi Airport.",
            "safety_recommendations": "Stay on marked trails in Bukit Timah; do not feed wild monkeys.",
        },
        # 18. Punggol
        {
            "city_name": "Punggol",
            "description": "A new waterfront residential eco-town in the Northeast, famous for cycling and walks.",
            "transport_info": "Punggol MRT/LRT network, and rental bicycles.",
            "food_info": [
                {
                    "name": "Seafood Fried Rice",
                    "desc": "Fried rice cooked with eggs, shrimp, and spring onions.",
                    "type": "Non-Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Punggol Waterway Park",
                    "desc": "Scenic park built around a canal with pedestrian bridges.",
                    "rating": "4.6 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Coney Island Park",
                    "desc": "Rustic, forested offshore island park popular for bird watching and cycling.",
                    "rating": "4.5 ⭐",
                    "time": "Morning",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Crowne Plaza",
                    "desc": "Luxury hotel located a short train/taxi ride away.",
                    "price": "S$380 per night",
                },
                "mid_range": {
                    "name": "Punggol Ranch Serviced Rooms",
                    "desc": "Cozy cabins close to nature parks.",
                    "price": "S$150 per night",
                },
                "budget": {
                    "name": "Local Flat Stay Punggol",
                    "desc": "Comfortable budget rooms in residential areas.",
                    "price": "S$80 per night",
                },
            },
            "shopping_areas": [
                {"name": "Waterway Point", "desc": "Large retail shopping mall situated directly on the canal."},
                {"name": "Punggol Plaza", "desc": "Neighborhood shopping center serving local estates."},
            ],
            "airport_details": "Located 20 minutes by taxi or via TPE expressway from Changi Airport.",
            "safety_recommendations": "Very safe. Wear helmets when cycling long routes on park connectors.",
        },
        # 19. Clementi
        {
            "city_name": "Clementi",
            "description": "A mature residential and university town in the West, close to major research hubs.",
            "transport_info": "Clementi MRT station on the East-West line.",
            "food_info": [
                {
                    "name": "Fried Carrot Cake",
                    "desc": "Stir-fried cubes of radish cake cooked with eggs, garlic, and sweet soy sauce.",
                    "type": "Veg",
                }
            ],
            "tourist_places": [
                {
                    "name": "Clementi Woods Park",
                    "desc": "Quiet, wooded park featuring mature trees and playground loops.",
                    "rating": "4.3 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "West Coast Park",
                    "desc": "Large coastal park famous for campsite grounds and kite flying.",
                    "rating": "4.6 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Park Avenue Rochester",
                    "desc": "Premium business hotel located in leafy Vista Exchange.",
                    "price": "S$220 per night",
                },
                "mid_range": {
                    "name": "Santa Grand West Coast",
                    "desc": "Clean and modern business rooms near West Coast Park.",
                    "price": "S$130 per night",
                },
                "budget": {
                    "name": "Clementi Student Lodging",
                    "desc": "Value budget rooms close to university campuses.",
                    "price": "S$75 per night",
                },
            },
            "shopping_areas": [
                {"name": "The Clementi Mall", "desc": "Five-story retail mall connected directly to the MRT station."},
                {"name": "Clementi 448 Market", "desc": "Famous local hawker center and wet market complex."},
            ],
            "airport_details": "Access via East-West MRT line (40 mins from Changi Airport).",
            "safety_recommendations": "Generally very safe. Bring insect repellent when walking in West Coast Park.",
        },
        # 20. Serangoon
        {
            "city_name": "Serangoon",
            "description": "A residential hub in the North-East, famous for French restaurants and Chomp Chomp hawker center.",
            "transport_info": "Serangoon MRT interchange (Circle and North-East lines).",
            "food_info": [
                {
                    "name": "Sambal Stingray",
                    "desc": "Grilled stingray fish slathered with spicy sambal chili on banana leaf.",
                    "type": "Non-Veg",
                },
                {
                    "name": "Hokkien Mee",
                    "desc": "Fried egg noodles braised in rich prawn broth, served with pork belly.",
                    "type": "Non-Veg",
                },
            ],
            "tourist_places": [
                {
                    "name": "Serangoon Gardens",
                    "desc": "Historic private housing estate famous for cafes and pubs.",
                    "rating": "4.5 ⭐",
                    "time": "Evening",
                },
                {
                    "name": "Chomp Chomp Food Centre",
                    "desc": "Legendary night food center famous for local barbecue dishes.",
                    "rating": "4.7 ⭐",
                    "time": "Evening",
                },
            ],
            "hotel_info": {
                "luxury": {
                    "name": "Hotel Fort Canning",
                    "desc": "Luxury hotel located a short train ride away in central area.",
                    "price": "S$350 per night",
                },
                "mid_range": {
                    "name": "ibis Styles Singapore Albert",
                    "desc": "Colorful boutique hotel near MRT links.",
                    "price": "S$150 per night",
                },
                "budget": {
                    "name": "Serangoon Cozy Stay",
                    "desc": "Simple budget private rooms close to local markets.",
                    "price": "S$85 per night",
                },
            },
            "shopping_areas": [
                {"name": "NEX Mall", "desc": "One of Singapore's largest suburban retail shopping complexes."},
                {"name": "myVillage at Serangoon Gardens", "desc": "Cozy lifestyle mall housing cafes and boutiques."},
            ],
            "airport_details": "Access via taxi (20 mins) or taking Circle/East-West MRT connections.",
            "safety_recommendations": "Chomp Chomp food court gets extremely crowded on weekend nights; go early.",
        },
    ]

    for city in singapore_areas:
        cursor.execute(
            """
        INSERT INTO cities (
            country_id, city_name, description, transport_info, food_info, tourist_places, hotel_info, shopping_areas, airport_details, safety_recommendations
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """,
            (
                singapore_id,
                city["city_name"],
                city["description"],
                city["transport_info"],
                json.dumps(city["food_info"]),
                json.dumps(city["tourist_places"]),
                json.dumps(city["hotel_info"]),
                json.dumps(city["shopping_areas"]),
                city["airport_details"],
                city["safety_recommendations"],
            ),
        )
    # Clean old weather history data
    cursor.execute("DELETE FROM weather_history;")

    # Fetch all seeded cities to generate weather history records
    cursor.execute("SELECT id, city_name, country_id FROM cities;")
    cities_list = cursor.fetchall()

    for city_row in cities_list:
        cursor.execute("SELECT country_name FROM countries WHERE id = ?;", (city_row["country_id"],))
        country_row = cursor.fetchone()
        country_name = country_row["country_name"] if country_row else ""

        weather_records = generate_weather_for_city(city_row["city_name"], country_name)
        for record in weather_records:
            cursor.execute(
                """
                INSERT INTO weather_history (
                    city_id, month_num, month_name, avg_temp, rainfall, description, recommendation
                ) VALUES (?, ?, ?, ?, ?, ?, ?);
                """,
                (
                    city_row["id"],
                    record["month_num"],
                    record["month_name"],
                    record["avg_temp"],
                    record["rainfall"],
                    record["description"],
                    record["recommendation"],
                ),
            )

    conn.commit()
    conn.close()
    print("Database successfully seeded with 20 cities and weather history per country!")


def generate_weather_for_city(city_name, country_name):
    """Generates 12-month weather history data based on city/country climate profiles."""
    city_lower = city_name.lower()
    country_lower = country_name.lower()

    # 1. Japan Temperate (Tokyo, Kyoto, etc.)
    if country_lower in ["japan", "जापान", "జపాన్"]:
        desc_recs = [
            (1, "January", 5.0, 45.0, "Cold & Sunny", "Carry a heavy winter coat, gloves, and scarf. Great for hot springs."),
            (2, "February", 6.0, 50.0, "Cold & Sunny", "Winter coats are essential. Perfect time to see plum blossoms."),
            (3, "March", 10.0, 110.0, "Chilly & Windy", "A warm jacket is recommended. Cherry blossoms begin to open late in the month."),
            (4, "April", 15.0, 120.0, "Pleasant Spring", "Light jackets or sweaters. Peak cherry blossom season; book stays early."),
            (5, "May", 20.0, 130.0, "Warm & Sunny", "Comfortable spring clothes. Excellent sightseeing weather."),
            (6, "June", 22.0, 160.0, "Mild & Rainy", "Tsuyu rainy season. Bring an umbrella, waterproof shoes, and light layers."),
            (7, "July", 26.0, 140.0, "Hot & Humid", "Breathable cotton clothing. Summer festivals and fireworks are starting."),
            (8, "August", 27.0, 150.0, "Very Hot & Humid", "Sunscreen, sunglasses, and light clothing. Stay hydrated; watch out for typhoons."),
            (9, "September", 23.0, 210.0, "Warm & Wet", "Light clothing and rain gear. Peak typhoon season; check transit updates."),
            (10, "October", 18.0, 160.0, "Cool Autumn", "Sweaters and light jackets. Beautiful autumn foliage starting in northern areas."),
            (11, "November", 12.0, 90.0, "Chilly Autumn", "Warm coats. Peak autumn leaf viewing; dry and clear days."),
            (12, "December", 8.0, 50.0, "Cold Winter", "Heavy winter coats. Perfect for winter illuminations and holiday shopping.")
        ]

    # 2. Singapore Tropical
    elif country_lower in ["singapore", "सिंगापुर", "సింగపూర్"]:
        desc_recs = [
            (1, "January", 27.0, 240.0, "Warm & Showery", "Carry an umbrella. High humidity with brief cooling afternoon showers."),
            (2, "February", 27.5, 110.0, "Warm & Clear", "Light cotton clothes and sunscreen. Best time for walking tours."),
            (3, "March", 28.0, 170.0, "Hot & Humid", "T-shirts and shorts. Sudden afternoon thunderstorms are common."),
            (4, "April", 28.5, 160.0, "Hot & Humid", "Breathable summer clothes. High UV index; stay hydrated."),
            (5, "May", 29.0, 170.0, "Very Hot", "Light shirts. Southwest monsoon starts; warm and hazy at times."),
            (6, "June", 29.0, 130.0, "Warm & Breezy", "Light clothing. Perfect time for indoor shopping and dining."),
            (7, "July", 28.5, 150.0, "Warm & Breezy", "Comfortable summer wear. Great for visiting theme parks and gardens."),
            (8, "August", 28.5, 150.0, "Warm & Humid", "Breathable cottons. Celebrate National Day outdoor events with sun hats."),
            (9, "September", 28.0, 130.0, "Warm & Humid", "Light cotton clothing. Occasional morning squalls; carry an umbrella."),
            (10, "October", 28.0, 190.0, "Warm & Wet", "Raincoat or umbrella recommended. Frequent afternoon thundershowers."),
            (11, "November", 27.0, 260.0, "Warm & Rainy", "Waterproof gear. Northeast monsoon starts; steady rainfall on some days."),
            (12, "December", 26.5, 320.0, "Mild & Wet", "Monsoon gear and light sweaters for indoor AC. Wettest month of the year.")
        ]

    # 3. Hyderabad (Semi-Arid)
    elif "hyderabad" in city_lower or "हैदराबाद" in city_lower or "హైదరాబాద్" in city_lower:
        desc_recs = [
            (1, "January", 22.0, 5.0, "Pleasant & Clear", "Light cottons for daytime, light jacket or sweater for cool nights."),
            (2, "February", 25.0, 2.0, "Warm & Sunny", "Comfortable cotton clothes. Sunny days, perfect for Golconda Fort."),
            (3, "March", 28.0, 10.0, "Warm & Dry", "Sunscreen and light clothing. Drink plenty of water."),
            (4, "April", 32.0, 25.0, "Hot & Dry", "Light linen/cotton clothes, sunglasses, and hats. Stay indoors during noon."),
            (5, "May", 35.0, 35.0, "Peak Summer", "Loose cotton clothing, umbrella for sun protection. High heat index."),
            (6, "June", 31.0, 120.0, "Humid & Showery", "Carry an umbrella. Southwest monsoon brings relief from summer heat."),
            (7, "July", 27.0, 170.0, "Cool & Rainy", "Raincoats or umbrella. Pleasant weather, ideal for local spicy Biryani."),
            (8, "August", 26.5, 150.0, "Cool & Cloudy", "Light rain gear. Constant breeze and frequent light showers."),
            (9, "September", 27.0, 140.0, "Pleasant & Wet", "Carry an umbrella. Lush green surroundings post-monsoon."),
            (10, "October", 26.0, 80.0, "Pleasant & Clear", "Comfortable daywear. Mild evenings; festive shopping season."),
            (11, "November", 23.0, 20.0, "Cool & Pleasant", "Light jackets for evening outings. Excellent travel weather."),
            (12, "December", 21.0, 5.0, "Chilly Nights", "Sweaters and jackets for nights. Coolest and most pleasant month.")
        ]

    # 4. Mumbai / Visakhapatnam / Indian Coastal Monsoonal Profile
    elif any(n in city_lower for n in ["mumbai", "visakhapatnam", "मुंबई", "विशाखापट्टनम", "ముంబై", "విశాఖపట్నం"]):
        desc_recs = [
            (1, "January", 24.0, 5.0, "Warm & Pleasant", "Light cotton clothes. Mild sea breezes, perfect beach days."),
            (2, "February", 25.5, 2.0, "Warm & Breezy", "Sunny days and comfortable evenings. Low humidity."),
            (3, "March", 27.5, 2.0, "Warm & Humid", "Light clothing. Rising humidity levels."),
            (4, "April", 29.5, 10.0, "Hot & Humid", "Breathable cottons, sunglasses. High humidity."),
            (5, "May", 31.5, 30.0, "Very Hot & Humid", "Lighter fabrics. Occasional pre-monsoon thunder showers."),
            (6, "June", 29.0, 450.0, "Severe Monsoons", "Heavy raincoats and umbrellas. Expect transit disruptions and high surf."),
            (7, "July", 27.0, 700.0, "Heavy Non-Stop Rain", "Waterproof footwear and sturdy umbrellas. Heavy monsoonal rainfall."),
            (8, "August", 27.0, 500.0, "Heavy Monsoon", "Rain gear. Continuous showers, cool temperatures, high humidity."),
            (9, "September", 27.5, 320.0, "Warm & Wet", "Carry an umbrella. Intermittent showers with sunny breaks."),
            (10, "October", 28.5, 120.0, "Hot & Humid", "Light clothes. Post-monsoon warmth and rising afternoon humidity."),
            (11, "November", 27.0, 15.0, "Pleasant & Dry", "Light cottons. Cool breezes in the evening, very pleasant."),
            (12, "December", 25.0, 5.0, "Mild & Breezy", "Light cardigans for night. Cool sea breeze and clear skies.")
        ]

    # 5. Fallback Mild Profile
    else:
        desc_recs = [
            (1, "January", 15.0, 10.0, "Mild & Sunny", "Light jackets for morning/evening, pleasant day."),
            (2, "February", 18.0, 15.0, "Warm & Sunny", "Comfortable casual clothes."),
            (3, "March", 22.0, 20.0, "Warm & Breezy", "Perfect sightseeing weather."),
            (4, "April", 26.0, 30.0, "Warm & Humid", "Light cotton clothing."),
            (5, "May", 30.0, 40.0, "Hot", "Sunscreen and breathable clothes."),
            (6, "June", 28.0, 150.0, "Wet & Humid", "Carry an umbrella."),
            (7, "July", 26.0, 200.0, "Rainy", "Waterproof gear."),
            (8, "August", 26.0, 180.0, "Rainy & Humid", "Regular showers."),
            (9, "September", 25.0, 120.0, "Mild & Wet", "Rain gear."),
            (10, "October", 22.0, 50.0, "Pleasant & Clear", "Comfortable travel weather."),
            (11, "November", 18.0, 20.0, "Cool & Clear", "Light jackets."),
            (12, "December", 15.0, 10.0, "Mild & Cool", "Sweaters for evenings.")
        ]

    records = []
    for m_num, m_name, temp, rain, desc, rec in desc_recs:
        records.append({
            "month_num": m_num,
            "month_name": m_name,
            "avg_temp": temp,
            "rainfall": rain,
            "description": desc,
            "recommendation": rec
        })
    return records



if __name__ == "__main__":
    from utils.database import init_db

    init_db()
