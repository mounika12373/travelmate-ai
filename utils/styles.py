import streamlit as st


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
        html, body, .stMarkdown, p, h1, h2, h3, h4, h5, h6, li, button, input, select, textarea {
            font-family: 'Outfit', sans-serif;
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
        
        /* Custom Sidebar navigation spacing */
        div[data-testid="stSidebarNav"] {
            margin-top: 10px;
        }
        </style>
    """)


import base64


def get_image_base64(image_path):
    """Converts a local image file to a base64 encoded string."""
    try:
        with open(image_path, "rb") as image_file:
            encoded = base64.b64encode(image_file.read()).decode()
            return f"data:image/png;base64,{encoded}"
    except Exception:
        return ""


def render_hero(title, subtitle, image_path=None):
    """Renders a beautiful hero header, optionally with a background image."""
    style_attr = ""
    if image_path:
        base64_img = get_image_base64(image_path)
        if base64_img:
            style_attr = f"style=\"background-image: linear-gradient(135deg, rgba(13, 21, 39, 0.85), rgba(26, 54, 93, 0.65)), url('{base64_img}'); background-size: cover; background-position: center;\""

    render_html(f"""
        <div class="hero-banner" {style_attr}>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </div>
    """)


def render_image_card(title, content, image_path, badges=None, height="260px"):
    """Helper to render a styled HTML card with a background image and text overlay."""
    base64_img = get_image_base64(image_path)

    badge_html = ""
    if badges:
        if isinstance(badges, list):
            for b in badges:
                badge_html += f'<span class="tag-badge" style="background: rgba(0,0,0,0.6); color: white; border: 1px solid rgba(255,255,255,0.2);">{b}</span>'
        else:
            badge_html = f'<span class="rating-badge">{badges}</span>'

    bg_style = (
        f"background-image: linear-gradient(180deg, rgba(0,0,0,0.1), rgba(11, 19, 43, 0.9)), url('{base64_img}');"
        if base64_img
        else "background: var(--secondary-background-color);"
    )

    render_html(f"""
        <div class="travel-card" style="{bg_style} background-size: cover; background-position: center; min-height: {height}; display: flex; flex-direction: column; justify-content: flex-end; color: white !important;">
            <div style="position: absolute; top: 15px; right: 15px; display: flex; gap: 5px;">
                {badge_html}
            </div>
            <div style="text-shadow: 0 2px 4px rgba(0,0,0,0.8);">
                <h3 style="margin-top: 0; margin-bottom: 5px; font-weight: 700; font-size: 1.25rem; color: white !important;">{title}</h3>
                <p style="margin-bottom: 0; font-size: 0.88rem; line-height: 1.4; color: rgba(255,255,255,0.9) !important;">{content}</p>
            </div>
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
