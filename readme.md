#Main Dashboard
It is the page that actually does the work of that is alloted to us in our project.

The page pages\5_🧳_travel_viz.py allows the user to interactively filter the data based on time periods. The heatmaps for the locations can also be plotted. Along with the heatmaps, there is an option to show histograms for the data points by different time periods like hour, months & years. Additionally, a specified number of random images can be obtained from Unsplash images of the locations in the dataset.

*Installation
Install the dependencies

#pip install -r requirements.txt

Instructions for Running
Get the Google Maps location history from Google Takeout.

Clean the data by running data_cleaning.py. It removes all data except latitude, longitude & timestamps. The data is also converted in to the standard format. A sample data file containing 10K data points is provided in this repo clean_data_sample.csv.

For getting images from Unsplash, you need to create an app & get the API key & secret.
The API key & secret are stored in a .env file. Create a copy of .env.example & rename it to .env & add the values for the app secret & api key for Unsplash services.


To use Mapbox for the streamlit maps, please configure the settings following the documentation on Streamlit.(if needed.)


#The sample is pre-generated for the ease of work of the app. 

Application will run by running
```
streamlit run Welcome.py
```