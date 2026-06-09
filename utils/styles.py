import streamlit as st
import textwrap

def render_html(html_str, sidebar=False):
    """Cleanly renders HTML in Streamlit without markdown code-block triggers."""
    # Strip all leading/trailing whitespace and join as a single-line string
    cleaned = "".join([line.strip() for line in html_str.split("\n")])
    target = st.sidebar if sidebar else st
    target.markdown(cleaned, unsafe_allow_html=True)

def inject_global_css():
    """Injects custom global CSS into the Streamlit app to ensure a premium UI/UX."""
    render_html("""
        <style>
        /* Import Premium Font */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

        /* Apply Font */
        html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, h5, h6, li, span, button, input, select, textarea {
            font-family: 'Outfit', sans-serif !important;
        }

        /* Custom Card Styling */
        .travel-card {
            background-color: var(--secondary-background-color);
            border: 1px solid rgba(128, 128, 128, 0.15);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 20px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        }
        
        .travel-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            border-color: var(--primary-color);
        }

        /* Badge Styling */
        .rating-badge {
            background: linear-gradient(135deg, #FFD700, #FFA500);
            color: #1a1a1a;
            padding: 4px 10px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85rem;
            display: inline-block;
            margin-bottom: 10px;
        }
        
        .price-badge {
            background: linear-gradient(135deg, #10B981, #059669);
            color: white;
            padding: 4px 10px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.85rem;
            display: inline-block;
            margin-bottom: 10px;
        }
        
        .tag-badge {
            background: rgba(128, 128, 128, 0.15);
            color: var(--text-color);
            padding: 4px 10px;
            border-radius: 20px;
            font-weight: 500;
            font-size: 0.85rem;
            display: inline-block;
            margin-right: 5px;
            margin-bottom: 5px;
        }

        /* Hero Banner Container */
        .hero-banner {
            position: relative;
            background: linear-gradient(135deg, rgba(26, 54, 93, 0.9), rgba(49, 130, 206, 0.7));
            border-radius: 20px;
            padding: 50px 30px;
            color: white !important;
            text-align: center;
            margin-bottom: 30px;
            overflow: hidden;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
        }

        .hero-banner h1 {
            color: white !important;
            font-weight: 800 !important;
            font-size: 2.8rem !important;
            margin-bottom: 10px !important;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }

        .hero-banner p {
            color: rgba(255, 255, 255, 0.9) !important;
            font-size: 1.2rem !important;
            max-width: 700px;
            margin: 0 auto !important;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2);
        }

        /* Itinerary Timeline Cards */
        .timeline-day {
            border-left: 3px solid var(--primary-color);
            padding-left: 20px;
            margin-left: 10px;
            margin-bottom: 25px;
            position: relative;
        }

        .timeline-day::before {
            content: '';
            width: 12px;
            height: 12px;
            background-color: var(--primary-color);
            border: 3px solid var(--background-color);
            border-radius: 50%;
            position: absolute;
            left: -8px;
            top: 5px;
        }

        /* Key Metrics Grid */
        .metric-box {
            background-color: var(--secondary-background-color);
            border: 1px solid rgba(128, 128, 128, 0.1);
            border-radius: 12px;
            padding: 15px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.02);
        }
        .metric-label {
            font-size: 0.85rem;
            color: gray;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 5px;
        }
        .metric-value {
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--primary-color);
        }

        /* Adjust Streamlit padding and margins */
        .block-container {
            padding-top: 2.5rem !important;
            padding-bottom: 3rem !important;
        }
        
        div[data-testid="stSidebarNav"] {
            display: none !important;
        }
        </style>
    """)

def render_hero(title, subtitle):
    """Renders a beautiful hero header."""
    render_html(f"""
        <div class="hero-banner">
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
    """)

def render_card(title, content, badges=None, price_badge=None, extra_html=""):
    """Helper to render a styled HTML card."""
    badge_html = ""
    if badges:
        if isinstance(badges, list):
            for b in badges:
                badge_html += f'<span class="tag-badge">{b}</span>'
        else:
            badge_html = f'<span class="rating-badge">{badges}</span>'
            
    p_badge_html = ""
    if price_badge:
        p_badge_html = f'<span class="price-badge">{price_badge}</span>'
        
    render_html(f"""
        <div class="travel-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap;">
                <h3 style="margin-top: 0; margin-bottom: 10px; font-weight: 700; font-size: 1.3rem;">{title}</h3>
                <div>
                    {p_badge_html}
                    {badge_html}
                </div>
            </div>
            <p style="margin-bottom: 10px; font-size: 0.95rem; line-height: 1.5; color: var(--text-color);">{content}</p>
            {extra_html}
        </div>
    """)

