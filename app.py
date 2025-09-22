import streamlit as st

# --- Page Configuration ---
# Set the page title and a relevant icon.
st.set_page_config(page_title="PlastiCo Products", page_icon="📦")

# --- Main Application ---

# Add a title to the app.
st.title("PlastiCo Manufacturing Products")

# Create the navigation tabs.
tab_list = ["Home", "Our Products", "Contact Us"]
tab1, tab2, tab3 = st.tabs(tab_list)

# --- Tab Content ---

# Use the 'with' notation to add content to each tab.
with tab1:
    st.header("Welcome to PlastiCo")
    st.write("Your trusted partner in high-quality plastic manufacturing.")
    st.write("This is the home page. Here we can display company information, news, or welcome messages.")
    st.image("https://storage.googleapis.com/gweb-uniblog-publish-prod/images/new_streamilt_logo.width-1200.format-webp.webp", width=400) # Placeholder image

with tab2:
    st.header("Product Showcase")
    st.write("This section will display our range of plastic products. We will add interactive filters and detailed views for each category.")

    # Placeholders for product categories
    st.subheader("Rope Products")
    st.write("Details, specifications, and images for various types of plastic ropes will be available here.")

    st.subheader("Agricultural Bags")
    st.write("Information about our durable bags for agricultural use will be displayed in this section.")

    st.subheader("Agricultural Fabric")
    st.write("Here you will find details about our specialized fabrics for various agricultural applications.")

with tab3:
    st.header("Get in Touch")
    st.write("This area will contain our contact information, a contact form, and a map.")
    st.write("**Company Address:** 123 Industrial Way, Manufacturing City, 45678")
    st.write("**Email:** contact@plastico.dev")
    st.write("**Phone:** (123) 456-7890")
