import streamlit as st

# Page configuration
st.set_page_config(
    page_title="GoodToEat - Handcrafted Irish Ghee",
    page_icon="🧈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #2E7D32;
        text-align: center;
        padding: 1rem 0;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 2rem;
    }
    .product-card {
        background-color: #F5F5F5;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .feature-box {
        background-color: #E8F5E9;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #4CAF50;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Navigation
st.markdown('<div class="main-header">🧈 GoodToEat</div>', unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Products", "About", "Contact Us"])

# Home Page
if page == "Home":
    st.markdown('<div class="sub-header">Handcrafted Irish Ghee, Made with Love</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.image("https://images.unsplash.com/photo-1618164436266-44628842d3f2?w=600", 
                 caption="Handcrafted Irish Ghee", use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="feature-box">
        <h3>Welcome to GoodToEat</h3>
        <p>We specialize in creating premium, handcrafted ghee using the finest Irish dairy products. 
        Each batch is carefully made in small quantities to ensure the highest quality and freshness.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        ### Why Choose Our Ghee?
        - ✅ Made from 100% Irish dairy products
        - ✅ Handcrafted in small batches
        - ✅ Freshly made in Ireland
        - ✅ Premium quality guaranteed
        - ✅ Traditional methods, modern standards
        """)
    
    st.markdown("---")
    
    col3, col4, col5 = st.columns(3)
    
    with col3:
        st.markdown("""
        <div class="feature-box">
        <h4>🌿 Natural & Pure</h4>
        <p>No additives, preservatives, or artificial ingredients. Just pure, natural ghee.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-box">
        <h4>🇮🇪 Irish Heritage</h4>
        <p>Proudly made in Ireland using locally sourced Irish dairy products.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
        <div class="feature-box">
        <h4>👨‍🍳 Small Batch</h4>
        <p>Handcrafted in small quantities to ensure freshness and quality in every jar.</p>
        </div>
        """, unsafe_allow_html=True)

# Products Page
elif page == "Products":
    st.markdown('<div class="sub-header">Our Products</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="product-card">
    <h2>🧈 Premium Irish Ghee</h2>
    <p><strong>Price:</strong> €24.99</p>
    <p><strong>Size:</strong> 500g Jar</p>
    <p><strong>Description:</strong></p>
    <p>Our signature handcrafted ghee is made fresh in small batches using the finest Irish dairy products. 
    This premium ghee is carefully crafted using traditional methods, ensuring a rich, buttery flavor 
    that enhances any dish. Perfect for cooking, baking, or simply spreading on your favorite bread.</p>
    
    <h4>Key Features:</h4>
    <ul>
        <li>Made from 100% Irish butter</li>
        <li>Handcrafted in small quantities</li>
        <li>Freshly made in Ireland</li>
        <li>No additives or preservatives</li>
        <li>Rich, nutty flavor</li>
        <li>High smoke point - perfect for cooking</li>
        <li>Lactose-free and casein-free</li>
    </ul>
    
    <h4>Storage:</h4>
    <p>Store in a cool, dry place. No refrigeration required. Best consumed within 12 months of production.</p>
    
    <h4>Nutritional Information (per 100g):</h4>
    <ul>
        <li>Energy: 900 kcal</li>
        <li>Fat: 100g (of which saturated: 65g)</li>
        <li>Carbohydrates: 0g</li>
        <li>Protein: 0g</li>
        <li>Salt: 0g</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Product ordering section
    st.subheader("Order Now")
    col1, col2 = st.columns(2)
    
    with col1:
        quantity = st.number_input("Quantity", min_value=1, max_value=10, value=1, step=1)
        total_price = quantity * 24.99
        
    with col2:
        st.metric("Total Price", f"€{total_price:.2f}")
    
    if st.button("Add to Cart", type="primary"):
        st.success(f"Added {quantity} jar(s) to cart! Total: €{total_price:.2f}")
        st.balloons()

# About Page
elif page == "About":
    st.markdown('<div class="sub-header">About GoodToEat</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-box">
    <h3>Our Story</h3>
    <p>GoodToEat was born from a passion for quality, tradition, and the rich dairy heritage of Ireland. 
    We believe that the best food comes from the best ingredients, prepared with care and attention to detail.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Our Mission")
    st.markdown("""
    To bring you the finest handcrafted ghee, made fresh in small batches using premium Irish dairy products. 
    We are committed to quality, authenticity, and the traditional methods that make our ghee special.
    """)
    
    st.markdown("### Our Values")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **🌿 Quality First**
        - We use only the finest Irish dairy products
        - Every batch is carefully crafted and tested
        - No shortcuts, no compromises
        
        **🇮🇪 Irish Heritage**
        - Proudly made in Ireland
        - Supporting local dairy farmers
        - Preserving traditional methods
        """)
    
    with col2:
        st.markdown("""
        **👨‍🍳 Small Batch Production**
        - Handcrafted in small quantities
        - Ensures freshness and quality
        - Attention to detail in every jar
        
        **💚 Sustainability**
        - Environmentally conscious practices
        - Supporting sustainable dairy farming
        - Eco-friendly packaging where possible
        """)
    
    st.markdown("### Our Process")
    st.markdown("""
    1. **Sourcing**: We carefully select the finest Irish butter from trusted local suppliers
    2. **Preparation**: Using traditional methods, we slowly clarify the butter
    3. **Crafting**: Each batch is handcrafted with attention to detail
    4. **Quality Control**: Every jar is tested to ensure it meets our high standards
    5. **Packaging**: Freshly packaged and ready for you to enjoy
    """)
    
    st.markdown("### Why Small Batches?")
    st.markdown("""
    We believe that quality comes from care and attention. By producing in small batches, we can:
    - Ensure freshness in every jar
    - Maintain consistent quality
    - Give each batch the attention it deserves
    - Preserve the traditional handcrafted methods
    """)

# Contact Us Page
elif page == "Contact Us":
    st.markdown('<div class="sub-header">Get in Touch</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="feature-box">
        <h3>Contact Information</h3>
        <p><strong>📍 Address:</strong><br>
        GoodToEat<br>
        Ireland</p>
        
        <p><strong>📧 Email:</strong><br>
        info@goodtoeat.ie</p>
        
        <p><strong>📞 Phone:</strong><br>
        +353 (0) 1 XXX XXXX</p>
        
        <p><strong>🕒 Business Hours:</strong><br>
        Monday - Friday: 9:00 AM - 5:00 PM<br>
        Saturday: 10:00 AM - 2:00 PM<br>
        Sunday: Closed</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### Follow Us")
        st.markdown("""
        - Facebook: @GoodToEatIreland
        - Instagram: @goodtoeat_ie
        - Twitter: @GoodToEatIE
        """)
    
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
                    
                    # Display submitted information (in a real app, this would be sent to a backend)
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

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
<p>© 2024 GoodToEat. All rights reserved. | Handcrafted in Ireland 🇮🇪</p>
</div>
""", unsafe_allow_html=True)

