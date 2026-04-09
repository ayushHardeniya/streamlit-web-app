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
pg = st.navigation([about_page, contact_page, profile_page])
pg.run() 