import streamlit as st

# Define the pages
main_page = st.Page("home.py", title="Home", icon="🏠")
page_2 = st.Page("Projects\project.py", title="Projects", icon="🚀")
page_3 = st.Page("Certification\cert.py", title="Certifications", icon="🏅")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3], position='top')

# Run the selected page
pg.run()