import streamlit as st
from src.core.planner import Planner
from dotenv import load_dotenv

load_dotenv()

st.title("AI Travel Planner")
st.set_page_config(page_title="AI Travel Planner", page_icon=":earth_americas:")
st.write("Plan your next trip by poviding the city and your interests")

with st.form("travel_planner_form"):
    city = st.text_input("Enter the city you want to visit")
    interests = st.text_input("Enter your interests (comma-seperated )")
    submit_button = st.form_submit_button("Create Itenary")

if submit_button:
    if not city or not interests:
        st.error("Please enter a city and your interests")
        st.stop()
    planner = Planner()
    planner.set_city(city)
    planner.set_interests(interests)
    itenary = planner.create_itenary()
    
    st.subheader("Your Itenary")
    st.write(itenary)
