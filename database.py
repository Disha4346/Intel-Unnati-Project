import sqlite3
import pandas as pd
import streamlit as st
import random

# Connect to the database
def connect_db():
    return sqlite3.connect("GPS_DATA.db")

# Table creation functions
def create_user_data():
    connection = connect_db()
    connection.execute('''CREATE TABLE IF NOT EXISTS user_data (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        daily_travel REAL,
        weekly_travel REAL,
        monthly_travel REAL,
        yearly_travel REAL
    )''')
    connection.close()

def create_toll_data():
    connection = connect_db()
    connection.execute('''CREATE TABLE IF NOT EXISTS toll_data (
        toll_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        latitude REAL,
        longitude REAL,
        toll_paid BOOLEAN,
        FOREIGN KEY(user_id) REFERENCES user_data(user_id)
    )''')
    connection.close()

def create_user_table():
    connection = connect_db()
    connection.execute('''CREATE TABLE IF NOT EXISTS USER(
        user_id INT PRIMARY KEY,
        phone_number INT (12) NOT NULL,
        first_name VARCHAR(10) NOT NULL,
        middle_name VARCHAR(10),
        last_name VARCHAR(20) NOT NULL,
        street_number VARCHAR NOT NULL,
        street_name VARCHAR NOT NULL,
        city VARCHAR(20) NOT NULL,
        province VARCHAR NOT NULL,
        vehicle_code varchar(10) NOT NULL
    )''')
    connection.close()

def register_user(q, w, e, r, t, y, u, i, o, p):
    connection = connect_db()
    cursor = connection.cursor()
    query = '''INSERT INTO USER (user_id, phone_number, first_name, middle_name, last_name, street_number, street_name, city, province, vehicle_code)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cursor.execute(query, (q, w, e, r, t, y, u, i, o, p))
    connection.commit()
    connection.close()

def update_user_details(user_id):
    try:
        connection = connect_db()
        cursor = connection.cursor()
        query = """
        SELECT user_id, phone_number, first_name, middle_name, last_name,
               street_number, street_name, city, province, vehicle_code
        FROM USER WHERE user_id = ?
        """
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchone()
        connection.close()
        return user_data
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None

def save_2fa_secret(user_id, secret):
    connection = connect_db()
    cursor = connection.cursor()
    query = '''INSERT INTO user_2fa_secrets (user_id, secret) VALUES (?, ?)'''
    cursor.execute(query, (user_id, secret))
    connection.commit()
    connection.close()

def create_safe():
    connection = connect_db()
    cursor = connection.cursor()
    query='''Create table if not exists user_2fa_secrets(
    user_id INTEGER NOT NULL,
    secret TEXT NOT NULL,
    PRIMARY KEY (user_id),
    FOREIGN KEY (user_id) REFERENCES USER(user_id)
    )'''
    cursor.execute(query)
    connection.commit()
    connection.close()

def get_2fa_secret(user_id):
    connection = connect_db()
    cursor = connection.cursor()
    query = '''SELECT secret FROM user_2fa_secrets WHERE user_id = ?'''
    cursor.execute(query, (user_id,))
    secret = cursor.fetchone()
    connection.close()
    if secret:
        return secret[0]
    return None

def get_user(q, phone_number):
    connection = connect_db()
    cursor = connection.cursor()
    query = '''SELECT user_id, phone_number FROM USER WHERE user_id=? AND phone_number=?'''
    cursor.execute(query, (q, phone_number))
    user = cursor.fetchone()
    connection.close()
    return user

def delete_user(user_id):
    connection = connect_db()
    query = '''DELETE FROM USER WHERE user_id = ?'''
    connection.execute(query, (user_id,))
    query2='''DELETE FROM user_2fa_secrets WHERE user_id = ?'''
    connection.execute(query2, (user_id,))
    connection.commit()
    connection.close()

# Data insertion functions
def insert_user_data(username, password):
    connection = connect_db()
    daily_travel = random.uniform(10, 50)
    weekly_travel = daily_travel * 7
    monthly_travel = weekly_travel * 4
    yearly_travel = monthly_travel * 12
    query = '''INSERT INTO user_data (username, password, daily_travel, weekly_travel, monthly_travel, yearly_travel)
               VALUES (?, ?, ?, ?, ?, ?)'''
    data = (username, password, daily_travel, weekly_travel, monthly_travel, yearly_travel)
    connection.execute(query, data)
    connection.commit()
    connection.close()

def insert_toll_data(user_id, latitude, longitude, toll_paid):
    connection = connect_db()
    query = '''INSERT INTO toll_data (user_id, latitude, longitude, toll_paid)
               VALUES (?, ?, ?, ?)'''
    data = (user_id, latitude, longitude, toll_paid)
    connection.execute(query, data)
    connection.commit()
    connection.close()

# Data update functions
def update_user_data(user_id, daily_travel=None, weekly_travel=None, monthly_travel=None, yearly_travel=None):
    connection = connect_db()
    query = '''UPDATE user_data SET daily_travel = COALESCE(?, daily_travel), 
                                     weekly_travel = COALESCE(?, weekly_travel), 
                                     monthly_travel = COALESCE(?, monthly_travel), 
                                     yearly_travel = COALESCE(?, yearly_travel) 
               WHERE user_id = ?'''
    data = (daily_travel, weekly_travel, monthly_travel, yearly_travel, user_id)
    connection.execute(query, data)
    connection.commit()
    connection.close()

def update_toll_data(toll_id, toll_paid):
    connection = connect_db()
    query = '''UPDATE toll_data SET toll_paid = ? WHERE toll_id = ?'''
    data = (toll_paid, toll_id)
    connection.execute(query, data)
    connection.commit()
    connection.close()


def generate_random_travel_data():
    return random.uniform(1, 100), random.uniform(100, 700), random.uniform(700, 3000), random.uniform(3000, 36000)
    # under this the required code can come for the smooth functioning.

def calculate_and_update_travel_data(username,conn):
    daily, weekly, monthly, yearly = generate_random_travel_data()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE user_data SET daily_travel = ?, weekly_travel = ?, monthly_travel = ?, yearly_travel = ? WHERE username = ?",
                   (daily, weekly, monthly, yearly, username))
    conn.commit()
    conn.close()

def admin():
    connection=connect_db()
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM user_data")
    data=cursor.fetchall()
    cursor.execute("SELECT * FROM toll_data")
    toll_data=cursor.fetchall()
    connection.close()
    return data,toll_data

def read_sql_query(query,conn):
    conn=connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data




#Database using json files- specifically for pages\4_📈_Main_Dashboard.py file.


from classes import Organizer

# Vehicle Information
vehicle_number = 5674
vehicle_type = "Car"
vehicle_class = "Light Vehicle"

# Bank Information
car_gps_id = ''
issuer_bank = ''
bank_account = ''
account_holder_name = ''

# Driver/Owner Information
owner_name = ''
contact_number = ''
email_address = ''

points_geojson = 'geo_data/Indian_States.geojson'
zones_geojson = 'geo_data/square_zone.geojson'

org = Organizer(vehicle_number)
nationalHighways = org.load_national_highways(points_geojson)
tollZones = org.load_toll_zones(zones_geojson)
