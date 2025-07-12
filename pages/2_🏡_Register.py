import pandas as pd
import pyotp
import qrcode
import streamlit as st
from streamlit_option_menu import option_menu
import database as db

st.set_page_config(page_title='GPS Based Simulation',
                   layout='wide',
                   page_icon=r"Logos/gps.png")
st.sidebar.title("GPS Based Simulation")
# Page Setup 
#Image In Sidebar 
with st.sidebar.container(): 
    st.image(r'Logos/gps-logo.jpeg', use_column_width=True, caption='GPS Based Project')
st.sidebar.markdown("---")

def print_praise():
    praise_quotes = """
    Disha Gupta
    """
    title = "**Brought to you By -**\n\n"
    return title + praise_quotes

st.sidebar.success(print_praise())   
st.sidebar.write("---\n")
st.sidebar.info("Special Thanks to my Internal Mentor\n\nDr.Ankur Rai Sir,\n\nGLA UNIVERSITY, MATHURA")

def streamlit_menu():
    selected = option_menu(
        menu_title='Employees',  # required
        options=["Register", "Delete User"],  # required
        icons=["house", "envelope"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
        orientation="horizontal",
    )
    return selected

if 'user_id' not in st.session_state:
    st.session_state['user_id'] = None
if 'user_id' not in st.session_state:
    st.session_state['phone_number'] = None
if 'user_id' not in st.session_state:
    st.session_state['First_Name'] = None
if 'user_id' not in st.session_state:
    st.session_state['Middle_name'] = None
if 'user_id' not in st.session_state:
    st.session_state['Last_name'] = None
if 'user_id' not in st.session_state:
    st.session_state['Street_Number'] = None
if 'user_id' not in st.session_state:
    st.session_state['Street_Name'] = None
if 'user_id' not in st.session_state:
    st.session_state['City'] = None
if 'user_id' not in st.session_state:
    st.session_state['Province'] = None
if 'user_id' not in st.session_state:
    st.session_state['Vehicle_Identity_code'] = None


selected = streamlit_menu()
if selected=="Register":
    st.title("Register")
    st.subheader("Register your account")
    st.markdown("---")
    st.markdown("Please fill in the form below to register your account")
    with st.form("my_form"):
        col1,col2,col3,col4,col5 =  st.columns([2,2,2,2,2])
        col6,col7,col8,col9,col10=st.columns([2,5,2,2,2])
        with col1:
            st.session_state['user_id'] =st.text_input("User ID")
        with col2:
            st.session_state['phone_number']=st.text_input("Phone Number")
        with col3:
            st.session_state['First_Name']=st.text_input("First Name")
        with col4:
            st.session_state['Middle_name']=st.text_input("Middle Name")
        with col5:
            st.session_state['Last_name']=st.text_input("Last Name")
        with col6:
            st.session_state['Street_Number']=st.text_input("Street Number")
        with col7:
            st.session_state['Street_Name']=st.text_input("Street Name")
        with col8:
            st.session_state['City']=st.text_input("City")
        with col9:
            st.session_state['Province']=st.text_input("Province")
        with col10:
            st.session_state['Vehicle_Identity_code']=st.text_input("Vehicle-Identity Code")

        create=st.form_submit_button("Create")
    if col1 and col2 and col3 and col4 and col5 and col6 and create:
        db.register_user(st.session_state['user_id'],st.session_state['phone_number'],st.session_state['First_Name'],st.session_state['Middle_name'],st.session_state['Last_name']
                         ,st.session_state['Street_Number'],st.session_state['Street_Name'],st.session_state['City'],st.session_state['Province'],st.session_state['Vehicle_Identity_code'])
        data = db.update_user_details(st.session_state['user_id'])
          # Add this line for debugging
        if data and len(data) == 10:
            df = pd.DataFrame([data], columns=['ID', 'Phone Number', 'First Name', 'Middle Name', 'Last Name', 'Street Number', 'Street Name', 'City', 'Province', 'Vehicle-Identity Code'])
            #st.write(df)
            # Generate 2FA secret and create QR code
            secret = pyotp.random_base32()
            #st.write("Debug: Secret:", secret)
            db.save_2fa_secret(st.session_state['user_id'], secret)
            otp_uri = pyotp.totp.TOTP(secret).provisioning_uri(name=st.session_state['First_Name'] + " " + st.session_state['Last_name'], issuer_name="GPS Based Project")
            qr = qrcode.make(otp_uri)
            qr.save(f"qr_codes/{st.session_state['user_id']}.png")
            st.image(f"qr_codes/{st.session_state['user_id']}.png", caption="Scan this QR code with Google Authenticator")

            st.success("User Registered successfully. Scan the QR code with Google Authenticator.")
            st.balloons()
        else:
            st.error("Error retrieving user data. Please check the database and try again.")
        
if selected =="Delete User":
    a=st.text_input("Enter Your User Id")
    dele=st.button("Delete")
    try:
        if dele:
            data=db.delete_user(a)
            st.write("The following data is deleted")
            st.success("Data has been deleted")    
    except Exception as e:
        st.error(e)


    

