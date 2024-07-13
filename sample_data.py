from database import *
#This files sole purpose is to enter some random data in the sqlite page.

#
## Function to insert sample data into both tables
#def insert_sample_data():
#    connection = connect_db()
#
#    # Sample user data
#    user_data = [
#        ('Alice', 'password1', 10.5, 50.2, 200.5, 1200.7),
#        ('Bob', 'password2', 8.2, 45.7, 180.3, 1100.9),
#        ('Charlie', 'password3', 12.3, 55.1, 220.6, 1300.4)
#    ]
#
#    # Sample toll data
#    toll_data = [
#        (1, 40.1234, -74.5678, True),
#        (2, 39.9876, -75.3456, False),
#        (3, 41.2345, -73.9876, True)
#    ]
#
#    # Insert sample user data
#    connection.executemany('''INSERT INTO user_data (username, password, daily_travel, weekly_travel, monthly_travel, yearly_travel)
#                            VALUES (?, ?, ?, ?, ?, ?)''', user_data)
#
#    # Insert sample toll data
#    connection.executemany('''INSERT INTO toll_data (user_id, latitude, longitude, toll_paid)
#                            VALUES (?, ?, ?, ?)''', toll_data)
#
#    connection.commit()
#    connection.close()
#insert_sample_data()
#print("Done")

#conn=connect_db()
#cursor=conn.cursor()
#cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#rows=cursor.fetchall()
#for row in rows:
#    print(row)
#conn.commit()
#conn.close()

#import sqlite3
#import random
#
## Connect to the database (replace 'your_database.db' with your actual database name)
#connection = sqlite3.connect('GPS_DATA.db')
#cursor = connection.cursor()
#
## Function to generate random float values
#def random_float(min_value, max_value):
#    return round(random.uniform(min_value, max_value), 1)
#
## Function to generate random latitude and longitude
#def random_lat_long():
#    latitude = round(random.uniform(35.0, 45.0), 4)
#    longitude = round(random.uniform(-80.0, -70.0), 4)
#    return latitude, longitude
#
## Generate sample user data
#user_data = []
#for i in range(4, 104):  # Starting from user_id 4 to 103 (100 entries)
#    username = f'User{i}'
#    password = f'password{i}'
#    daily_travel = random_float(5.0, 15.0)
#    weekly_travel = random_float(30.0, 60.0)
#    monthly_travel = random_float(150.0, 300.0)
#    yearly_travel = random_float(1000.0, 1500.0)
#    user_data.append((username, password, daily_travel, weekly_travel, monthly_travel, yearly_travel))
#
## Generate sample toll data
#toll_data = []
#for i in range(4, 104):  # Assuming each user has one toll data entry
#    latitude, longitude = random_lat_long()
#    toll_paid = random.choice([True, False])
#    toll_data.append((i, latitude, longitude, toll_paid))
#
## Insert sample user data
#cursor.executemany('''INSERT INTO user_data (username, password, daily_travel, weekly_travel, monthly_travel, yearly_travel)
#                      VALUES (?, ?, ?, ?, ?, ?)''', user_data)
#
## Insert sample toll data
#cursor.executemany('''INSERT INTO toll_data (user_id, latitude, longitude, toll_paid)
#                      VALUES (?, ?, ?, ?)''', toll_data)
#
## Commit the transaction and close the connection
#connection.commit()
#connection.close()
#
#print("Sample data inserted successfully.")
