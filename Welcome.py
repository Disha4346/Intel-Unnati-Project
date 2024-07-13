import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from database import *
import folium
from streamlit_folium import folium_static
import sqlite3

def edit():
    st.set_page_config(page_title='GPS Based Simulation',
                       layout='wide',
                       page_icon="Logos\gps.png")
    st.sidebar.title("GPS Based Simulation")
    st.snow()
    st.balloons()
    st.image("Logos\Main-logo.png", use_column_width=True)
    
    # Page Setup 
    # Image In Sidebar 
    with st.sidebar.container(): 
        st.image('Logos\gps-logo.jpeg', use_column_width=True, caption='GPS Based Project')
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
edit()
connect_db()
create_user_table()
create_user_data()
create_toll_data()
create_safe()
