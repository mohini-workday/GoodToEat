import streamlit as st
from PIL import Image
import os


# Style sidebar with primary color and peach highlights
st.markdown("""
    <style>
        /* Sidebar styling - primary color with peach highlights */
        section[data-testid="stSidebar"] {
            background-color: var(--primary);
        }
        
        section[data-testid="stSidebar"] * {
            color: white;
        }
        
        section[data-testid="stSidebar"] a:hover {
            color: var(--secondary);
        }
        
        /* Selected/active items in sidebar - peach highlight */
        section[data-testid="stSidebar"] [data-baseweb="menu"] [aria-selected="true"],
        section[data-testid="stSidebar"] .stRadio label[data-testid="stRadio"]:has(input:checked),
        section[data-testid="stSidebar"] button:focus,
        section[data-testid="stSidebar"] a:focus,
        section[data-testid="stSidebar"] [class*="selected"],
        section[data-testid="stSidebar"] [class*="active"] {
            background-color: var(--secondary);
            color: #2B2B2B;
        }
    </style>
""", unsafe_allow_html=True)

# Custom CSS for modern, elegant styling inspired by reference sites
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Lato:wght@300;400;600&display=swap');
    
    /* Centralized Color System */
    :root {
        --primary: #007C91;      /* Cobalt Teal */
        --secondary: #F7ACB8;    /* Peach */
        --accent: #B27A5E;      /* Bronze */
        --bg: #FAF8F4;          /* Ivory */
        --text: #2B2B2B;        /* Charcoal */
        
        /* Color Variations */
        --primary-dark: #005A6B;
        --primary-light: #009EB5;
        --accent-dark: #8F5F47;
        --accent-light: #D4A574;
        --bg-light: #FFFFFF;
        --bg-dark: #E8E5DC;
        --text-light: #6B7A5F;
        --text-muted: #999999;
        --white: #FFFFFF;
        --black: #000000;
    }
    
    .main {
        font-family: 'Lato', sans-serif;
    }
    
    /* Headings - bold and modern using primary color */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', serif;
        color: var(--primary);
        font-weight: 700;
    }
    
    /* Body text stays neutral */
    p, li, span {
        color: var(--text);
    }
    
    .main-header {
        font-family: 'Playfair Display', serif;
        font-size: 3.5rem;
        font-weight: 700;
        color: var(--accent-light);
        text-align: center;
        padding: 2rem 0 1rem 0;
        margin-bottom: 0.5rem;
        letter-spacing: 2px;
    }
    
    .tagline {
        font-family: 'Lato', sans-serif;
        font-size: 1.2rem;
        color: var(--text-light);
        text-align: center;
        font-style: italic;
        margin-bottom: 2rem;
    }
    
    .hero-section {
        background: linear-gradient(135deg, var(--bg) 0%, var(--bg-dark) 100%);
        padding: 4rem 2rem;
        border-radius: 15px;
        margin: 2rem 0;
        text-align: center;
    }
    
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        color: var(--text);
        margin-bottom: 1rem;
        font-weight: 700;
    }
    
    .hero-subtitle {
        font-family: 'Lato', sans-serif;
        font-size: 1.3rem;
        color: var(--text-light);
        line-height: 1.8;
        max-width: 800px;
        margin: 0 auto;
    }
    
    .section-box {
        background-color: var(--bg-light);
        padding: 2.5rem;
        border-radius: 12px;
        margin: 2rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.08);
        border-top: 4px solid var(--accent-light);
    }
    
    .feature-card {
        background: linear-gradient(135deg, var(--bg) 0%, var(--bg-light) 100%);
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
        transition: transform 0.3s ease;
        border-left: 3px solid var(--accent-light);
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    }
    
    /* Product Cards - white background, subtle shadow, bronze accent border */
    .card {
        background-color: white;
        border-left: 4px solid var(--accent);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.06);
        margin-bottom: 1.5rem;
    }
    
    .product-card {
        background-color: white;
        border-left: 4px solid var(--accent);
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.06);
        margin-bottom: 1.5rem;
    }
    
    .testimonial-box {
        background: linear-gradient(135deg, var(--bg) 0%, var(--bg-dark) 100%);
        padding: 2rem;
        border-radius: 10px;
        margin: 1.5rem 0;
        border-left: 5px solid var(--accent-light);
        font-style: italic;
    }
    
    .blog-card {
        background-color: var(--bg-light);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        border-top: 3px solid var(--accent-light);
    }
    
    /* CTA Buttons - Cobalt Teal with Peach hover and Bronze focus */
    .stButton > button {
        background-color: var(--primary);
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.2em;
        border: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: var(--secondary);
        color: #2B2B2B;
    }
    
    .stButton > button:focus {
        outline: 2px solid var(--accent);
    }
    
    /* Navigation button styles - consistent sizing */
    /* Force equal column widths */
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
        flex: 1 1 0% !important;
        min-width: 0 !important;
        max-width: none !important;
        width: auto !important;
    }
    
    div[data-testid="column"] {
        width: 100% !important;
        min-width: 0 !important;
        flex: 1 1 0% !important;
        padding: 0 0.25rem !important;
        max-width: 100% !important;
    }
    
    div[data-testid="column"] button {
        width: 100% !important;
        min-width: 0 !important;
        max-width: 100% !important;
        height: 50px !important;
        min-height: 50px !important;
        max-height: 50px !important;
        font-size: 0.75rem !important;
        padding: 0.4rem 0.2rem !important;
        margin: 0 !important;
        border-radius: 5px;
        font-weight: 500;
        transition: all 0.3s ease;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        text-align: center !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
        line-height: 1.15 !important;
        box-sizing: border-box !important;
        overflow-wrap: break-word !important;
    }
    
    /* Ensure button text wraps properly for long names */
    div[data-testid="column"] button p {
        margin: 0 !important;
        padding: 0 !important;
        font-size: 0.75rem !important;
        line-height: 1.15 !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
    }
    
    /* Active navigation button */
    div[data-testid="column"] button[kind="primary"] {
        background: linear-gradient(135deg, var(--accent-light) 0%, var(--accent) 100%) !important;
        color: var(--white) !important;
        font-weight: 600 !important;
    }
    
    /* Inactive navigation button */
    div[data-testid="column"] button[kind="secondary"] {
        background: transparent !important;
        color: var(--text) !important;
        border: 1px solid var(--bg-dark) !important;
    }
    
    div[data-testid="column"] button[kind="secondary"]:hover {
        background-color: var(--bg) !important;
        border-color: var(--accent-light) !important;
        color: var(--accent-light) !important;
    }
    
    .nav-link {
        color: var(--text);
        text-decoration: none;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    
    .nav-link:hover {
        background-color: var(--bg);
    }
    
    /* Dark footer using Cobalt Teal with bronze links */
    .footer {
        background-color: var(--primary);
        padding: 2rem;
        color: white;
        text-align: center;
        margin-top: 4rem;
    }
    
    .footer a {
        color: var(--accent);
        text-decoration: none;
    }
    
    .footer a:hover {
        color: var(--accent-light);
        text-decoration: underline;
    }
    
    .award-badge {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        color: var(--text);
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
        margin: 0.5rem;
    }
    
    .highlight-text {
        color: var(--accent-light);
        font-weight: 600;
    }
    
    /* Highlight sections with peach background */
    .highlight {
        background-color: var(--secondary);
        padding: 1.2rem;
        border-radius: 10px;
        color: #2B2B2B;
    }
    
    /* Bronze color for icons */
    .icon,
    [class*="icon"],
    svg,
    .emoji-icon {
        color: var(--accent);
    }
    
    /* Style emoji icons in content */
    div:has(> div > div[style*="font-size: 2rem"]) {
        color: var(--accent);
    }
    
    /* Top Navigation Bar */
    .top-nav {
        background-color: var(--bg-light);
        padding: 1.5rem 0 1rem 0;
        margin: 0 0 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        position: sticky;
        top: 0;
        z-index: 1000;
    }
    
    .nav-container {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 0 2rem;
    }
    
    /* Logo styling - centered for all screen sizes */
    .logo-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        margin: 1rem 0;
        padding: 0;
        text-align: center;
    }
    
    /* Center Streamlit image within logo wrapper */
    .logo-wrapper > div {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
    }
    
    .logo-wrapper img {
        max-height: 400px;
        width: auto;
        height: auto;
        object-fit: contain;
        display: block;
        margin: 0 auto !important;
    }
    
    /* Center logo image in Streamlit */
    div[data-testid="stImage"] img {
        max-width: 400px !important;
        width: 400px !important;
        height: auto !important;
        display: block !important;
        margin: 0 auto !important;
    }
    
    /* Ensure logo container is centered */
    div[data-testid="stImage"] {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 0 auto !important;
        width: 100% !important;
    }
    
    /* Center logo image specifically */
    div[data-testid="stImage"] img {
        display: block !important;
        margin: 0 auto !important;
    }
    
    .nav-links {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
    }
    
    .nav-item {
        padding: 0.75rem 1.25rem;
        color: #2C3E2D;
        text-decoration: none;
        font-family: 'Lato', sans-serif;
        font-size: 0.95rem;
        font-weight: 500;
        border-radius: 5px;
        transition: all 0.3s ease;
        cursor: pointer;
        border: none;
        background: transparent;
    }
    
    .nav-item:hover {
        background-color: #F8F6F0;
        color: #D4A574;
    }
    
    .nav-item.active {
        background: linear-gradient(135deg, #D4A574 0%, #B8935F 100%);
        color: white;
        font-weight: 600;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Adjust main content padding */
    .main .block-container {
        padding-top: 2rem;
    }
    
    /* Set full website background and default text color */
    .stApp {
        background-color: var(--bg);
        color: var(--text);
    }
    
    /* Ensure body and main content use the color variables */
    body {
        background-color: var(--bg);
        color: var(--text);
    }
    
    .main {
        background-color: var(--bg);
        color: var(--text);
    }
    </style>
""", unsafe_allow_html=True)

# Helper function to load images
def load_image(image_path):
    try:
        if os.path.exists(image_path):
            return Image.open(image_path)
        return None
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

# Page configuration
st.set_page_config(
    page_title="GoodToEat - Handcrafted Irish Ghee",
    page_icon="🧈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state for page navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

# Navigation pages
pages = ["Home", "Products", "The Founder", "The Brand", "About Ghee", "Ghee Moments", "Ghee Blogs", "Contacts", "FAQs"]


# Display logo image centered at the top - double size and centered
logo_img = load_image("Images/Logo G2E-01.png")
if logo_img:
    # Center the logo using columns for proper centering, double size (400px)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(logo_img, use_container_width=False, width=400)
else:
    # Fallback to text if image not found
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div style="font-family: \'Playfair Display\', serif; font-size: 1.8rem; font-weight: 700; color: var(--accent-light); text-align: center; margin-bottom: 1rem;">🧈 GoodToEat</div>', unsafe_allow_html=True)



# Navigation buttons in a row - all same size with consistent spacing
st.markdown('<div style="max-width: 1200px; margin: 0 auto; padding: 0 1rem;">', unsafe_allow_html=True)
nav_cols = st.columns(len(pages), gap="small")
for i, page_name in enumerate(pages):
    with nav_cols[i]:
        button_type = "primary" if st.session_state.current_page == page_name else "secondary"
        if st.button(page_name, key=f"nav_{page_name}", use_container_width=True, type=button_type):
            st.session_state.current_page = page_name
            st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# Get current page
page = st.session_state.current_page

# Home Page
if page == "Home":
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">The Golden Touch of Home</div>
        <div class="hero-subtitle">
            A little home business with a lot of warmth. Everything we do is personal. 
            The ghee is handcrafted in small batches, the orders are packed with care, 
            and the conversations are real. From our holistic kitchen to yours.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Main Image
    ghee_img = load_image("Images/Ghee.png")
    if ghee_img:
        st.image(ghee_img, use_container_width=True, caption="Premium Handcrafted Irish Ghee")
    
    st.markdown("---")
    
    # Key Features
    st.markdown("### ✨ Why GoodToEat?")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
        <h4>🇮🇪 Irish Heritage</h4>
        <p>Proudly handcrafted in Ireland using the finest locally sourced Irish dairy products. 
        Each batch celebrates our rich dairy heritage.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
        <h4>👨‍🍳 Small Batch Crafted</h4>
        <p>Made fresh in small quantities to ensure the highest quality and freshness. 
        Every jar receives personal attention and care.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
        <h4>🌿 Pure & Natural</h4>
        <p>No additives, preservatives, or artificial ingredients. Just pure, natural ghee 
        made with traditional methods and modern standards.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Why GTE Section
    why_gte_img = load_image("Images/WhyGTE.png")
    if why_gte_img:
        col1, col2 = st.columns([1, 1])
        with col1:
            st.image(why_gte_img, use_container_width=True)
        with col2:
            st.markdown("""
            <div class="section-box">
            <h3>Our Essential Identity</h3>
            <ul style="line-height: 2;">
                <li><strong>Laboratory Tested</strong> - Every batch is tested for quality and purity</li>
                <li><strong>Award Winning Products</strong> - Recognized for excellence in taste and quality</li>
                <li><strong>Artisan-Made With Love & Care</strong> - Handcrafted with passion</li>
                <li><strong>Certified Organic and Grass-Fed</strong> - Premium ingredients only</li>
                <li><strong>Gut Health Benefits</strong> - Supporting your wellness journey</li>
                <li><strong>Sterilised Glass Jars</strong> - Preserving freshness and quality</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Taste the Difference
    taste_img = load_image("Images/TasteTheDifference.png")
    if taste_img:
        st.image(taste_img, use_container_width=True)
    
    st.markdown("---")
    
    # Use Cases
    st.markdown("### 🍳 Use Ghee Anywhere You Would Use Butter or Oil!")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    uses = [
        ("Cook", "👨‍🍳"),
        ("Sauté", "🍳"),
        ("Spread", "🍞"),
        ("Sear", "🔥"),
        ("Bake", "🧁")
    ]
    
    for i, (use, icon) in enumerate(uses):
        with [col1, col2, col3, col4, col5][i]:
            st.markdown(f"""
            <div style="text-align: center; padding: 1rem;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{icon}</div>
                <div style="font-weight: 600; color: var(--text);">{use}</div>
            </div>
            """, unsafe_allow_html=True)

# Products Page
elif page == "Products":
    st.markdown("### 🧈 Our Products")
    st.markdown('<p style="text-align: center; color: var(--text-light); font-size: 1.1rem;">Handcrafted in small batches, GoodToEat brings pure warmth and refined depth of flavor to your meals.</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Product 1 - 200g
    col1, col2 = st.columns([1, 1])
    with col1:
        product_200g = load_image("Images/200G_Mockup.png")
        if product_200g:
            st.image(product_200g, use_container_width=True)
    with col2:
        st.markdown("""
        <div class="product-card">
        <h3>Premium Irish Ghee - 200g</h3>
        <p><strong class="highlight-text">Price:</strong> €14.99</p>
        <p><strong>Size:</strong> 200g Glass Jar</p>
        <p>Perfect for trying our premium ghee or as a thoughtful gift. Made from 100% Irish butter, 
        handcrafted in small batches with traditional methods.</p>
        <h4>Key Features:</h4>
        <ul>
            <li>Made from 100% Irish butter</li>
            <li>Handcrafted in small quantities</li>
            <li>Freshly made in Ireland</li>
            <li>No additives or preservatives</li>
            <li>Rich, nutty flavor</li>
            <li>Lactose-free and casein-free</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        quantity_200g = st.number_input("Quantity (200g)", min_value=0, max_value=10, value=0, key="qty_200g")
        if st.button("Add to Cart", key="add_200g"):
            if quantity_200g > 0:
                st.success(f"Added {quantity_200g} x 200g jar(s) to cart!")
                st.balloons()
    
    st.markdown("---")
    
    # Product 2 - 500ml
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        <div class="product-card">
        <h3>Premium Irish Ghee - 500ml</h3>
        <p><strong class="highlight-text">Price:</strong> €24.99</p>
        <p><strong>Size:</strong> 500ml Glass Jar</p>
        <p>Our most popular size! Ideal for regular use in your kitchen. This premium ghee is carefully 
        crafted using traditional methods, ensuring a rich, buttery flavor that enhances any dish.</p>
        <h4>Key Features:</h4>
        <ul>
            <li>Made from 100% Irish butter</li>
            <li>Handcrafted in small quantities</li>
            <li>Freshly made in Ireland</li>
            <li>No additives or preservatives</li>
            <li>High smoke point - perfect for cooking</li>
            <li>Lactose-free and casein-free</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        quantity_500ml = st.number_input("Quantity (500ml)", min_value=0, max_value=10, value=0, key="qty_500ml")
        if st.button("Add to Cart", key="add_500ml"):
            if quantity_500ml > 0:
                st.success(f"Added {quantity_500ml} x 500ml jar(s) to cart!")
                st.balloons()
    with col2:
        product_500ml = load_image("Images/500ml_V4.png")
        if product_500ml:
            st.image(product_500ml, use_container_width=True)
    
    st.markdown("---")
    
    # Product 3 - 1KG
    col1, col2 = st.columns([1, 1])
    with col1:
        product_1kg = load_image("Images/1KG_V3_Mockup_2.png")
        if product_1kg:
            st.image(product_1kg, use_container_width=True)
    with col2:
        st.markdown("""
        <div class="product-card">
        <h3>Premium Irish Ghee - 1KG</h3>
        <p><strong class="highlight-text">Price:</strong> €44.99</p>
        <p><strong>Size:</strong> 1KG Glass Jar</p>
        <p>Our largest size, perfect for families or those who love to cook with ghee regularly. 
        Best value for money while maintaining the same premium quality.</p>
        <h4>Key Features:</h4>
        <ul>
            <li>Made from 100% Irish butter</li>
            <li>Handcrafted in small quantities</li>
            <li>Freshly made in Ireland</li>
            <li>No additives or preservatives</li>
            <li>Rich, nutty flavor</li>
            <li>Long shelf life - no refrigeration needed</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        quantity_1kg = st.number_input("Quantity (1KG)", min_value=0, max_value=10, value=0, key="qty_1kg")
        if st.button("Add to Cart", key="add_1kg"):
            if quantity_1kg > 0:
                st.success(f"Added {quantity_1kg} x 1KG jar(s) to cart!")
                st.balloons()
    
    st.markdown("---")
    
    # Nutritional Information
    st.markdown("### 📊 Nutritional Information (per 100g)")
    st.markdown("""
    <div class="section-box">
    <ul style="line-height: 2;">
        <li><strong>Energy:</strong> 900 kcal</li>
        <li><strong>Fat:</strong> 100g (of which saturated: 65g)</li>
        <li><strong>Carbohydrates:</strong> 0g</li>
        <li><strong>Protein:</strong> 0g</li>
        <li><strong>Salt:</strong> 0g</li>
    </ul>
    <p><strong>Storage:</strong> Store in a cool, dry place. No refrigeration required. 
    Best consumed within 12 months of production.</p>
    </div>
    """, unsafe_allow_html=True)

# The Founder Page
elif page == "The Founder":
    st.markdown("### 👤 The Founder")
    
    # Founder Image
    founder_img1 = load_image("Images/Gemini_Generated_Image_ja0t4mja0t4mja0t.png")
    founder_img2 = load_image("Images/Gemini_Generated_Image_xpzlvsxpzlvsxpzl.png")
    
    col1, col2 = st.columns([1, 1])
    if founder_img1:
        with col1:
            st.image(founder_img1, use_container_width=True)
    if founder_img2:
        with col2:
            st.image(founder_img2, use_container_width=True)
    
    st.markdown("""
    <div class="section-box">
    <h3>A Little Home Business with a Lot of Warmth</h3>
    <p style="line-height: 1.8; font-size: 1.1rem;">
    We're a small home-based business, and that's something we're proud of. Everything we do is personal. 
    The ghee is handcrafted in small batches, the orders are packed with care, and the conversations are real.
    </p>
    <p style="line-height: 1.8; font-size: 1.1rem;">
    If you ever need help, have a question, or just want to share your experience, reach out anytime. 
    You won't be speaking to a system. You'll be speaking to me, the founder of GoodToEat.
    </p>
    <p style="line-height: 1.8; font-size: 1.1rem;">
    We love connecting with people, and we're always here to make sure you feel looked after. 
    From our holistic kitchen to yours, we're committed to bringing you the finest handcrafted ghee 
    made with love and care.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
    <h4>Our Story</h4>
    <p>GoodToEat was born from a passion for quality, tradition, and the rich dairy heritage of Ireland. 
    What started as a small home kitchen experiment has grown into a beloved business that brings 
    authentic, handcrafted ghee to families across Ireland and beyond.</p>
    <p>Every jar tells a story of dedication, care, and the belief that the best food comes from 
    the best ingredients, prepared with attention to detail and a whole lot of heart.</p>
    </div>
    """, unsafe_allow_html=True)

# The Brand Page
elif page == "The Brand":
    st.markdown("### 🏷️ The Brand")
    
    st.markdown("""
    <div class="hero-section">
        <div class="hero-title">GoodToEat</div>
        <div class="hero-subtitle">
            More than just ghee. We're a brand built on authenticity, quality, and the belief 
            that food should nourish both body and soul.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Brand Values
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
        <h4>🌿 Our Mission</h4>
        <p>To bring you the finest handcrafted ghee, made fresh in small batches using premium 
        Irish dairy products. We are committed to quality, authenticity, and the traditional 
        methods that make our ghee special.</p>
        </div>
        
        <div class="feature-card">
        <h4>🇮🇪 Irish Heritage</h4>
        <p>Proudly made in Ireland using locally sourced Irish dairy products. We support 
        local dairy farmers and preserve traditional methods while maintaining modern quality standards.</p>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
        <h4>👨‍🍳 Small Batch Production</h4>
        <p>Handcrafted in small quantities to ensure freshness and quality. Every jar receives 
        personal attention and care, preserving the traditional handcrafted methods.</p>
        </div>
        
        <div class="feature-card">
        <h4>💚 Sustainability</h4>
        <p>We believe in environmentally conscious practices, supporting sustainable dairy farming, 
        and using eco-friendly packaging where possible. Our commitment extends beyond the product 
        to the planet we share.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Brand Identity
    st.markdown("### Our Essential Identity")
    st.markdown("""
    <div class="section-box">
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.5rem; margin-top: 1rem;">
        <div style="text-align: center; padding: 1.5rem; background: var(--bg); border-radius: 8px;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🧪</div>
            <div style="font-weight: 600;">Laboratory Tested</div>
        </div>
        <div style="text-align: center; padding: 1.5rem; background: var(--bg); border-radius: 8px;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🏆</div>
            <div style="font-weight: 600;">Award Winning</div>
        </div>
        <div style="text-align: center; padding: 1.5rem; background: var(--bg); border-radius: 8px;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">❤️</div>
            <div style="font-weight: 600;">Made With Love</div>
        </div>
        <div style="text-align: center; padding: 1.5rem; background: var(--bg); border-radius: 8px;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🌿</div>
            <div style="font-weight: 600;">Certified Organic</div>
        </div>
        <div style="text-align: center; padding: 1.5rem; background: var(--bg); border-radius: 8px;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">💚</div>
            <div style="font-weight: 600;">Gut Health Benefits</div>
        </div>
        <div style="text-align: center; padding: 1.5rem; background: var(--bg); border-radius: 8px;">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🫙</div>
            <div style="font-weight: 600;">Sterilised Glass Jars</div>
        </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

# About Ghee Page
elif page == "About Ghee":
    st.markdown("### 🧈 About Ghee")
    
    about_img = load_image("Images/About.png")
    if about_img:
        st.image(about_img, use_container_width=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div class="section-box">
    <h3>What is Ghee?</h3>
    <p style="line-height: 1.8; font-size: 1.1rem;">
    Ghee is a form of clarified butter that has been used in traditional cooking for thousands of years. 
    It's made by slowly simmering butter to remove water and milk solids, leaving behind pure, golden, 
    nutrient-rich fat with a rich, nutty flavor.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
        <h4>✨ Health Benefits</h4>
        <ul style="line-height: 2;">
            <li><strong>Rich in Vitamins:</strong> Contains vitamins A, D, E, and K</li>
            <li><strong>Gut Health:</strong> Contains butyric acid that supports digestive health</li>
            <li><strong>Lactose-Free:</strong> Safe for those with lactose intolerance</li>
            <li><strong>High Smoke Point:</strong> Ideal for high-heat cooking</li>
            <li><strong>Antioxidants:</strong> Contains antioxidants that support overall wellness</li>
            <li><strong>Anti-Inflammatory:</strong> May help reduce inflammation</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
        <h4>🍳 Culinary Uses</h4>
        <ul style="line-height: 2;">
            <li><strong>Cooking:</strong> Perfect for sautéing, frying, and roasting</li>
            <li><strong>Baking:</strong> Adds rich flavor to baked goods</li>
            <li><strong>Spreading:</strong> Delicious on toast, bread, or crackers</li>
            <li><strong>Flavor Enhancer:</strong> Adds depth to any dish</li>
            <li><strong>Traditional Recipes:</strong> Essential in many cultural cuisines</li>
            <li><strong>Coffee:</strong> Popular in bulletproof coffee recipes</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("""
    <div class="section-box">
    <h3>Why Choose GoodToEat Ghee?</h3>
    <p style="line-height: 1.8; font-size: 1.1rem;">
    Our ghee is handcrafted using traditional methods passed down through generations, combined with 
    modern quality standards. Made from 100% Irish butter, each batch is carefully crafted in small 
    quantities to ensure the highest quality and freshness.
    </p>
    <p style="line-height: 1.8; font-size: 1.1rem;">
    Unlike mass-produced alternatives, our ghee maintains its authentic flavor and nutritional benefits, 
    making it a premium choice for health-conscious consumers and culinary enthusiasts alike.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    ghee_food_img = load_image("Images/GheeFood.png")
    if ghee_food_img:
        st.image(ghee_food_img, use_container_width=True)

# Ghee Moments Page
elif page == "Ghee Moments":
    st.markdown("### 📸 Ghee Moments")
    st.markdown('<p style="text-align: center; color: var(--text-light); font-size: 1.1rem;">Celebrating the joy of cooking with GoodToEat Ghee</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Customer Testimonials
    st.markdown("### 💬 What Our Customers Say")
    
    testimonials = [
        {
            "name": "Sarah M.",
            "text": "The best ghee I've ever tasted! The flavor is incredible and it's made such a difference in my cooking. You can really taste the quality.",
            "rating": "⭐⭐⭐⭐⭐"
        },
        {
            "name": "Michael D.",
            "text": "As someone who's lactose intolerant, finding high-quality ghee was a game-changer. GoodToEat ghee is now a staple in my kitchen!",
            "rating": "⭐⭐⭐⭐⭐"
        },
        {
            "name": "Emma K.",
            "text": "I love that it's made in small batches in Ireland. You can tell the care and attention that goes into every jar. Highly recommend!",
            "rating": "⭐⭐⭐⭐⭐"
        },
        {
            "name": "James L.",
            "text": "The 1KG jar is perfect for our family. We use it for everything - cooking, baking, even in our morning coffee. Excellent quality!",
            "rating": "⭐⭐⭐⭐⭐"
        }
    ]
    
    col1, col2 = st.columns(2)
    for i, testimonial in enumerate(testimonials):
        with [col1, col2][i % 2]:
            st.markdown(f"""
            <div class="testimonial-box">
            <div style="font-size: 1.2rem; margin-bottom: 0.5rem;">{testimonial['rating']}</div>
            <p style="font-size: 1.05rem; margin-bottom: 1rem;">"{testimonial['text']}"</p>
            <div style="font-weight: 600; color: var(--accent-light);">— {testimonial['name']}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Recipe Ideas
    st.markdown("### 🍳 Recipe Ideas")
    
    recipes = [
        {
            "title": "Golden Roasted Vegetables",
            "description": "Toss your favorite vegetables in GoodToEat ghee before roasting for a rich, golden finish."
        },
        {
            "title": "Ghee-Fried Eggs",
            "description": "Start your day with eggs fried in ghee - the perfect way to add flavor and nutrition."
        },
        {
            "title": "Homemade Popcorn",
            "description": "Drizzle melted ghee over freshly popped popcorn for a delicious, healthy snack."
        },
        {
            "title": "Ghee Rice",
            "description": "Add a spoonful of ghee to your rice for an aromatic, flavorful side dish."
        }
    ]
    
    for recipe in recipes:
        st.markdown(f"""
        <div class="blog-card">
        <h4>{recipe['title']}</h4>
        <p>{recipe['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Ghee Blogs Page
elif page == "Ghee Blogs":
    st.markdown("### 📝 Ghee Blogs")
    
    blog_img = load_image("Images/Blog.png")
    if blog_img:
        st.image(blog_img, use_container_width=True)
    
    st.markdown("---")
    
    blogs = [
        {
            "title": "The History and Tradition of Ghee",
            "date": "January 15, 2024",
            "excerpt": "Discover the rich history of ghee, from ancient Ayurvedic practices to modern culinary uses. Learn how this golden elixir has been cherished for thousands of years.",
            "read_time": "5 min read"
        },
        {
            "title": "Health Benefits of Ghee: A Comprehensive Guide",
            "date": "January 10, 2024",
            "excerpt": "Explore the numerous health benefits of ghee, from supporting gut health to providing essential vitamins. Understand why ghee is considered a superfood in many cultures.",
            "read_time": "7 min read"
        },
        {
            "title": "Cooking with Ghee: Tips and Techniques",
            "date": "January 5, 2024",
            "excerpt": "Master the art of cooking with ghee. Learn about its high smoke point, flavor profile, and discover new ways to incorporate this versatile ingredient into your meals.",
            "read_time": "6 min read"
        },
        {
            "title": "Why Small Batch Production Matters",
            "date": "December 28, 2023",
            "excerpt": "At GoodToEat, we believe in the power of small batch production. Learn how this approach ensures quality, freshness, and maintains the authentic flavor of our ghee.",
            "read_time": "4 min read"
        },
        {
            "title": "Irish Dairy: The Foundation of Quality Ghee",
            "date": "December 20, 2023",
            "excerpt": "Discover why Irish dairy products are among the finest in the world and how they contribute to the exceptional quality of GoodToEat ghee.",
            "read_time": "5 min read"
        }
    ]
    
    for blog in blogs:
        st.markdown(f"""
        <div class="blog-card">
        <h3>{blog['title']}</h3>
        <p style="color: var(--text-light); font-size: 0.9rem; margin-bottom: 1rem;">
            <span style="color: var(--accent-light);">📅</span> {blog['date']} • <span style="color: var(--accent-light);">⏱️</span> {blog['read_time']}
        </p>
        <p style="line-height: 1.8; font-size: 1.05rem;">{blog['excerpt']}</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.6em 1.2em; border-radius: 8px; margin-top: 1rem; cursor: pointer; font-weight: 600; transition: all 0.3s ease;" onmouseover="this.style.backgroundColor='var(--secondary)'; this.style.color='#2B2B2B';" onmouseout="this.style.backgroundColor='var(--primary)'; this.style.color='white';" onfocus="this.style.outline='2px solid var(--accent)';" onblur="this.style.outline='none';">
            Read More →
        </button>
        </div>
        """, unsafe_allow_html=True)

# Contacts Page
elif page == "Contacts":
    st.markdown("### 📞 Contact Us")
    st.markdown('<p style="text-align: center; color: var(--text-light); font-size: 1.1rem;">We\'d love to hear from you! Get in touch anytime.</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="section-box">
        <h3>Contact Information</h3>
        <p style="line-height: 2.5; font-size: 1.1rem;">
        <strong>📍 Address:</strong><br>
        GoodToEat<br>
        Ireland<br><br>
        
        <strong>📧 Email:</strong><br>
        <a href="mailto:info@goodtoeat.ie" style="color: var(--accent-light);">info@goodtoeat.ie</a><br><br>
        
        <strong>📞 Phone:</strong><br>
        +353 (0) 1 XXX XXXX<br><br>
        
        <strong>🕒 Business Hours:</strong><br>
        Monday - Friday: 9:00 AM - 5:00 PM<br>
        Saturday: 10:00 AM - 2:00 PM<br>
        Sunday: Closed
        </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Follow Us")
        st.markdown("""
        <div style="display: flex; gap: 1rem; margin-top: 1rem;">
            <div style="padding: 1rem; background: #F8F6F0; border-radius: 8px; text-align: center; flex: 1;">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📘</div>
                <div style="font-weight: 600;">Facebook</div>
                <div style="font-size: 0.9rem; color: var(--text-light);">@GoodToEatIreland</div>
            </div>
            <div style="padding: 1rem; background: var(--bg); border-radius: 8px; text-align: center; flex: 1;">
                <div style="font-size: 1.5rem; margin-bottom: 0.5rem;">📷</div>
                <div style="font-weight: 600;">Instagram</div>
                <div style="font-size: 0.9rem; color: var(--text-light);">@goodtoeat_ie</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Send us a Message")
        
        with st.form("contact_form"):
            name = st.text_input("Your Name *")
            email = st.text_input("Your Email *")
            phone = st.text_input("Phone Number")
            subject = st.selectbox("Subject", [
                "General Inquiry",
                "Product Question",
                "Order Inquiry",
                "Wholesale Inquiry",
                "Feedback",
                "Other"
            ])
            message = st.text_area("Your Message *", height=150)
            submitted = st.form_submit_button("Send Message", type="primary")
            
            if submitted:
                if name and email and message:
                    st.success("Thank you for your message! We'll get back to you soon.")
                    st.balloons()
                    
                    st.info(f"""
                    **Message Sent Successfully!**
                    
                    Name: {name}  
                    Email: {email}  
                    Phone: {phone}  
                    Subject: {subject}  
                    Message: {message}
                    """)
                else:
                    st.error("Please fill in all required fields (marked with *)")

# FAQs Page
elif page == "FAQs":
    st.markdown("### ❓ Frequently Asked Questions")
    
    faq_img = load_image("Images/Ghee_FAQ.png")
    if faq_img:
        st.image(faq_img, use_container_width=True)
    
    st.markdown("---")
    
    faqs = [
        {
            "question": "What is ghee?",
            "answer": "Ghee is a form of clarified butter that has been used in traditional cooking for thousands of years. It's made by slowly simmering butter to remove water and milk solids, leaving behind pure, golden, nutrient-rich fat with a rich, nutty flavor."
        },
        {
            "question": "Is ghee lactose-free?",
            "answer": "Yes! During the clarification process, the milk solids (which contain lactose) are removed, making ghee safe for those with lactose intolerance. However, if you have a severe dairy allergy, please consult with your healthcare provider."
        },
        {
            "question": "How should I store ghee?",
            "answer": "Ghee should be stored in a cool, dry place away from direct sunlight. No refrigeration is required. It will remain solid at room temperature and can last for up to 12 months when stored properly."
        },
        {
            "question": "What makes GoodToEat ghee different?",
            "answer": "Our ghee is handcrafted in small batches using 100% Irish dairy products. We use traditional methods combined with modern quality standards, ensuring each jar is fresh, pure, and of the highest quality. Every batch is personally crafted with care and attention to detail."
        },
        {
            "question": "Can I use ghee for high-heat cooking?",
            "answer": "Absolutely! Ghee has a high smoke point (around 485°F/250°C), making it perfect for sautéing, frying, roasting, and other high-heat cooking methods. It won't burn or smoke like regular butter."
        },
        {
            "question": "What sizes do you offer?",
            "answer": "We currently offer three sizes: 200g (perfect for trying), 500ml (our most popular size), and 1KG (best value for families or regular users). All come in sterilized glass jars."
        },
        {
            "question": "Do you ship internationally?",
            "answer": "Currently, we primarily ship within Ireland. For international shipping inquiries, please contact us directly at info@goodtoeat.ie and we'll do our best to accommodate your request."
        },
        {
            "question": "Is your ghee organic?",
            "answer": "We use premium Irish dairy products from trusted local suppliers. While we prioritize quality and sustainability, please check individual product listings for specific organic certifications."
        },
        {
            "question": "How long does shipping take?",
            "answer": "Standard shipping within Ireland typically takes 2-3 business days. We also offer express shipping options. You'll receive a tracking number once your order ships."
        },
        {
            "question": "What is your return policy?",
            "answer": "We stand behind the quality of every jar. If you're not completely satisfied with your purchase, please contact us within 30 days for a full refund. No questions asked."
        }
    ]
    
    for i, faq in enumerate(faqs):
        with st.expander(f"**{faq['question']}**", expanded=False):
            st.markdown(f"<p style='line-height: 1.8; font-size: 1.05rem;'>{faq['answer']}</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("""
    <div class="section-box" style="text-align: center;">
    <h4>Still have questions?</h4>
    <p>Don't hesitate to reach out! We're here to help.</p>
    <p><strong>Email:</strong> <a href="mailto:info@goodtoeat.ie" style="color: #D4A574;">info@goodtoeat.ie</a></p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
<p style="margin: 0.5rem 0;">© 2024 GoodToEat. All rights reserved.</p>
<p style="margin: 0.5rem 0;">Handcrafted in Ireland 🇮🇪 | Made with Love & Care</p>
<p style="margin: 0.5rem 0; font-size: 0.9rem;">
    <a href="#" style="margin: 0 1rem;">Privacy Policy</a> | 
    <a href="#" style="margin: 0 1rem;">Terms of Service</a> | 
    <a href="#" style="margin: 0 1rem;">Shipping Policy</a>
</p>
</div>
""", unsafe_allow_html=True)
