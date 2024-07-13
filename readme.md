# GPS-Based-Toll-System

## Project Overview

This project simulates a GPS-based toll system, integrating vehicle tracking, toll calculation, and visualization features. It uses user authentication with 2-factor authentication (2FA) to ensure secure access. Key functionalities include simulating vehicle movement, calculating tolls based on entry and exit points, and displaying user travel data in an interactive dashboard.

## Features

1. User Authentication and 2FA:
   - Secure login with user ID and phone number.
   - 2FA using Google Authenticator.

2. Vehicle Tracking and Toll Calculation:
   - Converts entry and exit points into geographical coordinates.
   - Calculates toll zones between entry and exit points.
   - Computes total toll tax based on the distance traveled within toll zones.

3. Simulation and Visualization:
   - Simulates vehicle movement on a map using Folium.
   - Visualizes entry and exit points along with toll zones.
   - Displays user travel data with interactive dashboards using Seaborn and Matplotlib.

## Technology Stack

- Frontend: Streamlit
- Backend: Python
- Database: Custom module for user and travel data
- Geospatial Libraries: Geopy
- Visualization Libraries: Folium, Matplotlib, Seaborn

## Installation and Setup

### Prerequisites

- Python 3.8 or higher
- Streamlit, Pandas, Folium, Streamlit-Folium, Matplotlib, Seaborn, PyOTP, Geopy

### Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/gps-based-toll-system.git
   cd gps-based-toll-system #can be skipped
   ```

2. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run Welcome.py
   ```

## Usage

1. **Login**: Enter your user ID and phone number, then verify with the 2FA code from Google Authenticator.
2. **Dashboard**: View your travel data visualized in interactive plots.
3. **Simulate Vehicle Movement**: Input entry and exit points to calculate toll zones and simulate vehicle movement on a map.

## Contributions

Contributions are welcome! Please submit a pull request or open an issue to discuss changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Special Thanks

Special thanks to:
- **Dr. Ankur Rai** (GLA University, Mathura) for mentorship and guidance.


**Some more info about pages**


# Main Dashboard
It is the page that actually does the work of that is alloted to us in our project.

# 🧳_travel_viz.py 
- this page allows the user to interactively filter the data based on time periods. The heatmaps for the locations can also be plotted. Along with the heatmaps, there is an option to show histograms for the data points by different time periods like hour, months & years. Additionally, a specified number of random images can be obtained from Unsplash images of the locations in the dataset.

Instructions for Running
Get the Google Maps location history from Google Takeout.

Clean the data by running data_cleaning.py. It removes all data except latitude, longitude & timestamps. The data is also converted in to the standard format. A sample data file containing 10K data points is provided in this repo clean_data_sample.csv.

For getting images from Unsplash, you need to create an app & get the API key & secret.
The API key & secret are stored in a .env file. Create a copy of .env.example & rename it to .env & add the values for the app secret & api key for Unsplash services.


To use Mapbox for the streamlit maps, please configure the settings following the documentation on Streamlit.(if needed.)


#The sample is pre-generated for the ease of work of the page.

# admin.py
This page can be accessed only when the admin enter, here, since i have created this, 
Details are: admin_streamlit1
Password: Stream_lits
