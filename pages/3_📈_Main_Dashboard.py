import streamlit as st
import streamlit.components.v1 as components
from database import org, tollZones, nationalHighways as NH
import json
from threading import Thread
from time import sleep

# -------------------- Streamlit Page Setup -------------------- #
st.set_page_config(
    page_title='GPS Based Simulation',
    layout='wide',
    page_icon="Logos/gps.png"
)

st.sidebar.title("GPS Based Simulation")
st.image("Logos/Main-logo.png", use_column_width=False)

with st.sidebar.container():
    st.image('Logos/gps-logo.jpeg', use_column_width=True, caption='GPS Based Project')
st.sidebar.markdown("---")

def print_praise():
    praise_quotes = "Disha Gupta"
    title = "**Brought to you By -**\n\n"
    return title + praise_quotes

st.sidebar.success(print_praise())
st.sidebar.write("---\n")
st.sidebar.info("Special Thanks to my Internal Mentor\n\nDr.Ankur Rai Sir,\n\nGLA UNIVERSITY, MATHURA")

# -------------------- Session State Initialization -------------------- #
default_state = {
    "previous_coord": [],
    "latitude": '',
    "longitude": ''
}

for key, value in default_state.items():
    if key not in st.session_state:
        st.session_state[key] = value

# -------------------- Core Toll Calculation Logic -------------------- #
def car_travelling_on_toll_road(coord):
    on_road = org.is_vehicle_on_any_toll_road(coord, NH)
    zone = org.return_toll_zone_and_tax_rate(coord, tollZones)

    if st.session_state["previous_coord"]:
        previous_zone = org.return_toll_zone_and_tax_rate(
            st.session_state["previous_coord"], tollZones
        )
    else:
        previous_zone = [False, None, 1]

    if on_road[0]:
        st.write("🚗 Car is travelling on toll road")
        if zone[1] != previous_zone[1]:
            org.zone_wise_distance_toll_collection(previous_zone[2])
            org.entity.coordinates.clear()

        car_coord = f'{coord[0]},{coord[1]}'
        org.entity.coordinates.append(car_coord)
    else:
        envoice = org.zone_wise_distance_toll_collection(zone[2])
        if not envoice:
            st.write("🚧 Car not on toll road")
        else:
            org.entity.coordinates.clear()

    st.session_state["previous_coord"] = coord

# -------------------- Form for Manual GPS Input -------------------- #
st.title("📍 GPS Coordinate Processing")

with st.form("gps_form"):
    st.session_state['latitude'] = st.text_input("Latitude", value=st.session_state['latitude'])
    st.session_state['longitude'] = st.text_input("Longitude", value=st.session_state['longitude'])
    submit_button = st.form_submit_button(label='Submit Coordinates')

if submit_button:
    try:
        lat = float(st.session_state['latitude'])
        lon = float(st.session_state['longitude'])

        st.session_state["previous_coord"] = [lat, lon]
        car_travelling_on_toll_road([lat, lon])

        st.success(f"✅ Coordinates received: Latitude = {lat}, Longitude = {lon}")
    except ValueError:
        st.error("❌ Invalid coordinates entered. Please enter valid numbers.")

# -------------------- GPS Coordinate Simulation -------------------- #
def gps_coordinate_simulation():
    simulated_coords = [
        [27.12, 77.32],
        [27.13, 77.33],
        [27.14, 77.34],
        [27.15, 77.35]
    ]
    for coord in simulated_coords:
        car_travelling_on_toll_road(coord)
        sleep(1)

if st.button("▶️ Start GPS Simulation"):
    thread = Thread(target=gps_coordinate_simulation)
    thread.start()

# -------------------- Show Live Map Panel -------------------- #
components.html(open("gps_tracking.html").read(), height=500)

# -------------------- Shutdown Button -------------------- #
if st.button("🛑 Shutdown Server"):
    st.write("🧾 Final Envoices:")
    for envoice in org.envoices:
        st.write(envoice[0])
    st.write("💰 Total Toll Collected:")
    st.write(org.total_toll_collection())
    st.success("✅ Server shutdown complete.")
