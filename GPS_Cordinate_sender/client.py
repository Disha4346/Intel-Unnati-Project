import streamlit as st
import requests
import time

# Define your server URLs
server_url = 'http://localhost:5000/gps'
frontend_url = 'http://localhost:4000/gps'

# Load coordinates from file
def load_coordinates(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()

    coords = []
    for index, line in enumerate(lines):
        if index < 180:
            continue
        line = line.strip()
        lon, lat = map(float, line.split(','))
        coords.append([lon, lat])
    coords.append([1, 1])  # Append the dummy coordinate
    return coords

coords = load_coordinates('geo_data/Car_Path.txt')

# Streamlit UI
st.title("GPS Coordinate Sender")

if st.button("Send Coordinates"):
    st.write("Sending coordinates...")

    for index, coord in enumerate(coords):
        data = {
            'latitude': coord[1],
            'longitude': coord[0]
        }
        response_server = requests.post(server_url, json=data)
        response_frontend = requests.post(frontend_url, json=data)
        
        st.write(f"Server response: {response_server.json()} (Index: {index + 1})")
        time.sleep(1)  # Simulate delay between sending coordinates

    st.write("All coordinates sent.")
    
    # Optional: Shutting down the server
    shutdown_url = 'http://localhost:5000/shutdown'
    response = requests.get(shutdown_url)
    st.write("Server shutdown response:", response.json())

# To run the Streamlit app, use the following command in your terminal:
# streamlit run streamlit_app.py
