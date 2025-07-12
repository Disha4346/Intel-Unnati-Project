import streamlit as st
import pandas as pd
import database as db

st.set_page_config(page_title='GPS Based Simulation', layout='wide', page_icon=r"Logos\gps.png")
st.sidebar.title("GPS Based Simulation")
st.image(r"Logos\Main-logo.png", use_column_width=False)

with st.sidebar.container():
    st.image(r'Logos\gps-logo.jpeg', use_column_width=True, caption='GPS Based Project')
st.sidebar.markdown("---")

def print_praise():
    praise_quotes = "Disha Gupta"
    title = "**Brought to you By -**\n\n"
    return title + praise_quotes

st.sidebar.success(print_praise())
st.sidebar.write("---\n")
st.sidebar.info("Special Thanks to my Internal Mentor\n\nDr.Ankur Rai Sir,\n\nGLA UNIVERSITY, MATHURA")

st.sidebar.write("---\n")
st.sidebar.info("Special Thanks to my External Mentor\n\nDr. Shri Harsha Sir,\n")

#this page will be displayed only when the admin details will be entered.
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ''
if 'password' not in st.session_state:
    st.session_state['password'] = ''

def display_admin_page():
    
    st.title("Admin Page")
    user_data = pd.read_sql_query("SELECT username,daily_travel,weekly_travel,monthly_travel,yearly_travel FROM user_data",db.connect_db())
    toll_data = pd.read_sql_query("SELECT * FROM toll_data",db.connect_db())

    st.subheader("Travellers:")
    st.dataframe(user_data)
    st.subheader("Toll Data:")
    st.dataframe(toll_data)

    st.subheader("Number of Travelers")
    num_travelers = user_data['username'].nunique()
    st.write(f"Total unique travelers: {num_travelers}")

    st.subheader("Unpaid Toll Taxes")
    unpaid_tolls = toll_data[toll_data['toll_paid'] == 0]
    st.write(f"Total unpaid tolls: {len(unpaid_tolls)}")
    st.dataframe(unpaid_tolls)
    st.image(r'https://vajiramandravi.s3.us-east-1.amazonaws.com/media/2020/9/5/10/56/46/road.jpg')

def admin_login():
    st.title("Admin Login")
    st.subheader("Login into the admin account")
    st.markdown("---")
    with st.form("my_form"):
        col1, col2 = st.columns(2)
        with col1:
            st.session_state['user_name'] = st.text_input("Admin User name", value=st.session_state['user_name'])

        with col2:
            st.session_state['password'] = st.text_input("password", value=st.session_state['password'])
        login=st.form_submit_button("Proceed")
        
    if login and col2:
        if st.session_state['user_name'] == 'admin_streamlit1' and st.session_state['password']=="Stream_lits":
            display_admin_page()
    




if __name__ == '__main__':
    admin_login()
