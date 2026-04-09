import streamlit as st
st.title("Streamlit Web App")

st.divider() #adds a horizontal line as divider

about_page = st.Page(
    page = 'views/about.py',
    title = "About Us",
    default = True  #this will set the about page as the default page when the app is loaded
)

contact_page = st.Page(
    page = 'views/contact.py',
    title = "Contact Us"
)

profile_page = st.Page(
    page = 'views/profile.py',
    title = "My Profile"
)

st.logo('exercise.png')

#folowing code will create a navigation menu with the three pages defined above and run the app
# pg = st.navigation({
#     'info' : [about_page, contact_page, profile_page],
#     'My Social Links': {'Website': 'https://www.ayushhardeniya.site', 'GitHub': 'https://www.github.com/ayushHardeniya', 'LinkedIn': 'https://www.linkedin.com/in/ayushhardeniya/', 'Twitter': 'https://x.com/ayushhardeniya'}
# })
# pg.run() 

pg = st.navigation({
    "Info": [about_page, contact_page, profile_page],
})

# 3. Add your social links to the sidebar manually
with st.sidebar:
    st.write("### My Social Links")
    st.link_button("Website", "https://www.ayushhardeniya.site")
    st.link_button("GitHub", "https://www.github.com/ayushHardeniya")
    st.link_button("LinkedIn", "https://www.linkedin.com/in/ayushhardeniya/")
    st.link_button("Twitter/X", "https://x.com/ayushhardeniya")

# 4. Run the navigation
pg.run()