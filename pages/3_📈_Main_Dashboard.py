import streamlit as st
import streamlit.components.v1 as components
from database import org, tollZones, nationalHighways as NH
import json
from threading import Thread
from time import sleep

st.set_page_config(page_title='GPS Based Simulation', layout='wide', page_icon=r"Logos/gps.png")
st.sidebar.title("GPS Based Simulation")
st.image(r"Logos/Main-logo.png", use_column_width=False)

with st.sidebar.container():
    st.image(r'Logos/gps-logo.jpeg', use_column_width=True, caption='GPS Based Project')
st.sidebar.markdown("---")

def print_praise():
    praise_quotes = "Disha Gupta"
    title = "**Brought to you By -**\n\n"
    return title + praise_quotes

st.sidebar.success(print_praise())
st.sidebar.write("---\n")
st.sidebar.info("Special Thanks to my Internal Mentor\n\nDr.Ankur Rai Sir,\n\nGLA UNIVERSITY, MATHURA")


# Initialize previous_coord
previous_coord = []

def car_travelling_on_toll_road(coord):
    global previous_coord

    on_road = org.is_vehicle_on_any_toll_road(coord, NH)
    zone = org.return_toll_zone_and_tax_rate(coord, tollZones)
    if previous_coord:
        previous_zone = org.return_toll_zone_and_tax_rate(previous_coord, tollZones)
    else:
        previous_zone = [False, None, 1]
    if on_road[0]:
        st.write("Car is travelling on toll road")
        if zone[1] != previous_zone[1]:
            org.zone_wise_distance_toll_collection(previous_zone[2])
            org.entity.coordinates.clear()
        car_coord = f'{coord[0]},{coord[1]}'
        org.entity.coordinates.append(car_coord)
    else:
        envoice = org.zone_wise_distance_toll_collection(zone[2])
        if envoice == False:
            st.write("Car not travelling on toll road")
        else:
            org.entity.coordinates.clear()

    previous_coord = [coord[0], coord[1]]

# Streamlit Page for receiving GPS data
st.title("GPS Coordinate Processing")

if 'previous_coord' not in st.session_state:
    st.session_state.previous_coord = []
if 'latitude' not in st.session_state:
    st.session_state['latitude'] = None
if 'longitude' not in st.session_state:
    st.session_state['longitide']= None

# Form to receive GPS coordinates
with st.form("gps_form"):
    st.session_state['latitude'] = st.text_input("Latitude")
    st.session_state['longitide'] = st.text_input("Longitude")
    submit_button = st.form_submit_button(label='Submit Coordinates')

if submit_button:
    try:
        st.session_state['latitude'] = float(st.session_state['latitude'])
        longitude = float(st.session_state['longitide'])
        if st.session_state.previous_coord == []:
            st.session_state.previous_coord = [st.session_state['latitude'], st.session_state['longitide']]

        st.write(f"Received GPS coordinates: Latitude={st.session_state['latitude']}, Longitude={st.session_state['longitide']}")
        car_travelling_on_toll_road([st.session_state['latitude'],st.session_state['longitide']])
        st.write({"message": "Coordinates received"})

    except ValueError:
        st.write({"error": "Invalid coordinates"})


def gps_coordinate_simulation():
    global previous_coord
    #Assumptions
    coords =st.session_state.previous_coord
    for coord in coords:
        car_travelling_on_toll_road([coord[st.session_state['latitude']], coord[st.session_state['longitide']]])
        previous_coord = [coord[st.session_state['latitude']], coord[st.session_state['longitide']]]
        sleep(1)

# Display the HTML file content
components.html(open("gps_tracking.html").read(), height=500)

# Button to start the GPS simulation
if st.button("Start GPS Simulation"):
    thread = Thread(target=gps_coordinate_simulation)
    thread.start()

# Endpoint to serve the coordinates to the frontend
@st.cache_resource
def serve_coordinates():
    if previous_coord:
        coord = {
            'latitude': previous_coord[0],
            'longitude': previous_coord[1]
        }
        return json.dumps(coord)
    return json.dumps({'latitude': 0, 'longitude': 0})

# Endpoint for the frontend to fetch coordinates
#st.experimental_get_query_params("coordinates", serve_coordinates)

# Button to shutdown server and display envoices
if st.button("Shutdown Server"):
    for envoice in org.envoices:
        st.write(envoice[0])
    st.write(org.total_toll_collection())
    st.write({"message": "Server shutting down"})
