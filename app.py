import streamlit as st
import random
import time
from datetime import datetime
import base64
from io import BytesIO

# Set page config
st.set_page_config(
    page_title="Kleio - Craft your Style Story",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    padding: 2rem;
    border-radius: 10px;
    margin-bottom: 2rem;
}

.feature-card {
    background: white;
    padding: 1.5rem;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    margin: 1rem 0;
    border-left: 4px solid #667eea;
}

.stat-box {
    background: linear-gradient(45deg, #ff9a9e 0%, #fecfef 100%);
    padding: 1rem;
    border-radius: 8px;
    text-align: center;
    color: #333333;
}

.chat-message {
    padding: 1rem;
    border-radius: 10px;
    margin: 0.5rem 0;
}

.user-message {
    background: #e3f2fd;
    margin-left: 2rem;
}

.ai-message {
    background: #f3e5f5;
    margin-right: 2rem;
}

.sustainability-score {
    background: linear-gradient(45deg, #4CAF50, #81C784);
    color: #333333;
    padding: 0.5rem;
    border-radius: 20px;
    text-align: center;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}
if 'wardrobe_items' not in st.session_state:
    st.session_state.wardrobe_items = []

# Sidebar Navigation
st.sidebar.title("✨ Kleio Navigation")
page = st.sidebar.selectbox(
    "Choose a feature:",
    [
        "🏠 Home",
        "🤖 AI Personal Stylist", 
        "👕 Capsule Wardrobe Generator",
        "📸 Virtual Try-On",
        "🌱 Sustainable Fashion Finder",
        "🔄 Fashion Swap Hub",
        "👤 Body Type Styler",
        "✨ Wardrobe Care Assistant"
    ]
)

# Main Header
st.markdown("""
<div class="main-header">
    <h1 style="color: white; text-align: center; margin: 0;">✨ Kleio - Craft your Style Story</h1>
    <p style="color: white; text-align: center; margin: 0; opacity: 0.9;">Your AI-Powered Fashion Companion</p>
</div>
""", unsafe_allow_html=True)

# Home Page
if page == "🏠 Home":
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-box">
            <h3>10K+</h3>
            <p>Happy Users</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-box">
            <h3>50K+</h3>
            <p>Style Recommendations</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-box">
            <h3>200+</h3>
            <p>Fashion Brands</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-box">
            <h3>95%</h3>
            <p>Satisfaction Rate</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.header("🎯 Features Overview")
    
    features = [
        ("🤖 AI Personal Stylist", "Get personalized fashion advice powered by AI"),
        ("👕 Capsule Wardrobe", "Create a versatile wardrobe with fewer pieces"),
        ("📸 Virtual Try-On", "Visualize outfits before you buy"),
        ("🌱 Sustainable Fashion", "Discover eco-friendly fashion brands"),
        ("🔄 Fashion Swap", "Exchange clothes with other fashion lovers"),
        ("👤 Body Type Styler", "Personalized styling for your body type"),
        ("✨ Wardrobe Care", "Keep your clothes looking their best")
    ]
    
    col1, col2 = st.columns(2)
    for i, (title, desc) in enumerate(features):
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="feature-card">
                <h4>{title}</h4>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# AI Personal Stylist
elif page == "🤖 AI Personal Stylist":
    st.header("🤖 AI Personal Stylist")
    st.subheader("Your 24/7 Fashion Companion")
    
    # Chat Interface
    st.markdown("### 💬 Chat with your AI Stylist")
    
    # Display chat history
    for message in st.session_state.chat_history:
        if message['role'] == 'user':
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>You:</strong> {message['content']}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message ai-message">
                <strong>AI Stylist:</strong> {message['content']}
            </div>
            """, unsafe_allow_html=True)
    
    # User input
    user_input = st.text_input("Ask your stylist anything about fashion:")
    
    if st.button("Send Message"):
        if user_input:
            # Add user message
            st.session_state.chat_history.append({"role": "user", "content": user_input})
            
            # Generate AI response
            ai_responses = [
                f"Based on your style preferences, I recommend building a capsule wardrobe with neutral tones. For your {random.choice(['casual', 'professional', 'evening'])} look, try pairing a {random.choice(['white button-up', 'black turtleneck', 'navy blazer'])} with {random.choice(['dark jeans', 'tailored trousers', 'midi skirt'])}.",
                f"For your body type, I suggest {random.choice(['A-line dresses', 'high-waisted bottoms', 'wrap tops'])} which will be most flattering. Consider colors like {random.choice(['navy blue', 'forest green', 'burgundy'])} that complement your skin tone.",
                f"Given your lifestyle, I recommend investing in versatile pieces like a quality {random.choice(['trench coat', 'little black dress', 'white sneakers'])} that can be dressed up or down for different occasions.",
                f"Your color palette would work beautifully with {random.choice(['jewel tones', 'earth tones', 'pastels'])}. Try incorporating {random.choice(['emerald green', 'sapphire blue', 'ruby red'])} into your wardrobe."
            ]
            
            response = random.choice(ai_responses)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            st.rerun()
    
    # Quick suggestions
    st.markdown("### 🎯 Quick Style Questions")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Business Casual Outfits"):
            st.session_state.chat_history.append({"role": "user", "content": "Show me business casual outfits"})
            st.session_state.chat_history.append({"role": "assistant", "content": "For business casual, try: Navy blazer + white button-up + dark wash jeans + loafers. Or: Midi skirt + blouse + cardigan + ankle boots. These looks are professional yet approachable!"})
            st.rerun()
    
    with col2:
        if st.button("Date Night Looks"):
            st.session_state.chat_history.append({"role": "user", "content": "Suggest date night looks"})
            st.session_state.chat_history.append({"role": "assistant", "content": "For date night: Little black dress + statement jewelry + heels, or high-waisted trousers + silk camisole + blazer + ankle boots. Choose comfortable yet elegant pieces!"})
            st.rerun()
    
    with col3:
        if st.button("Weekend Casual"):
            st.session_state.chat_history.append({"role": "user", "content": "Weekend casual style ideas"})
            st.session_state.chat_history.append({"role": "assistant", "content": "Weekend vibes: High-waisted jeans + crop top + denim jacket + white sneakers, or maxi dress + sandals + sun hat. Comfort meets style!"})
            st.rerun()

# Capsule Wardrobe Generator
elif page == "👕 Capsule Wardrobe Generator":
    st.header("👕 Capsule Wardrobe Generator")
    st.subheader("Build a versatile wardrobe with fewer, better pieces")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🎯 Preferences")
        season = st.selectbox("Season:", ["Spring", "Summer", "Fall", "Winter"])
        style = st.selectbox("Style:", ["Minimalist", "Classic", "Modern", "Bohemian", "Edgy"])
        budget = st.slider("Budget ($):", 200, 2000, 800)
        color_palette = st.selectbox("Color Palette:", ["Neutral", "Monochrome", "Earth Tones", "Jewel Tones"])
        
        if st.button("Generate Capsule Wardrobe"):
            st.session_state.wardrobe_items = [
                {"category": "Tops", "item": "White Button-up Shirt", "price": 89, "essential": True},
                {"category": "Tops", "item": "Black Turtleneck", "price": 65, "essential": True},
                {"category": "Tops", "item": "Navy Blazer", "price": 120, "essential": True},
                {"category": "Bottoms", "item": "Dark Wash Jeans", "price": 95, "essential": True},
                {"category": "Bottoms", "item": "Black Trousers", "price": 78, "essential": True},
                {"category": "Bottoms", "item": "Midi Skirt", "price": 55, "essential": False},
                {"category": "Shoes", "item": "White Sneakers", "price": 85, "essential": True},
                {"category": "Shoes", "item": "Black Ankle Boots", "price": 110, "essential": True},
                {"category": "Outerwear", "item": "Trench Coat", "price": 150, "essential": True},
                {"category": "Dresses", "item": "Little Black Dress", "price": 98, "essential": True}
            ]
    
    with col2:
        if st.session_state.wardrobe_items:
            st.markdown("### 🛍️ Your Capsule Wardrobe")
            
            total_cost = sum(item['price'] for item in st.session_state.wardrobe_items)
            essential_items = [item for item in st.session_state.wardrobe_items if item['essential']]
            
            st.metric("Total Cost", f"${total_cost}")
            st.metric("Essential Items", len(essential_items))
            st.metric("Total Pieces", len(st.session_state.wardrobe_items))
            
            # Group by category
            categories = {}
            for item in st.session_state.wardrobe_items:
                cat = item['category']
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append(item)
            
            for category, items in categories.items():
                with st.expander(f"{category} ({len(items)} items)"):
                    for item in items:
                        col_a, col_b, col_c = st.columns([2, 1, 1])
                        with col_a:
                            st.write(f"**{item['item']}**")
                        with col_b:
                            st.write(f"${item['price']}")
                        with col_c:
                            if item['essential']:
                                st.success("Essential")
                            else:
                                st.info("Optional")

# Virtual Try-On
elif page == "📸 Virtual Try-On":
    st.header("📸 Virtual Try-On Studio")
    st.subheader("Visualize outfits before you buy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📷 Upload Your Photo")
        uploaded_file = st.file_uploader("Choose a photo", type=['jpg', 'jpeg', 'png'])
        
        if uploaded_file is not None:
            st.image(uploaded_file, caption="Your Photo", use_column_width=True)
            
            st.markdown("### 🎨 Try-On Controls")
            outfit_size = st.selectbox("Size:", ["XS", "S", "M", "L", "XL"])
            fit_preference = st.selectbox("Fit:", ["Slim", "Regular", "Loose"])
            
            if st.button("Apply Virtual Try-On"):
                with st.spinner("Processing virtual try-on..."):
                    time.sleep(2)
                    st.success("Virtual try-on applied! (This is a mockup)")
    
    with col2:
        st.markdown("### 👗 Choose Outfit")
        
        outfits = [
            {"name": "Business Casual", "items": ["Navy Blazer", "White Shirt", "Dark Jeans"]},
            {"name": "Weekend Chic", "items": ["Striped Top", "High-waist Jeans", "White Sneakers"]},
            {"name": "Date Night", "items": ["Black Dress", "Ankle Boots", "Statement Jewelry"]},
            {"name": "Office Professional", "items": ["Black Suit", "White Blouse", "Pumps"]}
        ]
        
        selected_outfit = st.selectbox("Select an outfit:", [outfit["name"] for outfit in outfits])
        
        # Display selected outfit details
        outfit_details = next(outfit for outfit in outfits if outfit["name"] == selected_outfit)
        st.markdown(f"**{selected_outfit}**")
        for item in outfit_details["items"]:
            st.write(f"• {item}")
        
        if st.button("Try This Outfit"):
            st.info(f"Applying {selected_outfit} to your photo...")
            
        st.markdown("### 🛒 Purchase Options")
        st.write("Find similar items:")
        for item in outfit_details["items"]:
            st.write(f"🛍️ {item} - From ${random.randint(30, 150)}")

# Sustainable Fashion Finder
elif page == "🌱 Sustainable Fashion Finder":
    st.header("🌱 Sustainable Fashion Finder")
    st.subheader("Discover eco-friendly brands that align with your values")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    with col1:
        category = st.selectbox("Category:", ["All", "Clothing", "Shoes", "Accessories"])
    with col2:
        price_range = st.slider("Price Range ($):", 0, 300, (50, 200))
    with col3:
        sustainability_min = st.slider("Min Sustainability Score:", 0, 100, 80)
    
    # Sample sustainable brands
    brands = [
        {
            "name": "EcoThread",
            "category": "Clothing",
            "rating": 4.8,
            "sustainability": 95,
            "price": 65,
            "description": "Organic cotton basics made from recycled materials",
            "certifications": ["GOTS", "Fair Trade", "Carbon Neutral"]
        },
        {
            "name": "GreenStyle Co",
            "category": "Accessories", 
            "rating": 4.6,
            "sustainability": 88,
            "price": 89,
            "description": "Handcrafted accessories from sustainable materials",
            "certifications": ["Vegan", "Recycled Materials"]
        },
        {
            "name": "Pure Earth Fashion",
            "category": "Clothing",
            "rating": 4.9,
            "sustainability": 92,
            "price": 125,
            "description": "Luxury sustainable fashion with zero waste production",
            "certifications": ["B-Corp", "Climate Positive", "GOTS"]
        },
        {
            "name": "Ocean Sole",
            "category": "Shoes",
            "rating": 4.5,
            "sustainability": 85,
            "price": 165,
            "description": "Innovative footwear made from ocean plastic",
            "certifications": ["Ocean Positive", "Vegan"]
        }
    ]
    
    # Filter brands
    filtered_brands = [
        brand for brand in brands 
        if (category == "All" or brand["category"] == category) and
           (price_range[0] <= brand["price"] <= price_range[1]) and
           (brand["sustainability"] >= sustainability_min)
    ]
    
    st.markdown(f"### 🏪 Found {len(filtered_brands)} sustainable brands")
    
    for brand in filtered_brands:
        with st.expander(f"{brand['name']} - {brand['category']}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.write(f"**{brand['description']}**")
                st.write(f"⭐ Rating: {brand['rating']}/5")
                st.write(f"💰 Average Price: ${brand['price']}")
                
                # Certifications
                cert_text = " • ".join(brand['certifications'])
                st.write(f"🏆 Certifications: {cert_text}")
            
            with col2:
                st.markdown(f"""
                <div class="sustainability-score">
                    Sustainability Score<br>
                    <h2>{brand['sustainability']}%</h2>
                </div>
                """, unsafe_allow_html=True)
                
                if st.button(f"Visit {brand['name']}", key=brand['name']):
                    st.success(f"Redirecting to {brand['name']}...")

# Fashion Swap Hub
elif page == "🔄 Fashion Swap Hub":
    st.header("🔄 Fashion Swap Hub")
    st.subheader("Exchange clothes with other fashion lovers")
    
    tab1, tab2, tab3 = st.tabs(["🛍️ Browse Swaps", "📤 List Item", "💬 My Swaps"])
    
    with tab1:
        st.markdown("### 🔍 Available Items for Swap")
        
        # Sample swap items
        swap_items = [
            {"user": "Sarah_M", "item": "Vintage Leather Jacket", "size": "M", "condition": "Like New", "looking_for": "Denim Jacket"},
            {"user": "Emily_K", "item": "Designer Handbag", "size": "One Size", "condition": "Good", "looking_for": "Crossbody Bag"},
            {"user": "Alex_R", "item": "Wool Sweater", "size": "L", "condition": "Excellent", "looking_for": "Cardigan"},
            {"user": "Maya_P", "item": "Silk Scarf", "size": "One Size", "condition": "New", "looking_for": "Statement Necklace"}
        ]
        
        for item in swap_items:
            with st.container():
                col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
                
                with col1:
                    st.write(f"**{item['item']}**")
                    st.write(f"👤 by {item['user']}")
                
                with col2:
                    st.write(f"📏 Size: {item['size']}")
                    st.write(f"✨ {item['condition']}")
                
                with col3:
                    st.write("🔄 Looking for:")
                    st.write(item['looking_for'])
                
                with col4:
                    if st.button("Propose Swap", key=f"swap_{item['user']}"):
                        st.success("Swap proposal sent!")
                
                st.markdown("---")
    
    with tab2:
        st.markdown("### 📤 List Your Item for Swap")
        
        with st.form("list_item"):
            item_name = st.text_input("Item Name:")
            item_category = st.selectbox("Category:", ["Tops", "Bottoms", "Dresses", "Shoes", "Accessories", "Outerwear"])
            item_size = st.selectbox("Size:", ["XS", "S", "M", "L", "XL", "One Size"])
            item_condition = st.selectbox("Condition:", ["New with Tags", "Like New", "Excellent", "Good", "Fair"])
            item_description = st.text_area("Description:")
            looking_for = st.text_input("What are you looking for in return?")
            
            uploaded_image = st.file_uploader("Upload item photo:", type=['jpg', 'jpeg', 'png'])
            
            if st.form_submit_button("List Item"):
                if item_name and item_category:
                    st.success(f"Your {item_name} has been listed for swap!")
                else:
                    st.error("Please fill in all required fields.")
    
    with tab3:
        st.markdown("### 💬 Your Swap Activity")
        
        st.markdown("#### 📤 Your Listed Items")
        st.info("You have 2 items listed for swap")
        
        st.markdown("#### 🔄 Active Proposals")
        proposals = [
            {"item": "Blue Denim Jacket", "with_user": "Sarah_M", "status": "Pending", "date": "2024-01-15"},
            {"item": "Black Ankle Boots", "with_user": "Emily_K", "status": "Accepted", "date": "2024-01-14"}
        ]
        
        for proposal in proposals:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write(f"**{proposal['item']}**")
            with col2:
                st.write(f"👤 {proposal['with_user']}")
            with col3:
                if proposal['status'] == 'Pending':
                    st.warning(proposal['status'])
                else:
                    st.success(proposal['status'])
            with col4:
                st.write(proposal['date'])

# Body Type Styler
elif page == "👤 Body Type Styler":
    st.header("👤 Body Type Styler")
    st.subheader("Personalized styling for your unique body type")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 📝 Body Type Assessment")
        
        # Body measurements input
        height = st.slider("Height (inches):", 48, 84, 64)
        body_type = st.selectbox("Body Type:", [
            "Select...", "Apple", "Pear", "Hourglass", "Rectangle", "Inverted Triangle"
        ])
        
        # Style preferences
        style_goals = st.multiselect("Style Goals:", [
            "Enhance curves",
            "Create balance", 
            "Elongate silhouette",
            "Define waist",
            "Broaden shoulders",
            "Minimize midsection"
        ])
        
        occasions = st.multiselect("Occasions to dress for:", [
            "Work/Professional",
            "Casual/Everyday", 
            "Date night",
            "Special events",
            "Travel",
            "Workouts"
        ])
        
        if st.button("Get Personalized Recommendations"):
            if body_type != "Select...":
                st.session_state.body_recommendations = True
            else:
                st.error("Please select your body type")
    
    with col2:
        if hasattr(st.session_state, 'body_recommendations') and st.session_state.body_recommendations:
            st.markdown("### 🎯 Your Personalized Style Guide")
            
            # Body type specific recommendations
            if body_type == "Apple":
                recommendations = {
                    "best_styles": ["V-necks", "A-line dresses", "High-waisted bottoms", "Structured blazers"],
                    "avoid": ["Tight fitting tops", "Low-waisted pants", "Horizontal stripes across midsection"],
                    "colors": ["Darker colors on top", "Brighter colors on bottom", "Monochromatic looks"]
                }
            elif body_type == "Pear":
                recommendations = {
                    "best_styles": ["Boat necks", "Statement tops", "Straight-leg pants", "A-line skirts"],
                    "avoid": ["Skinny jeans", "Tight skirts", "Baggy tops"],
                    "colors": ["Bright colors on top", "Darker colors on bottom", "Bold patterns up top"]
                }
            elif body_type == "Hourglass":
                recommendations = {
                    "best_styles": ["Wrap dresses", "Belted styles", "Fitted tops", "High-waisted bottoms"],
                    "avoid": ["Boxy styles", "Oversized clothing", "Drop-waist dresses"],
                    "colors": ["Any colors work", "Emphasize waist with belts", "Monochromatic looks"]
                }
            elif body_type == "Rectangle":
                recommendations = {
                    "best_styles": ["Ruffles and textures", "Belted waists", "Layering", "Curved hemlines"],
                    "avoid": ["Straight, boxy cuts", "Shapeless dresses"],
                    "colors": ["Color blocking", "Bold patterns", "Contrasting belts"]
                }
            else:  # Inverted Triangle
                recommendations = {
                    "best_styles": ["A-line bottoms", "Wide-leg pants", "Detailed bottoms", "Simple tops"],
                    "avoid": ["Shoulder pads", "Horizontal stripes on top", "Skinny jeans"],
                    "colors": ["Darker colors on top", "Patterns and bright colors on bottom"]
                }
            
            # Display recommendations
            st.markdown("#### ✅ Best Styles for You:")
            for style in recommendations["best_styles"]:
                st.write(f"• {style}")
            
            st.markdown("#### ❌ Styles to Avoid:")
            for avoid in recommendations["avoid"]:
                st.write(f"• {avoid}")
            
            st.markdown("#### 🎨 Color Recommendations:")
            for color in recommendations["colors"]:
                st.write(f"• {color}")
            
            # Shopping suggestions
            st.markdown("#### 🛍️ Shopping List for Your Body Type:")
            shopping_items = [
                f"Essential {random.choice(['blazer', 'dress', 'top'])} in {random.choice(['navy', 'black', 'white'])}",
                f"Flattering {random.choice(['jeans', 'trousers', 'skirt'])} in your size",
                f"Statement {random.choice(['accessories', 'shoes', 'jewelry'])} to complete looks",
                f"Versatile {random.choice(['cardigan', 'jacket', 'sweater'])} for layering"
            ]
            
            for item in shopping_items:
                st.write(f"🛒 {item}")

# Wardrobe Care Assistant
elif page == "✨ Wardrobe Care Assistant":
    st.header("✨ Wardrobe Care Assistant")
    st.subheader("Keep your clothes looking their best")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🧼 Care Guide", "📅 Maintenance Schedule", "🔧 Quick Fixes", "📊 Wardrobe Analytics"])
    
    with tab1:
        st.markdown("### 🧼 Fabric Care Guide")
        
        fabric_type = st.selectbox("Select fabric type:", [
            "Cotton", "Wool", "Silk", "Linen", "Polyester", "Denim", "Leather", "Cashmere"
        ])
        
        care_guides = {
            "Cotton": {
                "washing": "Machine wash warm, tumble dry medium",
                "drying": "Can tumble dry, may shrink slightly",
                "ironing": "Iron on high heat while damp",
                "storage": "Fold or hang, breathable storage",
                "tips": ["Pre-treat stains", "Wash similar colors together"]
            },
            "Wool": {
                "washing": "Hand wash cold or dry clean",
                "drying": "Lay flat to dry, never wring",
                "ironing": "Steam or iron on low with pressing cloth",
                "storage": "Fold with cedar balls for moths",
                "tips": ["Use wool detergent", "Never bleach"]
            },
            "Silk": {
                "washing": "Hand wash cold or dry clean",
                "drying": "Air dry away from direct sunlight",
                "ironing": "Iron on low heat inside out",
                "storage": "Hang on padded hangers",
                "tips": ["Use silk detergent", "Test for colorfastness"]
            }
        }
        
        if fabric_type in care_guides:
            guide = care_guides[fabric_type]
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### 🧺 Washing")
                st.info(guide["washing"])
                
                st.markdown("#### 🌬️ Drying")
                st.info(guide["drying"])
            
            with col2:
                st.markdown("#### 👕 Ironing")
                st.info(guide["ironing"])
                
                st.markdown("#### 📦 Storage")
                st.info(guide["storage"])
            
            st.markdown("#### 💡 Pro Tips")
            for tip in guide["tips"]:
                st.write(f"• {tip}")
    
    with tab2:
        st.markdown("### 📅 Maintenance Schedule")
        
        st.markdown("#### 🗓️ This Week's Tasks")
        weekly_tasks = [
            {"task": "Wash workout clothes", "priority": "High", "estimated_time": "30 min"},
            {"task": "Iron work shirts", "priority": "Medium", "estimated_time": "45 min"},
            {"task": "Organize closet", "priority": "Low", "estimated_time": "1 hour"}
        ]
        
        for task in weekly_tasks:
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            with col1:
                st.write(f"📋 {task['task']}")
            with col2:
                if task['priority'] == 'High':
                    st.error(task['priority'])
                elif task['priority'] == 'Medium':
                    st.warning(task['priority'])
                else:
                    st.info(task['priority'])
            with col3:
                st.write(task['estimated_time'])
            with col4:
                if st.button("Complete", key=f"task_{task['task']}"):
                    st.success("Task completed!")
        
        st.markdown("#### 📆 Monthly Reminders")
        monthly_tasks = [
            "Deep clean leather items",
            "Rotate seasonal clothes", 
            "Check for repairs needed",
            "Donate unused items"
        ]
        
        for task in monthly_tasks:
            st.write(f"📅 {task}")
    
    with tab3:
        st.markdown("### 🔧 Quick Fixes & Emergency Care")
        
        issue = st.selectbox("What issue are you dealing with?", [
            "Stain removal",
            "Wrinkle emergency", 
            "Button repair",
            "Hem adjustment",
            "Odor removal",
            "Pilling removal"
        ])
        
        solutions = {
            "Stain removal": [
                "🍷 Wine: Blot immediately, rinse with cold water, apply salt",
                "🥗 Oil: Sprinkle cornstarch, let sit 10 minutes, brush off, wash",
                "💄 Makeup: Use makeup remover or dish soap, then wash",
                "☕ Coffee: Rinse with cold water, apply white vinegar"
            ],
            "Wrinkle emergency": [
                "💨 Steam in bathroom while showering",
                "🧊 Ice cubes in dryer for 10 minutes",
                "💧 Damp towel in dryer with wrinkled item",
                "🚿 Hang in steamy bathroom"
            ],
            "Button repair": [
                "🧵 Use thread that matches fabric color",
                "🔄 Create X pattern for 4-hole buttons",
                "🎯 Sew through fabric and button multiple times",
                "✂️ Tie off thread securely on inside"
            ]
        }
        
        if issue in solutions:
            st.markdown(f"#### 🛠️ Solutions for {issue}:")
            for solution in solutions[issue]:
                st.write(solution)
    
    with tab4:
        st.markdown("### 📊 Your Wardrobe Analytics")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Items", "127", "+5 this month")
        with col2:
            st.metric("Cost Per Wear", "$2.45", "-$0.30")
        with col3:
            st.metric("Sustainability Score", "85%", "+12%")
        
        st.markdown("#### 📈 Wardrobe Insights")
        
        insights = [
            "👕 You wear your white button-up shirt most often (12 times this month)",
            "👗 Your little black dress has the best cost-per-wear ratio ($1.20)",
            "👠 Consider donating shoes you haven't worn in 6+ months (8 pairs)",
            "🌱 70% of your recent purchases are from sustainable brands",
            "💰 You've saved $340 this year by choosing quality over quantity"
        ]
        
        for insight in insights:
            st.write(insight)
        
        st.markdown("#### 🎯 Recommendations")
        st.info("🛍️ You could benefit from 2 more versatile tops to complete your capsule wardrobe")
        st.info("🧹 Schedule a closet organization session - you have items that haven't been worn in 12+ months")
        st.info("💡 Your style evolution shows you prefer minimalist pieces - consider this for future purchases")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>✨ Kleio - Craft your Style Story | Your AI-Powered Fashion Companion</p>
    <p>Made with ❤️ for fashion lovers everywhere</p>
</div>
""", unsafe_allow_html=True)
